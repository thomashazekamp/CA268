#!/usr/bin/env python3

def main():
    
    nums_list = []
    prev_list = []

    print("Enter numbers (-1 to end): ", end="")
    num = int(input())

    if num == -1:
        exit
    else:
        nums_list.append(num)

    while num != -1:
        print("Enter numbers (-1 to end): ", end="")
        num = int(input())

        if num in nums_list and num != -1:
            prev_list.append(num)
        elif num != -1:
            nums_list.append(num)
    
    prev_list = " ".join([str(i) for i in prev_list])
    print(f"Previous: {prev_list}")

    
    
if __name__ == '__main__':
    main()

# # Correct code 

# #!/usr/bin/env python3

# print("Enter numbers (-1 to end): ", end="")

# num = int(input())
# numbers = []
# while num != -1:
#   numbers.append(num)
#   num = int(input())

# dic = {}
# collection = []
# for number in numbers:
#   if number not in dic:
#     dic[number] = 1
#   else:
#     collection.append(number)

# for num in collection:
#   print(str(num) + " ", end="")

# print()
