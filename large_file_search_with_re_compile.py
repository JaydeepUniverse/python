#!/usr/bin/env python2.7

import re

def run_search():

    pattern = "HREF"
    pattern_compile = re.compile(pattern)
    infile = open("largefile", "r")
    lines = 0
    match_count = 0

    for line in infile:
        match = pattern_compile.search(line)
        if match:
            match_count += 1
        lines += 1
    return(lines, match_count)

if __name__ == "__main__":
    lines, match_count = run_search()
    print "Lines : ", lines
    print "Match_Count : ", match_count
