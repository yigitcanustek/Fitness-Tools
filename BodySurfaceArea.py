import math
from BodyMassIndex import BMI

def BSA(weight, height):
	return math.pow(weight, 0.425) * math.pow(height, 0.725) * 0.007184



#print(BMI(80,180))

print(BSA(80,180))
