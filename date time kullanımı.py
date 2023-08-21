#trafiğe çıkış tarihi alınan bir aracın servis zamanını ağağıdaki bilgilere göre hesaplayınız

#1.Bakım => 1.yıl
#2.Bakım => 2.yıl
#3.bakım=> 3.yıl
# süre hesabını alınan gün ,ay, yıl bilgisine göre gün bazlı hesaplayınız
#datetime modülü kullan


import datetime

tarih = input("Araç hangi tarihe trafikte (2023/8/1:")
tarih = tarih.split('/')# / ile ayırmak için yazıyoruz

trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

simdi = datetime.datetime.now()   #bugünün bilgisini alıyoruz
fark = simdi - trafigeCikis # şimdiki tarih ile çıkış arasındaki farkı alıcaz

days = fark.days


if days<=365:
    print("1.Servis aralığı")
elif days > 365 and days<=365*2: #days 365 den büyük ise ya da 365*2 den  yani 1 yıl ile 2 yıl arasında ise 2.  serbis bakımı
    print("2.Servis aralığı")
elif days>365*2 and days<=365*3:
    print("3.Servis aralığı")
else:
    print("hatalı süre")
