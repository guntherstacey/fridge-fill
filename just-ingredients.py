def read_file(text_file):
  if ".txt" in text_file:
    recipe_list = open(text_file)
    opened_recipe_list = (recipe_list.read())
    return opened_recipe_list
  else:
    print ("Invalid Input: Not a .txt file")

def ilist(string_input):
	preingredients = string_input.split("#")
	ingredients = []
	for e in preingredients:
		ingredients = ingredients.append([e])
		print ingredients

#def ingredients(ilist):
#	ingredients = []
#	for e in ilist:
#		if "$" in e:
#			e.split("$")
#			i = e[1]
#			ingredients.append(i)
	#print ingredients
	
read_file("fridge-fill-sample-input.txt")
ilist(read_file("fridge-fill-sample-input.txt"))
#ingredients(ilist(read_file("fridge-fill-sample-input.txt")))
	
