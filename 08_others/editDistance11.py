from enum import Enum
import numpy as np
import enchant

class DistanceAlgorithm(Enum):
    LEVENSHTEIN = 0                 # Levenshtein algorithm.
    DAMERAU = 1                 # Damerau optimal string alignment algorithm

class EditDistance(object):
    def __init__(self, algorithm):
        self._algorithm = algorithm
        if algorithm == DistanceAlgorithm.DAMERAU:
            self._distance_comparer = Damerau()
        elif algorithm == DistanceAlgorithm.LEVENSHTEIN:
            self._distance_comparer = Levenshtein()
        else:
            raise ValueError("Unknown distance algorithm")
    
    def compare(self, string1, string2, max_distance):
        return self._distance_comparer.distance(string1, string2, max_distance)
    

class AbstractDistanceCompare23(object):
    def distance(self, string1, string2, max_distance):
        raise NotImplementedError("implement cheyyale :( ")
    
class Damerau(AbstractDistanceCompare23):
    def distance(self, string1, string2, max_distance):
        return -1       ### returning default value -1
    
class Levenshtein(AbstractDistanceCompare23):
    def distance(self, string1, string2, max_distance):
        return enchant.utils.levenshtein(string1, string2)