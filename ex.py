#!/usr/bin/env python3
# Modify file data
# -*- coding: utf-8 -*-

fs = open('PSIconsLowRes_.dat','rb')
stm = fs.read()
fs.close()

i = 4
while True:
    p = stm.find(b'IEND', i)
    if p != -1:
        fs = open('Low2_\\%08X.png' % i, 'wb')
        fs.write(stm[i:p+8])
        i = p+8
        fs.close()
    else:
        break
