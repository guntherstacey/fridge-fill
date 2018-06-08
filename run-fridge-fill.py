def read_file(text_file):
  if ".txt" in text_file:
    recipe_list = open(text_file)
    opened_recipe_list = (recipe_list.read())
    #print opened_recipe_list
    return opened_recipe_list
  else:
    print ("Invalid Input: Not a .txt file")

def ingredients(recipes):
  ingredients_block = recipes.splitlines()
  for item in ingredients_block:
    start = item[item.index("$") + 1]
    stop = item[item.index("$", start)]
    new_ingredients_block += item[start:stop]
    print new_ingredients


recipe_block = read_file("fridge-fill-sample-input.txt")
just_ingredients = ingredients(recipe_block)
