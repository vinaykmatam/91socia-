original_dictionary = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
print("original dictionaries: ",original_dictionary)

sorted_dictionary = sorted(original_dictionary, key = lambda x: x['color'])
print("sorted dictionary: ",sorted_dictionary)

