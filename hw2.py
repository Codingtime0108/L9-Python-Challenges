#swap number by empting a variable!!! Tiya is solving a mathematical problem. But she has mistakenly interchanged 3 of the values. So now she needs to place them in their correct position. So design a program for swapping 3 values.

a = int(input("Enter any number:"))
b = int(input("Enter another number:"))
c = 0
print("This is ur first num:",a)
print("This is ur 2nd number:",b)
c=a
a=b
b=c
print("These are ur numbers swapped!")
print(a)
print(c)