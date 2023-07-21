def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    ind=0
    ans=0
    while ind<len(s):
        if s[ind] in "13579":
            ans+=int(s[ind])
        ind+=1
    return ans
print(main("1abcd7uj8"))