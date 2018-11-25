idNumber = str(input("enter id number:"))
size = len(idNumber)
numStr = [0,0,0,0,0,0,0,0,0]
if size <= 9:                               
    if size < 9:                            
        num = 9 - size
        zeros = num * "0"
        idNumber = zeros + idNumber
    i = 0
    start = 0
    end = 9
    for i in range(start,end):
        
        if i %2 != 0:
            numStr[i] = int(idNumber[i]) * 2
        else:
            numStr[i] = int(idNumber[i])
        if numStr[i] > 9: 
           numStr[i] = int((numStr[i])/10) + int((numStr[i])%10)
        i += 1
    j = 0
    sum = 0
    while(j < size):
        sum += numStr[j]
        j += 1
    if sum % 10 == 0:
        print("Id number{0}is good".format(numStr))
    else:
        print("Id number{0} is not good".format(numStr))
else:
    print("the id number is worng")
 

 