try:
    sayı=int(input("birsayı girin: "))
    sonuç=2*sayı
    print(f"sayının 2 katı:{sonuç}")
except ValueError:
    print("bu bir sayı değil")
