l1=[1,2,2,3,4,5,6]
print(sum(l1))
T=('a','e','f','g')
print(T)
print(T[0])
print(T*3)
print(T[-1])
print(T[1:3])
print(T[2:-1])
print(l1[1:6:3])
tup=(1,1,2,3,4,3,3)
print(tup.count(3),l1.count(2))
sval=sorted(tup)
print(sval)
sd=sorted(l1)
print(sd)
t=tuple(l1)
print(t)
tre=(1,2,(1,3,5,6,7))
print(tre[2][3])
months={"january":31,"february":28}
print(months)
print(months["january"])
print(months.keys())
print(months.values())
import json
print(json.dumps(months,indent=2))
