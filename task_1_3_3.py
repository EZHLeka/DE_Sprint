one = ["I","V"]
ten = ["X","L"]
hundred = ["C","D"]
thousand = ["M"]

y = input("Введите x: ")
x= int(y)
t = (x // 1000)
tt = thousand[0]*(x // 1000)
s = (x // 100 % 10)
ss =  hundred[0]*((s % 5)*(s < 4))+hundred[0]*((s == 4))+hundred[1]*((s // 5)*(s!=9))+hundred[0]*((s % 5)*(s > 5)*(s!=9))+hundred[0]*((s==9))+thousand[0]*((s == 9))
d = (x // 10 % 10) 
dd = ten[0]*((d % 5)*(d < 4))+ten[0]*((d == 4))+ten[1]*((d // 5)*(d!=9))+ten[0]*((d % 5)*(d > 5)*(d!=9))+ten[0]*((d==9))+hundred[0]*((d == 9))
e = (x % 10)
ee = one[0]*((e % 5)*(e < 4))+one[0]*((e == 4))+one[1]*((e // 5)*(e!=9))+one[0]*((e % 5)*(e > 5)*(d!=9))+one[0]*((e==9))+ten[0]*((e== 9)) 

print (tt+ss+dd+ee)

