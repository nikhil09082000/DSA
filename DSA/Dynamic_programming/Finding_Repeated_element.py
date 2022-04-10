a=[2,1,4,3,4]
#a=[1,5,2,3,4,2]

#we are traversing loop one time
#for every abs(element) in array find respective element
#with index as that elemnt
#if that element is non -ve make it as negitive
#if finded elemnt is negitive, break the loop and print that element
tm=0
for i in range(len(a)):
    b=abs(a[i])
    if a[b-1]<0:
        tm=i
        break
    else:
        a[b-1]=0-a[b-1]
print(a[tm])
