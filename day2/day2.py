#!/usr/bin/env python3

# Advent of Code 2023
# Day 2: Cube Conundrum
# ----------------------------------------------------------------------------
import time


def part1(file=str):
    ans = 0
    with open(file, 'r') as f:
        for i, line in enumerate(f.readlines(), 1): # each input file line
            rolls = line.split(": ")
            rolls = rolls[1].split("; ")
            for j, r in enumerate(rolls): # each set in a game
                temp = r.split(" ")
                possible = can = True
                for k in range(len(temp)-1, -1, -2): # each roll in a set
                    if temp[k][0] == 'r' and int(temp[k-1]) > 12 \
                    or temp[k][0] == 'b' and int(temp[k-1]) > 14 \
                    or temp[k][0] == 'g' and int(temp[k-1]) > 13:
                        possible = False
                        can = False
                        break
                    if not can:
                        break
                if not possible:
                    break
            if possible:
                ans += i
    return ans


def part2(file=str):
    ans = 0
    with open(file, 'r') as f:
        for i, line in enumerate(f.readlines(), 1): # each input file line
            red = blue = green = 0
            rolls = line.split(": ")
            rolls = rolls[1].split("; ")
            for j, r in enumerate(rolls): # each set in a game
                temp = r.split(" ")
                for k in range(len(temp)-1, -1, -2): # each roll in a set
                    num = int(temp[k-1])
                    if temp[k][0] == 'r' and num > red:
                        red = num
                    elif temp[k][0] == 'b' and num > blue:
                        blue = num
                    elif temp[k][0] == 'g' and num > green:
                        green = num
            ans += red * blue * green
    return ans


def main():
    start1 = time.monotonic()
    p1 = part1("/home/darwu/projects/aoc2023/day2/input.txt")
    end1 = time.monotonic()
    print(f"[{(end1 - start1)*1000:.3f} ms]", end=" ")
    print(f"Part 1: {p1}")
    start2 = time.monotonic()
    p2 = part2("/home/darwu/projects/aoc2023/day2/input.txt")
    end2 = time.monotonic()
    print(f"[{(end2 - start2)*1000:.3f} ms]", end=" ")
    print(f"Part 2: {p2}")
    return None


if __name__ == "__main__":
    main()