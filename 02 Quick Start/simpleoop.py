#!/usr/bin/python3

# simple fibonacci series
# the sum of two elements defines the next set
class Fibonacci():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def series(self):
        while(True):
            yield(self.b)
            self.a, self.b = self.b, self.a + self.b

f = Fibonacci(0, 1)
for k in f.series():
    if k > 500: break    
    print(k, end=' ')

