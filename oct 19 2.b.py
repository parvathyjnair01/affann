first_name = input("entre your first name:")
last_name = input("entre your last name:")
name = first_name+" "+last_name
print(name)
first_name_length=len(first_name)
print(first_name_length)
extracted_first_name=name[:first_name_length+1]
print(extracted_first_name)
