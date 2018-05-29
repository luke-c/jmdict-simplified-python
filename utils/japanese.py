from utils.constants import (
    HIRAGANA_START,
    HIRAGANA_END,
    KATAKANA_START,
    KATAKANA_END,
    KANJI_START,
    KANJI_END,
    PROLONGED_SOUND_MARK,
    JAPANESE_RANGES,
    ROMAJI_RANGES,
)


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


def is_japanese(text: str) -> bool:
    if not text:
        return False

    return all(is_char_japanese(char) for char in text)


def is_romaji(text: str) -> bool:
    if not text:
        return False

    return all(is_char_romaji(char) for char in text)


def is_mixed(text: str, pass_kanji=True) -> bool:
    has_kanji = False

    if not pass_kanji:
        has_kanji = any(is_kanji(char) for char in text)

    is_hiragana_or_katakana = any(is_hiragana(char) for char in text) or any(
        is_katakana(char) for char in text
    )

    return (
        is_hiragana_or_katakana
        and any(is_romaji(char) for char in text)
        and not has_kanji
    )


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


def is_char_japanese(char: str) -> bool:
    return any(is_char_in_range(char, start, end) for (start, end) in JAPANESE_RANGES)


def is_char_romaji(char: str) -> bool:
    return any(is_char_in_range(char, start, end) for (start, end) in ROMAJI_RANGES)


def is_char_in_range(char: str, start: int, end: int) -> bool:
    code: int = ord(char)
    return start <= code <= end


def is_char_long_dash(char: str = ""):
    code: int = ord(char)
    return code == PROLONGED_SOUND_MARK
