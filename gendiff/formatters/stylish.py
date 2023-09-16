def stylish(diff, replacer=' ', spaces_count=1):
    return stylize(diff, replacer, spaces_count)


def stylize(diff, replacer=' ', spaces_count=1, level=1):

    result = []

    for item in diff:

        prekey_replacer = replacer * (spaces_count * level * 4 - 2)
        prebracket_replacer = replacer * (spaces_count * level * 4)

        match item['action']:

            case 'nested':
                result.append(
                    f'{prekey_replacer}  {item["key"]}: {"{"}'
                )
                kids = stylize(
                    item["children"],
                    replacer, spaces_count,
                    level + 1
                )
                result.append(
                    f'{kids}'
                    f'\n{prebracket_replacer}{"}"}'
                )

            case 'added':
                stringed_val = stringify(
                    item["value"],
                    replacer,
                    spaces_count,
                    level
                )
                result.append(
                    f'{prekey_replacer}+ {item["key"]}: '
                    f'{stringed_val}'
                )

            case 'deleted':
                stringed_val = stringify(
                    item["value"],
                    replacer,
                    spaces_count,
                    level
                )
                result.append(
                    f'{prekey_replacer}- {item["key"]}: '
                    f'{stringed_val}'
                )

            case 'unchanged':
                stringed_val = stringify(
                    item["value"],
                    replacer,
                    spaces_count,
                    level
                )
                result.append(
                    f'{prekey_replacer}  {item["key"]}: '
                    f'{stringed_val}'
                )

            case 'changed':
                stringed_old_val = stringify(
                    item["old_value"],
                    replacer,
                    spaces_count,
                    level
                )
                result.append(
                    f'{prekey_replacer}- {item["key"]}: '
                    f'{stringed_old_val}'
                )

                stringed_new_val = stringify(
                    item["new_value"],
                    replacer,
                    spaces_count,
                    level
                )
                result.append(
                    f'{prekey_replacer}+ {item["key"]}: '
                    f'{stringed_new_val}'
                )
    if level == 1:
        result = ['{'] + result + ['}']
    return '\n'.join(result)


def stringify(val, replacer=' ', spaces_count=1, level=0):

    if isinstance(val, dict):
        result = []
        prekey_replacer = replacer * (spaces_count * level * 4 + 4)
        prebracket_replacer = replacer * (spaces_count * level * 4)

        result.append('{')
        for key in val:

            result.append(
                f'\n{prekey_replacer}{key}: '
                f'{stringify(val[key], replacer, spaces_count + 1, level)}'
            )

        result.append(f'\n{prebracket_replacer}{"}"}')
        return ''.join(result)

    if val is None:
        return 'null'
    if isinstance(val, bool):
        return str(val).lower()
    if isinstance(val, str):
        return val
    return str(val)
