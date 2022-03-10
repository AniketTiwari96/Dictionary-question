# dict={1:"aniket",2:18,}
# dict[3]="male"
# print(dict)

# car_detals={"brand":"suzuki","model":"dsire","year":2020}
# car_detals.pop("brand")
# print(car_detals)


# car_detals={"brand":"suzuki","model":"dsire","year":2020}
# car_detals.popitem()
# print(car_detals)


# d={"brand":"suzuki","model":"dsire","year":2020}
# del d ["brand"]
# print(d)


# car_detals={"brand":"suzuki","model":"dsire","year":2020}
# for i,y in car_detals. items():
#     prin

# d={}
# rang=int(input("enter your range"))
# for i in range(rang):
#     key=input("enter your key")
#     va=input("enter your va")
#     d.update({key:va})
# print(d)


# d1={1:10,2:20}
# d2={3:30,4:40}
# d3={5:50,6:60}
# d4={}
# for i in (d1, d2, d3):
#     d4.update(i)
# # print(d4)
# a=Counter(d1)
# b=Counter(d2)
# c=Counter(d3)
# add=a+b+c
# d4=dict(add)
# print(d4)
# d4={**d1,**d2,**d3}
# print(d4)


# dic={"name":"aniket","marks":56}
# d={}
# ran=int(input("enter your range"))
# for i in range(ran):
#     key=input("enter your key")
#     v=input("enter your vailu")
#     d.update({key:v})

# d={"data1":100,"data2":-54,"data3":247}
# s=0
# for i in d.values():
#     s+=i
# print(s)
# d={1:"aniket tiwari",2:"in",3:{"a":"aniket","b":"tiwari","c":"uttar prdesh"}}
# del d[3]["a"]
# print(d)

# d1=["one","two","three","four","five"]
# d2=[1,2,3,4,5]
# d={}
# a=dict(zip(d1,d2))
# print(a)
# for i in d1:
#     for j in d2:
#         d[i]=j
#         d2.remove(j)
#         break
# print(d)

# d={"b":"red","bat":"4","w":8,"b":"green","bat":"3"}
# # d1=list(dict.fromkeys(d))
# # d1=list(set(d))
# # print(d)
# d1=[]
# d2=dict()
# for key,values in d.items():
#     if values not in d1:
#         d1.append(values)
#         d2[key]=values
# print(d)
# d={}
# sum=0
# rang=int(input("enter your number"))
# for i in range(rang):
#     key=input("enter your key")
#     value=int(input("enter your value"))
#     d.update({key:value})
# print(d)
# for i in d.values():
#     sum+=i
# print(sum)

# v=set(val for i in d for val in i.values())
# print(v)

# count={"M":0,"I":0,"S":0,"P":0}
# word="MISSISSIPPI"
# for i in word:
#     if i=="M":
#         count["M"]=count["M"]+1
#     elif i=="I":
#             count["I"]=count["I"]+1
#     elif i=="S":
#                 count["S"]+=1
#     elif i=="P":
#                     count["P"]+=1
# print(count)
        
        
# d={"aniket":["sub1","sub2","sub3"],"tiwari":["sub1","sub2"]}
# count=0
# for i in d.values():
#     if i:
#         count+=len(i)
# print(count) 

# for key,values in d.items():
#     if values :
#         count+=len(values)
#     else:
#         count+=len(key)
# print(count)

# d={"a":10,"b":20,"c":3,"d":30,"e":2}
# n=3
# d1=(n,d, key =d.get)
# d1=sorted(d)
# print(d1)
# for key, values in  sorted(d.items()):
#     if values>3:
#         print(values)
    # print(key,values)
# dict={}
# rang=int(input("enter yur range"))
# for i in range(rang):
#     key=input("enter your key")
#     value=int(input("enter your values"))
#     dict.update({key:value})
# for key,values in sorted(dict.items()):
#     if values>57 and values<=100:
#         print(values)

# dict=dict()
# for i in range(1,16):
#     dict[i]=i**2
# print(dict)

# dict1={"aniket":45,"tiwari":60,"ram":30,"sayam":20,"roshan":50}
# d=sorted(dict1.items(),key=lambda t:t [1],reverse=True)
# print(d)
# d1=dict(sorted(dict1.items(),key=lambda item: item[1], reverse=(dict1)))
# print(d1)

# a={(1,2):1,(2,3):2}
# print(a[1,2])
# a={"a":1,"b":2,"c":3}
# print(a["a"])

# s={}
# a={}
# d={}
# s["name"]="aniket tiwari"
# a["aage"]=18
# d["s"]=s
# d["a"]=a
# print(len(d["s"]))

# dict={}
# dict[1,2,4]=8
# dict[4,2,1]=10
# dict[1,2]=12
# sum=0
# for i in dict:
#     sum+=dict[i]
# print(sum)
# print(dict)
# 
# dict1={"aniket":45,"tiwari":60,"ram":30,"sayam":20,"roshan":50}
# d=sorted(dict1.items(),key=lambda t:t [1])

# list1=[]
# rang=int(input("enter your range "))
# for i in range(rang):
#     values=int(input("enter your  number"))
#     list.append(values)
# # print(list)
# d=dict(list)
# for i in range(rang):
#     for j in range(0,rang-i-1):
#         if list1[j]>list1[j+1]:
#             a=list1[j]
#             list1[j]=list1[j+1]
#             list1[j+1]=a
# d=dict(list1)
# print(d)

# dict={}
# rang=int(input("entr your range"))
# for i in range(rang):
#     key=input("enter your key")
#     value=input("enter your values")
#     dict.update({key:value})
# print(dict)
# for i in range(rang):
#     for j in (0,rang-i-1):
#         if dict[j]>dict[j+1]:
#             d=dict[j]
#             dict[j]=dict[j+1]
#             dict[j+1]=d
# print(dict)

# t=(1,2,3,3)
# t[2]=10
# print(t)
        


# qlist=["1.what is your name","2.where are you live",]
# op=[["a.aniket","b.tiwari","c.kumar","d.aniket tiwari","e.fiftiy"],["a,punjab","b.himachal pradesh","c.uttar pradesh","d.goa","e.fiftiy"]]
# ans=["d","d"]
# fiftiy=[["a"],["d"],["b"],["c"]]
# ans.append(fiftiy)
# scor=0
# right_ans=0
# index=0
# for i in range(len(qlist)):
#     print(qlist[i])
#     for j in (op[i]):
#         print(j)
#     g=input("plese enter your guess ")   
#     if g in ans:   
#             print("your guess is right")
#             print("aapka dusra question hai")
#             # if g in fiftiy:          
#     else:
#         print("sorry your guess is wrong")
#         print("appka dusra question hai

# dict={}
# r=int(input("enter your rangr"))
# for i in range(r):
#     key=input("entr your key")
#     v=input("enter your value")
#     dict.update({key:v})
# print(dict)
# import sys
# list=[1,2,3,4,"aniket"]
# tupal=(1,2,3,4,"anikwt")
# print(sys.getsizeof(list))
# print(sys.getsizeof(tupal))

# tupal=(1,2,3,4,"ani")
# tupal=(1,2,3,4,"anikwt")
# t=tupal+tupal
# print(t*3)
# t=tupal[2:]
# print(t)
# for i in range(len(tupal)):
#     print(tupal[i])
    
# tupal=(1,2,3,4,"anikwt")
# l=list(tupal)
# l[1]=5
# print(l)
# tupal=tuple(l)
# print(tupal)

# tupal=(1,2,3,4,"anikwt")
# t=tuple("aniket")
# print(t)

# name=("aniuket","tiwari",1,2,3)
# name=(1,2,1,2,6,3,)

# a=name.count(2)
# print(a)
# a=name.index(3)
# print(a)
# print(min(name))
# l=len(name)
# print(l)
# print(len(name))
# print(max(name))

# d=tuple({1:"w",2:"f"})
# print(d)

# t=("aniket","tiwari","aniket tiwari")

# a={"aniket","tiwari","rahul","kumar"}
# b={"aniket","kumar","sita","rita","sabana"}
# a={"aniket"}
# b={"tiwari"}
# c=a.isdisjoint(b)
# print(c)
# c=a.union(b)
# print(c)
# c=a.difference(b)
# print(c)
# c=a.issubset(b)
# print(c)
# a.difference_update(b)
# print(a)

# def fun(a=12,b=12):
#     print(a//b)
#     return a*b
# fun(a=a,b=2)

# def my_name():
#     print("aniket tiwari kumar")
# my_name()

# import datetime
# a=datetime.datetime.now()
# print(a)
# import random
# l=["aniket","tirari","jhure"]
# print(random.choices(l))\

# import random
# # l=[1,3,2,5,9,7,6,5]
# print(random.randrange(1,9))

# import random
# # l=[1,3,2,5,9,7,6,5]
# print(random.randint(1,9))

# import random
# #  l=[1,3,2,5,9,7,6,5]
# print(random.random())


# import random
# i=[1,2,3,4,5,6,7,8,9,0]
# for a in range(1,101):
#     x=random.choice(i)
#     i.remove(a)
#     print(x)
# i=[1,2,3,4,5,6,7,8,9,0]
# i.count(2)
# print(i)i=[1,2,3,4,5,6,7,8,9,0]
# i.count(2)
# print(i)
# list=[1,2,3,4,5,6,7,8,9,0]
# l=list.pop(7)
# print(l)


# d={"name":"aniket","age":18,"place":"india",1:"aniket tiwari",2:"sabana"}
# l=len(d)
# print(l)

# d={"name":"aniket","age":18,"place":"india",1:"aniket tiwari",2:"sabana"}
# d.pop("name")
# print(d)

# d={"age":18,"place":"india",1:"aniket tiwari",2:"sabana"}
# d1=d.setdefault("name","sabaana")
# print(d)
# d={"aniket","tiwari","aniket tiwari"}
# d1=2
# d3=dict.fromkeys(d,d1)
# print(d3)
# d1=d.copy()
# print(d1)
# del d
# print(d)
# d.clear()
# print(d)

# d={1:{},2:{}}
# print(d)


# d={"brand":"sujuki","model":"diser","year":2022}
# s=dict(d)
# print(s)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisdict)
# print(mydict)

# for i,y in d.items():
#     print(i,y)
# for i in d.keys():
#     print(i)

# for i in d.values():
#     print(i)
# for i in d:
#     print(d[i])
# d.clear()
# print(d)
# del d 
# print(d)
# del d["brand"]
# print(d)
# d.popitem()
# print(d)
# d["year1"]=1234
# print(d)
# d.update({"year1":2023})
# print(d)
# d["year"]=2025
# print(d)
# a=d.items()
# print(a)
# a=d.values()
# print(a)
# d["colors"]="white"
# print(d)
# a=d.keys()
# print(a)
# d1=d.keys()
# print(d1)
# d1=d.get(d)
# print(d)
# print(d["brand"])

# d={"name":{"name":"aniket tiwari","year":18},"age":{1:18,2:20},"place":{1:"india",2:"pakistan"}}
# print(d["name"]["year"])
# d={"name":"aniket tiwari","age":18,"gendar":"male","place":"india"}
# a=d["name"]
# print(a)

# d={"name":"aniket tiwari","age":18}
# d["place"]="india"
# print(d)


# d={"name":"aniket tiwari","age":18}
# d.update({"name":"sabana"})
# print(d)
# d["name"]="sabana"
# print(d)


# d={"name":"aniket tiwari","age":18}
# a=d.copy()
# print(a)


# d={"name":"aniket tiwari","age":18}
# d.pop("name")
# print(d)
# # d.popitem()
# # print(d)


# # d={"name":"aniket tiwari","age":18,"place":"india"}
# # for i in d:
# #     print(d[i])


# # d={"name":"aniket tiwari","age":18,"place":"india"}
# # for i,y in d.items():
# #     print(i,y)

# d1={1:2,3:4}
# d2={5:6,7:8}
# d3={9:10,11:12}
# d4={}
# for i in (d1, d2, d3):
#     d4.update(i)
# print(d4)

# d1={1:10,2:20}
# d2={3:30,4:40}
# d3={5:50,6:60}
# d4={}
# for i in (d1, d2, d3):
#     d4.update(i)
# print(d4)


# d1={1:10,2:20}
# d2={3:30,4:40}
# d3={5:50,6:60}
# d4={}
# d4={**d1,**d2,**d3}
# print(d4)
# a=Counter(d1)
# b=Counter(d2)
# c=Counter(d3)
# d=a+b+c
# d4=dict(d)
# print(d4)

# a=Counter(d1)
# b=Counter(d2)
# c=Counter(d3)
# add=a+b+c
# d4=dict(add)
# print(d4)

# d={1:"navgurukul",2:"in",3:{"a":"aniket","b":"anikrt tiwari","c":"tiwari"}}
# del d[3]["a"]
# print(d)

# d1=["one","two","three","four","five"]
# d2=[1,2,3,5,6]
# # d={}
# a=dict(zip(d1,d2))
# print(a)

# dic={}
# for key in dlist:
#     for vailus in dlist2:
#         dic[key]=vailus
#         dlist2.remove(vailus)
#         break
# print(dic)


# d={"name":"aniket tiwari","age":18,"place":"india","name":"aniket tiwari","age":18}
# d1=[]
# d2=dict()
# for key,vailus in d.items():
#     d1.append(vailus)
#     d2[key]=vailus
# print(d2)
# d=list(dict.fromkeys(d))
# print(d)

# d=[{"fist":"1"},{"second":"2"},{"third":1},{"four":5}]

# a=set(val for dic in d for val in dic.values())
# for i in a:
#     print(i)
# a=[]
# for i in d:
#     for j in i.values():
#         a.add(j)
# print(a)
# s=set()
# for i in d:
#     for v in i.values():
#         s.add(v)
# print(s)
# d=list(set(d))
# print(d)


# d=,{4:"c",}{1:"a",2:"b",3:"a"}
# a=[]
# for i in d:
    # if i not in a:
        # a.append(i)
        # print(i)

# d=[{"fist":"1"},{"second":"2"},{"third":'1'},{"four":'5'}]
    # s=d[a]
    # s1=s.values()
    # print(a.values())
    # if s1 not in d1:
        # d1.append(s1)
# d1 = []
# for i in d:
#     for j in i:
#         if i[j] not in d1:
#             d1.append(i[j])
# print(d1)

# d={}
# ran=int(input("enter your range"))
# for i in range(ran):
#     key=input("enter your key")
#     values=int(input("enter your values"))
#     d.update({key:values})
# print(d)

# d={"m":0,"i":0,"s":0,"p":0}
# a={"v":0}
# d=[]
# c=dict(d)
# ran=int(input("enter your range"))
# for i in range(ran):
#     v=input("enter your values")
#     d.append(v)
# d=dict(d)
# word="mississippi"
# for i in word:
#     if i=="v":
#         d[""]+=1
#     elif i=="v":
#         d[v]+=1
#     elif i=="v":
#         d["v"]+=1
#     elif i=="v":
#         d["v"]+=1
# print(c)

# d={"aniket":{"a1","a2","a3",'a4'},"aniket tiwari":{"b1","b2","b3","b4"}}
# count=0
# for i,j in d.items():
#     if j:
#         count+=len(j)
# print(count)


# dict1={"aniket":45,"tiwari":60,"ram":30,"sayam":20,"roshan":50}
# d=sorted(dict1.items())
# print(d[-3:])
# dict2=sorted(dict1,Values=dict1.get,reverse=True)[:3]
# print(dict2)
# d=sorted(dict1.items(),key=lambda t:t [1])


# dict1={"aniket":45,"tiwari":60,"ram":30,"sayam":20,"roshan":50}
# for i in dict1.keys():

#     print(i)
# user_input= raw_input()
# if dict1.has_key(user_input):
#     print(user_input,dict1[user_input])
# else:
#     print("n")
# word = {'right':'left','up':'down','good':'bad','cool':'hot','east':'west'}
# print( "Enter any word from following words")
# for i in word.keys():
# 	print (i)
# user_input = raw_input()
# if word.has_key(user_input):
# 	print ("Antonym of",user_input,"is",word[user_input])
# else:
# 	print ("Enter correct input")


# d={}
# r=int(input("entr your range"))
# for i in range(r):
#     key=input("enter your key")
#     values=int(input("enter your values"))
#     d.update({key:values})
# d1=sorted(d.values())
# print(d1)

# d={}
# for i in range(1,16):
#     d[i]=i**2
# print(d)

# d={(1,2):1,(3,4):2}
# print(d.items())

# d=["no bun ","bug bun bug bug bug","bunny bug ","buggy bug bug buggy"]
# b="bug"
# a={}
# for i in d:
#     c=0
#     for j in i.split():
#         if j==b:
#             c+=1
#     a[c]=i
# x=[]
# for s in sorted(a):
#     x.append(a[s])
# # x.reverse()
# print(x)

# import operator
# d={1:1,2:2,3:3,4:4,5:1,6:2}
# a=dict(sorted(d.items(),key=operator.itemgetter(1)))
# print("ascending order")
# print(a)
# print("descending order")
# a=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
# print(a)

# print("how can print ascending and descing order")
# d={1:1,2:2,3:3,4:4,5:1,6:2}
# a=(sorted(d.items()))
# print(dict(a))
# b=a[::-1]
# print(dict(b))

# d={0:10,1:20}
# d[2]=30
# print(d)

# d1={1:10,2:20}
# d2={3:30,4:40}
# d3={5:50,6:50}
# d4={}
# for i in d1,d2,d3:
#     d4.update(i)
# print(d4)

# d={1:1,2:2,3:3,4:4,5:1,6:2}
# n=int(input("enter your key"))
# v=int(input("enter your v"))
# if n and v in d:
#     print("h")
# else:
#     print("n")


# d1={1:10,2:20}
# d2={3:30,4:40}
# d3={}
# for i in d1,d2:
#     d3.update(i)
# print(d3)

# a=d1.copy()
# a.update(d2)
# print(a)

# print("how can multiply")
# d={"a":100,"b":20,"c":30}
# s=1
# for i in d:
#     s=s*d[i]
# print(s)

# d={"a":100,"b":20,"c":30}
# if "a" in d:
#     del d["a"]
# print(d)


# d={1:30,2:30,3:20}
# a=sorted(d.items())
# print(dict(a[-1::]))
# print(dict(a[::-1]))
# print(d[1])

# from collections import Counter
# d1={"a":30,"B":20}
# d2={"c":20,"B":40}
# a= Counter(d1) + Counter(d2)
# print(a)

# d1=[]
# for i in d:
#     for j in i:
#         # if i[j] not in d1:
#         if i[j]:
#             d1.append(i[j])
# print(d1)

# d1={1:["a","b"],2:["c","d"]}
# a,b=d1.values()
# for i in a:
#     for j in b:
#         print(i+j)

# d=[{"item":"item1","amount":400},
#   {"item":"item2","amount":300},
#   {"item":"item1","amount":700}]
# d1={}
# for i in d:
#       if i["item"]not in d1:
#           d1.update({i["item"]:i["amount"]})
#       else:
#           d1[i["item"]]= d1[i["item"]]+i["amount"]
# print(d1)

# d={"a1":[1,2,3],"a2":[5,6,7],"a3":[9,10,11]}
# a=(list(d.values()))
# for i in range(len(a)):
#     print(*(a[i]))

# def d():
#     print("aniket tiwari")
# d()

# a=lambda x:x+10
# p=(a(20)
# print(p))
# class p:

# print("roman number")
#     def roman(self,number):
#         num=[1,2,3,4,5,9,10,40,50,90,100,400,500,900,1000]
#         sym=["I","II","III","IV","V","IX","X","XL","L","XC","C","CD","D","CM","m"]
#         i=0
#         roman_number=""
#         while number>0:
#             for _ in range(number//num[i]):
#                 roman_number+=sym[i]
#             i+=1
#         return roman_number
# print(p().roman(1))
# print(p().roman(400))

# print("roman nmber")
# num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
#            (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

# def roman(num):
#     roman = ''
#     while num > 0:
#         for i, r in num_map:
#             while num >= i:
#                 roman += r
#                 num -= i

#     return roman
# n=int(input("enter your nuber"))
# print(roman(n))


# print("roman number")
# def roman (number):
#     num=[1,2,3,4,5,9,10,40,50,90,100,400,500,900,1000]
#     sym=["I","II","III","IV","V","IX","X","XL","L","XC","C","CD","D","CM","m"]
#     r=""
#     a=0
#     while numbers>0:
#         div=numbers//num[a]
#         numbers=numbers%num[a]
#         while div:
#             r=r+sym[a]
#             div-=1
#         a+=1
#     return roman
# n=input("enter your nuber")
# print(roman(n))



# print("roman to integer")
# r = input("Enter roman : ")   
# d={"M":1000,"CM": 900,"D": 500,"CD": 400,"C": 100,"XC": 90,"L":50,"XL":40,"X":10,"IX":9,"V": 5,"IV":4,"I":1}
# ans=0
# for i in range(len(r)):
#     # if i+1!=len(r) and d[r[i]]<d[r[i+1]]:
#     if i:
#         ans=ans-(d[r[i]])
#     else:
#         ans=ans+d[r[i]]
# print(ans)


# # print("integer to roman")
# n=int(input("enter your number"))
# d= {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
# a=""
# for i in d:
#     b=n//i
#     c=b*d[i]
#     a+=c
#     n%=i
# print(a)

# print("entger to roman")
# list=[(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
#         (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
# roman = ''
# num=int(input("entr your number"))
# while num > 0:
#     for i,r in list:
#             while num >= i:
#              roman += r
# #              num -= i
# print(roman)
# print('bhupendra')

# print("two list  se dictionary ")
# d1=["one","two","three","four","five"]
# d2=[1,2,3,5,6]
# # d={}
# a=dict(zip(d1,d2))
# print(a)

# d1=["one","two","three","four","five"]
# d2=[1,2,3,5,6]
# d3=[11,22,33,44,55]
# # d={}
# a=dict(zip(d1,d2))
# print(a)

# d1=["one","two","three","four","five"]
# d2=[1,2,3,5,6]
# # d3=[11,22,33,44,55]
# d4={}
# for key in d1:
#     for values in d2:
#         d4[key]=values
#         d2.remove(values)        
#         break
# print(d4)

# d1=[1,2,3,5,6]
# d2=["one","two","three","four","five"]
# d3={}
# for i in range(len(d1)):
#     d3[d1[i]]=d2[i]
# print(d3)

# a = [1,2,3,4,5]
# b = ["Name","Age","Class","Roll-No"]
# c = [
#       ["Aarav",14,"9th",32],
#       ["Amit",12,"7th",7],
#       ["Saniya",12,"7th",34],
#       ["Kiran",10,"5th",23],
#       ["Prince",14,"8th",15]
# ]
# d={}
# d1=[]
# for i in range(len(c)):
#     for j in range(len(b)):
#         d[b[j]]=c[i][j]
#     if d not in d1:
#         d1.append(str(d))
# d3={}
# for k in range(len(a)):
#     d3[a[k]]=d1[int(k)]
# print(d3)


# a = [1,2,3,4,5]
# b = ["Name","Age","Class","Roll-No"]
# c = [
#       ["Aarav",14,"9th",32],
#       ["Amit",12,"7th",7],
#       ["Saniya",12,"7th",34],
#       ["Kiran",10,"5th",23],
#       ["Prince",14,"8th",15]]
# d={}
# d1=[]
# for i in range(len(c)):
#     for j in range(len(b)):
#         d[b[j]]=c[i][j]
#     if d not in d1:
#         d1.append(str(d))
        
# d3={}
# for k in range(len(a)):
#     d3[a[k]]=d1[int(k)]
# print(d3)

# n=int(input("enter your number"))
# a1=0
# a2=1
# a3=a1+a2
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(str(a3)+"  ",end="")
    #     a3=a1+a2
    #     a1=a2
    #     a2=a3
    # print()


# a= [1,2,3,4,5]
# b=["Name","Age","Class","Roll-No"]
# c=[["Aarav",14,"9th",32],
#    ["Amit",12,"7th",7],
#    ["Saniya",12,"7th",34],
#    ["Kiran",10,"5th",23],
#    ["Prince",14,"8th",15]]
# d1={}
# for i in range(len(c)):
#     v = dict(zip(b,c[i]))
#     d1[a[i]]= v
# print(d1)

# d2=[]
# for i in range(len(c)):
#     for j in range(len(b)):
#         d1[b[j]]=c[i][j]
#     if d1 not in d2:
#         d2.append(str(d1))
# d3={}
# for k in range(len(a)):
#     d3[a[k]]=d2[int(k)]
# print(d3)


# print("roman to intger")
# d={"M":1000,"CM": 900,"D": 500,"CD": 400,"C": 100,"XC": 90,"L":50,"XL":40,"X":10,"IX":9,"V": 5,"IV":4,"I":1}
# n=input("entr your number")
# ans=0
# for i in range(len(n)):
#     if i+1 !=len(n) and d[n[i]]<d[n[i+1]]:      
#         ans-=d[n[i]]
#     else:
#         ans+=d[n[i]]
# print(ans)

# print("inter to roman")
# d= {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
# n=int(input("entr your number"))
# ans=""
# for i in d:
#     a=n//i
#     b=a*d[i]
#     ans+=b
#     n%=i
# print(ans)

# list=[(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
#         (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
# a=""
# n=int(input("enter your number"))
# while n>0:
#     for i,r in list:
#         while n>= i:
#             a+=r
#             n-=i
# print(a)

# from collections import defaultdict
# a = [1,2,3,4,5]
# b = ["Name","Age","Class","Roll-No"]
# c= [
#       ["Aarav",14,"9th",32],
#       ["Amit",12,"7th",7],
#       ["Saniya",12,"7th",34],
#       ["Kiran",10,"5th",23],
#       ["Prince",14,"8th",15]]
# d = defaultdict(dict)
# for x, y, z in zip(a, b, c):
#     d[x][y] = z
# print(d)
# d = {}
# for x, y, z in zip(a, b, c):
#     d.setdefault(x,{})[y] = z

# print(d)


# d={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# # c=list(d)
# e=[]
# a=0
# for i in d.values():
#     if i>a:
#         a=i
#         e.append(int(a))
#         print(e)

# d1={"aniket":45,"tiwari":60,"ram":30,"sayam":20,"roshan":50}
# # d=sorted(d1.items())
# # print(dict(d))
# d=sorted(d1,values=d1.get,reverse=True)
# print(dict(d))



# markdict={"aniket":45,"tiwari":60,"ram":30,"sayam":20,"roshan":50}
# marklist=list(markdict.items())
# print(marklist)
# l=len(marklist)
# for i in range(l-1):
#     for j in range(i+1,l):
#         if marklist[i][1]>marklist[j][1]:
#             t=marklist[i]
#             marklist[i]=marklist[j]
#             marklist[j]=t
#     sortdict=dict(marklist)
# print(sortdict)

# a=input("enter")
# for i in range(len(a)-1,-1,-1):
#     print(a[i],end=" ")


# d={"brand":"ford","model":"mustang","year":2020,"year":2022}
# d= {"name":"aniket tiwari"}
# d1={"name":"sabana"}
# d2={"name":"aniket sanaba"}
# a={"d":d,"d1":d1,"d2":d2}
# print(a)# d1=dict(d)
# print(d1)
# for i,y in d.items():
#     print(i,y)

# for i in d:
#     print(d[i])
# print("remove item")
# d.clear()
# print(d)
# del d["model"]
# print(d)
# d.popitem()
# print(d)
# d.pop("model")
# print(d)
# d.update({"brand":"tiwari"})
# print(d)
# d["brand"]="tiwari"
# print(d)
# if "model" in d:
#     print("ys")
# else:
#     print("no")
# a=d.items()
# d["colors"]="red"
# print(dict(a))
# x=d.values()
# print(x)
# d["colors"]="red"
# print(d)
# d1=d.keys()
# print(d1)
# e=d.get("model")
# print(e)
# d1=d["model"]
# print(d1)
# print(d["year"])
# print(d)

# d={"brand":"ford","model":"mustang","year":2020,"year":2022}
# a=dict(d)
# print(a)
# a=d.copy()
# print(a)
# d.clear()
# print(d)

# d={"brand":"ford","model":"mustang","year":2020,"year":2022}
# a=("a","b")
# b=(1,2)
# c=dict.fromkeys(a,b)
# print(c)

# d=("key1","key2","key3")
# d1=dict.fromkeys(d)
# print(d1)

# d={"brand":"ford","model":"mustang","year":2020,"year":2022}
# a=d.get("place","india")
# print(a)

# a=d.get("brand")
# print(d.get("model"))

# d={"brand":"ford","model":"mustang","year":2020,"year":2022}
# print(d.setdefault("model","india"))

# d={"brand":"ford","model":"mustang","year":2020,"year":2022}
# d.update({"color":"white"})
# print(d)
# d.update({"brand":"tiwari"})
# print(d)

# d=dict(name="aniket",age=20)
# print(d)

# d={1:"aniket",2:"tiwari"}
# print(d)
# d={"name":"aniket",1:[1,2,3]}
# print(d[1])

# d={"name":"aniket","age":20,"gender":"male",4:{"organisation":"navgrukul","place":"dharamsala",}}
# print(d["gender"])
# print(d[4])
# print(d[4]["place"])

# d={"name":"aniket","age":18}
# d["place"]="india"
# print(d)
# d.update({"place":"india"})
# print(d)

# d={"name":"sabaan","age":18}
# d[3]={"name":"aniket","place":"india"}
# print(d)

# d={"name":"sabaan","age":18}
# a=d.copy()
# print(a)
# s=dict.copy(d)
# print(s)



# d={"name":"aniket","age":20,"gender":"male",4:{"organisation":"navgrukul","place":"dharamsala",}}
# del d ["name"]

# print(d)
# del d[4]
# print(d)

# d={"name":"aniket","age":20,"gender":"male",4:{"organisation":"navgrukul","place":"dharamsala",}}
# for i in d:
#     if i==4:
#         for j in d[i]:
#             print(j)


# d={"name":"aniket","age":20,"gender":"male",4:{"organisation":"navgrukul","place":"dharamsala",}}
# print(len(d))

# d1={1:10,2:20}
# d2={3:30,4:40}
# d3={5:50,6:60}
# d={}
# d={"d1":d1,"d2":d2,"d3":d3}
# print(d)
# for i in d1,d2,d3:
#     if i:
#         d.update(i)
# print(d)

# d={"a1":100,"a2":200,"a3":-53}
# s=0
# for i in d.values():
#     s+=i
# print(s)

# d={1:"navgurukul",2:"in",3:{"a":"welcome","b":"to",'c':"dharamsala"}}
# del d[3]["a"]
# print(d)

# l1=["one","two","three","four","five"]
# l2=[1,2,3,4,5]
# d={}
# # d=dict(zip(l1,l2))
# # print(d)
# for key in l1:
#     for values in l2:
#         d[key]=values
#         l2.remove(values)
#         break 
# print(d)


# n=int(input("enter your number"))
# a1=0
# a2=1
# a3=a1+a2
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(str(a3)+"  ",end="")
#         a3=a1+a2
#         a1=a2
#         a2=a3
#     print()

# n=int(input("entre your numbner")
# num=1
# v=""
# for i in range(1,n+1):
#     if i%2!=0:
#         for j in range(n):
#             v=v+" "+str(num)
#             num+=1
#     else:
#         for j in range(n):
#             v=str(num)+" "+v
#             num+=1
#     print(v.strip())
#     v=" "

# n=int(input("enter your number"))
# for i in range(1,n+1):
#     for j in range(n+1,i-1):
#         print(" ",end="")
#     c=1
#     for k in range(i-1,-i,-1):
#         print(i-abs(k),end="")
#     print( )

# n=int(input("enter your number"))
# for i in range(n+1):
#     for j in range(i):
#         print("",end="")
#     c=1
#     for k in range(1,i+1):
#         print(c,end="")
#         c=c*(i-k)//k
#     print()

# n=int(input("enter your number"))
# for i in range(1,n+1):
#     n1=1
#     for j in range(1,i+1):
#         print(n1,end=" ")
#         n1=n1*(i-j)//j
#     print()

# i=1 
# n=int(input("enter your number"))
# k=1 

# for x in range(1,n+1): 
#     if k%2==1: 
#         print((i),end=" ") 
#         print((i+1),end=" ")
#         print((i+2),end=" ") 
#         print((i+3),end=" ") 
#         # print((i+4),end=" ") 
#         k+=1 
#         i+=n  
#     else: 
#         # print((i+4),end=" ") 
#         print((i+3),end=" ") 
#         print((i+2),end=" ") 
        
#         print((i+1),end=" ") 
#         print((i),end=" ") 
#         k+=1 
#         i+=n
#     print() 

# h="a,b,c,d,e,f,g,h,i,j,k,l,m,n.o,p,q,r,s,t,u,v,w,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
# s="The quick brown ox jumps over lazy dog"
# for i in s:
#     if i in h:
#         print("yes")
#     else:
#         print("no")

# a=[2,3,1,4,5,]
# p=sorted(a)
# print(p)







# def h(s):
#     for i in range(len(s),-1,-1,-1):
#         print(s[i])
# a=input("enter")
# h(a)
