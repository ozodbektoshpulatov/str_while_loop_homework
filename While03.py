def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    ind=0
    ans=0
    while ind<len(s):
        if not s[ind] in "0123456789abcdefgihjklmnopqrstuvxyshchng":
            ind+=1
        ans+=1
    return ans
print(main("q'h'hx;uidhi"))