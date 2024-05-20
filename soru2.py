class Insan:
    def __init__(self, ad, soyad, yas, ulke, sehir):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        self.yetenekler = []

    def kisi_bilgileri(self):
        return print("Ad:", self.ad, "\nSoyad:", self.soyad, "\nYas:", self.yas, "\nUlke:", self.ulke, "\nSehir:", self.sehir, "\nYetenekler:", self.yetenekler)

    def yetenek_ekle(self, yetenek):
        self.yetenekler.append(yetenek)


insan = Insan("Selcen", "MERSINLI", 23, "Turkıye", "Mersin")
insan.yetenek_ekle("Java")
insan.yetenek_ekle("Selenium")
insan.kisi_bilgileri()
