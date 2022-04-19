# list_splitter.py

import sys
import re

def list_split(list, divider):
    return [list[i:i+divider] for i in range(0, len(list), divider)]

if(len(sys.argv) > 2):
    reg_ex = "([^[]+(?=]))"

    list = [int(i) for i in re.search(reg_ex, sys.argv[1]).group().split(",")]

    divider = int(sys.argv[2])

    print(list_split(list, divider))
