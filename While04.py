def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    ind=0
    ans=0
    while ind<len(s):
        if s[ind] in "QWERTYYYYYYYYYYYYUUUUUUUUUUUUIOPASDFGHJKLZXCVBNM":
            ind+=1
        ans+=1
    return ans
print(main("ASDFGH"))