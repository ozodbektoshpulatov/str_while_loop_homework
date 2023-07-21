def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    ind=0
    ans=0
    while ind<len(s):
        if s[ind] in "0123456789":
            ans+=int(s[ind])
        ind+=1
    return ans
print(main("absc234hd76"))

