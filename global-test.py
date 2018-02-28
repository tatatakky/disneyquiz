count=0
x=10
def Test():
    global x
    count+=1
    if count == 1:
        x=count+10
        print(x)
    elif count == 11:
        x=count+20
        print(x)
    elif count ==31:
        x=count+30
    else:
        print(x)

for i in range(4):
    Test()
