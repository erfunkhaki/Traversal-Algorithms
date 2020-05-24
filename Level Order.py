message = "Hello please put your dictionary tree model in 'binary_tree' in order and you will see the level and pre model results in a correct list."
print (message)
def level_order(tree, root):
    final_list = []
    need_to_check = []

    for x in tree:
        need_to_check.append(x)
    
    final_list.append(root)

    while(len(need_to_check) > 0):
        current_value = need_to_check[0]
        for x in tree[current_value]:
            final_list.append(x)
        need_to_check.pop(0)

    print("Final level order list is: " + str(final_list))




binary_tree = {'r': ['a','b'], 'a' : ['c','d'], 'b' : ['e','f'], 'c' : ['h'], 'd' : ['i','j'], 'e' : ['k'], 'f' : [], 'h' : [], 'i' : [], 'j' : ['l'], 'k' : [], 'l' : []} #Examples from powerpoint

level_order(binary_tree,'r') #To run level order function



