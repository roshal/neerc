import time
def main(number):
	vectors = sorted(enumerate((6, 2, 5, 5, 4, 5, 6, 3, 7, 6)), **{
		'key': lambda c: c[0] / (c[1] + 1),
	})
	maximum = 0
	count = 0
	power = number
	stack = []
	state = vectors.copy()
	first = True
	while True:
		while state:
			vector = state[-1]
			number = power - vector[1]
			if 0 < number:
				count += vector[0]
				power -= vector[1]
				stack.append(state)
				state = vectors.copy()
				break
			if not number:
				number = count + vector[0]
				if maximum < number:
					maximum = number
			state.pop()
		else:
			if not stack:
				break
			state = stack.pop()
			vector = state.pop()
			count -= vector[0]
			power += vector[1]
	return maximum
if __name__ == '__main__':
	with open('auxiliary.in') as stream_r:
		number = int(stream_r.read().rstrip())
	output = main(number)
	with open('auxiliary.out', 'w') as stream_w:
		print(output, **{
			'file': stream_w,
		})
