#1
L1=[]
n=int(input("enter no. of values:"))
for x in range(n):
    x=input("enter data:")
    L1.append(x)
print (L1)

#2
L2=['google','apple','facebook','microsoft','tesla']
L1.extend(L2)
print(L1)

#3
List=[2,3,3,2,4,1]
print("TOTAL NUMBER OF COUNT :",List.count(1))

#4)
L3=[5,1,3,2,8,6]
L3.sort()
print("SORTED LIST IS:",L3)


#5)
A=[]
B=[]
n=int(input("enter total no. of values in list A:"))
for x in range(n):
    x=int(input("enter data:"))
    A.append(x)
n2=int(input("enter total no. of values in list B:"))
for x in range(n2):
    x=int(input("enter data:"))
    B.append(x)
A.sort()
B.sort()
print("Sorted list A:",A)
print("Sorted list B:",B)
A.extend(B)
A.sort()
C=A
print('Merged sorted list is :',C)

#6
L=[]
n=int(input("enter total no. of values:"))
for x in range(n):
    x=int(input("enter numbers:"))
    L.append(x)
even=0
odd=0
for j in L:
    if j%2==0:
        even+=1
    else:
        odd+=1
print('Total even numbers are:',even)
print('Total odd numbers are:',odd)
#the topic of tuples hasn't been covered yet.




