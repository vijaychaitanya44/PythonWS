status = False
names=["Python","Java","Selenium","JS","Csharp"]

for name in names:
    if name=="JS":
        status=True
        break
    else:
        print("Please wait still looking for it")

if status:
    print("We found the record")
else:
    print("No record found")