## Given two strings a and b. The task is to find if the string 'b' can be obtained by rotating another string 'a' by exactly 2 places.

def isRotated(s1, s2):
    if len(s1) != len(s2):
        return False

    if len(s1) < 2:
        return s1 == s2
    clockwise = ""
    anticlockwise = ""
    l = len(s2)

    anticlockwise = anticlockwise + s2[l-2:] + s2[0: l-2]
    clockwise = clockwise + s2[2:] +s2[0:2]

    return (s1 == clockwise or s2 == anticlockwise)

s1 = "amazon"
s2 = "azonam"
isRotated(s1, s2)
