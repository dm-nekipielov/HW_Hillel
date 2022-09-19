# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c
# The goal of this exercise is to convert a string to a new string where each character
# in the new string is "(" if that character appears only once in the original string,
# or ")" if that character appears more than once in the original string.
# Ignore capitalization when determining if a character is a duplicate.
#
# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("

def duplicate_encode(word: str) -> str:
    lower_case_word = word.lower()
    return "".join(")" if lower_case_word.count(i) > 1 else "(" for i in lower_case_word)


if __name__ == "__main__":
    assert (duplicate_encode("din") == "(((")
    assert (duplicate_encode("recede") == "()()()")
    assert (duplicate_encode("Success") == ")())())")
    assert (duplicate_encode("(( @") == "))((")
    print("Success!")
