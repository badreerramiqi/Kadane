# Initialize an empty list 't'
t = []

# Take user input for the size of the array
U = int(input("Enter the size of the array: "))

# Populate the array 't' with user-input numbers
for i in range(U):
    n = float(input("Type the number: "))
    t.append(n)

# Initialize variables for maximum sum calculation
sm = t[0] + t[1]  # Initialize with the sum of the first two elements
h = 0             # Initialize the starting index of the subarray
m = 1             # Initialize the ending index of the subarray

# Iterate through the array to find the subarray with the maximum sum
for i in range(0, len(t)):
    p = i
    s = 0
    for j in range(p, len(t)):
        s += t[j]
        # Update the maximum sum and indices if a larger sum is found
        if s >= sm:
            h = i
            m = j
            sm = s

# Initialize an empty list 'b' to store the subarray with the maximum sum
b = []

# Print the maximum sum and the corresponding subarray
print("The maximum sum is:", sm)
for i in range(h, m+1):
    b.append(t[i])

print("The subarray with the maximum sum is:", b)
