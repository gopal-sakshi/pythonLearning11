# sort() function will modify the list it is called on. 
# The sorted() function will create a new list containing a sorted version of the list it is given. 
# The sorted() function will not modify the list
# sort() function modifies the list in-place and has no return value.


vegetables = ['squash', 'pea', 'carrot', 'potato']
new_list = sorted(vegetables)
print("new_list ====> ", new_list)

vegetables.sort()
print("using sort modifies 'vegetables' ===> ", vegetables)