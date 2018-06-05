def read_file(text_file):
  if ".txt" in text_file:
    recipe_list = open(text_file)
    opened_recipe_list = (recipe_list.read())
    print opened_recipe_list
  else:
    print ("Invalid Input: Not a .txt file")

def data_structure(string_input):

