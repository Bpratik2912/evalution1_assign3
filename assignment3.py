
# print(p[5])
# from curses import keyname
# from typing import final


def listtodict(p):
    key=[]
    value=[]
    # print(len(p))
    for i in range(len(p)):
        # print("len of p",len(p))
        # print(i)
        if(i%2==0):
            key = key + [p[i]]
            # print(key)
        else:
            value = value + [p[i]]
            # print(value)

    dict1 = zip(key,value)
    finaldict = dict(dict1)
    return finaldict

p = ['a',1,'b',2,'c',3]
print(listtodict(p))
# print(len(p))