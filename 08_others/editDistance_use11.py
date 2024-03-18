from editDistance11 import DistanceAlgorithm, EditDistance
import sys

####        python3 08_others/editDistance_use11.py scout count


n = len(sys.argv)           # total length of arguments passed
for i in range(1, n):
    print(sys.argv[i], end = " ")

def calcDist():
    distance_algorithm = DistanceAlgorithm.LEVENSHTEIN
    distance_comparer = EditDistance(distance_algorithm)
    distance = distance_comparer.compare(sys.argv[1], sys.argv[2], 3)
    print("distance b/w scout & count ===> ", distance)

calcDist()