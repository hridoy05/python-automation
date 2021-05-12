import re


def isValid(s):
    Pattern = re.compile("^(?:\+88|88)?(01[3-9]\d{8})$")
    print(Pattern.match(s))
    return Pattern.match(s)


# Driver Code
s = "01707112674"
if isValid(s):
    print("Valid Number")
else:
    print("Invalid Number")
