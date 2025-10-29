
def isAnagram(word1,word2):

    list1=list(word1)
    list2=list(word2)

    list1.sort()
    list2.sort()

    if list1 == list2:
        print("The words are Anagrams")
    else:
        print("The words are not Anagrams")


# Main

word1 = input("Enter the first word:")

word2 = input("Enter the second word:")

isAnagram(word1,word2)