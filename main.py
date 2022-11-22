import sys

#sample list
list1 = [2,6,3,7,4,9,5]
#        0 1 2 3 4 5 6

#create pivot
piv = list1[0] or list1[6]
print("Pivot is " + str(piv))

# first sort
for i in list1:

    if i <= piv:

        smaller = []
        smaller.append[int(i)]
        for i in range(len(list1)):
            print(str(i))