def main(formula):
	negative = set()
	positive = set()
	for string in formula.split('|'):
		if string[0] is '~':
			negative.add(string[1:])
		else:
			positive.add(string)
	return 2 ** len(negative | positive) + bool(negative & positive) - 1
if __name__ == '__main__':
	with open('boolean.in') as stream_r:
		formula = stream_r.read().rstrip()
	output = main(formula)
	with open('boolean.out', 'w') as stream_w:
		print(output, **{
			'file': stream_w,
		})
