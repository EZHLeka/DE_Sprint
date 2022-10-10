# s = input("Введите: ")
s= "{}({[]}())"
print("Ввод: ", s)

dic = {
    ')': '(',
    ']': '[',
    '}': '{'
}
close_sim =[')', ']', '}']
st = []
i = 0
for  char in s :
    if (char in close_sim): 
        ss = st.pop()       
        if (dic[char] != ss): 
            print ("Вывод:", dic[char] == ss)
            break            
    else: 
        st.append(char)       

if  len(st) == 0:   
    print("Вывод:", len(st)== 0)


