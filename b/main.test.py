from main import main
from sys import path
path.insert(0, '..')
from test import test
path.pop(0)
del path
test = test(main)
if __name__ == '__main__':
	test('a', 1)
	test('B|~B', 2)
	test('c|~C', 3)
	test('i|c|p|c', 7)
	test('a|b', 3)
	test('a|~a|b|c', 8)
	test('a|~a|b|~b|c|d', 16)
