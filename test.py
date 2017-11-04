def test(function):
	def test(accepted, expected):
		actual = function(accepted)
		if actual is expected:
			print('+', actual, '~', repr(accepted))
		else:
			print('-', actual, '~', repr(accepted))
			print(' ', expected)
	return test
if __name__ == '__main__':
	def main(number):
		return number
	test = test(main)
	test(0, 0)
	test(0, 1)
	test(1, 0)
	test(1, 1)
