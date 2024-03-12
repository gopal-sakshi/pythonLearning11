##################
## double star
a=3
b=5
print('double star 3^5 =====> ', a**b)

def kwargsAnteEnti(**kwargs):
    for key, value in kwargs.items():
        print("key2323 ==> {} ; value23 ===> {}".format(key, value))
 

kwargsAnteEnti(player1="Kroos", player2="Ramos", player3="Alonso")
##################