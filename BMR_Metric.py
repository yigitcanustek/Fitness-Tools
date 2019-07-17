#Mifflin-St Jeor Equation

import math



def BMR_Metric_Men(age, weight, height):
	return math.floor((9.99 * weight) + (6.25 * height) - (4.92 * age) + 5)


def BMR_Metric_Women(age, weight, height):
	return math.floor((9.99 * weight) + (6.25 * height) - (4.92 * age) - 161)




print(BMR_Metric_Men(20, 81.25, 178))


