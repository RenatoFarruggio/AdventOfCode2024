import warnings

@warnings.deprecated()
def transpose_list_of_lists(list_of_lists: [[]]) -> [[]]:
    # Returns the transposed list of lists.
    # E.g.
    # [[1,2,3], [4,5,6], [7,8,9]]
    # ->
    # [[1,4,7], [2,5,8], [3,6,9]]
    #
    # I took this answer from: https://stackoverflow.com/a/6473742

    transposed_list_of_lists = [list(i) for i in zip(*list_of_lists)]
    return transposed_list_of_lists

@warnings.deprecated()
def transpose_list_of_strings(list_of_strings: [str]) -> [str]:
    transposed_list_of_strings = [''.join(line) for line in transpose_list_of_lists(list_of_strings)]
    return transposed_list_of_strings

@warnings.deprecated()
def replace_recursively(string: str, oldvalue: str, newvalue: str) -> str:
    while True:
        should_break = True
        if oldvalue in string:
            should_break = False
            string = string.replace(oldvalue, newvalue)
        if should_break:
            break
    return string


if __name__ == "__main__":
    print("Testing helpers.py")
    dots = '..........'
    print(f"Input string: '{dots}'")
    dots = replace_recursively(dots, '..', '.')
    print(f"Output string: '{dots}'")
