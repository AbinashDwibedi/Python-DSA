# string = "racecare"
# def checkStringPalindrome(string,i,j):
#     if i >= j:
#         return True
#     if string[i] != string[j]:
#         return False
    
#     return checkStringPalindrome(string,i+1,j-1)
# print(checkStringPalindrome(string,0,len(string)-1))

def isPalindrome(s) -> bool:
        n = len(s)
        s= s.upper()
        def helper(i,j):
            if i>= j:
                return True
            if not s[i].isalnum():
                return helper(i+1,j)
            if not s[j].isalnum():
                return helper(i,j-1)
            if s[i] != s[j]:
                return False
            return helper(i+1,j-1)
        return helper(0,n-1)