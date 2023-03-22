#Python program to interchange ﬁrst and last elements in a list
# Python3 program to swap ﬁrst and last element of a list 
# Swap function
def swapList(newList):
    newList[0], newList[-1] = newList[-1], newList[0] #12,24=24,12
    return newList 
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList)) 
