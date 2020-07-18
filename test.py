#!/usr/bin/env python3
# Icon Resources Idx file reader
# -*- coding: utf-8 -*-

import re

def getStruct(ss, size=8, base=16, rng=40):
    return [int(ss[i * size:(i + 1) * size], base) for i in range(rng)]

def run():
    pattern = re.compile(r'[^:]+: "([ABCDEF0123456789]*)".*')

    lines = open('IconResources.idx', 'rb').read().decode().split('\r\n')

    for line in lines:
        match = pattern.match(line)
        if match:
            struct = getStruct(match.group(1))
            for i in range(len(struct)):
                if (i%4 == 2) or (i%4 == 3):#and ((i%20!=2) and (i%20!=3)):
                    if struct[i] != 0:
                        print(line)
                        break
##if __name__ == '__main__':
run()
