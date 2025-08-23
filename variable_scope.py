# local scope
num_1 = 0

def display_num():
    global num_1 
    num_1 = 20
    return num_1

print(display_num())
print(num_1)

