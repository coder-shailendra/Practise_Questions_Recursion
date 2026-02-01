def print_list(list,idx=0):
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)


name = ["madhav","bhavya","shreya","preeti","karan"]
print_list(name)