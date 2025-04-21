# Program developed by Sam Espana (texbook - Figure 67)
# Program edited by Nolan Becker
# Date: 3/5/2025

print("Displaying for loops with range (single value)\n")
for index1 in range(4):
    print("Python for loop with range of single value. Index = ", index1)
index1 = 0
print("Python while loop with index 1 value. Index = ", index1)

while (index1 < 4):
    print("Index1 = ", index1)
    index1 += 1

print("\n Python for loop with two parameters (1,5) \n")
for index2 in range(1, 5):
    print("Index 2 =", index2)

print("\n Python while loop with two parameters (1,5) \n")
# while loop below
index2 = 0
while (index2 < 5):
    print("Index2 = ", index2)
    index2 += 1

print("\nTimes table for #X\n")

intNumber = int(input("Enter integer number for table > 0: "))

intLowerBound = 1
intUpperBound = 10

for index3 in range(intLowerBound, intUpperBound + 1):
    print(intNumber, "x", index3, "=", intNumber * index3)

# while loop below
index3 = intLowerBound
while (index3 <= intUpperBound):
    print(intNumber, "x", index3, "=", intNumber * index3)
    index3 += 1

print("Nolan Becker")
