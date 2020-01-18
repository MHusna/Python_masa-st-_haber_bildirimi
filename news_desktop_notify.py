import time
import notify2
from desktop_news import masaustu_haber_fonksiyonu

#Haberin başında gözükmesini stediğimiz icon'un tam adresini atadık.
ICON_PATH = ("jamaican-jerk-chicken.svg")

#Önceki fonksiyonumuzda return ettiğimiz haberleri değişkene atıyoruz.
haber_ogeleri = masaustu_haber_fonksiyonu()

#Masaüstü bus'ına bağlandık.
notify2.init("Haber Bildirimi")

#yeni nesne oluşturduk ve iconu atadık.
n = notify2.Notification(None, icon = ICON_PATH)

#Aciliyet seviyesi ayarlama yaptık.
n.set_urgency(notify2.URGENCY_NORMAL)

#Bildirim için zaman aşımını ayarladık.
n.set_timeout(10000)


#Aldığımız haberlerin içinde gezerek, haberleri düzenliyoruz.
for i in range(len(haber_ogeleri)):
	
	
	j = haber_ogeleri[i].text
	j = j.replace("\n","")
	n.update(j.strip()) 
	
	#Burada ise haberi ekranda gösteriyoruz.
	n.show()
	
	#Kaç saniyede bir haber geçiceğini belirtiyoruz.
	time.sleep(5)




