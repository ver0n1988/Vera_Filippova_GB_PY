list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list=[]
for string in list:
    if string.isdigit():
       new_list.append(f'"{int(string):02d}"')
    elif string[0]=="+" and string[1].isdigit():
       new_list.append(f'"{int(string):02d}"')
    else:
        new_list.append(string)
print(' '.join(new_list))


