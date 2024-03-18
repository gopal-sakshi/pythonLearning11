import re, sys

def is_acronym(word):
    """
        Return: True if the word is all caps and/or contain numbers ==> ABCDE, AB12C
        Return: False if the word contains lower case letters ==> abcde, ABCde, abcDE
    """
    return re.match(r"\b[A-Z0-9]{2,}\b", word) is not None

print("the word ", sys.argv[1], " ===> ", is_acronym(sys.argv[1]))

# python3 08_others/regex_acronym11.py FIFA
# python3 08_others/regex_acronym11.py FiFA