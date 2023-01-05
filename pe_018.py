string = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

import numpy as np
import math

def line_count(text):                                                               # Pyramidenhöhe
    counter = 0
    for line in string.splitlines(): counter += 1
    return counter

def make_array(text):
    N = line_count(text)
    array_in = np.zeros([N, N], dtype = int)
    for i in range(N):
        for j in range(len(text.splitlines()[i].split(" "))):
            array_in[i, j] = text.splitlines()[i].split(" ")[j]
    return array_in

def find_max_sum(text):
    matrix = make_array(string)
    for i in range(len(matrix)-1, 0, -1):
        for j in range(len(matrix[i])-1):
            if matrix[i, j] >= matrix[i, j+1]: matrix[i-1, j] += matrix[i, j]
            else: matrix[i-1, j] += matrix[i, j+1]
    return matrix[0,0]

find_max_sum(string)
