import re

def parse_words(phrase, preserve_case=False):
    """create a non-unique wordlist from sample text
    """
    # \W non-words, use negated set to ignore non-words and "_" (underscore)
    # Compatible with non-latin characters, does not split words at
    # apostrophes
    if preserve_case:
        return re.findall(r"([^\W_]+['']*[^\W_]*)", phrase)
    else:
        return re.findall(r"([^\W_]+['']*[^\W_]*)", phrase.lower())
    

########## not working #########
print(parse_words("Control, control, you must learn control"))