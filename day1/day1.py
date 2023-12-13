# Advent of Code 2023
# Day 1: Trebuchet?!
# ----------------------------------------------------------------------------
import re
import time


def part1(file=str):
    summ = 0
    with open(file, 'r') as f:
        for line in f.readlines():
            summ += int(re.search(r"\d", line).group()) * 10 \
                    + int(re.search(r"\d", line[::-1]).group())
    return summ


def part2(file=str):
    numbers = {"one": 1, "two": 2, "three": 3, "four": 4,
               "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    summ = 0
    with open(file, 'r') as f:
        for line in f.readlines():
            first = re.search(r"\d|one|two|three|four|five|six|seven|eight|nine", line).group()
            last = re.search(r"\d|one|two|three|four|five|six|seven|eight|nine", line[::-1]).group()
            if first.isdigit():
                first = int(first)
            else:
                first = numbers[first]
                re.sub(r"<first>", "", line)
            if last.isdigit():
                last = int(last)
            elif not last:
                pass
            else:
                last = numbers[last]
            summ += first * 10 + last
    return summ


def main():
    res = None
    part = int(input("1 or 2> "))
    while part != 1 and part != 2:
        part = int(input("1 or 2> "))
    if part == 1:
        res = part1("day1\input.txt")
    else:
        res = part2("day1\input.txt")
    print(f"Part {part} Sum: {res}")
    return res

if __name__ == "__main__":
    main()