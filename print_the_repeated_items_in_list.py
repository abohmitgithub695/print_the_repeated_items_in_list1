# python prograsm to print the repeate items in the given list
##########################################################
#list with repeate items
list_with_repeate_item=[1,2,3,4,5,4,5,3]
list2=[]
list3=[]
for i in list_with_repeate_item:
    if i not in list2:
        list2.append(i)
for m in list2:
    if list_with_repeate_item.count(m)>1:
        list3.append(m)
print(f"The repeate items in list_with_repeate_item is {list3}")


############ by abdulrahman yaslam ben hamdan##################