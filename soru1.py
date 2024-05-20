class Ogrenci:
    def __init__(self, ogrenci_adi, ogrenci_soyadi, ogrenci_sinifi):
        self.ogrenci_adi = ogrenci_adi
        self.ogrenci_soyadi = ogrenci_soyadi
        self.ogrenci_sinifi = ogrenci_sinifi


class Soru:
    @staticmethod
    def net_sayisi(dogru_sayisi, yanlis_sayisi):
        return dogru_sayisi - (yanlis_sayisi / 4)

    @staticmethod
    def hesapla(net_sayisi):
        return net_sayisi * 2


ogrenci_adi = input("Ogrencinin adini giriniz: ")
ogrenci_soyadi = input("Ogrencinin soyadini giriniz: ")
ogrencinin_sinifi = input("Ogrencinin sinif bilgisini giriniz:")
ogrenci1 = Ogrenci(ogrenci_adi, ogrenci_soyadi, ogrencinin_sinifi)


ogrencinin_dogru_sayisi = 50
ogrencinin_yanlis_sayisi = 50
while ogrencinin_dogru_sayisi + ogrencinin_yanlis_sayisi > 50:
    print("Sinav 50 sorudur. Dogru ve yanlis sayisinin toplami 50'yi geçmemelidir!")
    ogrencinin_dogru_sayisi = int(input("Dogru sayisini giriniz: "))
    ogrencinin_yanlis_sayisi = int(input("Yanlis sayisini giriniz: "))

net_sayisi = Soru.net_sayisi(ogrencinin_dogru_sayisi, ogrencinin_yanlis_sayisi)
puan = Soru.hesapla(net_sayisi)

print(ogrenci1.ogrenci_sinifi, ogrenci1.ogrenci_adi, ogrenci1.ogrenci_soyadi, "bilgilerine sahip ogrencinin puanı", str(puan))
