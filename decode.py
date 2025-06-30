# id решение 139693592
import string


def decode(encoded_string: str) -> str:
    DECIMAL_BASE = 10
    DIGITS = frozenset(string.digits)
    stack: list[str] = []
    code = ''
    num = 0

    for element in encoded_string:
        if element in DIGITS:
            num = num * DECIMAL_BASE + int(element)
        elif element == '[':
            stack.append((code, num))
            code, num = '', 0
        elif element == ']':
            prev_str, prev_num = stack.pop()
            code = prev_str + code * prev_num
        else:
            code += element

    return code


def main():
    decode_inp = input().strip()
    code_good = decode(decode_inp)
    print(code_good)


if __name__ == '__main__':
    main()
