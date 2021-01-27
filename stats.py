# stats.py

def get_scores():
	"""Get scores interactively from the user

	post: return a list of numbers obtained from user"""

	input_string = input("Enter a list of numbers separeted by a comma: ")
	my_list = input_string.split(',')
	return my_list
		


def min_value(nums):
	"""find the minimum

	pre: nums is a list of numbers and len(nums) > 0
	post: returns smalles number in nums"""
	
	
	nums = min(nums)
	print("The lowest value is: " + nums)
	return nums

def max_value(nums):
	""" find the maximum

	pre : nums is a list of numbers and len(nums) > 0
	post : returns largest number in nums """ 

	
	nums = max(nums)
	print("The maximum value is: " + nums)
	return nums

def average(nums):
	""" calculate the mean
	pre : nums is a list of numbers and len(nums) > 0
	post : returns the mean (a float) of the values in nums """

	my_sum = 0
	num_of_elements = 0
	for i in range(nums):
		my_sum += nums[i]
		num_of_elements = i
	
	print(my_sum / num_of_elements)
	return my_sum / num_of_elements

def std_deviation(nums):
	""" calculate the standard deviation

	pre : nums is a list of numbers and len(nums) > 1
	post : returns the standard deviation (a float) of the values
	in nums """

#min_value(get_scores())
#max_value(get_scores())
average(get_scores())
