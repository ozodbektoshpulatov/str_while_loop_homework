def main(s):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    s=input()
    ind=0
    ans=0
    while ind<len(s):
        if s[ind] in "0123456789":
            ans+=1
        ind+=1
    return ans
print(main("0123456789"))