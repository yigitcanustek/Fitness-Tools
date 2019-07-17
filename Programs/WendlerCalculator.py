#import Wendler's Book

#This program design 90% of your max. Don't do your 100%!  

#########################################################
#    Week 1   |    Week 2   |    Week 3   |    Week 4*  |           
#-------------|-------------|-------------|-------------| 
# 65% x 5 reps| 70% x 3 reps| 75% x 5 reps| 40% x 5 reps|           
#             |             |             |             |
# 75% x 5 reps| 80% x 3 reps| 85% x 3 reps| 50% x 5 reps|           
#             |             |             |             |
# 85% x 5 reps| 90% x 3 reps| 95% x 1 rep | 60% x 5 reps|       
#     or      |     or      |     or      |             |  
#  more reps  |  more reps  |  more reps  |             |         
#########################################################

#*Deload Week*#

#Estimate 1RM of the Big 3 = Weight x Reps x .0333 + Weight = Estimated 1RM 

import math 
def OneRepMax(weight, reps): #kg or pound choose one, i think pound is better because higher 
 return math.ceil(weight * reps * ((10/3) * pow(10,-2)) + weight)





def Squat(weight, maks):
 submax = OneRepMax(weight, maks) * (9/10)
 print(  "\nSquat\nHafta 1:\t\tHafta 2:\t\tHafta 3:\t\tHafta 4:\n"
        	+ (str)(submax * 65/100) + " x 5 tekrar\t" 
 		+ (str)(submax * 70/100) + " x 5 tekrar\t"           
		+ (str)(submax * 75/100) + " x 5 tekrar\t" 
		+ (str)(submax * 40/100) + " x 5 tekrar\n"

 		+ (str)(submax * 75/100) + " x 5 tekrar\t"
		+ (str)(submax * 80/100) + " x 5 tekrar\t"
		+ (str)(submax * 85/100) + " x 5 tekrar\t"
		+ (str)(submax * 50/100) + " x 5 tekrar\n"
		
		+ (str)(submax * 85/100) + " x 5 tekrar\t"
		+ (str)(submax * 90/100) + " x 5 tekrar\t"
		+ (str)(submax * 95/100) + " x 5 tekrar\t"
		+ (str)(submax * 60/100) + " x 5 tekrar\n")


def Deadlift(weight, maks):
 submax = OneRepMax(weight, maks) * (9/10)
 print(  "\nDeadlift\nHafta 1:\t\tHafta 2:\t\tHafta 3:\t\tHafta 4:\n"
                + (str)(submax * 65/100) + " x 5 tekrar\t"
                + (str)(submax * 70/100) + " x 5 tekrar\t"
                + (str)(submax * 75/100) + " x 5 tekrar\t"
                + (str)(submax * 40/100) + " x 5 tekrar\n"

                + (str)(submax * 75/100) + " x 5 tekrar\t"
                + (str)(submax * 80/100) + " x 5 tekrar\t"
                + (str)(submax * 85/100) + " x 5 tekrar\t"
                + (str)(submax * 50/100) + " x 5 tekrar\n"

                + (str)(submax * 85/100) + " x 5 tekrar\t"
                + (str)(submax * 90/100) + " x 5 tekrar\t"
                + (str)(submax * 95/100) + " x 5 tekrar\t"
                + (str)(submax * 60/100) + " x 5 tekrar\n")


def BenchPress(weight, maks):
 submax = OneRepMax(weight, maks) * (9/10)
 print(  "\nBench Press\nHafta 1:\t\tHafta 2:\t\tHafta 3:\t\tHafta 4:\n"
                + (str)(submax * 65/100) + " x 5 tekrar\t"
                + (str)(submax * 70/100) + " x 5 tekrar\t"
                + (str)(submax * 75/100) + " x 5 tekrar\t"
                + (str)(submax * 40/100) + " x 5 tekrar\n"

                + (str)(submax * 75/100) + " x 5 tekrar\t"
                + (str)(submax * 80/100) + " x 5 tekrar\t"
                + (str)(submax * 85/100) + " x 5 tekrar\t"
                + (str)(submax * 50/100) + " x 5 tekrar\n"

                + (str)(submax * 85/100) + " x 5 tekrar\t"
                + (str)(submax * 90/100) + " x 5 tekrar\t"
                + (str)(submax * 95/100) + " x 5 tekrar\t"
                + (str)(submax * 60/100) + " x 5 tekrar\n")


def TheStandingPress(weight, maks):
 submax = OneRepMax(weight, maks) * (9/10)
 print(  "\nOverhead Press\nHafta 1:\t\tHafta 2:\t\tHafta 3:\t\tHafta 4:\n"
                + (str)(submax * 65/100) + " x 5 tekrar\t"
                + (str)(submax * 70/100) + " x 5 tekrar\t"
                + (str)(submax * 75/100) + " x 5 tekrar\t"
                + (str)(submax * 40/100) + " x 5 tekrar\n"

                + (str)(submax * 75/100) + " x 5 tekrar\t"
                + (str)(submax * 80/100) + " x 5 tekrar\t"
                + (str)(submax * 85/100) + " x 5 tekrar\t"
                + (str)(submax * 50/100) + " x 5 tekrar\n"

                + (str)(submax * 85/100) + " x 5 tekrar\t"
                + (str)(submax * 90/100) + " x 5 tekrar\t"
                + (str)(submax * 95/100) + " x 5 tekrar\t"
                + (str)(submax * 60/100) + " x 5 tekrar\n")
