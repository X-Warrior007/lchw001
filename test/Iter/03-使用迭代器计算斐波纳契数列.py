class Fib(object):
    def __init__(self,n):
        # 计算次数
        self.n = n
        # 当前计算次数
        self.index = 0
        self.number1 = 0
        self.number2 = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < self.n:
            data = self.number1
            self.number1,self.number2 = self.number2,self.number1+self.number2
            self.index += 1
            return data
        else:
            raise StopIteration

# 0 1 1 2 3 5 某一项的值等于前两项的和
for i in Fib(10): # fibiter= iter(Fib())
    # next(fibiter)
    print(i)

print(list(Fib(10)))
print(tuple(Fib(10)))