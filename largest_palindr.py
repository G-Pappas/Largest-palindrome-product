    # A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
    # Find the largest palindrome made from the product of two 3-digit numbers.

    # determines whether or not an integer is a palindrome;
    # that is, if it reads the same from both ways
def reverseNumber(n):#reverse the number
    s = str(n)
    reverseString = ""

    for i in range (len(s) - 1, -1, -1):#start value, end value , step
        reverseString += s[i]#reverse the string

    return reverseString == s#return True is number is palindrome False if it's not

    # returns largest palindrome that is a multiple of two 3 digit numbers
def LargestPalindrome():
    palindrome = 0

    for i in range (999, 99, -1):
        for j in range (999, 99, -1):
            # if product is palindrome and is greater than last recorded palindrome
            if reverseNumber(i * j) and i * j > palindrome:
                palindrome = i * j
    return palindrome;

print (LargestPalindrome())
