#ACCESSING ELEMENTS FROM A TUPLE

lst = []
n=int(input("Enter the number of elements:"))
for i in range (0,n):
    ele=input()
    lst.append(ele)
tupl=tuple(lst)
p=int(input("Enter the index of the element you want to see:"))
print (tupl[p])
m=int(input("Enter the index from which index you want to access tuple : "))
print (tupl[m:])


#DELETING ELEMENTS FROM DICTIONARY

n=int(input("ENTER NUMBER OF ELEMENTS IN YOUR DICTIONARY: "))
mark_list={}
for i in range (0,n):
    sub=input()
    marks=input()
    mark_list[sub]=marks
print(mark_list)
sub1=input("ENTER THE SUBJECT YOU WANT TO DELETE: ")
mark_list.pop(sub1)
print(mark_list)

#ASSIGNING ELEMENTS TO LIST

lst1=[]
lst2=[]
n=int(input(" enter no of elements in list 1: "),base=10)
m=int(input("enter no of elements in list 2: " ),base=10)
for i in range (0,n):
    ele=(input())
    lst1.append(ele)
for j in range (0,m):
    ele=(input())
    lst2.append(ele)

lst1.append(lst2)
print(lst1)
    

