from xml.etree import ElementTree
import json


class JmdictParser:
    def __init__(self, file='Jmdict.xml') -> None:
        tree = ElementTree.parse(file)
        self.__xml_root = tree.getroot()

    def parse(self) -> None:
        words = []
        for entry in self.__xml_root.iter('entry'):
            entry_id = entry.find('ent_seq').text

            kanji_list = []
            for kanji in entry.findall('k_ele'):
                kanji_list.append(self.__parse_kanji(kanji))

            full_entry = {'id': entry_id, 'kanji': kanji_list}
            words.append(full_entry)

        file = open('JMdict.json', 'w', encoding='utf-8')
        json.dump(words, file, indent=4, ensure_ascii=False)
        file.close()

    @staticmethod
    def __parse_kanji(kanji) -> dict:
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
