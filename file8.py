#assingment: find the largest number in a list
new_list= [2, 5, 11, 19, 6, 4]
max_num= 0
for num in new_list:
    if max_num < num:
        max_num = num #reset max to this new number
print(max_num)