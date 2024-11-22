from unittest.util import sorted_list_difference

l1 = [22,44,55,77,5,44,21]
l2 = [12,2,31,22,456,4456,4874]

combined_list = l1 + l2
even_list = []
odd_list = []
for i in combined_list:
    if i % 2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
even_list.sort()
odd_list.sort()
sorted_list=even_list+odd_list
merged_list=l1+l2
print(l1,"list number one")
print(l2,"list number two")
print(merged_list,"merged_list")
print(sorted_list,"Sorted list")