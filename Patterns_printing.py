# Pattern 1
for i in range(1,6):
    for j in range(1,6):
        print(j, end=" ")
    print()

# Pattern 2
for i in range(1,6):
    for j in range(1,6):
        print(i, end=" ")
    print()

# Pattern 3
for i in range(5,1,-1):
    for j in range(5,1,-1):
        print(j, end=" ")
    print()

# Pattern 4
for i in range(1,6):
    for j in range(1,i):
        print(j, end=" ")
    print()

# Pattern 5
for i in range(1,6):
    for j in range(1,i):
        print(i, end=" ")
    print()

# Pattern 6
for i in range(1,6):
    for j in range(i,0,-1):
        print(j, end=" ")
    print()

# Pattern 7
for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j, end=" ")
    print()

# Pattern 8 - Half Pyramid
for i in range(1,6):
    for j in range(i,5):
        print(" ", end=" ")
    for k in range(1,i+1):
        print("*", end=" ")
    print()

# Pattern 9 - Full Pyramid
for i in range(1,6):
    for j in range(i,5):
        print(" ", end=" ")
    for k in range(1,(i*2)):
        print("*", end=" ")
    print()

# Pattern 10 - Diamond
for i in range(1,6):
    for j in range(i,5):
        print(" ", end=" ")
    for k in range(1,(i*2)):
        print("*", end=" ")
    print()

for i in range(4,0,-1):
    for j in range(5,i,-1):
        print(" ", end=" ")
    for k in range(1,(i*2)):
        print("*", end=" ")
    print()

# Pattern 11
for i in range(4):
    print("*")

# Pattern 12
for i in range(4):
    print("*", end=" ")

# Pattern 13 - Square
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()

# Pattern 14
for i in range(1,6):
    for j in range(i):
        print(j, end=" ")
    print()

# Pattern 15
for i in range(1,6):
    for j in range(i):
        print("*", end=" ")
    print()

# Pattern 16
for i in range(4,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()

# Pattern 17
for i in range(1,5):
    for j in range(2):
        print(i, end=" ")
    print()

# Pattern 18
for i in range(5):
    for j in range(1,5):
        print(j, end=" ")
    print()
