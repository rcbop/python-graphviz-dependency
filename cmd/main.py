import argparse

from dotgen import DotGenerator
from files import FileCrawler
from imports import ImportsParser


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='path to search')
    args = parser.parse_args()

    files = FileCrawler(args.path).crawl()

    dependencies_map = {}
    for file in files:
        dependencies_map[file] = ImportsParser(file).parse()

    DotGenerator(dependencies_map).generate()


if __name__ == '__main__':
    main()
