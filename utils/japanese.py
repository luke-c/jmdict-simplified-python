from utils.constants import HIRAGANA_START, HIRAGANA_END, KATAKANA_START, KATAKANA_END, KANJI_START, KANJI_END, \
    PROLONGED_SOUND_MARK


def is_kana(text: str) -> bool:
    if not text:
        return False

    return all(is_char_kana(char) for char in text)


def any_kana(text: str) -> bool:
    if not text:
        return False

    return any(is_char_kana(char) for char in text)


def is_hiragana(text: str) -> bool:
    if not text:
        return False

    return all(is_char_hiragana(char) for char in text)


def is_katakana(text: str) -> bool:
    if not text:
        return False

    return all(is_char_katakana(char) for char in text)


def is_kanji(text: str) -> bool:
    if not text:
        return False

    return all(is_char_kanji(char) for char in text)


def any_kanji(text: str) -> bool:
    if not text:
        return False

    return any(is_char_kanji(char) for char in text)


def is_char_kana(char: str) -> bool:
    if not char:
        return False

    return is_char_hiragana(char) or is_char_katakana(char)


def is_char_hiragana(char: str) -> bool:
    if not char:
        return False

    if is_char_long_dash(char):
        return True

    return is_char_in_range(char, HIRAGANA_START, HIRAGANA_END)


def is_char_katakana(char: str) -> bool:
    return is_char_in_range(char, KATAKANA_START, KATAKANA_END)


def is_char_kanji(char: str) -> bool:
    return is_char_in_range(char, KANJI_START, KANJI_END)


def is_char_in_range(char: str, start: int, end: int) -> bool:
    code: int = ord(char)
    return start <= code <= end


def is_char_long_dash(char: str = ''):
    code: int = ord(char)
    return code == PROLONGED_SOUND_MARK
