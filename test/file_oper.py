#!/usr/bin/python
# -*- coding: utf-8 -*-

with open("src/file.txt", mode='r', encoding='utf-8') as f:
    for line in f:
        print(line)