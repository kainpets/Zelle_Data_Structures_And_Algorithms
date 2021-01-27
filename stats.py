# stats.py

def get_scores():
	"""Get scores interactively from the user

	post: return a list of numbers obtained from user"""

	input_string = input("Enter a list of numbers separeted by a comma: ")
	my_list = input_string.split(',')
	return my_list
		


def min_value():
	"""find the minimum

	pre: nums is a list of numbers and len(nums) > 0
	post: returns smalles number in nums"""

	minimum = min(get_scores())
	print(minimum)

def max_value(nums):
	""" find the maximum

	pre : nums is a list of numbers and len(nums) > 0
	post : returns largest number in nums """ 

def average(nums):
	""" calculate the mean
	pre : nums is a list of numbers and len(nums) > 0
	post : returns the mean (a float) of the values in nums """

def std_deviation(nums):
	""" calculate the standard deviation

	pre : nums is a list of numbers and len(nums) > 1
	post : returns the standard deviation (a float) of the values
	in nums """

min_value()