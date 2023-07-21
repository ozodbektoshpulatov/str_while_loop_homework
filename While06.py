def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    constant=0
    ans=0
    while constant<len(s):
        if s[constant] in "qwrtypsdfghjklzxcvbnm":
            ans+=1
        constant+=1
    return ans
print(main("abdeofafgswertum"))