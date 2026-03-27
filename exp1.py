
# Experiment 1:
    #Stack ADT (Design + Use)
# Aim:
    #Design a Stack ADT and build confidence in LIFO behavior and constant-time operations.
# What you will implement (in lab):
    #Implement StackADT with push, pop, peek, isEmpty, size. Use it once meaningfully (e.g.,store steps of recursion trace, undo operations, or expression symbols).
# Input / Output expectation:
    #Input: sequence of operations. Output: returned values (pop/peek) + final stack state + safe underflow handling.
# Lab checkpoints (faculty verifies):
    #• All operations behave correctly (LIFO)
    #• Underflow handled safely (no crash)
    #• Stack used in a small real task (not only basic testing)
# Viva:
    #1. What is an ADT?
    #2. Why push/pop can be O(1)?
    #3. One real-world use of stack?

class Stack:
    def __init__(self):
        self.items = []
        
    def push(self,x):
        self.items.append(x)
        
    def pop(self):
        if len(self.items) == 0:
            return "Underflow"
        else:
            return self.items.pop()
        
    def peek(self):
        if len(self.items) == 0:
            return "Underflow"
        else:
            return self.items[-1]
        
    def isempty(self):
         return len(self.items) == 0
     
    def size(self):
        return len(self.items)
    
s = Stack()
s.push(10)
s.push(20)
print("Top element:", s.peek())
print("Removed element:", s.pop())
# this example is showcasing it's LIFO behaviour as 20 goes last but while using fncn peek it comes out first.
    
    # Another Approach where we can use all the functions again and again in a better and user-friendly way.
     
# def choice():
#     s = Stack()
#     while True:
#         print("1. Push")
#         print("2. Pop")
#         print("3. Peek")
#         print("4. isEmpty")
#         print("5. Size")
#         print("0. Exit")
#         wish = input("Enter the function you want to use: ")
#         wish = wish.strip()
        
#         if wish == "1":
#             val = input("Enter the value you want to push: ")
#             s.push(val)
#             print("PUSHED VALUE :",val)
            
#         elif wish == "2":
#             removed = s.pop()
            
#             if removed is None:
#                 print("Underflow")
#             else:
#                 print("Removed :",removed)
                
#         elif wish == "3":
#             top = s.peek()
#             if top is None:
#                 print("Underflow")
#             else:
#                 print("Peeked :",top)
                
#         elif wish == "4":
#             print("isempty:",s.isempty())
        
#         elif wish == "5":
#             print("Size of the stack:",s.size())
            
#         elif wish == "0":
#             print("EXITING THE STACK: ")
#             break
#         else:
#             print("Invalid input") 

# choice()
            
