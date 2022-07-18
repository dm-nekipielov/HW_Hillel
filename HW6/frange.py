class frange():
    def __init__(self, start, stop=None, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        if self.stop is None:
            self.stop = self.start
            self.start = 0

    def __iter__(self):
        count = 0
        while True:
            val = self.start + self.step * count
            if self.step > 0 and val >= self.stop:
                break
            if self.step < 0 and val <= self.stop:
                break
            yield self.start + self.step * count
            count += 1


assert (list(frange(5)) == [0, 1, 2, 3, 4])
assert (list(frange(2, 5)) == [2, 3, 4])
assert (list(frange(2, 10, 2)) == [2, 4, 6, 8])
assert (list(frange(10, 2, -2)) == [10, 8, 6, 4])
assert (list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert (list(frange(1, 5)) == [1, 2, 3, 4])
assert (list(frange(0, 5)) == [0, 1, 2, 3, 4])
assert (list(frange(0, 0)) == [])
assert (list(frange(100, 0)) == [])

print('SUCCESS!')
