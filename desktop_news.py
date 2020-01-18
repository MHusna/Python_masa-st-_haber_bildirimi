import requests
from bs4 import BeautifulSoup
import subprocess

def masaustu_haber_fonksiyonu():
	#Haber sitesine istek attık.
	r = requests.get('https://www.haber.com/gundem')
	
	#Aldığımız haberleri parçaladık.
	source= BeautifulSoup(r.content, "html5lib")
	
	#Parçaladığımız haberlerin istediğimiz kısımlarına ulaştık.
	haberler = source.find("div",{"class":"row show_more_views"}).find_all("h6",{"class":"m-0"})
	
	#Ve haberi masaüstü ortamında yazdırmak için return ettik.
	return haberler
	


