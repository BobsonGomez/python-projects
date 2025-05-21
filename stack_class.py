class stack:
    count = 0
    def __init__(self,lst,n):
        self.lst = lst
        self.n = n
    def push(self,x):
        if self.n==stack.count:
            print("Overflow")
        else:
            self.lst.append(x)
            stack.count = stack.count+1
    def pop(self):
        if stack.count==0:
            print("Underflow")
        else:
            print(self.lst.pop(),"has been popped")
            stack.count = stack.count-1
    def display(self):
        if not self.lst:
            print("Empty stack")
        else:
            for i in self.lst:
                print(i,"\t",end = '')
            print("")
