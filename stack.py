n = int(input("Enter the size of the stack:"))
count = 0
lst = []
def push(x,lst):
    global count
    if count==n:
        print("\nOverflow")
    else:
        lst.append(x)
        count+=1
def pop(lst):
    global count
    if count==0:
        print("\nUnderflow")
    else:
        count-=1
        print(lst.pop()," has been popped")

def display(lst):
    if lst == []:
        print("Empty stack")
    for i in lst:
        print(i,"\t", end='')

while(1):
    print("\nEnter operation to be performed:")
    opt = int(input("1.push \n2.pop \n3.display \n4.exit:"))
    if opt==1:
        element = int(input("Enter the element to be pushed"))
        push(element,lst)
    elif opt==2:
        pop(lst)
    elif opt==3:
        display(lst)
    elif opt==4:
        break
print("You've successfully exited the program")

