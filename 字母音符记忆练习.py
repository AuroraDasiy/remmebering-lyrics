import random as r
import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
list1='CDEFGAB'
list1=list(list1)
list2='do、re、mi、fa、sol、la、ti'
list2=list2.split('、')
dicr={}
dicf={'E': 0, 'G': 0, 'D': 0, 'A': 0, 'B': 0, 'F': 0, 'C': 0}
while True:
    num=r.randrange(0,7)
    print("{}请输入对应音符-->".format(list1[num]),end='')
    x=input()
    if x=='exit':
        break
    if x==list2[num]:
        print("恭喜你答对了(输入exit退出)")

    else:
        print("你答错了,正确答案是{}(输入exit退出)".format(list2[num]))
        if list1[num] in dicf :
            dicf[list1[num]]+=1
        else :
            dicf[list1[num]]=1
a=list(dicf.items())
a.sort(key=lambda x:x[1],reverse=True)
print("\n您の错误排行如下")
for i in a:
    print("{}--{}:{}次".format(i[0],list2[list1.index(i[0])],i[1]))
x=list(range(0,7))
y=[dicf['C'],dicf['D'],dicf['E'],dicf['F'],dicf['G'],dicf['A'],dicf['B']]
f=sp.interpolate.lagrange(x,y)
x1=np.arange(0,7)
plt.title('(CDEFGAB-->0123456)')
plt.plot(x1,f(x1))
plt.show()



