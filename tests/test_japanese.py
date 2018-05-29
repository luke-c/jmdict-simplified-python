import pytest

from utils.japanese import is_japanese, is_romaji, is_mixed


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("泣き虫", True),
        ("あア", True),
        ("２月", True),  # Zenkaku numbers allowed
        ("泣き虫。！〜＄", True),  # Zenkaku/JA punctuation
        ("泣き虫.!~$", False),  # Latin punctuation fails
        ("A泣き虫", False),
        ("≪偽括弧≫", False),
        ("A", False),
        ("泣き虫。＃！〜〈〉《》〔〕［］【】（）｛｝〝〟", True),  # With Zenkaku punctuation
        ("泣き虫.!~", False),  # Romaji punctuation is not Japanese
        ("０１２３４５６７８９", True),  # Zenkaku numbers are Japanese
        ("0123456789", False),  # Latin numbers are not Japanese
        ("　", True),  # Japanese space is Japanese
        (" ", False),  # English space is not Japanese
        ("ＭｅＴｏｏ", True),  # Zenkaku latin letters are Japanese
        ("２０１１年", True),  # Mixed with numbers is Japanese
        ("ﾊﾝｶｸｶﾀｶﾅ", True),  # Hankaku Katakana is Japanese
        ("Latin text", False),
    ],
)
def test_is_japanese(test_input, expected):
    assert is_japanese(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (None, False),
        ("", False),
        ("A", True),
        ("xYz", True),
        ("Tōkyō and Ōsaka", True),
        ("Tokyo and Osaka", True),
        ("あアA", False),
        ("お願い", False),
        ("熟成", False),
        ("a*b&c-d", True),  # Passes Latin punctuation
        ("0123456789", True),  # Passes Latin numbers
        ("a！b&cーd", False),  # Fails Zenkaku punctuation
        ("ｈｅｌｌｏ", False),  # Fails Zenkaku Latin
    ],
)
def test_is_romaji(test_input, expected):
    assert is_romaji(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("Aア", True),
        ("Aあ", True),
        ("Aあア", True),
        ("２あア", False),
        ("お腹A", True),
        ("お腹", False),
        ("腹", False),
        ("A", False),
        ("あ", False),
        ("ア", False),
    ],
)
def test_is_mixed(test_input, expected):
    assert is_mixed(test_input) == expected


def test_is_mixed_with_pass_kanji_false():
    assert not is_mixed("お腹A", pass_kanji=False)
