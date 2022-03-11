#你已经是个成熟的Buger了，需要学会写规范的代码
#程序下面这么多波浪线但是可以运行，试试重开编辑器



def for_loop(): #一个简单的循环
    for i in range(6):
        print (i**2)
    colors = ['red','green','blue']
    names = ('123','asd','hjx','test')
    for color in colors:
        print (color)
    for i in range(len(colors)):
        print (i,'--->',colors[i])
    for name,color in zip(names,colors):
        print(name,color)

for_loop()