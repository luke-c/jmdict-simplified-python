from _elementtree import Element
from xml.etree import ElementTree
import json
import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Time taken: {(end - start)} seconds')
        return result
    return wrapper


@timeit
def parse_jmdict(file: str ='Jmdict.xml') -> None:
    entries_processed = 0
    tree = ElementTree.parse(file)
    xml_root = tree.getroot()

    words = []
    for entry in xml_root.iter('entry'):
        entry_id = entry.find('ent_seq').text

        kanji_list = []
        for kanji in entry.findall('k_ele'):
            kanji_list.append(__parse_kanji(kanji))

        kana_list = []
        for kana in entry.findall('r_ele'):
            kana_list.append(__parse_kana(kana))

        full_entry = {'id': entry_id, 'kanji': kanji_list, 'kana': kana_list}
        words.append(full_entry)
        entries_processed += 1

    __write_to_json(words)

    print(f'Entries processed: {entries_processed}')


def __write_to_json(words: list) -> None:
    file = open('JMdict.json', 'w', encoding='utf-8')
    json.dump(words, file, indent=4, ensure_ascii=False)
    file.close()


def __parse_kanji(kanji: Element) -> dict:
    text = kanji.find('keb').text

    for priority in kanji.findall('ke_pri'):
        if priority.text in ["news1", "ichi1", "spec1", "spec2", "gai1"]:
            common = True
            break
    else:
        common = False

    tags = []
    for info in kanji.findall('ke_inf'):
        tags.append(info.text)

    kanji_entry = {'text': text, 'common': common, 'tags': tags}
    return kanji_entry


def __parse_kana(kana: Element) -> dict:
    text = kana.find('reb').text

    for priority in kana.findall('re_pri'):
        if priority.text in ["news1", "ichi1", "spec1", "spec2", "gai1"]:
            common = True
            break
    else:
        common = False

    tags = []
    for info in kana.findall('re_inf'):
        tags.append(info.text)

    no_kanji = kana.find('re_nokanji')

    applies_to_kanji = []
    if no_kanji is None:
        for item in kana.findall('re_restr'):
            applies_to_kanji.append(item.text)

        if not len(applies_to_kanji):
            applies_to_kanji = ['*']

    kana_entry = {'text': text, 'common': common, 'tags': tags, 'appliesToKanji': applies_to_kanji}
    return kana_entry
