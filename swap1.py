#Python program to interchange ﬁrst and last elements in a list
# Python3 program to swap ﬁrst and last element of a list
newList = [12, 35, 9, 56, 24] 
# Swap function
def swapList(newList):
    size = len(newList)#size=5
    #Swapping
    temp = newList[0] #temp=12
    newList[0] = newList[size - 1] #newlist[0]=24(newlist[5-1]
    newList[size - 1] = temp #newlist[4]=temp(12)
    return newList 
# Driver code
print(swapList(newList)) 
