from jmdict import Parser, TagService


def main() -> None:
    tag_service = TagService()
    parser = Parser(tag_service)

    parser.parse_jmdict()


if __name__ == '__main__': main()
