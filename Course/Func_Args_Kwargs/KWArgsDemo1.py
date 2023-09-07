def print_names(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(kwargs["ID"])

print_names(name="vjc",address="404022add", phone="802873",location="Banglore", ID=44)



def hello_world(fname,*args,**kwargs):
    print(fname)
    print(args)
    print(kwargs)

hello_world(829,5,2,5, name="RAju", lang="Telugu")