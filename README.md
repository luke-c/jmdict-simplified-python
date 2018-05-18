# [JMdict-simplified](https://github.com/scriptin/jmdict-simplified), but in Python!

See the jmdict-simplified [readme](https://github.com/scriptin/jmdict-simplified/blob/master/README.md) for more information.

## Building

Requirements: Python 3.6

~~~
Usage examples:
> python convert-jmdict.py
~~~

## Format of JMdict

There are some minor changes compared to jmdict-simplified, namely around the xref and gloss elements.

### Custom types

- `xref` (array of objects) := has the following structures:

      - `kanji` (string) := The kanji keb element this sense applies to
      - `kana` (string) := The kana reb element this sense applies to 
      - `senseIndex` (int) := The index of a sense, counting from 1

    Examples: `{'kanji': "丸", 'kana': "まる", 'senseIndex': 1}`, `{'kanji': "○", 'kana': "まる", 'senseIndex': 1}`, `{'kanji': "二重丸", 'kana': "にじゅうまる", 'senseIndex': null}`, `{'kanji': "漢数字", 'kana': null, 'senseIndex': null}`, etc.

- `tag` (string) := all tags are listed in a separate section of the file, see the description of root JSON object

### Root JSON object
An An array of the following object, each representing one 'entry'

  - `id` (number) := unique identifier
  - `kanji` (array of objects) := kanji (and other non-kana) writings
      - `common` (boolean) := `true` if this particular spelling is common. This field combines all the `*_pri` fields from original files in a same way as [jisho.org][] and other on-line dictionaries do ("common" word markers). It gets rid of bunch of `*_pri` fields which are not typically used. Words marked with "news1", "ichi1", "spec1", "spec2", "gai1" in the original file are treated as common, which may or may not be true according other sources.
      - `text` (string) := any non-kana-only writing, may contain kanji, kana, and some other characters
      - `tags` (array of tags) := tags applied to this writing
  - `kana` (array of objects) := kana-only (with few exceptions) writings, typically considered as "readings", but these can be a word writings by themselves
      - `common` (boolean) := same as for kanji elements
      - `text` (string) := kana-only writing, may only accidentally contain middle-dot and other punctuation-like characters
      - `tags` (array of tags) := same as for kanji
      - `appliesToKanji` (array of strings) := list of kanji writings within this word which this kana version applies to. `"*"` means "all", empty array means "none"
  - `sense` (array of objects) := senses (translations + some related data) for this words
      - `partOfSpeech` (array of tags) := all parts of speech for this sense. Unlike the original dictionary file, this field is never empty/missing. In the original file, part-of-speech from earlier sense elements may apply to following elements, in which case latter don't have defined part-of-speech
      - `appliesToKanji` (array of strings) := list of kanji writings within this word which this sense applies to. `"*"` means "all", empty array means "none"
      - `appliesToKana` (array of strings) := list of kana writings within this word which this sense applies to. `"*"` means "all", empty array means "none"
      - `related` (array of xrefs) := xrefs to related words
      - `antonym` (array of xrefs) := xrefs to antonyms of this word
      - `field` (array of tags) := fields of application
      - `dialect` (array of tags) := dialects
      - `misc` (array of tags) := other related tags
      - `info` (array of strings) := other info
      - `languageSource` (array of objects) := source language info for borrowed words and wasei-eigo
          - `lang` (string) := language code from the ISO 639-2 standard
          - `full` (boolean) := indicates whether the sense element fully or partially describes the source word or phrase of the loanword
          - `wasei` (boolean) := indicates that the Japanese word has been constructed from words in the source language, and not from an actual phrase in that language. See [Wasei-eigo](https://en.wikipedia.org/wiki/Wasei-eigo)
          - `text` (string or null) := text in the language defined by a `lang` element, or `null`
      - `gloss` (array of objects) := translations
          - `lang` (string) := language code from the ISO 639-2 standard
          - `type` (string) := specifies that the gloss is of a particulartype, e.g. "lit" (literal), "fig" (figurative), "expl" (explanation)
          - `text` (string) := a word or phrase

Notes:

1. All fields in all objects are always present, none ever omitted
2. Array fields are never `null`, only empty
3. The only place which allows `null` values is `sense->languageSource->text` field in word element, and xref fields (if at least one xref object exists in the list)

## License

Original XML files, **JMdict_e.xml** and **JMnedict.xml** are property of the Electronic Dictionary Research and Development Group, and are used in conformance with the Group's [licence](http://www.edrdg.org/edrdg/licence.html). Project started in 1991 by [Jim Breen](http://www.csse.monash.edu.au/~jwb/).

All derived files are distributed under the same license, as the original license requires it.

Source files of this project (excluding distribution archives containing JSON files) are available under [Creative Commons Attribution-ShareAlike License v4.0](http://creativecommons.org/licenses/by-sa/4.0/). See [LICENSE.txt](LICENSE.txt)
