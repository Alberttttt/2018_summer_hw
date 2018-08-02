
class Stack:
    """模拟栈"""
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items)==0 
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop() 
    
    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]
        
    def size(self):
        return len(self.items) 


def move( fromP, toP, disknum ) :
    global step
    step = step + 1
    print("Step:", step, "Move disk number", disknum, "from", fromP, "plot to", toP, "plot.")

print("Input the height of your hanoi tower")
num = input()
A = Stack()
B = Stack()
C = Stack()
global step
step = 0


for i in range ( int(num), 0, -1):
    A.push(i)

if int(num) % 2 == 1 :
    for i in range ( 1 , 2 ** int(num)) :
        if i % 3 == 1 :
            
            if C.isEmpty() :
                
                C.push(A.peek())
                A.pop()
                move('A', 'C', C.peek())
            
            elif A.isEmpty() :

                A.push(C.peek())
                C.pop()
                move('C', 'A', A.peek())

            elif A.peek() < C.peek() :

                C.push(A.peek())
                A.pop()
                move('A', 'C', C.peek())

            else :

                A.push(C.peek())
                C.pop()
                move('C', 'A', A.peek())


        elif i % 3 == 2 :

            if B.isEmpty() :
                
                B.push(A.peek())
                A.pop()
                move('A', 'B', B.peek())
            
            elif A.isEmpty() :

                A.push(B.peek())
                B.pop()
                move('B', 'A', A.peek())

            elif A.peek() < B.peek() :

                B.push(A.peek())
                A.pop()
                move('A', 'B', B.peek())

            else :

                A.push(B.peek())
                B.pop()
                move('B', 'A', A.peek())

        else :

            if C.isEmpty() :
                
                C.push(B.peek())
                B.pop()
                move('B', 'C', C.peek())
            
            elif B.isEmpty() :

                B.push(C.peek())
                C.pop()
                move('C', 'B', B.peek())

            elif B.peek() < C.peek() :

                C.push(B.peek())
                B.pop()
                move('B', 'C', C.peek())

            else :

                B.push(C.peek())
                C.pop()
                move('C', 'B', B.peek())

else :
    for i in range ( 1 , 2 ** int(num)) :
        if i % 3 == 1 :
            
            if B.isEmpty() :
                
                B.push(A.peek())
                A.pop()
                move('A', 'B', B.peek())
            
            elif A.isEmpty() :

                A.push(B.peek())
                B.pop()
                move('B', 'A', A.peek())

            elif A.peek() < B.peek() :

                B.push(A.peek())
                A.pop()
                move('A', 'B', B.peek())

            else :

                A.push(B.peek())
                B.pop()
                move('B', 'A', A.peek())


        elif i % 3 == 2 :

            if C.isEmpty() :
                
                C.push(A.peek())
                A.pop()
                move('A', 'C', C.peek())
            
            elif A.isEmpty() :

                A.push(C.peek())
                C.pop()
                move('C', 'A', A.peek())

            elif A.peek() < C.peek() :

                C.push(A.peek())
                A.pop()
                move('A', 'C', C.peek())

            else :

                A.push(C.peek())
                C.pop()
                move('C', 'A', A.peek())

        else :

            if C.isEmpty() :
                
                C.push(B.peek())
                B.pop()
                move('B', 'C', C.peek())
            
            elif B.isEmpty() :

                B.push(C.peek())
                C.pop()
                move('C', 'B', B.peek())

            elif B.peek() < C.peek() :

                C.push(B.peek())
                B.pop()
                move('B', 'C', C.peek())

            else :

                B.push(C.peek())
                C.pop()
                move('C', 'B', B.peek())

# C.push(A.peek())
# print(C.peek())
# A.pop()

# print(A.peek())
# if A.peek() > C.peek():
#     print("777")
# move('A', 'C', C.peek())
