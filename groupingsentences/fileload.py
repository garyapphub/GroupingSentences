# -*- coding: utf-8 -*-
"""
:集合各种计算句子间距离的函数，可以自己选择使用
"""

import os

def load_cells_from_file(file_name, encoding='gb18030', max_items = 500000):
    #FILENAME = './dataset/1.csv'
    cells = []
    count = 0
    with open(file_name, 'r', encoding=encoding) as f:
        while True: 
            count += 1
            # Get next line from file 
            line = f.readline() 
            # if line is empty 
            # end of file is reached 
            if not line: 
                break
            if count > max_items:
                break
            #print("Line{}: {}".format(count, line.strip())) 
            arr = line.strip().split(',')
            if len(arr) > 0:
                cells.append(arr[0])
            else:
                cells.append(line.strip())
        f.close()
    return cells