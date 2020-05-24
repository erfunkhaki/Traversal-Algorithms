def pre_order(tree,root):
    final_list = []
    need_to_check = []
    visited = []

    for x in tree[root]:
        need_to_check.append(x)

    visited.append(root)
    
    while(len(visited) != len(tree)):
        current_value = need_to_check[0]
        visited.append(current_value)
        need_to_check.pop(0)
        for x in range(len(tree[current_value])):
            need_to_check.insert(x,tree[current_value][x])

    print("Final pre order list is: " + str(visited))


binary_tree = {'r': ['a','b'], 'a' : ['c','d'], 'b' : ['e','f'], 'c' : ['h'], 'd' : ['i','j'], 'e' : ['k'], 'f' : [], 'h' : [], 'i' : [], 'j' : ['l'], 'k' : [], 'l' : []} #Examples from powerpoint

pre_order(binary_tree,'r')  #To run pre order function

