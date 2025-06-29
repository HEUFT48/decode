# id решение 139657513
def decode(de_code: str) -> str:
    stack = []
    code = ""
    num = 0

    for element in de_code:
        if element.isdigit():
            num = num * 10 + int(element)
        elif element == '[':
            stack.append((code, num))
            code, num = "", 0
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
