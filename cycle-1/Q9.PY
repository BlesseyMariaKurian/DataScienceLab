print("SJC22MCA-2019-BLESSEY MARIA KURIAN-S3MCA")
# Input the first list from the user
list1 = input("Enter the first list of numbers separated by spaces: ").split()

# Input the second list from the user
list2 = input("Enter the second list of numbers separated by spaces: ").split()

# Convert the input strings to integer lists
list1 = [int(x) for x in list1]
list2 = [int(x) for x in list2]

# Initialize an empty list to store the result
result = []

# Check if the lists have the same length
if len(list1) == len(list2):
   # Loop through the lists and add elements element-wise
    for i in range(len(list1)):
     result.append(list1[i] + list2[i])

   # Display the result
    print("Result of element-wise addition:", result)
else:
  print("Lists must have the same length for element-wise addition.")