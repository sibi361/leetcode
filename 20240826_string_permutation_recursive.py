#!/bin/python3

import math
import os
import random
import re
import sys


def check_if_palindrome(ip):
    return ip == ip[::-1]


def gen_substrings(ip, parent=False):
    if not ip:
        return []

    if len(ip) == 1:
        return [ip]

    out = []
    for string in [ip, ip[::-1]]:
        for i, c in enumerate(string):
            if parent:
                print(f"[{"#" * (i + 1)}{" " * (len(string) - i - 1)}]",
                      end="\r", flush=True)

            new_sub = string[0:i] + string[i+1:]
            out.extend(
                [c + substring for substring in gen_substrings(new_sub)])

        if parent:
            print()
    return list(set(out))


if __name__ == '__main__':
    ip = "abcdabcd"

    permutations = gen_substrings(ip, True)

    # print(permutations)
    print(f"Total permutations: {len(permutations)}")

    palindromes = [x for x in permutations if check_if_palindrome(x)]

    print(palindromes)
    print(f"Total palindromes: {len(palindromes)}")
