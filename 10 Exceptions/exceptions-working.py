#!/usr/bin/python3
# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

def main():
    try:
        for line in readfile('lines.xtxt'): print(line.strip())
    except IOError:
        print('Error Occured!!!')
    except ValueError as e:
        print('Antoher error!!', e)
def readfile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else: raise ValueError('File name must end with .txt')

if __name__ == "__main__": main()
