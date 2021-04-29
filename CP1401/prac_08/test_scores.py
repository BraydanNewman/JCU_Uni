# Below 50% = N (fail)
# 50 up to but not including 65 = P (pass)
# 65 up to but not including 75 = C
# 75 up to but not including 85 = D
# 85 and over = HD


MAX_SCORE = 100
NUMBER_OF_SCORES = 4


def get_valid_number(prompt, min_number, max_number, error_message=None):
	while  True:
		number = float(input(prompt))
		if min_number <= number <= max_number:
			return number
		if error_message:
			print(error_message)


def calculate_grade(score):
	if score >= 85:
		return "HD"
	elif score >= 75:
		return "D"
	elif score >= 65:
		return "P"
	elif score >= 50:
		return "P"
	else:
		return "N"


def average(lst):
	return sum(lst) / len(lst)


def main():
	scores = []
	grades = []
	for i in range(NUMBER_OF_SCORES):
		score = (get_valid_number(f"Score {i + 1}: ", 0, 100, "Invalid Score"))
		grades.append(calculate_grade(score))
		scores.append(score)

	for i in range(NUMBER_OF_SCORES):
		print(f"Score {i} was {scores[i]:5}, which is {grades[i]}")

	average_score = average(scores)

	print(f"The average score was {average_score}")

	if average_score > scores[-1]:
		print("Trend is not positive")
	else:
		print("Trend is positive")


if __name__ == '__main__':
	main()