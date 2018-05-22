def read_file(text_file):
  if ".txt" in text_file:
    recipe_list = open(text_file)
    opened_recipe_list = (recipe_list.read())
    return opened_recipe_list
  else:
    print ("Invalid Input: Not a .txt file")



def list(string_input):
	list = [string_input.split(".")]
    #print list
    	preingredients = list.pop()
	ingredients = []
	for e in preingredients:
        	if ":" in e:
            		e.split(":")
			ingredients.append(preingredients[1])
	print ingredients

read_file("fridge-fill-sample-input.txt")
list(read_file("fridge-fill-sample-input.txt"))
