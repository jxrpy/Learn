#!/usr/bin/env python3

def func1(a, b, *parmt, k1='1', k2='2', **parml):
  print('a=',a)
  print('b=',b)
  print('k1=',k1)
  print('k2=',k2)
  for i in range(0,len(parmt)):
    if i == 0:
      print('c=',parmt[i])
    elif i == 1:
      print('d=',parmt[i])
    elif i == 2:
      print('e=',parmt[i])
    else:
      print('unused val=',parmt[i])
  print('parml=',parml)
  for i in parml:
    print('keword name=',i,' value=',parml[i],sep='')
  return

print('Passed:',"'1p','2p','3p','4p','5p','6p','7p',k1=10,k2=20,t=1,m=2,n=3")
func1('1p','2p','3p','4p','5p','6p','7p',k1=10,k2=20,t=1,m=2,n=3)

