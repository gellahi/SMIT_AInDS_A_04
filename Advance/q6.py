def frequency_counter(myStr):
    freqDict={}
    tempList=[]
    for i in myStr:
        if i in tempList:
            count=freqDict[i]
            freqDict[i]=count+1
        else:
            freqDict[i]=1
            tempList.append(i)
    return freqDict

print(frequency_counter("particular"))
        