#!/usr/bin/env python3

# Advent of Code 2023
# Day 1: Trebuchet?!
# ----------------------------------------------------------------------------
import time


def part1(file=str):
    summ = 0
    with open(file, 'r') as f:
        for line in f.readlines():
            first = last = 0
            r_line = line[::-1]
            for char in line:
                if char.isdigit():
                    first = int(char)
                    last = first
                    break
            for char in r_line:
                if char.isdigit():
                    last = int(char)
                    break
            summ += first * 10 + last
    return summ


def part2(file=str):
    numbers = {"one": 1, "two": 2, "three": 3, "four": 4,
               "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    summ = 0
    with open(file, 'r') as f:
        for line in f.readlines():
            first = last = 0
            for i in range(len(line)):
                if line[i].isdigit():
                    first = int(line[i])
                    last = first
                    break
                else:
                    found = False
                    for key in numbers:
                        if line[i:].startswith(key):
                            first = numbers[key]
                            last = first
                            found = True
                            break
                    if found:
                        break
            for i in range(len(line)-1, -1, -1):
                if line[i].isdigit():
                    last = int(line[i])
                    break
                else:
                    found = False
                    for key in numbers:
                        if line[i:].startswith(key):
                            last = numbers[key]
                            found = True
                            break
                    if found:
                        break
            summ += first * 10 + last
    return summ


def main():
    start1 = time.monotonic()
    p1 = part1("/home/darwu/projects/aoc2023/day1/input.txt")
    end1 = time.monotonic()
    print(f"[Execution time: {(end1 - start1)*1000:.3f} ms]", end=" ")
    print(f"Part 1: {p1}")
    start2 = time.monotonic()
    p2 = part2("/home/darwu/projects/aoc2023/day1/input.txt")
    end2 = time.monotonic()
    print(f"[Execution time: {(end2 - start2)*1000:.3f} ms]", end=" ")
    print(f"Part 2: {p2}")
    return None


if __name__ == "__main__":
    main()