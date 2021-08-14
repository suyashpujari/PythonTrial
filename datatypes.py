# Write a program to manipulate List data

V=['Car','Bus','Train','Aeroplane','Boat',1,2,3,4,5]
print("\nList V :",V[:])

print("\nList V : 2 to 5",V[2:6])

print("\nList V in reverse:",V[::-1])

V.append('Vehicals')
print("\nList V after appending  :",V[:])

V.insert(3,'Bicycle')
print("\nList V after inserting  :",V[:])

V.pop(1)
print("\nList V after poping :",V[:])

V.remove('Boat')
print("\nList V after removing :",V[:])

del V[0]
print("\nList V after deleteing :",V[:])

V.clear()
print("\nList A after clearing :",V[:])

# Write a program to manipulate Tuple data

C=("Apple","Microsoft","Cisco","IBM","Google","Amazon",101,102,103,104)

print("\nTuple C:",C)

print("\nTuple C: 2 to 5",C[2:6])

print("\nTuple C in reverse:",C[::-1])

print("\nCount of Amazon is :",C.count('Amazon'))

print("\nIndex of Apple is",C.index('Apple'))