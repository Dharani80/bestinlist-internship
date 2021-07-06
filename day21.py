#1q
def listoftuples(11,12):
    return list(map(lambda x,y:(x,y),11,12))
list1 = [1,2,3]
list2 = ['a','b','c']
print(list of tuples(list1,list2))

def merge(list1,list2):
    merged_list = list(zip(list1,list2))
    return merged_list
list1 = [1,2,3]
list2 = ['a','b','c']
print(merge(list1,list2))

#2q
list1 = [1,2,3,4,5,6,7,8]
list2 = ['a','b','c','d','e','f','g','h',]
result = tuple(zip(list1,list2))

#3q
list1 = [1,2,3,4,5,6,7,8]
list2 = sorted(list1)
print(list2)

#4q
def filtereven(nums):
    if nums%2 !=0:
        return True
    else:
        return False
numbers = [55,36,74,25,32,3,65,22,3]
result = filter(filtereven,numbers)
for i in result:
    print(i)
