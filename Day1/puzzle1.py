
def create_lists(lines: [str]) -> ([int], [int]):
    list_a = []
    list_b = []

    for line in lines:
        line = line.rstrip()
        numbers = line.split(" ")
        number_a = int(numbers[0])
        number_b = int(numbers[-1])

        list_a.append(number_a)
        list_b.append(number_b)

    return list_a, list_b

def problem1(filename: str) -> int:
    with open(filename, "rt") as reader:
        list_a, list_b = create_lists(reader.readlines())

    list_a.sort()
    list_b.sort()

    differences = 0

    for (a,b) in zip(list_a, list_b):
        differences += (a-b)*(a>b) + (b-a)*(a<b)

    return differences

def problem2(filename: str) -> int:
    with open(filename, "rt") as reader:
        list_a, list_b = create_lists(reader.readlines())

    differences_scaled = 0

    for a in list_a:
        scaling_factor = list_b.count(a)
        differences_scaled += a*scaling_factor

    return differences_scaled

if __name__ == '__main__':
    filename_sample = "input_sample.txt"
    filename = "input.txt"

    #print(f"Answer to sample problem is {problem1(filename_sample)}")
    print(f"Answer to problem 1 is {problem1(filename)}")
    #print(f"Answer to sample problem for 2 is {problem2(filename_sample)}")
    print(f"Answer to problem 2 is {problem2(filename)}")
