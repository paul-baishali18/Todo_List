# program to check whether two strings are anagrams are not
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
# convert both the strings into lowercase

str1 = str1.lower()
str2 = str2.lower()

# sort the strings
sorted_str1 = sorted(str1)
sorted_str2 = sorted(str2)
# compare the sorted strings
if sorted_str1 == sorted_str2:
    print(f'"{str1}" and "{str2}" are anagrams.')
else:
    print(f'"{str1}" and "{str2}" are not anagrams.')