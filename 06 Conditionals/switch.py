#!/usr/bin/python3
# switch.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    choices = dict(
        one = 'First',
        two = 'Second',
        three = 'Third',
        four = 'Fourth',
        five = 'Fifth'
    )
    v = 'seven'
    print(choices.get(v, 'other'))

if __name__ == "__main__": main()
