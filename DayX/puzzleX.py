
def problem1(filename: str) -> int:
    with open(filename, "rt") as reader:
        while line := reader.readline():
            line = line.rstrip()
            print(line)
    return 999

def problem2(filename: str) -> int:
    with open(filename, "rt") as reader:
        while line := reader.readline():
            line = line.rstrip()
            print(line)
    return 999

if __name__ == '__main__':
    filename_sample = "input_sample.txt"
    filename = "input.txt"

    print(f"Answer to sample problem is {problem1(filename_sample)}")
    #print(f"Answer to problem 1 is {problem1(filename)}")
    #print(f"Answer to sample problem for 2 is {problem2(filename_sample)}")
    #print(f"Answer to problem 2 is {problem2(filename)}")
