class node:
    def __init__(self,item,ptr):
        self.item = item
        self.ptr = ptr
Start = None
while True:
    print("Enter the operation to be performed")
    opt = int(input("1.Insert into linked list\n2.delete from linked list\n3.display linked list\n4.exit from program:"))
    if opt==1:#inserting data into the SLL one way only
        item = int(input("Enter the data:"))
        ptr=None
        n = node(item,ptr)
        if Start==None:
            Start = n
            tr = Start
        else:
            tr.ptr=n
            tr=n
    elif opt==2:#deleting data from the linked list
        To_delete = int(input("Enter the data that has to be deleted:"))
        tr = Start
        if Start.item==To_delete:
            Start=Start.ptr
            tr.ptr=None
            print(tr.item," Has been deleted")
        else:
            tr1 = Start
            tr = Start.ptr
            if tr.item==To_delete:
                print(tr.item,"Has been deleted")
                tr1.ptr=None
            else:
                while tr.ptr!=None:
                    if tr.item==To_delete:
                        tr1.ptr=tr.ptr
                        print(tr.item,"Has been deleted")
                        tr.ptr=None
                    else:
                        tr1 = tr
                        tr = tr.ptr             
    elif opt==3:#displaying the current state of linked list
        if Start==None:
            print("Linked list is empty")
        else:
            tr = Start
            while tr.ptr!=None:
                print(tr.item,"\t",end='')
                tr = tr.ptr
            print(tr.item)
    else:
        break
print("You've successfully exited the program")
