sum = lambda x,y: x + y
print(sum(2,3))


l = [2,4,6,8]
list2 = list(map(lambda x: x*2, l))
print(list2)

lists = [1,2,3,4,5,6,7,8,9,10]
list3 = list(filter(lambda x: x % 2 ==0, lists))
print(list3)