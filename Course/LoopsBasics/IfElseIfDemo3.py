salary = input("input your salary: ")
print(type(salary))
sal=int(salary)
if sal>40000:
    print("eligible for carloan")
    if sal>80000:
        print("eligibel for homeloan")
        if sal>100000:
            print("eleigible for every loan")
else:
    print(" loan score is not good")

