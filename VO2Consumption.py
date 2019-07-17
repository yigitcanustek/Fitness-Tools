#https://www.ncbi.nlm.nih.gov/pubmed/7588904
from BodySurfaceArea import BSA
import math

def VO2_Men(weight, height, age):
	return (157.3*BSA(weight,height) + 10 - 10.5*math.log(age) +4.8)



print (VO2_Men(80,180,20))
