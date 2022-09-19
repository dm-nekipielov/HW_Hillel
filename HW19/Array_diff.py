# https://www.codewars.com/kata/523f5d21c841566fde000009
# Your goal in this kata is to implement a difference function,
# which subtracts one list from another and returns the result.
#
# It should remove all values from list a, which are present in list b keeping their order.
# array_diff([1,2],[1]) == [2]

# If a value is present in b, all of its occurrences must be removed from the other:
# array_diff([1,2,2,2,3],[2]) == [1,3]


def array_diff(a: list, b: list) -> list:
    for i in b:
        while i in a:
            a.remove(i)
    return a


if __name__ == "__main__":
    assert (array_diff([1, 2], [1]) == [2])
    assert (array_diff([1, 2, 2], [1]) == [2, 2])
    assert (array_diff([1, 2, 2], [2]) == [1])
    assert (array_diff([1, 2, 2], []) == [1, 2, 2])
    assert (array_diff([], [1, 2]) == [])
    assert (array_diff([1, 2, 3], [1, 2]) == [3])
    print("Success!")
