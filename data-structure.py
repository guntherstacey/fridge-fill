def read_file(text_file):
  if ".txt" in text_file:
    recipe_list = open(text_file)
    opened_recipe_list = (recipe_list.read())
    print opened_recipe_list
  else:
    print ("Invalid Input: Not a .txt file")




read_file("fridge-fill-sample-input.txt")
