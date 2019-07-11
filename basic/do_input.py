#!/usr/bin/env python3
# -*- coding: utf-8 -*-

ADULT_AGE = 18


name = input('Please Enter your name:')
print('Your name is:',name)

age = int(input('Please Enter your age:'))

if age > ADULT_AGE:
    print('you are adult')
else:
    print('you are teen')



