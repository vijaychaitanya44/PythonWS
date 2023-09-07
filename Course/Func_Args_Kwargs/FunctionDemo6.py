def check_even_number(list1):
    even_number=[]

    for x in list1:
        if x%2==0:
            even_number.append(x)
        else:
            pass
    return even_number
result =check_even_number([1,9,55,3])

if len(result)>0:
    print(result)
else:
    print("Sorry no evens present")


