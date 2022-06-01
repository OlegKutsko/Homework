
def comments(list_of_names):
    lenght = len(list_of_names)-2
    if len(list_of_names)==0:
        print("no one likes this")
    if len(list_of_names)==1:
        print(list_of_names[0], 'likes this')
    if len(list_of_names)==2:
        print(list_of_names[0],'and',list_of_names[1], 'likes this')
    if len(list_of_names)==3:
        print(list_of_names[0], ',', list_of_names[1], 'and', list_of_names[2], 'likes this')
    if len(list_of_names)>3:
        print(list_of_names[0], ',', list_of_names[1], 'and', lenght, 'others likes this')


comments(list_of_names=["Alex", "Jacob", "Max", "Hogn", "Garry"])