import sys

#sample list
list1 = [2,6,3,7,4,9,5]
#        0 1 2 3 4 5 6

#create pivot
piv = list1[0] or list1[6]
print("Pivot is " + str(piv))

# first sort
for i in list1:

    while list1[i-1] != 2:

        if list1[i-1] <= piv:

            smaller = []
            smaller.append(list1[i-1])
            for i in range(len(smaller)):
                print(larger[i])

        else:
            larger = []
            larger.append(list1[i-1])
            for i in range(len(larger)):
                print(larger[i])