def sign(x):
    return x >= 0

def practical1(a, b):
    ab, bc = 0, 0
    
    for i in range(len(a)):
        if a[i] > b[i]:
            ab += 1
        elif b[i] > a[i]:
            bc += 1
    
    if ab > bc:
        print("Chef 1 Wins!!")
    elif bc > ab:
        print("Chef 2 Wins!!")
    else:
        print("Tie")

print("Enter the array of points for Chef 1.")
a = list(map(int, input().split()))

print("Enter the array of points for Chef 2 .")
b = list(map(int, input().split()))

au = [x for x in a if sign(x)]
bu = [x for x in b if sign(x)]

practical1(au, bu)
