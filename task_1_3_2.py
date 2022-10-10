import string


palindrom = input("Введите: ")
# palindrom = "black cat"
palindrom1 = palindrom.replace(' ','')[::-1]
palindrom2 = palindrom.replace(' ','')
print("Вывод:", palindrom1 == palindrom2)
if palindrom1 == palindrom2:
    print(f"Пояснение: {palindrom} читается, как {palindrom[::-1]} слева направо так и справа налево.")
else:
    print(f"Пояснение: слева направо она читается как {palindrom} . Справа налево оно становится  {palindrom[::-1]}.")    
    print("Следовательно, это не палиндром.")

    