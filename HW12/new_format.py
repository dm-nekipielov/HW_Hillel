# 2. Написати фунцію шо задовільняє наступні тести

def new_format(string):
    str_list = list(string)
    for i in range(len(str_list), 0, -3):
        str_list.insert(i, ".")
    return ''.join(str_list).strip(".")


assert (new_format("1000000") == "1.000.000")
assert (new_format("100") == "100")
assert (new_format("1000") == "1.000")
assert (new_format("100000") == "100.000")
assert (new_format("10000") == "10.000")
assert (new_format("0") == "0")
