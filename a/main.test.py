from sys import path
path.insert(0, '..')
from test import test
path.pop(0)
del path
from main import main
test = test(main)
if __name__ == '__main__':
	test(4, 4)
	test(7, 11)
	test(6, 14)
