num = int(input("Enter number : "))
numbers = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
if  num < 1000:
    if  num>0 and num<10: 
            print(numbers[num -1])
    elif  num>9 and num<100:
        sum = int(((num/10) + (num%10)))
        print(sum)
    elif num>99 and num<1000:
        mulsum = 1
        while num != 0:
            mulsum *= num%10
            num = int(num/10)
        print(mulsum)
else:
    print("number has more than 3 digits")

     










