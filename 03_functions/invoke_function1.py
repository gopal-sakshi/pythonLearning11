def add_numbers(a, b):
    sum = a + b
    return sum

result = add_numbers(2, 3)
print("sum of 2 numbers ====> ", result)

################################################################

def mainFunc():
    print("main function lo unnaa")
    def nestedFunc():
        print("idi nested function abbaayi")
    
    nestedFunc()
mainFunc()

################################################################
def name_and_age(name,age):
    ### new way - to use f-strings ###
    print(f"I am {name} and I am {age} years old!")
    print("I am {name} and I am {age} years old!")          # notice the difference
    ### old way ###
    print("%s peru naadi; naaku %d vayassu" % (name,age))
    print('naa peru {}; {} years nindaayi naaku'.format(name,age))
    print('{name23} anu nenu, {age23} years ga bhoomi meeda unna'.format(name23=name,age23=age))
name_and_age('Cristiano', 41)
################################################################