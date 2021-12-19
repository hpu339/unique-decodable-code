# '''
# Author: YLX
# Date: 2021-12-18 23:40:46
# LastEditTime: 2021-12-19 19:27:47
# LastEditors: YLX
# Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
# FilePath: \.vscode\python\尾随后缀法\尾随后缀法.py
# '''
def not_empty(s):
    return s and s.strip()

def paixu(list1):    #从小到大排序
    for i in range(len(list1)):
        list1[i] = int('1'+list1[i])    #转换成数字

    list1.sort() #从小到大排序
    #print(list)

    for i in range(len(list1)):
        list1[i] = str(list1[i])    #转换成字符

    for i in range(len(list1)):
        list1[i] = list1[i][1:]   #切片去掉首字母
    ##注意，此时有可能会有空字符，所以需要用过滤器去掉
    list_c = list(filter(not_empty, list1))
    #print(list)
    return list_c

def IsRepeat(list): #对传入的列表进行重复判断，有重复返回1否则为0
    set_list = set(list)
    if len(set_list) == len(list):
        return 0
    else:
        return 1

def SeatLen(list):  #列表中长度变化的那个符号位置,如果等长，返回0
    for i in range(1,len(list)):
        if len(list[i]) == len(list[0]):
            if i != len(list)-1:
                continue
            else:
                return 0
        else:
            break   #找到唱长度变换的那个位置
    return i
    
def NewCall(list,newlist):   # ,list必须为字符串，no表示列表中长度变换的那个位置
    no = SeatLen(newlist)
    if no == 0: # 等长的
        print("是唯一可以码")
    else:
        for j in range(no,len(newlist)):
            for i in range(no,len(newlist)):
                #此时用列表的第一个元素去和比他长的元素进行匹配
                index = list[i].find(newlist[j])    #判断是否是子字符串
                if index == 0:
                    newlist.append(list[i][len(newlist[j]):])
                    # 把后面的值放到新集合里面
                    # 执行到这一句，此时第一个新集合生成，然后对其进行判断是否出
                    # 现重复项
                    if IsRepeat(newlist):
                        print("不是唯一可译码")
                        return
                    else:
                        pass
                else:
                    pass
            newlist = paixu(newlist) 
            # 排序完判断一次长度跳变位置
            no = SeatLen(newlist)   
        print("是唯一可以码")

StrC = input("请输入码字集合，相邻码字用空格分开：")+' '
Code = ''
list_c = []
newlist = []    #包括后缀的新集合
for i in StrC:
    #CodeNext = i
    if i!=' ':
        Code = Code+i
    else:
        list_c.append(Code) #添加进去，算一个码字
        Code = ''
#对列表进行排序
list_c = paixu(list_c)
# newlist = paixu(newlist)
newlist = list(list_c)  # 创建新列表并复制
# 判断是不是奇异码
if IsRepeat(list_c):
    print("奇异码")
else:
    print("非奇异码")
    NewCall(list_c,newlist)
