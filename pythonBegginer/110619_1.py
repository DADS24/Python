A=[1,3,5,7,9]
B=[2,4,6,8]

C = [] #Create an empty list
for i in A: #iter each element in A
    for j in B: #iter each element in B
        mult = i * j
        C.append(mult) #Append the result in the list C
print(C)
   

    