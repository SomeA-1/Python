#Arko Avarsalu
#11.10.22
#Harjutus03

"""
See palindroomi osa ei ole minu kood, aga ausalt see on liiga raske ja vähemalt see töötab


def isPalindrome(s):
    return s == s[::-1]

s = input("Sisestage palindroom:")
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")

#-------------------------------------------------#
#see osa on minu kood, mis on iseloomustatud selle poolt, et see ei tööta

algus = float(input("Sisestage tundide alguse aeg:"))
lõpp = float(input("Sisestage tundide lõpu aeg:"))
tund = "Tunnid algavad", algus ,"ja lõppevad ",lõpp

#print(type(tund))
koolipäev = lõpp-algus
#print(koolipäev)
H = koolipäev%1
print(H)
H2= H/60
print(H2)
"""
#Siit allapoole töötavad asjad
#Email
email=input("Sisestage oma email:")
print('@' in email)
#Nimi
nimi= input("Sisestage oma nimi:")
print("Tere,", nimi.capitalize().replace('Kurat', '*****').strip()+"!")



