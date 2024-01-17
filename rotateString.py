#Questions link for LC - https://leetcode.com/problems/rotate-string/
#Question number on CTCI book - 1.9

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        ans=
        return isSubstring(s,goal)

def strcmp(s1,s2,l):
    for i in range(0,l):
        if s1[i]!=s2[i]:
            return False
    return True

def isSubstring(s1,s2):
    l1=len(s1)
    l2=len(s2)
    if(l1!=l2):
        return False
    for i in range(0,l1):
        rotateds1=s1[i:l1]+s1[0:i]
        print(rotateds1)
        print("Compairing "+rotateds1+" & "+s2)
        if strcmp(rotateds1,s2,l1):
            return True
    return False
        