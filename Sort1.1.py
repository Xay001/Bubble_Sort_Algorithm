
sayilar = []
i = 0
j = 0
s = 0


uzunluk = int(input("How long your number array :"))
uz = uzunluk

while(i < uzunluk):
    sayilar.append(int(input("Enter numbers : ")))

    i = i + 1




while(j < uzunluk):
    s = 0

    while(s < uz-1):

        if(sayilar[s] > sayilar[s+1]):

            alternatif_sayi = sayilar[s]
            sayilar[s] = sayilar[s+1]
            sayilar[s+1] = alternatif_sayi

        s = s + 1

    j = j + 1

print(sayilar)