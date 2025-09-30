#napiši funkcijo is_empty(stack), ki prever, ali je sklad prazen
def is_empty(stack):
    return len(stack) == 0

stack1 = []
print(is_empty(stack1)) #True

stack1.append(5)
print(is_empty(stack1)) #False
stack1.pop()
print(is_empty(stack1)) #True