class StepValueError(ValueError):
    pass

class Iteratore():
    def __init__(self, start, stop, step=1) -> None:
        if step == 0:
            raise StepValueError("Step can not equals to zero (0)")
        
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
        self.begin = True

    def __iter__(self):
        self.pointer = self.start
        self.begin = True
        return self

    def __next__(self):
        if self.step < 0:
            if self.pointer + self.step < self.stop:
                raise StopIteration()
        else:
            if self.pointer + self.step > self.stop:
                raise StopIteration()
        
        if self.begin:
             self.begin = False
        else:
             self.pointer += self.step
        return self.pointer


try:
    iter1 = Iteratore(100, 200, 0)
    for i in iter1:
        print(i, end='')
except StepValueError:
    print("Error <step>'s value")

iter2 = Iteratore(-5, 1)
iter3 = Iteratore(6, 15, 2)
iter4 = Iteratore(5, 1, -1)
iter5 = Iteratore(10, 1)

for i in iter2:
    print(i, end=' ')
print('\niter2 done')
for i in iter3:
    print(i, end=' ')
print('\niter3 done')
for i in iter4:
    print(i, end=' ')
print('\niter4 done')
for i in iter5:
    print(i, end=' ')
print('\niter5 done')




