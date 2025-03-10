#replace the r on $ with except the first r. #IntegriChain company-16-7-24
# def replace_r_with_dollar(s):
#     # Find the first 'r'
#     first_r_index = s.find('r')
#
#     # Keep the first part unchanged and replace 'r' with '$' in the rest
#     new_string = s[:first_r_index + 1] + s[first_r_index + 1:].replace('r', '$')
#
#     return new_string
#
#
# # Original string
# original_string = "restartthecomputer"
#
# # Apply the function
# modified_string = replace_r_with_dollar(original_string)
#
# print(modified_string)
#output-resta$tthecompute$    - replace the r on $ with except the first r.


# numbers = [4, 6, 8, 3, 7, 6, 9, 1, 10, 10]
#
# #Find the second highest number
# result = second_highest_number(numbers)
#
# if result is None:
#     print("There are not enough unique numbers to determine the second highest.")
# else:
#     print("The second highest number is:", result)


# numbers = [10, 20, 4, 45, 99, 101, 1]
#
#
# def find_second_highest(numbers):
#     pass
#
#
# second_highest = find_second_highest(numbers)
# print("Second highest number:", second_highest)


# def find_second_highest(numbers):
#     # Convert the list to set to remove duplicates (if any)
#     unique_numbers = list(set(numbers))
#
#     # Sort the list in descending order
#     sorted_numbers = sorted(unique_numbers, reverse=True)
#
#     # Check if there are at least two distinct numbers in the list
#     if len(sorted_numbers) < 2:
#         return "There is no second highest number."
#
# Return the second highest number
#     return sorted_numbers[1]
#
# numbers = [4, 6, 8, 3, 7, 6, 9, 1, 10, 10]
#
# # Find the second highest number
# result = second_highest_number(numbers)
#
# if result is None:
#     print("There are not enough unique numbers to determine the second highest.")
# else:
#     print("The second highest number is:", result)

#==========================================

# examples = [
#     "restartthecomputer",
#     "rarelyrecognizablerotary",
#     "runner",
#     "error",
#     "irreversible",
#     "ruralarea",
#     "road",
#     "river",
#     "garage",
#     "restart"
# ]
#
# for example in examples:
#     modified_string = replace_r_with_dollar(example)
#     print(f"Original: {example} -> Modified: {modified_string}")

#=================================================================
# def change_char(str1):
#     # Get the first character of the input string 'str1' and store it in the variable 'char'.
#     char = str1[0]
#
#     # Replace all occurrences of the character 'char' with '$' in the 'str1' string.
#     str1 = str1.replace(char, '$')
#
#     # Reconstruct the 'str1' string by placing the original 'char' as the first character
#     # followed by the modified string starting from the second character.
#     str1 = char + str1[1:]
#
#     # Return the modified 'str1' string.
#     return str1
#
# # Call the change_char function with the argument 'restart' and print the result.
# print(change_char('restart'))  # Output: 'resta$t'

#====================================================2nd highest number
# Define a function named 'second_largest' that takes a list of numbers 'numbers' as a parameter
def second_largest(numbers):
    # Check if the length of the 'numbers' list is less than 2; return None in this case
    if len(numbers) < 2:
        return

    # Check if there are only two elements in the 'numbers' list, and they are the same; return None in this case
    if len(numbers) == 2 and numbers[0] == numbers[1]:
        return

    # Create an empty set 'dup_items' to store duplicate items and an empty list 'uniq_items' to store unique items
    dup_items = set()
    uniq_items = []

    # Iterate through the elements in the 'numbers' list
    for x in numbers:
        # Check if 'x' is not in 'dup_items'; if not, add it to 'uniq_items' and 'dup_items'
        if x not in dup_items:
            uniq_items.append(x)
            dup_items.add(x)

    # Sort the 'uniq_items' list in ascending order
    uniq_items.sort()

    # Return the second largest item from the sorted 'uniq_items' list, which is at index -2 (second from the end)
    return uniq_items[-2]

# Call the 'second_largest' function with different lists and print the results
print(second_largest([1, 2, 3, 4, 4]))
print(second_largest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
print(second_largest([2, 2]))  # Edge case with two identical elements, returns None
print(second_largest([1]))  # Edge case with a single element, returns None