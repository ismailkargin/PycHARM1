class tasinmazAdi():
    def __init__(self, ilceAdi, mahalleAdi, adaNo, parselNo):
        self.ilceAdi = ilceAdi
        self.mahalleAdi = mahalleAdi
        self.adaNo = adaNo
        self.parselNo = parselNo

        if adaNo != 0:
            self.tasinmazAdi = (ilceAdi + " İlçesi, " + mahalleAdi + " Mahallesi, " + str(adaNo) + " Ada " + str(parselNo) + " Parsel")
        else:
            self.tasinmazAdi = (ilceAdi + " İlçesi, " + mahalleAdi + " Mahallesi, " + str(parselNo) + " Parsel")

        print(self.tasinmazAdi)