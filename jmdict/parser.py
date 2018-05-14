from _elementtree import Element
from xml.etree import ElementTree
import json
import time

from jmdict.tags import convert_tag


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Time taken: {(end - start)} seconds')
        return result

    return wrapper


@timeit
def parse_jmdict(file: str = 'Jmdict.xml') -> None:
    tree = ElementTree.parse(file)
    root = tree.getroot()

    entries_processed = 0

    words = []
    for entry in root.iter('entry'):
        words.append(__parse_entry(entry))
        entries_processed += 1

    __write_to_json(words)

    print(f'Entries processed: {entries_processed}')


def __parse_entry(entry: Element) -> dict:
    entry_id = int(entry.find('ent_seq').text)

    kanji_list = []
    for kanji in entry.findall('k_ele'):
        kanji_list.append(__parse_kanji(kanji))

    kana_list = []
    for kana in entry.findall('r_ele'):
        kana_list.append(__parse_kana(kana))

    last_part_of_speech = []
    sense_list = []
    for sense in entry.findall('sense'):
        part_of_speech = sense.findall('pos')
        if len(part_of_speech):
            last_part_of_speech = []
            for item in part_of_speech:
                short_pos = convert_tag(item.text)
                last_part_of_speech.append(short_pos)

        sense_list.append((__parse_sense(sense, last_part_of_speech)))

    return {'id': entry_id, 'kanji': kanji_list, 'kana': kana_list, 'sense': sense_list}


def __write_to_json(words: list) -> None:
    file = open('JMdict.json', 'w', encoding='utf-8')
    json.dump(words, file, indent=4, ensure_ascii=False)
    file.close()


def __parse_kanji(kanji: Element) -> dict:
    text = kanji.find('keb').text

    priorities = kanji.findall('ke_pri')
    is_common = __is_common(priorities)

    tags = []
    for info in kanji.findall('ke_inf'):
        tags.append(convert_tag(info.text))

    return {'text': text, 'common': is_common, 'tags': tags}


def __parse_kana(kana: Element) -> dict:
    text = kana.find('reb').text

    priorities = kana.findall('re_pri')
    is_common = __is_common(priorities)

    tags = []
    for info in kana.findall('re_inf'):
        tags.append(convert_tag(info.text))

    no_kanji = kana.find('re_nokanji')

    applies_to_kanji = []
    if no_kanji is None:
        for item in kana.findall('re_restr'):
            applies_to_kanji.append(item.text)

        if not len(applies_to_kanji):
            applies_to_kanji = ['*']

    return {'text': text, 'common': is_common, 'tags': tags, 'appliesToKanji': applies_to_kanji}


def __parse_sense(sense: Element, last_part_of_speech: list) -> dict:
    part_of_speech = sense.findall('pos')

    if len(part_of_speech):
        pos = __transform_part_of_speech(part_of_speech)
    else:
        # If there are no pos entries for the current sense element, use the previous one
        pos = last_part_of_speech

    applies_to_kanji_search = sense.findall('stagk')
    if len(applies_to_kanji_search):
        applies_to_kanji = []
        for item in applies_to_kanji_search:
            applies_to_kanji.append(item.text)
    else:
        applies_to_kanji = ['*']

    applies_to_kana_search = sense.findall('stagr')
    if len(applies_to_kana_search):
        applies_to_kana = []
        for item in applies_to_kana_search:
            applies_to_kana.append(item.text)
    else:
        applies_to_kana = ['*']

    related = []
    for item in sense.findall('xref'):
        related.append(__transform_xref(item.text))

    antonym = []
    for item in sense.findall('ant'):
        antonym.append(__transform_xref(item.text))

    field = []
    for item in sense.findall('field'):
        field.append(convert_tag(item.text))

    dialect = []
    for item in sense.findall('dial'):
        dialect.append(convert_tag(item.text))

    misc = []
    for item in sense.findall('misc'):
        misc.append(convert_tag(item.text))

    info = []
    for item in sense.findall('info'):
        info.append(item.text)

    language_source = []
    for item in sense.findall('lsource'):
        lang = item.get('{http://www.w3.org/XML/1998/namespace}lang', 'eng')

        ls_wasei = item.get('ls_wasei', 'n')
        is_wasei = True if ls_wasei == 'y' else False

        ls_type = item.get('ls_type', 'full')
        is_full = True if ls_type == 'full' else False

        language_source_entry = {
            'lang': lang,
            'full': is_full,
            'wasei': is_wasei,
            'text': item.text
        }

        language_source.append(language_source_entry)

    gloss = []
    for item in sense.findall('gloss'):
        lang = item.get('{http://www.w3.org/XML/1998/namespace}lang', 'eng')
        g_type = item.get('g_type', None)

        gloss_entry = {
            'lang': lang,
            'type': g_type,
            'text': item.text
        }

        gloss.append(gloss_entry)

    return {
        'partOfSpeech': pos,
        'appliesToKanji': applies_to_kanji,
        'appliesToKana': applies_to_kana,
        'related': related,
        'antonym': antonym,
        'field': field,
        'dialect': dialect,
        'misc': misc,
        'info': info,
        'languageSource': language_source,
        'gloss': gloss
    }


def __transform_part_of_speech(part_of_speech: Element) -> list:
    pos = []
    for item in part_of_speech:
        pos.append(convert_tag(item.text))

    return pos


def __is_common(priorities: Element) -> bool:
    for item in priorities:
        if item.text in ["news1", "ichi1", "spec1", "spec2", "gai1"]:
            return True
    else:
        return False


# TODO: Return a dict or kanji, kana, number
def __transform_xref(xref: str) -> list:
    xref_item = []
    split_xref = xref.split('・')

    for part in split_xref:
        try:
            xref_item.append(int(part))
        except ValueError:
            xref_item.append(part)

    return xref_item
