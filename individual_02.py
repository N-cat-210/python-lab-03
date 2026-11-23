s = str(input("Введите что-нибудь: "))
c = 0 
f = s[0]
while c < len(s) and s[c] == f:
    c+= 1
print(c)
