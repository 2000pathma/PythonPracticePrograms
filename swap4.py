#Python program to interchange ﬁrst and last elements in a list
# Python3 program to swap ﬁrst
#and last element of a list 
# Swap function
def swapList(list):#parameters
    ﬁrst = list.pop(0) #pop(0)=12
    last = list.pop(-1) #pop(-1)=24
    list.insert(0, last) #0--->24
    list.append(ﬁrst) #last position append---->12
    return list
# Driver code
newList = [12, 35, 9, 56, 24] 
print(swapList(newList)) #arguements
