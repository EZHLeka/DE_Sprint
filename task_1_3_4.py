# s = input("Введите: ")
#s=""
#s = "{}({[]}())"
s = ")()("
#s = "(){[())]}"
#s = "(){}[])"
print("Ввод: ", s)

dic = {
    ')': '(',
    ']': '[',
    '}': '{'
}
close_sim =[')', ']', '}']
st = []
i = 0
e = (len(s) > 0)
for  char in s :
    if (char in close_sim): 
        if len(st)> 0:
            ss = st.pop()       
            if (dic[char] != ss): 
               e = (dic[char] == ss)
               break            
        else:
            e = (len(st)> 0)
            break  
    else: 
        st.append(char)       

print("Вывод:", e)


