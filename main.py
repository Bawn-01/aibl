#!/usr/bin/env python3

import subprocess


line =   []

nums = '1234567890'

# tokens
dot = '.'
up ='>'
down = '<'
endPR = '$'
clear = '|'
add = '+'
minus = '-'
divide = '/'
multiply = '*'
save = '?'
a='%'

ops = '*+-/'

lineUP = ''
sumLineUP = 0 * 0
smluOP = ''

cur_char = 0 # 0 == (space), 1 == a ect, ect
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class lexer:
    def __init__(self, ln, fn):
        global line,a,sumLineUP,ops,smluOP, chars, cur_char, lineUP, nums, dot, up, down, endPR, clear, add, minus, divide, multiply, save
        for i in ln:
            if i == clear:
                lineUP = ''
                cur_char = 0
            if i in nums:
                line.append(i)
            if i == dot:
                print(lineUP)
            if i == up:
                cur_char += 1
            if i == down:
                cur_char -= 1
            if i == a:
                lineUP += 'a'
            if i == save:
                if cur_char > 25:
                    lineUP += ' '
                elif cur_char <= 0:
                    lineUP += ' '
                else:
                    lineUP += chars[cur_char]
            if i == endPR:
                exit()
                

while True:
    q = input("aibl :: ")
    lx = lexer(q, 'stdin')
    print(line)
