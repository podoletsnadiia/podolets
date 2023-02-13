
#Generate 100 random numbers between 0 and 1000
import random
gen_rand = []
randomlist = random.sample(range(0, 1000), 100)
print(randomlist)

#Sort list from min to max (using bubbleSort)
#Step 1) Create a flag variable that monitors if any swapping has occurred in the inner loop
#Step 2) If the values have swapped positions, continue to the next iteration
#Step 3) If the benefits have not swapped positions, terminate the inner loop, and continue with the outer loop.
def bubbleSort(theSeq):
    n = len(theSeq)
    for i in range(n - 1):
        flag = 0
        for j in range(n - 1):
            if theSeq[j] > theSeq[j + 1]:
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
                flag = 1
        if flag == 0:
            break
    return theSeq
el = randomlist
result = bubbleSort(el)
print(result)

#calculate average for even and odd numbers
def average_lis(): # Create a function
    even = [] # Create an empty list for further count of even numbers
    odd = []  # Create an empty list for further count of odd numbers
    sum_even = 0  # Create a 'summator' for even numbers
    sum_odd = 0  # Create a 'summator' for odd numbers
    for i in el:
         if (i % 2) == 0: # Check whether the element of list is even number
           sum_even += i # Sum of even numbers
           even.append(i) # Append every even number to list 'even'
         if (i % 2) == 1: # Check whether the element of list is odd number
           sum_odd += i # Sum of odd numbers
           odd.append(i) # Append every even number to list 'odd'
    avg_even = sum_even / len(even) # Calculate the average of even numbers
    avg_odd = sum_odd / len(odd) # Calculate the average of odd numbers
    return avg_even, avg_odd
print('Averages of even and odd numbers:', average_lis())
