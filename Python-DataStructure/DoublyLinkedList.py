class Node(object):
    def __init__(self,d,n =None,p =None):
        self.data = d
        self.next_node =n
        self.prev_node = p

    def get_next(self,n):
        return self.next_node

    def set_next(self,n):
        self.next_node=n   
    
    def get_prev(self,p):
        return self.prev_node

    def set_prev(self, p):
        self.prev_node = p

    def get_data(self):
        return self.data

    def set_data(self,d):
        self.data=d

    def to_string(self):
        return "Node value: " + str(self.data)

    def has_next(self):
        if self.get_next() is None:
            return False
        else:
            return True

class DoublyLinkedList(object):
    def __init__(self):
        self.head=None
        self.tail=None
        self.size =0

    def isEmpty(self):
        if self.head==None:
            return True
        else:
            return False

    def insertToHead(self,d):

        if self.isEmpty():
            self.head=Node(d)
            self.head.next_node=None
            self.tail=self.head
        else:
            newNode= Node(d,self.head)
            newNode.next_node=self.head
            newNode.prev_node=None
            self.head=newNode
        self.size +=1   
    
    def InsertToTail(self,d):
        if self.isEmpty():
            self.insertToHead(d)
        else:
            new_node=Node(d,self.tail)
            new_node.next_node=None
            self.tail.next_node =new_node
            new_node.prev_node =self.tail
            

       
    def get_size(self):    
        return self.size

   
    


def main():
    L1 = DoublyLinkedList()
    L1.insertToHead(5)
    L1.insertToHead(3)    
    L1.insertToHead(6)
    L1.insertToHead(12)
    L1.insertToHead(45)
    print(L1.size)
main()