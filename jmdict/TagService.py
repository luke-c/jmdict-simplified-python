class TagService:

    def __init__(self) -> None:
        self.tags: dict = self.__generate_tags()

    # TODO: Generate the tags from the XML instead of hard-coding
    @staticmethod
    def __generate_tags() -> dict:
        return {
            "martial arts term": "MA",
            "rude or X-rated term (not displayed in educational software)": "X",
            "abbreviation": "abbr",
            "adjective (keiyoushi)": "adj-i",
            "adjective (keiyoushi) - yoi/ii class": "adj-ix",
            "adjectival nouns or quasi-adjectives (keiyodoshi)": "adj-na",
            "nouns which may take the genitive case particle `no'": "adj-no",
            "pre-noun adjectival (rentaishi)": "adj-pn",
            "`taru' adjective": "adj-t",
            "noun or verb acting prenominally": "adj-f",
            "adverb (fukushi)": "adv",
            "adverb taking the `to' particle": "adv-to",
            "archaism": "arch",
            "ateji (phonetic) reading": "ateji",
            "auxiliary": "aux",
            "auxiliary verb": "aux-v",
            "auxiliary adjective": "aux-adj",
            "Buddhist term": "Buddh",
            "chemistry term": "chem",
            "children's language": "chn",
            "colloquialism": "col",
            "computer terminology": "comp",
            "conjunction": "conj",
            "copula": "cop-da",
            "counter": "ctr",
            "derogatory": "derog",
            "exclusively kanji": "eK",
            "exclusively kana": "ek",
            "expressions (phrases, clauses, etc.)": "exp",
            "familiar language": "fam",
            "female term or language": "fem",
            "food term": "food",
            "geometry term": "geom",
            "gikun (meaning as reading) or jukujikun (special kanji reading)": "gikun",
            "honorific or respectful (sonkeigo) language": "hon",
            "humble (kenjougo) language": "hum",
            "word containing irregular kanji usage": "iK",
            "idiomatic expression": "id",
            "word containing irregular kana usage": "ik",
            "interjection (kandoushi)": "int",
            "irregular okurigana usage": "io",
            "irregular verb": "iv",
            "linguistics terminology": "ling",
            "manga slang": "m-sl",
            "male term or language": "male",
            "male slang": "male-sl",
            "mathematics": "math",
            "military": "mil",
            "noun (common) (futsuumeishi)": "n",
            "adverbial noun (fukushitekimeishi)": "n-adv",
            "noun, used as a suffix": "n-suf",
            "noun, used as a prefix": "n-pref",
            "noun (temporal) (jisoumeishi)": "n-t",
            "numeric": "num",
            "word containing out-dated kanji": "oK",
            "obsolete term": "obs",
            "obscure term": "obsc",
            "out-dated or obsolete kana usage": "ok",
            "old or irregular kana form": "oik",
            "onomatopoeic or mimetic word": "on-mim",
            "pronoun": "pn",
            "poetical term": "poet",
            "polite (teineigo) language": "pol",
            "prefix": "pref",
            "proverb": "proverb",
            "particle": "prt",
            "physics terminology": "physics",
            "quotation": "quote",
            "rare": "rare",
            "sensitive": "sens",
            "slang": "sl",
            "suffix": "suf",
            "word usually written using kanji alone": "uK",
            "word usually written using kana alone": "uk",
            "unclassified": "unc",
            "yojijukugo": "yoji",
            "Ichidan verb": "v1",
            "Ichidan verb - kureru special class": "v1-s",
            "Nidan verb with 'u' ending (archaic)": "v2a-s",
            "Yodan verb with `hu/fu' ending (archaic)": "v4h",
            "Yodan verb with `ru' ending (archaic)": "v4r",
            "Godan verb - -aru special class": "v5aru",
            "Godan verb with `bu' ending": "v5b",
            "Godan verb with `gu' ending": "v5g",
            "Godan verb with `ku' ending": "v5k",
            "Godan verb - Iku/Yuku special class": "v5k-s",
            "Godan verb with `mu' ending": "v5m",
            "Godan verb with `nu' ending": "v5n",
            "Godan verb with `ru' ending": "v5r",
            "Godan verb with `ru' ending (irregular verb)": "v5r-i",
            "Godan verb with `su' ending": "v5s",
            "Godan verb with `tsu' ending": "v5t",
            "Godan verb with `u' ending": "v5u",
            "Godan verb with `u' ending (special class)": "v5u-s",
            "Godan verb - Uru old class verb (old form of Eru)": "v5uru",
            "Ichidan verb - zuru verb (alternative form of -jiru verbs)": "vz",
            "intransitive verb": "vi",
            "Kuru verb - special class": "vk",
            "irregular nu verb": "vn",
            "irregular ru verb, plain form ends with -ri": "vr",
            "noun or participle which takes the aux. verb suru": "vs",
            "su verb - precursor to the modern suru": "vs-c",
            "suru verb - special class": "vs-s",
            "suru verb - irregular": "vs-i",
            "Kyoto-ben": "kyb",
            "Osaka-ben": "osb",
            "Kansai-ben": "ksb",
            "Kantou-ben": "ktb",
            "Tosa-ben": "tsb",
            "Touhoku-ben": "thb",
            "Tsugaru-ben": "tsug",
            "Kyuushuu-ben": "kyu",
            "Ryuukyuu-ben": "rkb",
            "Nagano-ben": "nab",
            "Hokkaido-ben": "hob",
            "transitive verb": "vt",
            "vulgar expression or word": "vulg",
            "`kari' adjective (archaic)": "adj-kari",
            "`ku' adjective (archaic)": "adj-ku",
            "`shiku' adjective (archaic)": "adj-shiku",
            "archaic/formal form of na-adjective": "adj-nari",
            "proper noun": "n-pr",
            "verb unspecified": "v-unspec",
            "Yodan verb with `ku' ending (archaic)": "v4k",
            "Yodan verb with `gu' ending (archaic)": "v4g",
            "Yodan verb with `su' ending (archaic)": "v4s",
            "Yodan verb with `tsu' ending (archaic)": "v4t",
            "Yodan verb with `nu' ending (archaic)": "v4n",
            "Yodan verb with `bu' ending (archaic)": "v4b",
            "Yodan verb with `mu' ending (archaic)": "v4m",
            "Nidan verb (upper class) with `ku' ending (archaic)": "v2k-k",
            "Nidan verb (upper class) with `gu' ending (archaic)": "v2g-k",
            "Nidan verb (upper class) with `tsu' ending (archaic)": "v2t-k",
            "Nidan verb (upper class) with `dzu' ending (archaic)": "v2d-k",
            "Nidan verb (upper class) with `hu/fu' ending (archaic)": "v2h-k",
            "Nidan verb (upper class) with `bu' ending (archaic)": "v2b-k",
            "Nidan verb (upper class) with `mu' ending (archaic)": "v2m-k",
            "Nidan verb (upper class) with `yu' ending (archaic)": "v2y-k",
            "Nidan verb (upper class) with `ru' ending (archaic)": "v2r-k",
            "Nidan verb (lower class) with `ku' ending (archaic)": "v2k-s",
            "Nidan verb (lower class) with `gu' ending (archaic)": "v2g-s",
            "Nidan verb (lower class) with `su' ending (archaic)": "v2s-s",
            "Nidan verb (lower class) with `zu' ending (archaic)": "v2z-s",
            "Nidan verb (lower class) with `tsu' ending (archaic)": "v2t-s",
            "Nidan verb (lower class) with `dzu' ending (archaic)": "v2d-s",
            "Nidan verb (lower class) with `nu' ending (archaic)": "v2n-s",
            "Nidan verb (lower class) with `hu/fu' ending (archaic)": "v2h-s",
            "Nidan verb (lower class) with `bu' ending (archaic)": "v2b-s",
            "Nidan verb (lower class) with `mu' ending (archaic)": "v2m-s",
            "Nidan verb (lower class) with `yu' ending (archaic)": "v2y-s",
            "Nidan verb (lower class) with `ru' ending (archaic)": "v2r-s",
            "Nidan verb (lower class) with `u' ending and `we' conjugation (archaic)": "v2w-s",
            "architecture term": "archit",
            "astronomy, etc. term": "astron",
            "baseball term": "baseb",
            "biology term": "biol",
            "botany term": "bot",
            "business term": "bus",
            "economics term": "econ",
            "engineering term": "engr",
            "finance term": "finc",
            "geology, etc. term": "geol",
            "law, etc. term": "law",
            "mahjong term": "mahj",
            "medicine, etc. term": "med",
            "music term": "music",
            "Shinto term": "Shinto",
            "shogi term": "shogi",
            "sports term": "sports",
            "sumo term": "sumo",
            "zoology term": "zool",
            "jocular, humorous term": "joc",
            "anatomical term": "anat"
        }

    def convert_tag(self, tag: str) -> str:
        return self.tags[tag]
