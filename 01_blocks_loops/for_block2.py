####################################################################3

users = {
    'Hans': 'active', 
    'Éléonore': 'inactive', 
    '景太郎': 'active'
}
print("users =====> ", users)

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print("edited users =====> ", users)

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print("active users =====> ", active_users)
####################################################################3

for i in range(5):
    print(i)


print(list(range(5, 10)))
####################################################################3

## len(a) ====> 5       ========> for i in range(5) ===> 1,2,3,4,5
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

####################################################################3