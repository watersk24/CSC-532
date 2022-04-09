"""
Name: Kevin Waters
Date: Jan 25, 2022
"""


def convert_to_list(file):
    file = open(file)
    int_list = []
    for line in file:
        int_list.append(int(line.strip()))
    return int_list


def bubble_sort(file):
    lst = convert_to_list(file)
    for i in range(len(lst)):
        for j in range((len(lst) - 1), 0, -1):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
    file = open('out.txt', 'w')
    for item in lst:
        file.write(str(item) + '\n')
    return file


def main():
    bubble_sort('numbers.txt')


if __name__ == "__main__":
    main()
