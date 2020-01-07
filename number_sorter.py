#Python Number Sorter
#Haven Smith
#7 January 2020
#_______________________________________________________________________
numbers = []

with open("unsorted_numbers.txt") as f:
    for line in f:
        numbers.append(int(line))

numbers.sort()

with open("sorted_numbers.txt", "w") as f:
    for x in numbers:
        f.write(str(x) + "\n")

print("Numbers all sorted!")