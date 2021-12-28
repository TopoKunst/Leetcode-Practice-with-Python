class Solution:
    def isPalindrome(self, x: int) -> bool:
        flag = True
        # transform to the list of string
        s = [i for i in str(x)]
        l= len(s)
        for i in range(l // 2):
            if not s[i] == s[l-i-1]:
                flag = False
        return flag

    '''
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]
    '''
    '''
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        # compute the palindrome number
        pal = 0
        temp = x
        while temp != 0:
            pal = pal * 10 + temp % 10
            temp = temp // 10
        return pal == x
    '''