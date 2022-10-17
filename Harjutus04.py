#Arko Avarsalu
#11.10.22
#Harjutus04


#FutBol
sugu = input("Sisestage oma sugu (m/n):")
if sugu == "mees":
    print("Palju õnne, sa oled mees")
    vanus = int(input("Sisestage oma vanus:"))
    lubatud  = 16,17,18
    if vanus in lubatud:
        print("YAY")
    
    else:
        print("EI MINE ÄRA")
    
else:
    print("Tunnen kaasa, olete naine")
    
    


#MÜÜK

hind = int(input("Sisestage toote hind:"))me
if hind >= 11:
   # print("Saate 20% allahindluse")
    discount = 0.2
else:
   # print("Saate 10% allahindluse")
   discount = 0.1

print(f"Toote lõpphind on {hind-hind*discount}€")


#JUUBEL
sp = "5.6.2017"
d,m,y = sp.split(".")
vanus=2022-int(y)
#print(vanus)

if vanus%5 == 0:
    print("JAH")
else:
    print("Ei")


#RUUT
a = input("Sisestage ruudu üks külg:")
b = input("Sisestage ruudu teine külg:")

if a == b:
    print(f"{a} ja {b} teevad kokku ruudu")
else:
    print(f"{a} ja {b} ei tee kokku ruudu")
    
#MATA
arv1 = input("Sisesta arv:")
arv2 = input("Sisesta arv:")
mark =  input("Sisesta tehtemärk ( + - * / )")
if mark =="+":
    vastus=arv1+arv2
elif mark=="-":
    vastus=arv1-arv2
elif mark=="*":
    vastus=arv1*arv2
elif mark=="/":
    vastus=arv1/arv2
else: vastus = "N/A"

print(f"{arv1}{mark}{arv2} = {vastus}")

"""