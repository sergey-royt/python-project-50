import argparse
from gendiff.gendiff import make_diff

def main():
    args = parse_arguments()
    print(make_diff(args.first_file, args.second_file, args.format))


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', action='store')
    parser.add_argument('second_file', action='store')
    parser.add_argument('-f',
                        '--format',
                        type=str,
                        default='stylish',
                        help='set format of output')
    return parser.parse_args()


if __name__ == '__main__':
    main()
