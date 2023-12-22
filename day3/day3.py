#!/usr/bin/env python3

# Advent of Code 2023
# Day 3: Gear Ratios
# ----------------------------------------------------------------------------
import time


def issymbol(s):
    # print(s)
    return not (s.isdigit() or s == '.')

def part1(file=str):
    ans = 0
    with open(file, 'r') as f:
        lines = f.read().splitlines()
        line_cnt = len(lines)
        line_len = len(lines[0])
        for i in range(len(lines)):
            j = 0
            k = 0
            while j < line_len:
                if lines[i][j].isdigit():
                    # Find location of entire number
                    while k < line_len and lines[i][k].isdigit():
                        k += 1
                    
                    # Check perimeter for any symbols
                    if j > 0 and issymbol(lines[i][j-1]):
                        ans += int(lines[i][j:k])
                    elif k < line_len-1 and issymbol(lines[i][k]):
                        ans += int(lines[i][j:k])
                    else:
                        start = j-1 if j > 0 else j
                        end = k+1 if k < line_len-1 else k
                        if i > 0:
                            for col in range(start, end):
                                if issymbol(lines[i-1][col]):
                                    ans += int(lines[i][j:k])
                                    break
                        if i < line_cnt-1:
                            for col in range(start, end):
                                if issymbol(lines[i+1][col]):
                                    ans += int(lines[i][j:k])
                                    break
                                
                    # Set 'j' to current position
                    j = k
                else:
                    j += 1
                    k += 1
            
    return ans


def part2(file=str):
    ans = 0
    with open(file, 'r') as f:
        lines = f.readlines()
    return ans


def main():
    start1 = time.monotonic()
    p1 = part1("/home/darwu/projects/aoc2023/day3/input.txt")
    end1 = time.monotonic()
    print(f"[{(end1 - start1)*1000:.3f} ms]", end=" ")
    print(f"Part 1: {p1}")
    start2 = time.monotonic()
    p2 = part2("/home/darwu/projects/aoc2023/day3/input.txt")
    end2 = time.monotonic()
    print(f"[{(end2 - start2)*1000:.3f} ms]", end=" ")
    print(f"Part 2: {p2}")
    return None


if __name__ == "__main__":
    main()