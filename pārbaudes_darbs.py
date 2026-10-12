vārds = input("Ievadi skolēna vārdu: ")
n = int(input("Ievadi atzīmju skaitu: "))

atzīmes = []
    
for i in range(n):
    atzīme = int(input("Ievadi atzīmi no 1 līdz 10: "))
    if n < 1 or n > 10:
        print("Kļūda! Atzīmei obligāti jābūt no 1 līdz 10!")
atzīme = int(input("Ievadi vēlreiz savu atzīmi: "))

atzīmes.append(atzīme)

augstākais = max(atzīmes)
mazākais = min(atzīmes)
vidējais_arit = sum(atzīmes) / n


print("Skolēna vārds:", vārds)
print("Vidējā atzīme:", round(vidējais_arit, 2))
print("Augstākā atzīme:", augstākais)
print("Zemākā atzīme:", mazākais)



