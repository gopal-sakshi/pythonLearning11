str1 = "wy"
str2 = "gf"
str3 = "u"
trg_string11 = "weeks__your__weeks"

table = trg_string11.maketrans(str1, str2, str3) 
print("after translation ===> ", trg_string11.translate(table))

str22 = [
    ['luka', 'modric', 'plays', 'as', 'midfielder'],
    ['he', 'is', 'from', 'croatia'],
    ['along', 'with', 'casemiro', 'kroos', 'he', 'formed', 'core', 'of', 'RMA', 'midfield' ]
]


for s in str22:
    print("s ===> ", s)

result23 = ' '.join(' '.join(s) for s in str22)
print("result23 ====> ", result23)