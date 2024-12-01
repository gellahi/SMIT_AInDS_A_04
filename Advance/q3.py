def flatten_list(nestedList):
    flattenList=[]
    for iList in nestedList:
        for i in iList:
            flattenList.append(i)
    return flattenList

nestedList=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(flatten_list(nestedList))
            