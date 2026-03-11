import pandas as pd

s = pd.Series([1,2,3], index = ["Piyush","Ambika","Ananya"])
#series are homogenous, mutable vales , immutable size, in case changing values new series is generated

print(s, type(s))
print(s.index)
print(s["Piyush"])
print(s[0])
print(s["Ambika"])

s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([10,20,30,40,50])

print(s1+s2)
s1[2] = 35
print(s1)
changed_s1 = s1.drop(2)
print(changed_s1)