import tasinmazAdiOlustuma

ilceAdi = input("İlçe adını giriniz: ")
mahalleAdi = input("Mahalle adını giriniz: ")
adaNo = input("Ada numarasını giriniz: ")
parselNo = input("Parsek numarasını giriniz: ")

tasinmaz = tasinmazAdiOlustuma.tasinmazAdi(ilceAdi, mahalleAdi, adaNo, parselNo)
olusanTasinmazAdi = tasinmaz.olusanTasinmazAdi

print(olusanTasinmazAdi)