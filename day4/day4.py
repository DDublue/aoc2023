#!/usr/bin/env python3

# Advent of Code 2023
# Day 4: Scratchcards
# ----------------------------------------------------------------------------
import time


def part1(file=str):
    ans = 0
    with open(file, 'r') as f:
        for line in f.read().splitlines():
            left, right = line.split(" | ")
            _, left = left.split(": ")
            left, right = set(left.split()), set(right.split())
            ans += int(2**(len(left.intersection(right))-1))
    return ans


def part2(file=str):
    ans = 0
    with open(file, 'r') as f:
        lines = f.read().splitlines()
        copies = [1] * (len(lines)+1)
        copies[0] = 0
        for card, line in enumerate(lines, 1):
            if not copies[card]:
                break
            left, right = line.split(" | ")
            _, left = left.split(": ")
            left, right = set(left.split()), set(right.split())
            matching = len(left.intersection(right))
            for c in range(matching):
                copies[card+c+1] += copies[card]
            ans += copies[card]
    return ans


def main():
    start1 = time.monotonic()
    p1 = part1("/home/darwu/projects/aoc2023/day4/input.txt")
    end1 = time.monotonic()
    print(f"[{(end1 - start1)*1000:.3f} ms]", end=" ")
    print(f"Part 1: {p1}")
    start2 = time.monotonic()
    p2 = part2("/home/darwu/projects/aoc2023/day4/input.txt")
    end2 = time.monotonic()
    print(f"[{(end2 - start2)*1000:.3f} ms]", end=" ")
    print(f"Part 2: {p2}")
    return None


if __name__ == "__main__":
    main()