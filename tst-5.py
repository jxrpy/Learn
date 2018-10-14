#!/usr/bin/env python3

colors = [
 (255,160,137),
 (143, 80,157),
 (255,255,255),
 (162,173,208),
 (255, 67,164),
 ]

nums = [255,143,137,162,67,164,173,80,157]
n = 0

def x(x):
  return(x[n])

def y(x):
  return(x[1])

def w(x):
  return(x[2])

print(sorted(colors))
print()
print(sorted(colors,key=lambda x: (x[n])))
print(sorted(colors,key=lambda x: (x[1])))
print(sorted(colors,key=lambda x: (x[2])))
print()
print(sorted(colors,key=x))
print(sorted(colors,key=y))
print(sorted(colors,key=w))
print()
print(nums)
print(sorted(nums))
print()
nums = sorted(nums)
print(nums)




