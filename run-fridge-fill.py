def read_file(text_file):
  if ".txt" in text_file:
    recipe_list = open(text_file)
    opened_recipe_list = (recipe_list.read())
    return opened_recipe_list
  else:
    print ("Invalid Input: Not a .txt file")

def ingredients(recipes):
  list_of_ingredients = []
  ingredients_block = recipes.splitlines()
  for ingredient in ingredients_block:
    start = ingredient.find("$") + 1
    end = ingredient.find("$", start)
    each_ingredient = ingredient[start:end]
    list_of_ingredients.append(each_ingredient)
  print(list_of_ingredients)
  


recipe_block = read_file("fridge-fill-sample-input.txt")
just_ingredients = ingredients(recipe_block)
