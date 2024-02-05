# sum = 0
# for i in range(10,21,2):
#     sum += i
#     print(i)
# print(sum)

# numbers = [4,4,4,4,4]
# sum = 0
# for i in numbers:
#     sum += i
# avg = sum/len(numbers)
# print("The average is: ", avg)

# name = "Muhammad Mahad"
# count = 0
# for char in name:
#     if char.lower() != 'm':
#         continue
#     else:
#         count = count + 1
# print('Total number of m is:', count)


# outer loop
# for i in range(1, 6):
#     print('Multiplication table of:', i)
#     count = 1
#     # inner loop to print multiplication table of current number
#     while count < 11:
#         print(i * count, end=' ')
#         count = count + 1
#     print('\n')

# dict1 = {"Name":"Mahad", "Designation": "DevOps developer"}
# for i in dict1:
#     print(i, " ", dict1[i])

# row = 10
# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print(j, end = " ")
#     print("")

# till = int(input("Enter the end point number: "))
# sum = 0
# for i in range(1,till+1):
#     sum += i
# print ("The sum is: ", sum)

# num = 2
# for i in range(1,11):
#     print(num*i)

num = 75869
count = 0
while num != 0:
    # floor division
    # to reduce the last digit from number
    num = num // 10
    # increment counter by 1
    count = count + 1
print(count)