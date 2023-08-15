import sys

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == '-h':
            print('''gendiff -h
usage: gendiff [-h] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output''')


if __name__ == '__main__':
    main()