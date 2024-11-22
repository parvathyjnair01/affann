print("Increasing Triangle")
n=int(input("Enter the no.of rows:"))
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print(" ")
print("Decreasing Triangle")
d=int(input("enter the no.of rows"))
for i in range(d):
    for j in range(n-i):
       print("*",end="")
    print(" ")
print("hill pattern")
e=int(input("enter the no.of rows"))

for i in range(1, e + 1):
    for j in range(e - i):
        print(" ", end="")
    for k in range(1, 2 * i):
        print("*", end="")
    print()
print("reverse hill pattern")
f=int(input("enter the no.of rows"))

for i in range(f,0,-1):
    for j in range(f - i):
        print(" ", end="")
    for k in range(i*2-1):
        print("*", end="")
    print()
