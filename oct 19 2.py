first_name = input("entre your first name:")
last_name = input("entre your last name:")
name = first_name+" "+last_name
print(name)
last_name_length=len(first_name)
print(last_name_length)
extracted_last_name=name[last_name_length+1:]
print(extracted_last_name)
