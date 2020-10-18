import time

class Timer():
	def __init__(self, count = 1):
		self.count = count

	def __enter__(self):
		self.start = time.time()
		return self.start

	def __exit__(self, *args):
		self.stop = time.time()
		print("Выполнение заняло %.5f секунд" % (self.stop - self.start))

	def __call__(self, func):
		def wrapper():
			avg_time = 0
			for _ in range(self.count):
				t0 = time.time()
				func()
				t1 = time.time()
				avg_time += (t1 - t0)
				avg_time /= self.count
			print("Выполнение заняло %.5f секунд" % avg_time)
		return wrapper

# тестовый код для проверки
if __name__ == "__main__":
    time_this = Timer(count = 1)

    @time_this
    def f():
        for i in range(10000000):
            pass
    print("Тест декоратора")
    f()
    print("Тест контекстного менеджера")
    with Timer() as t:
        a = list(range(10000000))
