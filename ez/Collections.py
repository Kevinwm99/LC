class Stack():
    # this version implementing stack by using an array
    def __init__(self,size):
        self.size = size                    # define a size of the stack
        self.stack = [None]*self.size       # define an array with the given size
        self.top = 0                        # define the pointer top
    def isEmpty(self):
        if self.top == 0:
            return True
        return False
    def push(self,key):                     
        if self.top == self.size :
            raise Exception("stack overflow")
        else:
            self.stack[self.top]=key        # add element by using the pointer
            print("{} is pushed to the stack".format(key))
            self.top+=1                     # increase the pointer to the next position
    def pop(self):
        # return the last added element to the stack and remove it                          
        if self.isEmpty():
            raise Exception("stack underflow")
        else:
            self.top-=1                     # decrease the pointer
            res = self.stack[self.top]      # store the popped value to res
            self.stack[self.top]=None       # delete the popped value from the stack
            return res
    def peek(self):                         # return the last added element without remove it 
        if self.isEmpty():
            raise Exception("stack underflow")
        else:
            return self.stack[self.top-1]
class Stack_l():
    # this version implementing stack using doubly linked list
    def __init__(self):
        self.stack = Doubly_linked_list()
    def isEmpty(self):
        self.stack.isEmpty()
    def push(self,key):
        self.stack.pushBack(key)
        return
    def pop(self):
        self.stack.popBack()
    def peek(self):
        return self.stack.tail.key
    def __len__(self):
        return len(self.stack)
class Queue():
# this version implementing queue by using an array
    def __init__(self,size):
        self.size = size                    # define size of the queue
        self.queue = [None]*size            # define an array with the given size
        self.head = 0
        self.tail = 0
    def enqueue(self,key):
        if (not None in self.queue) and self.head==self.tail:
            raise Exception("queue overflow")
        self.queue[self.tail]=key           # add new value to the queue
        if self.tail == self.size-1:        # check if whether the tail exceeds the size
            self.tail =0                    # if yes set tail to zero
        else:
            self.tail+=1                    # Otherwise increment tail value by 1
    def dequeue(self):
        if self.isEmpty():
            raise Exception("queue underflow")
        res = self.queue[self.head]         # get the value from the head pointer
        self.queue[self.head]=None          # delete the value
        if self.head == self.size-1:        # check if whether the head exceeds the size
            self.head =0                    # if yes reset the head to zero
        else:   
            self.head +=1                   # otherwise, increment head value by 1
        return res
    def isEmpty(self):
        if (None in self.queue) and self.head==self.tail:
            return True
        else: return False   
class Queue_l():
    # this version implementing queue using doubly linked list
    def __init__(self):
        self.queue = Doubly_linked_list()
    def enqueue(self,key):
        self.queue.pushBack(key)
    def dequeue(self):
        self.queue.popFront()
    def isEmpty(self):
        self.queue.isEmpty()
    def __len__(self):
        return len(self.queue)
class Dequeue():
    # this version implementing dequeue using doubly-linked list
    def __init__(self):
        self.deque = Doubly_linked_list()
    def pushBack(self,key):
        self.deque.pushBack(key)
    def pushFront(self,key):
        self.deque.pushFront(key)
    def popBack(self):
        self.deque.popBack()
    def popFront(self):
        self.deque.popFront()
    def back(self):
        self.deque.tail.key
    def top(self):
        self.deque.head.key
    def __len__(self):
        return len(self.deque)      
class Node():
    def __init__(self,key):
        self.key = key
        self.next = None
        self.prev = None
class Singly_linked_list():
    def __init__(self):
        self.head = None
    def pushBack(self,key):
        new_node = Node(key)
        if self.isEmpty():  
            self.head = new_node
            return
        last_node = self.head 
        while(last_node.next):              # transverse all the nodes
            last_node = last_node.next 
        last_node.next = new_node           # reached the last node, add new node to it
    def pushFront(self,key):
        new_node = Node(key)
        if self.isEmpty():
            self.head = new_node
            return
        old_head = self.head 
        new_node.next = old_head            # new node points to the old head
        self.head = new_node                # make new node as head
    def popFront(self):
        if self.isEmpty():
            raise Exception("list is empty") 
        pop_node = self.head
        if pop_node.next is None:           # if there is only one element in the list
            self.head = None
            return pop_node.key
        self.head = pop_node.next           # make the next element as head
        return pop_node.key
    def popBack(self):
        if self.isEmpty():
            raise Exception("list is empty") 
        pop_node = self.head
        while(pop_node):                    # transverse all the nodes
            if pop_node.next is None:       # if there is only one element in the list
                self.head = None            # make the list empty
                return pop_node.key
            if pop_node.next.next is None:  # next element will be the last element of the list
                pop_val = pop_node.next
                pop_node.next =None         # delete the popped element
                return pop_val.key
            pop_node =pop_node.next
    def findKey(self,key):
        if self.isEmpty():
            raise Exception("list is empty")
        find_key = self.head
        while(find_key):                    # transverse all the nodes
            if find_key.key == key:         # found key
                return find_key
            find_key=find_key.next
        raise Exception("can't find the key") 
    def erase(self,key):
        self.findKey(key)                   # find whether there is a key in the list
        find_key = self.head
        if find_key.key ==key:              # if the element is the head 
            self.head = self.head.next
            return
        while (find_key):                   # transverse all the nodes
            if find_key.next.key == key:    # if the next node is the key we want to erase
                prev_node = find_key        # define previous and next nodes
                next_node = find_key.next.next
                prev_node.next = next_node  # connect previous and next nodes
                find_key.next = None           # erase the node
                return
            find_key=find_key.next
    def addBefore(self,node,key):
        new_node = Node(key) 
        find_node = self.head
        if find_node.key == node:           # if there is only one element in the list
            old_head = find_node            # assign old head
            self.head = new_node            # make new node as head
            new_node.next = old_head        # point new node to the old head
            return
        while(find_node):                   # transverse all the nodes
            if find_node.next.key == node:  # if the next node is the node we want to add key before it
                old_node = find_node.next   # assign old node
                find_node.next = new_node   # add new node
                new_node.next = old_node    # point new node to old node
                return    
            find_node = find_node.next
    def addAfter(self,node,key):
        new_node = Node(key)
        find_node = self.head
        if find_node.key == node:           # this part is the same as addBefore
            old_tail = find_node.next
            find_node.next = new_node
            new_node.next = old_tail
            return
        while(find_node):                   # transverse all the nodes
            if find_node.key == node:       # found the node
                old_tail = find_node.next   # assign old tail
                find_node.next = new_node   # add new node
                new_node.next = old_tail    # point new node to old tail
                return
            find_node = find_node.next         
    def print_list(self):
        print_node = self.head
        if not self.isEmpty():print("head")
        else: raise Exception("the list is empty") 
        while print_node is not None:
            print(print_node.key)
            print_node = print_node.next
            if print_node is None: print("tail")
    def isEmpty(self):
        if self.head is None: 
            return True
        return False
class Doubly_linked_list():
    # _registry=[]
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0 

        # self._registry.append(self)
    def print_list(self):
        print_node = self.head
        if not self.isEmpty():print("head")
        else: raise Exception("the list is empty") 
        while print_node is not None:
            print(print_node.key)
            print_node = print_node.next
        print("tail")
    def isEmpty(self):
        if self.head is None: 
            return True
        return False
    def __len__(self):                      # return the size of the list
        return self.size
    def pushBack(self,key):
        new_node = Node(key)
        if self.isEmpty():                  # if list is empty
            self.head = new_node            # | set new node to be head 
            self.tail = new_node            # | and tail
            self.size +=1            
        else:
            self.tail.next = new_node       # | current tail points to new_node
            new_node.prev = self.tail       # | set new node to be old tail
            self.tail = new_node            # | update tail to be new node
            self.size +=1
    def pushFront(self,key):
        new_node = Node(key)    
        if self.isEmpty():                  # | if list is empty
            self.head = new_node            # | set new node to be head 
            self.tail = new_node            # | and tail
            self.size +=1
        else:
            self.head.prev = new_node       # current hed point to new_node
            new_node.next = self.head       # set new_node to be old head
            self.head = new_node            # update head to be new_node
            self.size +=1
    def popBack(self):
        if self.isEmpty(): raise Exception("the list is empty")
        if self.head == self.tail:          # if there is only one element in the list
            pop_val = self.head.key
            self.head = None                # | make the 
            self.tail = None                # | list empty
            self.size -=1
            return pop_val
        else:
            pop_val = self.tail.key         # get value from the tail
            self.tail = self.tail.prev      # assign tail to the previous element
            self.tail.next = None           # delete the popped element
            self.size -=1
            return pop_val
    def popFront(self):
        if self.isEmpty(): raise Exception("the list is empty")
        if self.head == self.tail:          # if there is only one element in the list
            pop_val = self.head.key
            self.head = None                # | make the 
            self.tail = None                # | list empty
            self.size -=1
            return pop_val
        else:
            pop_val = self.head.key         # get value from the head
            self.head = self.head.next      # assign head to next element
            self.head.prev = None           # delete the popped element
            self.size -=1
            return pop_val
    def addBefore(self,node,key):
        new_node = Node(key)                
        node = self.findKey(node)
        new_node.next = node                # | assign new_node to the middle 
        new_node.prev = node.prev           # | of node and 
        node.prev = new_node                # | node.prev
        if new_node.prev is not None:       # if not adding new_node at the head
            new_node.prev.next = new_node   # point the previous node to new node
        if self.head == node:                # if add new node at the head
            self.head = new_node            # update head to new node
        self.size +=1
    def addAfter(self,node,key):
        new_node = Node(key)
        node = self.findKey(node)
        new_node.next = node.next           # | assign new_node to middle, 
        new_node.prev = node                # | of node 
        node.next = new_node                # | and node.next
        if new_node.next is not None:       # if not adding new_node at the tail
            new_node.next.prev =new_node    # point the next of new_node to new node
        if self.tail == node:               # if adding new_node at the tail
            self.tail = new_node            # update tail to new node
        self.size +=1
    def findKey(self,key):
        if self.isEmpty():
            raise Exception("list is empty")
        find_key = self.head
        while(find_key):                    # transverse all the nodes
            if find_key.key == key:         # found key
                return find_key             # return the node
            find_key=find_key.next
        raise Exception("can't find the key") 
    def erase(self,key):
        if self.isEmpty():
            raise Exception("list is empty")
        find_key = self.findKey(key)
        if self.head == self.tail:          # if there is only one element in the list
            self.head = None
            self.tail = None
            print("{} has been removed from the list".format(find_key.key))
            self.size -=1
            return
        else:
            if find_key == self.head:       # if the erasing key is the head
                self.head = find_key.next
                self.head.prev = None
                print("{} has been removed from the list".format(find_key.key))
                self.size -=1
                return
            if find_key == self.tail:       # if the erasing key is the tail
                self.tail = find_key.prev
                self.tail.next = None
                print("{} has been removed from the list".format(find_key.key))
                self.size -=1
                return
            next_value = find_key.next      # Otherwise, delete it by connecting the previous and the next node
            prev_value =find_key.prev
            next_value.prev = prev_value
            prev_value.next = next_value
            print("{} has been removed from the list".format(find_key.key))
            self.size -=1
            return
class Dynamic_array():
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.arr = self.make_array()
    def make_array(self):
        return [None]*self.capacity
    def printarray(self):
        self.arr
    def __len__(self):
        return self.size
    def get(self,idx):
        if idx < 0 or idx >= self.size: raise Exception("index out of range")
        return self.arr[idx]
    def _set(self,idx,val):
        if idx < 0 or idx >= self.size: raise Exception("index out of range")
        self.arr[idx] = val
    def pushBack(self,val):
        if self.size == self.capacity:
            self.capacity *= 2
            new_array = self.make_array()
            for i in range(self.size):
                new_array[i]=self.arr[i]
            self.arr=new_array
        self.arr[self.size] = val
        self.size += 1
    def remove(self,idx):
        if idx < 0 or idx >= self.size: raise Exception("index out of range")
        for i in range(idx,self.size-1):
            self.arr[i] = self.arr[i+1]
            self.arr[i+1] = None
        self.size -= 1
        if self.size < self.capacity/2: self.capacity = int(self.capacity/2)