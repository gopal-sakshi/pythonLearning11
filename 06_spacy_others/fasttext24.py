# https://fasttext.cc/docs/en/supervised-tutorial.html

# head -n 12404 cooking.stackexchange.txt > cooking23.train
# tail -n 3000 cooking.stackexchange.txt > cooking23.valid
### split training data into 2 ---> train & valid


import fasttext
################# train the model ############################
#### APPROACH 1
# model = fasttext.train_supervised(input="resources_cookingStackXchange23/cooking23.train")
# model.save_model("06_spacy_others/fasttext_cookingMdl23.bin")

#### APPROACH 2
model = fasttext.load_model("06_spacy_others/fasttext_cookingMdl23.bin")
############ load the model if its already trained #############




########################### testing model #############
test23 = model.test("resources_cookingStackXchange23/cooking23.valid")
print(test23)
########################### testing model #############









############# use cases ###################### 
print(model.predict("Which baking dish is best to bake a banana bread ?")) ##   (('__label__baking',), array([0.07014001]))
output23 = model.predict("Why not put knives in the dishwasher??", k=5)         ## returns top 5 labels
print(output23)
############# use cases ######################