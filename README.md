# DIFFERENCE CALCULATOR

### Hexlet tests and linter status:
[![Actions Status](https://github.com/sergey-royt/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/sergey-royt/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/ea06a29ced52fcce1ee9/maintainability)](https://codeclimate.com/github/sergey-royt/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/ea06a29ced52fcce1ee9/test_coverage)](https://codeclimate.com/github/sergey-royt/python-project-50/test_coverage)

### Description:
This cli-application can compare two JSON or YAML files and show difference between them.

|File format      |Output format | Asciinema                                                       |
|:----------------|--------------|-----------------------------------------------------------------|
|JSON             |Stylish       |  [Link](https://asciinema.org/a/queDiNyUn2QfPXTc5naUlDzwD)      |
|YML/YAML         |Stylish       |  [Link](https://asciinema.org/a/1PvMTyxHukx4KBdgCywuX6ClX)      |
|Nested JSON      |Stylish       |  [Link](https://asciinema.org/a/k51nLHNRLoXmC7S7KoaLIfzZ6)      |
|Nested Yaml      |Plain         |  [Link](https://asciinema.org/a/8UfHsiXTTuwU9e7rZz2LPCTeJ)      |
|Nested Yaml      |Json          |  [Link](https://asciinema.org/a/UlSw0JegIYkziWSLS2cmV5SNc)      |

### Installation:

1. `git clone https://github.com/sergey-royt/python-project-50.git`
2. `python3 -m pip install --user dist/*.whl`

### Usage:

`gendiff [-h] [-f FORMAT] first_file second_file`

#### positional arguments:
* `first_file`
* `second_file`

#### optional arguments:
* -h, --help            show help message and exit
* -f FORMAT, --format FORMAT
                        set format of output
#### formats available:
* stylish - default formatter
* plain - text style formatter
* json - output in form of json file
