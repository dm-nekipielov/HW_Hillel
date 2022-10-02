test_dict = {"a": 1, "b": 2, "c": 3}


def func1(el):
    return el * 3


def func2(el):
    return el * 10


class custom_map:
    def __init__(self, func_for_key, func_for_val, dictionary):
        self.func_for_key = func_for_key
        self.func_for_val = func_for_val
        self._vals = iter(dictionary.values())
        self._keys = iter(dictionary.keys())

    def __iter__(self):
        return self

    def __next__(self):
        return self.func_for_key(next(self._keys)), self.func_for_val(
            next(self._vals))


print(dict(custom_map(func1, func2, test_dict)))
