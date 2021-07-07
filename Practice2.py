a= 1
print(a==1)
b = 2
print(5==a+b)
a = [10,20,30]

c = 30
d=60
print(c,d)

print(True + False + True)

buzz = (1,'a',2,'b')

print(buzz[0::2])
print(buzz[1::2])

obj0 = ['a','b','c','d']
obj1 = ['banana','cherry']

obj0[1:3] = obj1
print(obj0)

fruits = ['apple','banana','cherry']
for element in fruits:
    print(element[1:3])

def tester(**args):
    print(args)

tester(a = 'apple', b='banana')

value = input('값을 입력 하십시오')
print(f'입력하신 값은 {value}입니다.')