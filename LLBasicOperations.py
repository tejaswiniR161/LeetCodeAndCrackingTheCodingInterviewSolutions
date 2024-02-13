class node:
    def __init__(self,val):
        self.val=val
        self.next=None

def insert(head,val):
    if(head==None):
        return node(val)

    p=head
    while(p.next!=None):
        p=p.next
    p.next=node(val)
    return head

def insertMany(head,arr):
    if head==None:
        head=node(arr[0])
        p=head
    else:
        p=head
        while(p.next!=None):
            p=p.next
        p.next=node(arr[0])
        p=p.next

    for i in range(1,len(arr)):
        p.next=node(arr[i])
        p=p.next
    return head

def readAll(head):
    p=head
    while(p!=None):
        print(p.val,end =" ")
        if(p.next!=None):
            print(" -> ",end =" ")
        p=p.next
    print()

ans=insert(None,12)
readAll(ans)
ans=insertMany(ans,[1,2,3,4,5,3,2,1,90])
readAll(ans)