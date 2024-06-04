players11 = ("hierro", "benz", "asensio", "casemiro", "fede", "david alaba", "eduardo cammavinga", "guti")
normal11 = sorted(players11)
reverse11 = sorted(players11, reverse=True)
print("sorted normal ===> ", normal11)
print("sorted reverse ===> ", reverse11)


length11 = sorted(players11, key=len)
print("sorted on length ===> ", length11)

#######################################################################

def closest_to_10(n):
  return abs(10-n)

a = (5, 3, 1, 11, 2, 12, 17)
x = sorted(a, key=closest_to_10)
print("numbers closest to 10 ===> ", x)
#######################################################################