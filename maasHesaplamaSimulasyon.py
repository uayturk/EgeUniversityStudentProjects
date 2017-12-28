Esi_Calismakta_Olan_Calisan_Sayisi=0
cocugu_olan_calisan_sayisi=0
alti_yasindan_buyuk_cocugu_olan_calisan_sayisi=0
Esi_Calismayan_Calisan_Sayisi=0
Esi_Calisma_Durumu_Odenegi=0
Aylik_toplam_brut_ucret=0
Gelir_Vergisi_Kesintisi=0
Aylik_net_ucret=0
ucretin_tam_kisim_islemleri=0
kalan_kurus_kismi=0
En_Yuksek_Aylik_Toplam_Brut_Ucret=0
bakmakla_yukumlu_olunan_cocuk_say=0
engelli_calisan_say=0
engelli_calisan_yuzde=0
cocuk_sayisi_ucten_fazla_olan_calisan_say=0

Evli_Calisan_Sayisi=0
Bekar_Calisan_Sayisi=0
Bekar_Calisan_Sayisi_Yuzde=0
Evli_Calisan_Sayisi_Yuzde=0

yeni_gelen_aylik_toplam_brut_ucret=0
yeni_gelen_aylik_net_ucret=0

ikiyuzluk_banknot_sayisi=0
yuzluk_banknot_sayisi=0
ellilik_banknot_sayisi=0
yirmilik_banknot_sayisi=0
onluk_banknot_sayisi=0
beslik_banknot_sayisi=0

bir_lira_madeni_para_sayisi=0
elli_kurus_madeni_para_sayisi=0
yirmibes_kurus_madeni_para_sayisi=0
on_kurus_madeni_para_sayisi=0
bes_kurus_madeni_para_sayisi=0
bir_kurus_madeni_para_sayisi=0

yuzde_15_gelir_vergisi_calisan_sayisi=0
yuzde_20_gelir_vergisi_calisan_sayisi=0
yuzde_27_gelir_vergisi_calisan_sayisi=0
yuzde_35_gelir_vergisi_calisan_sayisi=0

yuzde_15_gelir_vergisi_calisan_yuzde=0
yuzde_20_gelir_vergisi_calisan_yuzde=0
yuzde_27_gelir_vergisi_calisan_yuzde=0
yuzde_35_gelir_vergisi_calisan_yuzde=0

ikiyuzluk_banknot_sayisi_bir_ay_toplam=0
yuzluk_banknot_sayisi_bir_ay_toplam=0
ellilik_banknot_sayisi_bir_ay_toplam=0
yirmilik_banknot_sayisi_bir_ay_toplam=0
onluk_banknot_sayisi_bir_ay_toplam=0
beslik_banknot_sayisi_bir_ay_toplam=0

bir_lira_madeni_para_sayisi_bir_ay_toplam=0
elli_kurus_madeni_para_sayisi_bir_ay_toplam=0
yirmibes_kurus_madeni_para_sayisi_bir_ay_toplam=0
on_kurus_madeni_para_sayisi_bir_ay_toplam=0
bes_kurus_madeni_para_sayisi_bir_ay_toplam=0
bir_kurus_madeni_para_sayisi_bir_ay_toplam=0
bin_besyuz_tl_alti_aylik_net_ucret_alan_calisan_sayisi=0
islem_icin_kalan_kurusları_tam_sayiya_cevir=0

Alti_Yasindan_Kucuk_Cocuk_Odenegi=25
Alti_Yasindan_Buyuk_Cocuk_Odenegi=45

alti_yasindan_buyuk_cocuk_icin_odenen_odenek_tutari=0
alti_yasindan_kucuk_cocuk_icin_odenen_odenek_tutari=0
toplam_cocuklar_icin_odenen_odenek_tutar=0

Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret=0

bir_ayda_odenen_aylik_toplam_net_ucret_tutari=0
devlete_aktarilan_aylik_toplam_gelir_vergisi_tutari=0

Tum_calisanlar_aylik_toplam_burut_ucret=0
Tum_calisanlar_aylik_toplam_burut_ucret_ortalama=0

Tum_calisanlar_aylik_toplam_net_ucret=0
Tum_calisanlar_aylik_toplam_net_ucret_ortalama=0

toplam_calisan_sayisi=0

while(True):

    toplam_calisan_sayisi=toplam_calisan_sayisi+1
    print("========================================== ",toplam_calisan_sayisi,". ÇALIŞAN  ============================================================================")
    calisanTC= input("Çalışanın TC kimlik numarasını giriniz:")
    CalisanADSoyad= input("Çalışanın Ad-Soyadını giriniz:")

    #Aylık bürüt ücret ile ilgili bilgi alımları
    aylik_brut_ucret=input("Çalışanın aylık bürüt ücretini giriniz: ")
    while(float(aylik_brut_ucret)<float(1777.50)):
       print("Çalışanın aylık bürüt ücretini yanlış giriniz!")
       aylik_brut_ucret=input("Çalışanın aylık bürüt ücretini giriniz: ")

    #Medeni durum ile ilgili bilgi alımları
    medenidurum=input("Çalışanın medeni durumunu giriniz(E/e/B/b):")
    while(str(medenidurum)!="E" and str(medenidurum)!="e" and str(medenidurum)!="B" and str(medenidurum)!="b"):
       print("Çalışanın medeni durumunu yanlış harfle belirttiniz!")
       medenidurum=input("Çalışanın medeni durumunu giriniz(E/e/B/b):")
    if(str(medenidurum)=="E" or str(medenidurum)=="e"):
        Evli_Calisan_Sayisi=Evli_Calisan_Sayisi+1
        es_calisma_durum=input("Eşinizin çalışma durumu(E/e/H/h):")
        while(str(es_calisma_durum)!="E" and str(es_calisma_durum)!="e" and str(es_calisma_durum)!="H" and str(es_calisma_durum)!="h"):#while'da eğer or kullanırsak mesela "e" denince,str(esdurum)!="E" false dönüyor bu da e'yi sanki yanlış girilmiş bir değermişcesine algılatıyor. and ile bunun önüne geçildi.
            print("Eş çalışma durumunu yanlış harfle belirttiniz!")
            es_calisma_durum=input("Eşinizin çalışma durumu(E/e/H/h):")
        if(str(es_calisma_durum)=="E" or str(es_calisma_durum)=="e"):
            Esi_Calismakta_Olan_Calisan_Sayisi=Esi_Calismakta_Olan_Calisan_Sayisi+1;
            Esi_Calisma_Durumu_Odenegi=0
        elif(str(es_calisma_durum)=="H" or str(es_calisma_durum)=="h"):
            Esi_Calismayan_Calisan_Sayisi=Esi_Calismayan_Calisan_Sayisi+1;
            Esi_Calisma_Durumu_Odenegi=220

    elif(str(medenidurum)=="B" or str(medenidurum)=="b"):
        Esi_Calisma_Durumu_Odenegi=0
        Bekar_Calisan_Sayisi=Bekar_Calisan_Sayisi+1

    #Çocuk durumu ile ilgili bilgi alımları ve ödenek hesaplamaları
    cocuk_sayisi=input("Çalışanın bakmakla yükümlü olduğu çocuk sayısını giriniz:")
    while(int(cocuk_sayisi)<0):
       print("Çalışanın bakmakla yükümlü olduğu çocuk sayısını yanlış girdiniz!")
       cocuk_sayisi=input("Çalışanın bakmakla yükümlü olduğu çocuk sayısını giriniz:")
    if(int(cocuk_sayisi)>0):
        cocugu_olan_calisan_sayisi=cocugu_olan_calisan_sayisi+1;
        bakmakla_yukumlu_olunan_cocuk_say=int(bakmakla_yukumlu_olunan_cocuk_say)+int(cocuk_sayisi)
        if(int(cocuk_sayisi)>3):
            cocuk_sayisi_ucten_fazla_olan_calisan_say=int(cocuk_sayisi_ucten_fazla_olan_calisan_say+1)
        alti_yasindan_buyuk_cocuk_sayisi=input("Altı yaşından büyük çocuk sayısını giriniz:")
        while(int(alti_yasindan_buyuk_cocuk_sayisi)<0):
            print("Altı yaşından büyük çocuk sayısını yanlış girdiniz!")
            alti_yasindan_buyuk_cocuk_sayisi=input("Altı yaşından büyük çocuk sayısını giriniz:")
        if(alti_yasindan_buyuk_cocuk_sayisi!=0):
            alti_yasindan_buyuk_cocugu_olan_calisan_sayisi=alti_yasindan_buyuk_cocugu_olan_calisan_sayisi+1
            alti_yasindan_buyuk_cocuk_icin_odenen_odenek_tutari=(int(alti_yasindan_buyuk_cocuk_sayisi)*45)

        alti_yasindan_kucuk_cocuk_sayisi=(int(cocuk_sayisi)-int(alti_yasindan_buyuk_cocuk_sayisi)) #mesela 3 cocuk var 2 tanesi 6 yas üstü,geri kalan 1 cocuk için de farklı hesaplama yapılmalı. o nedenle bu şekilde kalan cocuk varsa ou bulduk.
        alti_yasindan_kucuk_cocuk_icin_odenen_odenek_tutari=int(alti_yasindan_kucuk_cocuk_sayisi*25)
        #toplam ödenek hesaplandı çocukların durumuna göre
        toplam_cocuklar_icin_odenen_odenek_tutar=int(alti_yasindan_buyuk_cocuk_icin_odenen_odenek_tutari)+int(alti_yasindan_kucuk_cocuk_icin_odenen_odenek_tutari)
    elif(int(cocuk_sayisi)==0):
        toplam_cocuklar_icin_odenen_odenek_tutar=0

    Aylik_toplam_brut_ucret=(float(aylik_brut_ucret)+int(Esi_Calisma_Durumu_Odenegi)+int(toplam_cocuklar_icin_odenen_odenek_tutar))
    Tum_calisanlar_aylik_toplam_burut_ucret=Tum_calisanlar_aylik_toplam_burut_ucret+float(Aylik_toplam_brut_ucret)

    #Engellilik durumuyla ilgili bilgi alımları
    engellilik_durumu=input("Çalışanın engellilik durumunu giriniz(E/e/H/h):")
    while(str(engellilik_durumu)!="E" and str(engellilik_durumu)!="e" and str(engellilik_durumu)!="H" and str(engellilik_durumu)!="h"):
       print("Çalışanın engellilik durumunu ile ilgili yanlış harf girdiniz!")
       engellilik_durumu=input("Çalışanın engellilik durumunu giriniz(E/e/H/h):")
    if(str(engellilik_durumu)=="E" or str(engellilik_durumu)=="e"):
       engellilik_orani=input("Engellilik oranınızı giriniz:")
       while(int(engellilik_orani)<1 or int(engellilik_orani)>100):
           print("Engellilik oranınızı yanlış girdiniz!")
           engellilik_orani=input("Engellilik oranınızı giriniz:")
       #Engelli çalışanlar için gelir vergisi kesinti hesaplamaları
       if(int(engellilik_orani)>=80):
           engelli_calisan_say=engelli_calisan_say+1
           engel_derecesi=str("1.Derece Engelli Çalışan.")
           Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret=float(Aylik_toplam_brut_ucret-900)
           if(float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)<2000):
               Gelir_Vergisi_Kesintisi=(float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)*float(0.15))
               yuzde_15_gelir_vergisi_calisan_sayisi=int(yuzde_15_gelir_vergisi_calisan_sayisi+1)
           elif(float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)>=2000 and float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)<5000):
               Gelir_Vergisi_Kesintisi=(float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)*float(0.20))
               yuzde_20_gelir_vergisi_calisan_sayisi=int(yuzde_20_gelir_vergisi_calisan_sayisi+1)
           elif(float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)>=5000 and float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)<10000):
               Gelir_Vergisi_Kesintisi=(float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)*float(0.27))
               yuzde_27_gelir_vergisi_calisan_sayisi=int(yuzde_27_gelir_vergisi_calisan_sayisi+1)
           elif(float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)>=10000):
               Gelir_Vergisi_Kesintisi=(float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)*float(0.35))
               yuzde_35_gelir_vergisi_calisan_sayisi=int(yuzde_35_gelir_vergisi_calisan_sayisi+1)
       elif(int(engellilik_orani)>=60 and int(engellilik_orani)<80):
           engelli_calisan_say=engelli_calisan_say+1
           engel_derecesi=str("2.Derece Engelli Çalışan.")
           Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret=float(Aylik_toplam_brut_ucret-470)
           if(float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)<2000):
               Gelir_Vergisi_Kesintisi=(float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)*float(0.15))
               yuzde_15_gelir_vergisi_calisan_sayisi=int(yuzde_15_gelir_vergisi_calisan_sayisi+1)
           elif(float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)>=2000 and float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)<5000):
               Gelir_Vergisi_Kesintisi=(float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)*float(0.20))
               yuzde_20_gelir_vergisi_calisan_sayisi=int(yuzde_20_gelir_vergisi_calisan_sayisi+1)
           elif(float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)>=5000 and float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)<10000):
               Gelir_Vergisi_Kesintisi=(float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)*float(0.27))
               yuzde_27_gelir_vergisi_calisan_sayisi=int(yuzde_27_gelir_vergisi_calisan_sayisi+1)
           elif(float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)>=10000):
               Gelir_Vergisi_Kesintisi=(float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)*float(0.35))
               yuzde_35_gelir_vergisi_calisan_sayisi=int(yuzde_35_gelir_vergisi_calisan_sayisi+1)
       elif(int(engellilik_orani)>=40 and int(engellilik_orani)<60):
           engelli_calisan_say=engelli_calisan_say+1
           engel_derecesi=str("3.Derece Engelli Çalışan.")
           Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret=float(Aylik_toplam_brut_ucret-210)
           if(float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)<2000):
               Gelir_Vergisi_Kesintisi=(float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)*float(0.15))
               yuzde_15_gelir_vergisi_calisan_sayisi=int(yuzde_15_gelir_vergisi_calisan_sayisi+1)
           elif(float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)>=2000 and float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)<5000):
               Gelir_Vergisi_Kesintisi=(float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)*float(0.20))
               yuzde_20_gelir_vergisi_calisan_sayisi=int(yuzde_20_gelir_vergisi_calisan_sayisi+1)
           elif(float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)>=5000 and float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)<10000):
               Gelir_Vergisi_Kesintisi=(float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)*float(0.27))
               yuzde_27_gelir_vergisi_calisan_sayisi=int(yuzde_27_gelir_vergisi_calisan_sayisi+1)
           elif(float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)>=10000):
               Gelir_Vergisi_Kesintisi=(float(Muaf_Tutar_Cikarildiktan_Sonraki_Aylik_Top_Brut_Ucret)*float(0.35))
               yuzde_35_gelir_vergisi_calisan_sayisi=int(yuzde_35_gelir_vergisi_calisan_sayisi+1)
       elif(int(engellilik_orani)<40):
         engel_derecesi=str("İndirime tabi engel derecesi saptanamadı.")
         #engel için E girip engel derecesi olarak 40 altı insanlar için gelir normal vergisi kesinti hesaplamaları
         if(float(Aylik_toplam_brut_ucret)<2000):
            Gelir_Vergisi_Kesintisi=(float(Aylik_toplam_brut_ucret)*float(0.15))
            yuzde_15_gelir_vergisi_calisan_sayisi=int(yuzde_15_gelir_vergisi_calisan_sayisi+1)
         elif(float(Aylik_toplam_brut_ucret)>=2000 and float(Aylik_toplam_brut_ucret)<5000):
            Gelir_Vergisi_Kesintisi=(float(Aylik_toplam_brut_ucret)*float(0.20))
            yuzde_20_gelir_vergisi_calisan_sayisi=int(yuzde_20_gelir_vergisi_calisan_sayisi+1)
         elif(float(Aylik_toplam_brut_ucret)>=5000 and float(Aylik_toplam_brut_ucret)<10000):
            Gelir_Vergisi_Kesintisi=(float(Aylik_toplam_brut_ucret)*float(0.27))
            yuzde_27_gelir_vergisi_calisan_sayisi=int(yuzde_27_gelir_vergisi_calisan_sayisi+1)
         elif(float(Aylik_toplam_brut_ucret)>=10000):
            Gelir_Vergisi_Kesintisi=(float(Aylik_toplam_brut_ucret)*float(0.35))
            yuzde_35_gelir_vergisi_calisan_sayisi=int(yuzde_35_gelir_vergisi_calisan_sayisi+1)


       Aylik_net_ucret=(float(Aylik_toplam_brut_ucret)-float(Gelir_Vergisi_Kesintisi))
       if(float(Aylik_net_ucret)<1500):
           bin_besyuz_tl_alti_aylik_net_ucret_alan_calisan_sayisi=bin_besyuz_tl_alti_aylik_net_ucret_alan_calisan_sayisi+1

    elif(str(engellilik_durumu)=="H" or str(engellilik_durumu)=="h"):
        #Normal çalışanlar için gelir vergisi kesinti hesaplamaları
        if(int(Aylik_toplam_brut_ucret)<2000):
            Gelir_Vergisi_Kesintisi=(float(Aylik_toplam_brut_ucret)*float(0.15))
            yuzde_15_gelir_vergisi_calisan_sayisi=int(yuzde_15_gelir_vergisi_calisan_sayisi+1)
        elif(int(Aylik_toplam_brut_ucret)>=2000 and int(Aylik_toplam_brut_ucret)<5000):
            Gelir_Vergisi_Kesintisi=(float(Aylik_toplam_brut_ucret)*float(0.20))
            yuzde_20_gelir_vergisi_calisan_sayisi=int(yuzde_20_gelir_vergisi_calisan_sayisi+1)
        elif(int(Aylik_toplam_brut_ucret)>=5000 and int(Aylik_toplam_brut_ucret)<10000):
            Gelir_Vergisi_Kesintisi=(float(Aylik_toplam_brut_ucret)*float(0.27))
            yuzde_27_gelir_vergisi_calisan_sayisi=int(yuzde_27_gelir_vergisi_calisan_sayisi+1)
        elif(int(Aylik_toplam_brut_ucret)>=10000):
            Gelir_Vergisi_Kesintisi=(float(Aylik_toplam_brut_ucret)*float(0.35))
            yuzde_35_gelir_vergisi_calisan_sayisi=int(yuzde_35_gelir_vergisi_calisan_sayisi+1)

        Aylik_net_ucret=(float(Aylik_toplam_brut_ucret)-float(Gelir_Vergisi_Kesintisi))
        if(float(Aylik_net_ucret)<1500):
           bin_besyuz_tl_alti_aylik_net_ucret_alan_calisan_sayisi=bin_besyuz_tl_alti_aylik_net_ucret_alan_calisan_sayisi+1

    #En yüksek toplam bürüt ücret alan çalışanı buluyoruz burada.
    if(float(yeni_gelen_aylik_toplam_brut_ucret)<float(Aylik_toplam_brut_ucret)):
        En_Yuksek_Aylik_Toplam_Brut_Ucret=float(Aylik_toplam_brut_ucret)
        En_Yuksek_Aylik_Toplam_Brut_Ucret_TC=calisanTC
        En_Yuksek_Aylik_Toplam_Brut_Ucret_Ad_Soyad=CalisanADSoyad
        En_Yuksek_Aylik_Toplam_Brut_Ucret_Gelir_Vergi_Kesintisi=float(Gelir_Vergisi_Kesintisi)
        En_Yuksek_Aylik_Toplam_Brut_Ucret_Aylik_Net_Ucreti=float(Aylik_net_ucret)
        yeni_gelen_aylik_toplam_brut_ucret=float(Aylik_toplam_brut_ucret)

    #En yüksek net ücret alan çalışanı buluyoruz burada.
    if(float(yeni_gelen_aylik_net_ucret)<float(Aylik_net_ucret)):
        En_Yuksek_Aylik_Net_Ucret_Toplam_Brut_Ucret=float(Aylik_toplam_brut_ucret)
        En_Yuksek_Aylik_Net_Ucret_TC=calisanTC
        En_Yuksek_Aylik_Net_Ucret_Ad_Soyad=CalisanADSoyad
        En_Yuksek_Aylik_Net_Ucret_Gelir_Vergi_Kesintisi=float(Gelir_Vergisi_Kesintisi)
        En_Yuksek_Aylik_Net_Ucret_Aylik_Net_Ucreti=float(Aylik_net_ucret)
        yeni_gelen_aylik_net_ucret=float(Aylik_net_ucret)




    Tum_calisanlar_aylik_toplam_net_ucret=Tum_calisanlar_aylik_toplam_net_ucret+float(Aylik_net_ucret)

    bir_ayda_odenen_aylik_toplam_net_ucret_tutari=bir_ayda_odenen_aylik_toplam_net_ucret_tutari+float(Aylik_net_ucret);
    devlete_aktarilan_aylik_toplam_gelir_vergisi_tutari=devlete_aktarilan_aylik_toplam_gelir_vergisi_tutari+float(Gelir_Vergisi_Kesintisi);


    #maasın banknotlarla ödenme hesabı
    if(Aylik_net_ucret>200):#Mesela 1798 tl maasımız olsun
        ucretin_tam_kisim_islemleri=1
        ikiyuzluk_banknot_sayisi=int(Aylik_net_ucret/200)#böldük 1789 lirayı 200e,çünkü en az banknotla ödemek istiyoruz. Böldük tam kısmı atadık 200lük banknot sayısına
        ikiyuzluk_banknot_sayisi_bir_ay_toplam=ikiyuzluk_banknot_sayisi_bir_ay_toplam+ikiyuzluk_banknot_sayisi#Bu alan bir aylık toplam ödemeler için o para biriminin toplam adedini tutuyor.
        if( (int(Aylik_net_ucret)%200) != 0):#sonra o paranın 200'e göre modu sıfırsa dedik eğer buraya girelim,
            kalanmiktar1=int(Aylik_net_ucret%200)#200'e göre modunu alıp kalanı bir kalan değerine atayalım. Kalanımız:198 lira
            if( kalanmiktar1 >100):#kalanımız büyükse 100den girdik buraya
                yuzluk_banknot_sayisi=int(kalanmiktar1/100)#yine aynı mantıkla en büyük paraya böldük 198/100 yapıp tam kısmı yüzlük banknot sayısı kısmına atadık
                yuzluk_banknot_sayisi_bir_ay_toplam=yuzluk_banknot_sayisi_bir_ay_toplam+yuzluk_banknot_sayisi
                if((int(kalanmiktar1)%100) != 0):#bu mantıkla devam ettik.
                    kalanmiktar2=int(kalanmiktar1%100)
                    if( kalanmiktar2 > 50):
                        ellilik_banknot_sayisi=int(kalanmiktar2/50)
                        ellilik_banknot_sayisi_bir_ay_toplam=ellilik_banknot_sayisi_bir_ay_toplam+ellilik_banknot_sayisi
                        if((int(kalanmiktar2)%50) != 0):
                            kalanmiktar3=int(kalanmiktar2%50)
                            if(kalanmiktar3>20):
                                yirmilik_banknot_sayisi=int(kalanmiktar3/20)
                                yirmilik_banknot_sayisi_bir_ay_toplam=yirmilik_banknot_sayisi_bir_ay_toplam+yirmilik_banknot_sayisi
                                if((int(kalanmiktar3)%20) != 0):
                                    kalanmiktar4=int(kalanmiktar3%20)
                                    if(kalanmiktar4>10):
                                        onluk_banknot_sayisi=int(kalanmiktar4/10)
                                        onluk_banknot_sayisi_bir_ay_toplam=onluk_banknot_sayisi_bir_ay_toplam+onluk_banknot_sayisi
                                        if((int(kalanmiktar4)%10) != 0):
                                            kalanmiktar5=int(kalanmiktar4%10)
                                            if(kalanmiktar5>5):
                                                beslik_banknot_sayisi=int(kalanmiktar5/5)
                                                beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                                                bir_lira_madeni_para_sayisi=(kalanmiktar5%5)
                                                bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                            elif(kalanmiktar5<5):
                                                bir_lira_madeni_para_sayisi=int(kalanmiktar5)
                                                bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                            elif(kalanmiktar5==5):
                                                beslik_banknot_sayisi=int(kalanmiktar5/5)
                                                beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi

                                    elif(kalanmiktar4<10):#mesela 1798 lira maaşlı kişi için en son 8 tl kalıyor
                                        if(kalanmiktar4<5):
                                            bir_lira_madeni_para_sayisi=int(kalanmiktar4)
                                            bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                        elif(kalanmiktar4>5):
                                            beslik_banknot_sayisi=int(kalanmiktar4/5)
                                            beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                                            bir_lira_madeni_para_sayisi=int(kalanmiktar4%5)
                                            bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                        elif(kalanmiktar4==5):
                                            beslik_banknot_sayisi=int(kalanmiktar4/5)
                                            beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                                    elif(kalanmiktar4==10):
                                        onluk_banknot_sayisi=int(kalanmiktar4/10)
                                        onluk_banknot_sayisi_bir_ay_toplam=onluk_banknot_sayisi_bir_ay_toplam+onluk_banknot_sayisi
                            elif(kalanmiktar3<20):
                                if(kalanmiktar3>10):
                                    onluk_banknot_sayisi=int(kalanmiktar3/10)
                                    onluk_banknot_sayisi_bir_ay_toplam=onluk_banknot_sayisi_bir_ay_toplam+onluk_banknot_sayisi
                                    kalanmiktar4=int(kalanmiktar3%10)
                                    if(kalanmiktar4>5):
                                        beslik_banknot_sayisi=int(kalanmiktar4/5)
                                        beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                                        bir_lira_madeni_para_sayisi=int(kalanmiktar4%5)
                                        bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                    elif(kalanmiktar4<5):
                                        bir_lira_madeni_para_sayisi=int(kalanmiktar4)
                                        bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                    elif(kalanmiktar4==5):
                                        beslik_banknot_sayisi=int(kalanmiktar4/5)
                                        beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                                elif(kalanmiktar3<10):
                                    if(kalanmiktar3>5):
                                        beslik_banknot_sayisi=int(kalanmiktar3/5)
                                        beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                                        bir_lira_madeni_para_sayisi=int(kalanmiktar3%5)
                                        bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                    elif(kalanmiktar3<5):
                                        bir_lira_madeni_para_sayisi=int(kalanmiktar3)
                                        bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                    elif(kalanmiktar3==5):
                                        beslik_banknot_sayisi=int(kalanmiktar3/5)
                                        beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                                elif(kalanmiktar3==10):
                                    onluk_banknot_sayisi=int(kalanmiktar3/10)
                                    onluk_banknot_sayisi_bir_ay_toplam=onluk_banknot_sayisi_bir_ay_toplam+onluk_banknot_sayisi

                            elif(kalanmiktar3==20):
                                yirmilik_banknot_sayisi=int(kalanmiktar3/20)
                                yirmilik_banknot_sayisi_bir_ay_toplam=yirmilik_banknot_sayisi_bir_ay_toplam+yirmilik_banknot_sayisi

                    elif(kalanmiktar2 < 50):
                        if(kalanmiktar2>20):
                            yirmilik_banknot_sayisi=int(kalanmiktar2/20)
                            yirmilik_banknot_sayisi_bir_ay_toplam=yirmilik_banknot_sayisi_bir_ay_toplam+yirmilik_banknot_sayisi
                            if(int(kalanmiktar2%20)!=0):
                               kalanmiktar3=int(kalanmiktar2%20)
                               if(kalanmiktar3>10):
                                   onluk_banknot_sayisi=int(kalanmiktar3/10)
                                   onluk_banknot_sayisi_bir_ay_toplam=onluk_banknot_sayisi_bir_ay_toplam+onluk_banknot_sayisi
                                   if(int(kalanmiktar3%10)!=0):
                                       kalanmiktar4=int(kalanmiktar3%10)
                                       if(kalanmiktar4>5):
                                           beslik_banknot_sayisi=int(kalanmiktar4/5)
                                           beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                                           bir_lira_madeni_para_sayisi=int(kalanmiktar4%5)
                                           bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                       elif(kalanmiktar4<5):
                                           bir_lira_madeni_para_sayisi=int(kalanmiktar4)
                                           bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                       elif(kalanmiktar4==5):
                                           beslik_banknot_sayisi=int(kalanmiktar4/5)
                                           beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                               elif(kalanmiktar3<10):
                                   if(kalanmiktar3>5):
                                       beslik_banknot_sayisi=int(kalanmiktar3/5)
                                       beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                                       bir_lira_madeni_para_sayisi=int(kalanmiktar3%5)
                                       bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                   elif(kalanmiktar3<5):
                                       bir_lira_madeni_para_sayisi=int(kalanmiktar3)
                                       bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                   elif(kalanmiktar3==5):
                                       beslik_banknot_sayisi=int(kalanmiktar3/5)
                                       beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                               elif(kalanmiktar3==10):
                                   onluk_banknot_sayisi=int(kalanmiktar3/10)
                                   onluk_banknot_sayisi_bir_ay_toplam=onluk_banknot_sayisi_bir_ay_toplam+onluk_banknot_sayisi

                        elif(kalanmiktar2<20):
                            if(kalanmiktar2>10):
                                onluk_banknot_sayisi=int(kalanmiktar2/10)
                                onluk_banknot_sayisi_bir_ay_toplam=onluk_banknot_sayisi_bir_ay_toplam+onluk_banknot_sayisi
                                if(int(kalanmiktar2%10)!=0):
                                    kalanmiktar3=int(kalanmiktar2%10)
                                    if(kalanmiktar3>5):
                                        beslik_banknot_sayisi=int(kalanmiktar3/5)
                                        beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                                        if(int(kalanmiktar3%5)!=0):
                                            bir_lira_madeni_para_sayisi=int(kalanmiktar3%5)
                                            bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                    elif(kalanmiktar3<5):
                                        bir_lira_madeni_para_sayisi=int(kalanmiktar3)
                                        bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                    elif(kalanmiktar3==5):
                                        beslik_banknot_sayisi=int(kalanmiktar3)
                                        beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                            elif(kalanmiktar2<10):
                                if(kalanmiktar2>5):
                                    beslik_banknot_sayisi=int(kalanmiktar2/5)
                                    beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                                    bir_lira_madeni_para_sayisi=int(kalanmiktar2%5)
                                    bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                elif(kalanmiktar2<5):
                                    bir_lira_madeni_para_sayisi=int(kalanmiktar2)
                                    bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                elif(kalanmiktar2==5):
                                    beslik_banknot_sayisi=int(kalanmiktar2)
                                    beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi

                            elif(kalanmiktar2==10):
                                onluk_banknot_sayisi=int(kalanmiktar2/10)
                                onluk_banknot_sayisi_bir_ay_toplam=onluk_banknot_sayisi_bir_ay_toplam+onluk_banknot_sayisi

                        elif(kalanmiktar2==20):
                            yirmilik_banknot_sayisi=int(kalanmiktar2/20)
                            yirmilik_banknot_sayisi_bir_ay_toplam=yirmilik_banknot_sayisi_bir_ay_toplam+yirmilik_banknot_sayisi

                    elif(kalanmiktar2 == 50):
                        ellilik_banknot_sayisi=int(kalanmiktar2/50)
                        ellilik_banknot_sayisi_bir_ay_toplam=ellilik_banknot_sayisi_bir_ay_toplam+ellilik_banknot_sayisi
                        #---------------------------------------------------------
            elif( kalanmiktar1 < 100):
                if(kalanmiktar1>50):
                    ellilik_banknot_sayisi=int(kalanmiktar1/50)
                    ellilik_banknot_sayisi_bir_ay_toplam=ellilik_banknot_sayisi_bir_ay_toplam+ellilik_banknot_sayisi
                    kalanmiktar2=int(kalanmiktar1%50)
                    if(kalanmiktar2>20):
                        yirmilik_banknot_sayisi=int(kalanmiktar2/20)
                        yirmilik_banknot_sayisi_bir_ay_toplam=yirmilik_banknot_sayisi_bir_ay_toplam+yirmilik_banknot_sayisi
                        if(int(kalanmiktar2%20)!=0):
                            kalanmiktar3=int(kalanmiktar2%20)
                            if(kalanmiktar3>10):
                                onluk_banknot_sayisi=int(kalanmiktar3/10)
                                onluk_banknot_sayisi_bir_ay_toplam=onluk_banknot_sayisi_bir_ay_toplam+onluk_banknot_sayisi
                                if(int(kalanmiktar3%10)!=0):
                                    kalanmiktar4=int(kalanmiktar3%10)
                                    if(kalanmiktar4>5):
                                        beslik_banknot_sayisi=int(kalanmiktar4/5)
                                        beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                                        bir_lira_madeni_para_sayisi=int(kalanmiktar4%5)
                                        bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                    elif(kalanmiktar4<5):
                                        bir_lira_madeni_para_sayisi=int(kalanmiktar4)
                                        bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                    elif(kalanmiktar4==5):
                                        beslik_banknot_sayisi=int(kalanmiktar4/5)
                                        beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                            elif(kalanmiktar3<10):
                                if(kalanmiktar3>5):
                                    beslik_banknot_sayisi=int(kalanmiktar3/5)
                                    beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                                    bir_lira_madeni_para_sayisi=int(kalanmiktar3%5)
                                    bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                elif(kalanmiktar3<5):
                                    bir_lira_madeni_para_sayisi=int(kalanmiktar3)
                                    bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                elif(kalanmiktar3==5):
                                    beslik_banknot_sayisi=int(kalanmiktar3)
                                    beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                            elif(kalanmiktar3==10):
                                onluk_banknot_sayisi=int(kalanmiktar3/10)
                                onluk_banknot_sayisi_bir_ay_toplam=onluk_banknot_sayisi_bir_ay_toplam+onluk_banknot_sayisi

                    elif(kalanmiktar2<20):
                        if(kalanmiktar2>10):
                            onluk_banknot_sayisi=int(kalanmiktar2/10)
                            onluk_banknot_sayisi_bir_ay_toplam=onluk_banknot_sayisi_bir_ay_toplam+onluk_banknot_sayisi
                            if(int(kalanmiktar2%10)!=0):
                                kalanmiktar3=int(kalanmiktar2%10)
                                if(kalanmiktar3>5):
                                    beslik_banknot_sayisi=int(kalanmiktar3/5)
                                    beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                                    if(int(kalanmiktar3%5)!=0):
                                        bir_lira_madeni_para_sayisi=int(kalanmiktar3%5)
                                        bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                elif(kalanmiktar3<5):
                                    bir_lira_madeni_para_sayisi=int(kalanmiktar3)
                                    bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                elif(kalanmiktar3==5):
                                    beslik_banknot_sayisi=int(kalanmiktar3/5)
                                    beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                        elif(kalanmiktar2<10):
                            if(kalanmiktar2>5):
                                beslik_banknot_sayisi=int(kalanmiktar2/5)
                                beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                                bir_lira_madeni_para_sayisi=int(kalanmiktar2%5)
                                bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                            elif(kalanmiktar2<5):
                                bir_lira_madeni_para_sayisi=int(kalanmiktar2)
                                bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                            elif(kalanmiktar2==5):
                                beslik_banknot_sayisi=int(kalanmiktar2)
                                beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                        elif(kalanmiktar2==10):
                            onluk_banknot_sayisi=int(kalanmiktar2/10)
                            onluk_banknot_sayisi_bir_ay_toplam=onluk_banknot_sayisi_bir_ay_toplam+onluk_banknot_sayisi

                    elif(kalanmiktar2==20) :
                        yirmilik_banknot_sayisi=int(kalanmiktar2/20)
                        yirmilik_banknot_sayisi_bir_ay_toplam=yirmilik_banknot_sayisi_bir_ay_toplam+yirmilik_banknot_sayisi

                elif(kalanmiktar1<50):
                    if(kalanmiktar1>20):
                        yirmilik_banknot_sayisi=int(kalanmiktar1/20)
                        yirmilik_banknot_sayisi_bir_ay_toplam=yirmilik_banknot_sayisi_bir_ay_toplam+yirmilik_banknot_sayisi
                        if(int(kalanmiktar1%20)!=0):
                            kalanmiktar2=int(kalanmiktar1%20)
                            if(kalanmiktar2>10):
                                onluk_banknot_sayisi=int(kalanmiktar2/10)
                                onluk_banknot_sayisi_bir_ay_toplam=onluk_banknot_sayisi_bir_ay_toplam+onluk_banknot_sayisi
                                if(int(kalanmiktar2%10)!=0):
                                    kalanmiktar3=int(kalanmiktar2%10)
                                    if(kalanmiktar3>5):
                                        beslik_banknot_sayisi=int(kalanmiktar3/5)
                                        beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                                        bir_lira_madeni_para_sayisi=int(kalanmiktar3%5)
                                        bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                    elif(kalanmiktar3<5):
                                        bir_lira_madeni_para_sayisi=int(kalanmiktar3)
                                        bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                    elif(kalanmiktar3==5):
                                        beslik_banknot_sayisi=int(kalanmiktar3/5)
                                        beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                            elif(kalanmiktar2<10):
                                if(kalanmiktar2>5):
                                    beslik_banknot_sayisi=int(kalanmiktar2/5)
                                    beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                                    bir_lira_madeni_para_sayisi=int(kalanmiktar2%5)
                                    bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                elif(kalanmiktar2<5):
                                    bir_lira_madeni_para_sayisi=int(kalanmiktar2)
                                    bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                elif(kalanmiktar2==5):
                                    beslik_banknot_sayisi=int(kalanmiktar2)
                                    beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                            elif(kalanmiktar2==10):
                                onluk_banknot_sayisi=int(kalanmiktar2/10)
                                onluk_banknot_sayisi_bir_ay_toplam=onluk_banknot_sayisi_bir_ay_toplam+onluk_banknot_sayisi
                    elif(kalanmiktar1<20):
                        if(kalanmiktar1>10):
                            onluk_banknot_sayisi=int(kalanmiktar1/10)
                            onluk_banknot_sayisi_bir_ay_toplam=onluk_banknot_sayisi_bir_ay_toplam+onluk_banknot_sayisi
                            if(int(kalanmiktar1%10)!=0):
                                kalanmiktar2=int(kalanmiktar1%10)
                                if(kalanmiktar2>5):
                                    beslik_banknot_sayisi=int(kalanmiktar2/5)
                                    beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                                    if(int(kalanmiktar2%5)!=0):
                                        bir_lira_madeni_para_sayisi=int(kalanmiktar2%5)
                                        bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                elif(kalanmiktar2<5):
                                    bir_lira_madeni_para_sayisi=int(kalanmiktar2)
                                    bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                                elif(kalanmiktar2==5):
                                    beslik_banknot_sayisi=int(kalanmiktar2/5)
                                    beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                        elif(kalanmiktar1<10):
                            if(kalanmiktar1>5):
                                beslik_banknot_sayisi=int(kalanmiktar1/5)
                                beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi
                                bir_lira_madeni_para_sayisi=int(kalanmiktar1%5)
                                bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                            elif(kalanmiktar1<5):
                                bir_lira_madeni_para_sayisi=int(kalanmiktar1)
                                bir_lira_madeni_para_sayisi_bir_ay_toplam=bir_lira_madeni_para_sayisi_bir_ay_toplam+bir_lira_madeni_para_sayisi
                            elif(kalanmiktar1==5):
                                beslik_banknot_sayisi=int(kalanmiktar1)
                                beslik_banknot_sayisi_bir_ay_toplam=beslik_banknot_sayisi_bir_ay_toplam+beslik_banknot_sayisi

                        elif(kalanmiktar1==10):
                            onluk_banknot_sayisi=int(kalanmiktar1/10)
                            onluk_banknot_sayisi_bir_ay_toplam=onluk_banknot_sayisi_bir_ay_toplam+onluk_banknot_sayisi

                    elif(kalanmiktar1==20):
                        yirmilik_banknot_sayisi=int(kalanmiktar1/20)
                        yirmilik_banknot_sayisi_bir_ay_toplam=yirmilik_banknot_sayisi_bir_ay_toplam+yirmilik_banknot_sayisi

                elif(kalanmiktar1==50):
                    ellilik_banknot_sayisi=int(kalanmiktar1/50)
                    ellilik_banknot_sayisi_bir_ay_toplam=ellilik_banknot_sayisi_bir_ay_toplam+ellilik_banknot_sayisi
            elif(kalanmiktar1==100):
                yuzluk_banknot_sayisi=int(kalanmiktar1/100)
                yuzluk_banknot_sayisi_bir_ay_toplam=yuzluk_banknot_sayisi_bir_ay_toplam+yuzluk_banknot_sayisi


    #Bu if şunu yapıyor: Eger para küsüratlıysa ve paranın ana kısmının işlemleri bittiyse buraya girip kuruşları böldürecek
    if((Aylik_net_ucret>int(Aylik_net_ucret))and ucretin_tam_kisim_islemleri==1):
        kalan_kurus_kismi=round((Aylik_net_ucret-int(Aylik_net_ucret)),2)#kalan kuruslara round fonksiyonu ile virgülden sonra 2 tanesine kadarını atadık
        islem_icin_kalan_kurusları_tam_sayiya_cevir=int(kalan_kurus_kismi*100)#kalan kurusları tamsayıya cevirelim ki işimiz kolay olsun

        #şimdi aynı işlemleri kuruşlarımız için yapacağız Altta
        if(islem_icin_kalan_kurusları_tam_sayiya_cevir<100 and islem_icin_kalan_kurusları_tam_sayiya_cevir>0):#Tabi kuruşlarımız 100 değilken ve 0 dan büyükken bu işlemler yapılmalı
            #kuruşlar uygun aralıktaysa yukardaki mantıkla en az sekilde madeni para kullanarak nasıl ödenir hesaplatalım
            if(islem_icin_kalan_kurusları_tam_sayiya_cevir>50):
                elli_kurus_madeni_para_sayisi=int(islem_icin_kalan_kurusları_tam_sayiya_cevir/50)
                elli_kurus_madeni_para_sayisi_bir_ay_toplam=elli_kurus_madeni_para_sayisi_bir_ay_toplam+elli_kurus_madeni_para_sayisi
                if( (int(islem_icin_kalan_kurusları_tam_sayiya_cevir)%50) != 0):
                    kalan_miktar_kurus1=int(islem_icin_kalan_kurusları_tam_sayiya_cevir%50)
                    if(kalan_miktar_kurus1>25):
                        yirmibes_kurus_madeni_para_sayisi=int(kalan_miktar_kurus1/25)
                        yirmibes_kurus_madeni_para_sayisi_bir_ay_toplam=yirmibes_kurus_madeni_para_sayisi_bir_ay_toplam+yirmibes_kurus_madeni_para_sayisi
                        kalan_miktar_kurus2=int(kalan_miktar_kurus1%25)
                        if(kalan_miktar_kurus2>10):
                            on_kurus_madeni_para_sayisi=int(kalan_miktar_kurus2/10)
                            on_kurus_madeni_para_sayisi_bir_ay_toplam=on_kurus_madeni_para_sayisi_bir_ay_toplam+on_kurus_madeni_para_sayisi
                            kalan_miktar_kurus3=int(kalan_miktar_kurus2%10)
                            if(kalan_miktar_kurus3<5):
                                bir_kurus_madeni_para_sayisi=int(kalan_miktar_kurus3)
                                bir_kurus_madeni_para_sayisi_bir_ay_toplam=bir_kurus_madeni_para_sayisi_bir_ay_toplam+bir_kurus_madeni_para_sayisi
                            elif(kalan_miktar_kurus3==5):
                                bes_kurus_madeni_para_sayisi=int(kalan_miktar_kurus3/5)
                                bes_kurus_madeni_para_sayisi_bir_ay_toplam=bes_kurus_madeni_para_sayisi_bir_ay_toplam+bes_kurus_madeni_para_sayisi
                            elif(kalan_miktar_kurus3>5):
                                bes_kurus_madeni_para_sayisi=int(kalan_miktar_kurus3/5)
                                bes_kurus_madeni_para_sayisi_bir_ay_toplam=bes_kurus_madeni_para_sayisi_bir_ay_toplam+bes_kurus_madeni_para_sayisi
                                bir_kurus_madeni_para_sayisi=int(kalan_miktar_kurus3%5)
                                bir_kurus_madeni_para_sayisi_bir_ay_toplam=bir_kurus_madeni_para_sayisi_bir_ay_toplam+bir_kurus_madeni_para_sayisi
                        elif(kalan_miktar_kurus2==10):
                            on_kurus_madeni_para_sayisi=int(kalan_miktar_kurus2/10)
                            on_kurus_madeni_para_sayisi_bir_ay_toplam=on_kurus_madeni_para_sayisi_bir_ay_toplam+on_kurus_madeni_para_sayisi
                        elif(kalan_miktar_kurus2<10):
                            if(kalan_miktar_kurus2>5):
                                bes_kurus_madeni_para_sayisi=int(kalan_miktar_kurus2/5)
                                bes_kurus_madeni_para_sayisi_bir_ay_toplam=bes_kurus_madeni_para_sayisi_bir_ay_toplam+bes_kurus_madeni_para_sayisi
                                bir_kurus_madeni_para_sayisi=int(kalan_miktar_kurus2%5)
                                bir_kurus_madeni_para_sayisi_bir_ay_toplam=bir_kurus_madeni_para_sayisi_bir_ay_toplam+bir_kurus_madeni_para_sayisi
                            elif(kalan_miktar_kurus2==5):
                                bes_kurus_madeni_para_sayisi=int(kalan_miktar_kurus2/5)
                                bes_kurus_madeni_para_sayisi_bir_ay_toplam=bes_kurus_madeni_para_sayisi_bir_ay_toplam+bes_kurus_madeni_para_sayisi
                            elif(kalan_miktar_kurus2<5):
                                bir_kurus_madeni_para_sayisi=int(kalan_miktar_kurus2)
                                bir_kurus_madeni_para_sayisi_bir_ay_toplam=bir_kurus_madeni_para_sayisi_bir_ay_toplam+bir_kurus_madeni_para_sayisi

                    elif(kalan_miktar_kurus1<25):
                        if(kalan_miktar_kurus1>10):
                            on_kurus_madeni_para_sayisi=int(kalan_miktar_kurus1/10)
                            on_kurus_madeni_para_sayisi_bir_ay_toplam=on_kurus_madeni_para_sayisi_bir_ay_toplam+on_kurus_madeni_para_sayisi
                            kalan_miktar_kurus2=int(kalan_miktar_kurus1%10)
                            if(kalan_miktar_kurus2>5):
                                bes_kurus_madeni_para_sayisi=int(kalan_miktar_kurus2/5)
                                bes_kurus_madeni_para_sayisi_bir_ay_toplam=bes_kurus_madeni_para_sayisi_bir_ay_toplam+bes_kurus_madeni_para_sayisi
                                bir_kurus_madeni_para_sayisi=int(kalan_miktar_kurus2%5)
                                bir_kurus_madeni_para_sayisi_bir_ay_toplam=bir_kurus_madeni_para_sayisi_bir_ay_toplam+bir_kurus_madeni_para_sayisi
                            elif(kalan_miktar_kurus2==5):
                                bes_kurus_madeni_para_sayisi=int(kalan_miktar_kurus2/5)
                                bes_kurus_madeni_para_sayisi_bir_ay_toplam=bes_kurus_madeni_para_sayisi_bir_ay_toplam+bes_kurus_madeni_para_sayisi
                            elif(kalan_miktar_kurus2<5):
                                bir_kurus_madeni_para_sayisi=kalan_miktar_kurus2
                                bir_kurus_madeni_para_sayisi_bir_ay_toplam=bir_kurus_madeni_para_sayisi_bir_ay_toplam+bir_kurus_madeni_para_sayisi
                        elif(kalan_miktar_kurus1==10):
                            on_kurus_madeni_para_sayisi=int(kalan_miktar_kurus1/10)
                            on_kurus_madeni_para_sayisi_bir_ay_toplam=on_kurus_madeni_para_sayisi_bir_ay_toplam+on_kurus_madeni_para_sayisi
                        elif(kalan_miktar_kurus1<10):
                            if(kalan_miktar_kurus1>5):
                                bes_kurus_madeni_para_sayisi=int(kalan_miktar_kurus1/5)
                                bes_kurus_madeni_para_sayisi_bir_ay_toplam=bes_kurus_madeni_para_sayisi_bir_ay_toplam+bes_kurus_madeni_para_sayisi
                                bir_kurus_madeni_para_sayisi=int(kalan_miktar_kurus1%5)
                                bir_kurus_madeni_para_sayisi_bir_ay_toplam=bir_kurus_madeni_para_sayisi_bir_ay_toplam+bir_kurus_madeni_para_sayisi
                            elif(kalan_miktar_kurus1==5):
                                bes_kurus_madeni_para_sayisi=int(kalan_miktar_kurus1/5)
                                bes_kurus_madeni_para_sayisi_bir_ay_toplam=bes_kurus_madeni_para_sayisi_bir_ay_toplam+bes_kurus_madeni_para_sayisi
                            elif(kalan_miktar_kurus1<5):
                                bir_kurus_madeni_para_sayisi=int(kalan_miktar_kurus1)
                                bir_kurus_madeni_para_sayisi_bir_ay_toplam=bir_kurus_madeni_para_sayisi_bir_ay_toplam+bir_kurus_madeni_para_sayisi
            elif(islem_icin_kalan_kurusları_tam_sayiya_cevir<50):
                if(islem_icin_kalan_kurusları_tam_sayiya_cevir>25):
                    yirmibes_kurus_madeni_para_sayisi=int(islem_icin_kalan_kurusları_tam_sayiya_cevir/25)
                    yirmibes_kurus_madeni_para_sayisi_bir_ay_toplam=yirmibes_kurus_madeni_para_sayisi_bir_ay_toplam+yirmibes_kurus_madeni_para_sayisi
                    if((int(islem_icin_kalan_kurusları_tam_sayiya_cevir)%25) != 0):
                        kalan_miktar_kurus1=(int(islem_icin_kalan_kurusları_tam_sayiya_cevir)%25)
                        if(kalan_miktar_kurus1>10):
                            on_kurus_madeni_para_sayisi=int(kalan_miktar_kurus1/10)
                            on_kurus_madeni_para_sayisi_bir_ay_toplam=on_kurus_madeni_para_sayisi_bir_ay_toplam+on_kurus_madeni_para_sayisi
                            if((int(kalan_miktar_kurus1)%10) != 0):
                                kalan_miktar_kurus2=(int(kalan_miktar_kurus1)%10)
                                if(kalan_miktar_kurus2>5):
                                    bes_kurus_madeni_para_sayisi=int(kalan_miktar_kurus2/5)
                                    bes_kurus_madeni_para_sayisi_bir_ay_toplam=bes_kurus_madeni_para_sayisi_bir_ay_toplam+bes_kurus_madeni_para_sayisi
                                    bir_kurus_madeni_para_sayisi=int(kalan_miktar_kurus2%5)
                                    bir_kurus_madeni_para_sayisi_bir_ay_toplam=bir_kurus_madeni_para_sayisi_bir_ay_toplam+bir_kurus_madeni_para_sayisi
                                elif(kalan_miktar_kurus2<5):
                                    bir_kurus_madeni_para_sayisi=int(kalan_miktar_kurus2)
                                    bir_kurus_madeni_para_sayisi_bir_ay_toplam=bir_kurus_madeni_para_sayisi_bir_ay_toplam+bir_kurus_madeni_para_sayisi
                                elif(kalan_miktar_kurus2==5):
                                    bes_kurus_madeni_para_sayisi=int(kalan_miktar_kurus2/5)
                                    bes_kurus_madeni_para_sayisi_bir_ay_toplam=bes_kurus_madeni_para_sayisi_bir_ay_toplam+bes_kurus_madeni_para_sayisi
                        elif(kalan_miktar_kurus1<10):
                            if(kalan_miktar_kurus1>5):
                                bes_kurus_madeni_para_sayisi=int(kalan_miktar_kurus1/5)
                                bes_kurus_madeni_para_sayisi_bir_ay_toplam=bes_kurus_madeni_para_sayisi_bir_ay_toplam+bes_kurus_madeni_para_sayisi
                                bir_kurus_madeni_para_sayisi=int(kalan_miktar_kurus1%5)
                                bir_kurus_madeni_para_sayisi_bir_ay_toplam=bir_kurus_madeni_para_sayisi_bir_ay_toplam+bir_kurus_madeni_para_sayisi
                            elif(kalan_miktar_kurus1<5):
                                bir_kurus_madeni_para_sayisi=int(kalan_miktar_kurus1)
                                bir_kurus_madeni_para_sayisi_bir_ay_toplam=bir_kurus_madeni_para_sayisi_bir_ay_toplam+bir_kurus_madeni_para_sayisi
                            elif(kalan_miktar_kurus1==5):
                                bes_kurus_madeni_para_sayisi=int(kalan_miktar_kurus1/5)
                                bes_kurus_madeni_para_sayisi_bir_ay_toplam=bes_kurus_madeni_para_sayisi_bir_ay_toplam+bes_kurus_madeni_para_sayisi
                        elif(kalan_miktar_kurus1==10):
                            on_kurus_madeni_para_sayisi=int(kalan_miktar_kurus1/10)
                            on_kurus_madeni_para_sayisi_bir_ay_toplam=on_kurus_madeni_para_sayisi_bir_ay_toplam+on_kurus_madeni_para_sayisi
                elif(islem_icin_kalan_kurusları_tam_sayiya_cevir<25):
                        if(islem_icin_kalan_kurusları_tam_sayiya_cevir>10):
                            on_kurus_madeni_para_sayisi=int(islem_icin_kalan_kurusları_tam_sayiya_cevir/10)
                            on_kurus_madeni_para_sayisi_bir_ay_toplam=on_kurus_madeni_para_sayisi_bir_ay_toplam+on_kurus_madeni_para_sayisi
                            if((int(islem_icin_kalan_kurusları_tam_sayiya_cevir)%10) != 0):
                                kalan_miktar_kurus1=(int(islem_icin_kalan_kurusları_tam_sayiya_cevir)%10)
                                if(kalan_miktar_kurus1>5):
                                    bes_kurus_madeni_para_sayisi=int(kalan_miktar_kurus1/5)
                                    bes_kurus_madeni_para_sayisi_bir_ay_toplam=bes_kurus_madeni_para_sayisi_bir_ay_toplam+bes_kurus_madeni_para_sayisi
                                    bir_kurus_madeni_para_sayisi=int(kalan_miktar_kurus1%5)
                                    bir_kurus_madeni_para_sayisi_bir_ay_toplam=bir_kurus_madeni_para_sayisi_bir_ay_toplam+bir_kurus_madeni_para_sayisi
                                elif(kalan_miktar_kurus1<5):
                                    bir_kurus_madeni_para_sayisi=int(kalan_miktar_kurus1)
                                    bir_kurus_madeni_para_sayisi_bir_ay_toplam=bir_kurus_madeni_para_sayisi_bir_ay_toplam+bir_kurus_madeni_para_sayisi
                                elif(kalan_miktar_kurus1==5):
                                    bes_kurus_madeni_para_sayisi=int(kalan_miktar_kurus1/5)
                                    bes_kurus_madeni_para_sayisi_bir_ay_toplam=bes_kurus_madeni_para_sayisi_bir_ay_toplam+bes_kurus_madeni_para_sayisi
                        elif(islem_icin_kalan_kurusları_tam_sayiya_cevir<10):
                                if(islem_icin_kalan_kurusları_tam_sayiya_cevir>5):
                                    bes_kurus_madeni_para_sayisi=int(islem_icin_kalan_kurusları_tam_sayiya_cevir/5)
                                    bes_kurus_madeni_para_sayisi_bir_ay_toplam=bes_kurus_madeni_para_sayisi_bir_ay_toplam+bes_kurus_madeni_para_sayisi
                                    bir_kurus_madeni_para_sayisi=int(islem_icin_kalan_kurusları_tam_sayiya_cevir%5)
                                    bir_kurus_madeni_para_sayisi_bir_ay_toplam=bir_kurus_madeni_para_sayisi_bir_ay_toplam+bir_kurus_madeni_para_sayisi
                                elif(islem_icin_kalan_kurusları_tam_sayiya_cevir<5):
                                    bir_kurus_madeni_para_sayisi=int(islem_icin_kalan_kurusları_tam_sayiya_cevir)
                                    bir_kurus_madeni_para_sayisi_bir_ay_toplam=bir_kurus_madeni_para_sayisi_bir_ay_toplam+bir_kurus_madeni_para_sayisi
                                elif(islem_icin_kalan_kurusları_tam_sayiya_cevir==5):
                                    bes_kurus_madeni_para_sayisi=int(islem_icin_kalan_kurusları_tam_sayiya_cevir/5)
                                    bes_kurus_madeni_para_sayisi_bir_ay_toplam=bes_kurus_madeni_para_sayisi_bir_ay_toplam+bes_kurus_madeni_para_sayisi
                        elif(islem_icin_kalan_kurusları_tam_sayiya_cevir==10):
                            on_kurus_madeni_para_sayisi=int(islem_icin_kalan_kurusları_tam_sayiya_cevir/10)
                            on_kurus_madeni_para_sayisi_bir_ay_toplam=on_kurus_madeni_para_sayisi_bir_ay_toplam+on_kurus_madeni_para_sayisi
                elif(islem_icin_kalan_kurusları_tam_sayiya_cevir==25):
                    yirmibes_kurus_madeni_para_sayisi=int(islem_icin_kalan_kurusları_tam_sayiya_cevir/25)
                    yirmibes_kurus_madeni_para_sayisi_bir_ay_toplam=yirmibes_kurus_madeni_para_sayisi_bir_ay_toplam+yirmibes_kurus_madeni_para_sayisi
            elif(islem_icin_kalan_kurusları_tam_sayiya_cevir==50):
                elli_kurus_madeni_para_sayisi=int(islem_icin_kalan_kurusları_tam_sayiya_cevir/50)
                elli_kurus_madeni_para_sayisi_bir_ay_toplam=elli_kurus_madeni_para_sayisi_bir_ay_toplam+elli_kurus_madeni_para_sayisi




    print("============================ ",toplam_calisan_sayisi,". ÇALIŞAN İÇİN BİLGİLER  ======================================")
    print("Çalışan TC:",calisanTC)
    print("Çalışan Ad-Soyad:",CalisanADSoyad)
    print("Çalışan Aylık Brüt Ücret:",aylik_brut_ucret,"TL")
    if(str(medenidurum)=="E" or str(medenidurum)=="e"):
        if(str(es_calisma_durum)=="H" or str(es_calisma_durum)=="h"):
            print("Eş için aile yardımı ödeneği:",Esi_Calisma_Durumu_Odenegi,"TL")
        elif(str(es_calisma_durum)=="E" or str(es_calisma_durum)=="e"):
            print("Eş için aile yardımı ödeneği:",Esi_Calisma_Durumu_Odenegi,"TL")
    elif(str(medenidurum)=="B" or str(medenidurum)=="b"):
        print("Eş için aile yardımı ödeneği:",Esi_Calisma_Durumu_Odenegi,"TL")
    print("6 yasından buyuk cocuk ödeneği:",alti_yasindan_buyuk_cocuk_icin_odenen_odenek_tutari,"TL")
    print("6 yasından küçük cocuk ödeneği:",alti_yasindan_kucuk_cocuk_icin_odenen_odenek_tutari,"TL")

    if(cocuk_sayisi!=0):
        print("Çocuk için aile yardımı ödeneği:",int(toplam_cocuklar_icin_odenen_odenek_tutar),"TL")
    elif(cocuk_sayisi==0):
        print("Çocuk için aile yardımı ödeneği:",int(toplam_cocuklar_icin_odenen_odenek_tutar),"TL")
    print("Aylık toplam brüt ücreti:",float("{0:.2f}".format(Aylik_toplam_brut_ucret)),"TL")
    print("Gelir vergisi kesintisi:",float("{0:.2f}".format(Gelir_Vergisi_Kesintisi)),"TL")
    if(str(engellilik_durumu)=="E" or str(engellilik_durumu)=="e"):
        print("Engel derecesi (1./2./3.):",engel_derecesi)
    print("Aylık net ücreti (TL):",float("{0:.2f}".format(Aylik_net_ucret)))


    print("----------En Az Para Kullanacak Şekilde Banknotların Ödemesi----------")
    if(ikiyuzluk_banknot_sayisi!=0):
        print("200'lük Banknot Sayısı:" , ikiyuzluk_banknot_sayisi)
    if(yuzluk_banknot_sayisi!=0):
        print("100'lük Banknot Sayısı:" , yuzluk_banknot_sayisi)
    if(ellilik_banknot_sayisi!=0):
        print("50'lik Banknot Sayısı:" , ellilik_banknot_sayisi)
    if(yirmilik_banknot_sayisi!=0):
        print("20'lik Banknot Sayısı:" , yirmilik_banknot_sayisi)
    if(onluk_banknot_sayisi!=0):
        print("10'luk Banknot Sayısı:" , onluk_banknot_sayisi)
    if(beslik_banknot_sayisi!=0):
        print("5'lik Banknot Sayısı:" , beslik_banknot_sayisi)
    if(bir_lira_madeni_para_sayisi!=0):
        print("1'lik Madeni Para Sayısı:" , bir_lira_madeni_para_sayisi)

    print("----------En Az Para Kullanacak Şekilde Kuruşların Ödemesi----------")
    if(elli_kurus_madeni_para_sayisi!=0):
        print("50 Kuruş'luk Madeni Para Sayısı:" , elli_kurus_madeni_para_sayisi)
    if(yirmibes_kurus_madeni_para_sayisi!=0):
        print("25 Kuruş'luk Madeni Para Sayısı:" , yirmibes_kurus_madeni_para_sayisi)
    if(on_kurus_madeni_para_sayisi!=0):
        print("10 Kuruş'luk Madeni Para Sayısı:" , on_kurus_madeni_para_sayisi)
    if(bes_kurus_madeni_para_sayisi!=0):
        print("5 Kuruş'luk Madeni Para Sayısı:" , bes_kurus_madeni_para_sayisi)
    if(bir_kurus_madeni_para_sayisi!=0):
        print("1 Kuruş'luk Madeni Para Sayısı:" , bir_kurus_madeni_para_sayisi)

    ikiyuzluk_banknot_sayisi=0
    yuzluk_banknot_sayisi=0    #Bunları 0'ladım ki ikinci calısanımızı girerken hata almayalım en az banknot ile ödeme yapılması konusunda.
    ellilik_banknot_sayisi=0   #0'lamazsak önceki tutulan değerlerin üzerine ekleyerek devam eder.
    yirmilik_banknot_sayisi=0
    onluk_banknot_sayisi=0
    beslik_banknot_sayisi=0
    bir_lira_madeni_para_sayisi=0

    elli_kurus_madeni_para_sayisi=0
    yirmibes_kurus_madeni_para_sayisi=0
    on_kurus_madeni_para_sayisi=0
    bes_kurus_madeni_para_sayisi=0
    bir_kurus_madeni_para_sayisi=0

    islem_icin_kalan_kurusları_tam_sayiya_cevir=0
    print("==========================================================================================================================================")
    #başka çalışan var mı sorguluyoruz
    baska_çalışan=input("Başka çalışan var mı?(E/e/H/h)")
    while(str(baska_çalışan)!="E" and str(baska_çalışan)!="e" and str(baska_çalışan)!="H" and str(baska_çalışan)!="h"):
        print("Hatalı harf girişi!!")
        baska_çalışan=input("Başka çalışan var mı?(E/e/H/h)")

    if(str(baska_çalışan)=="H" or str(baska_çalışan)=="h"):
        break



Tum_calisanlar_aylik_toplam_burut_ucret_ortalama=(Tum_calisanlar_aylik_toplam_burut_ucret/int(toplam_calisan_sayisi))
Tum_calisanlar_aylik_toplam_net_ucret_ortalama=(Tum_calisanlar_aylik_toplam_net_ucret/int(toplam_calisan_sayisi))

yuzde_15_gelir_vergisi_calisan_yuzde=((int(yuzde_15_gelir_vergisi_calisan_sayisi)/toplam_calisan_sayisi)*100)
yuzde_20_gelir_vergisi_calisan_yuzde=((int(yuzde_20_gelir_vergisi_calisan_sayisi)/toplam_calisan_sayisi)*100)
yuzde_27_gelir_vergisi_calisan_yuzde=((int(yuzde_27_gelir_vergisi_calisan_sayisi)/toplam_calisan_sayisi)*100)
yuzde_35_gelir_vergisi_calisan_yuzde=((int(yuzde_35_gelir_vergisi_calisan_sayisi)/toplam_calisan_sayisi)*100)

Evli_Calisan_Sayisi_Yuzde=((int(Evli_Calisan_Sayisi)/toplam_calisan_sayisi)*100)
Bekar_Calisan_Sayisi_Yuzde=((int(Bekar_Calisan_Sayisi)/toplam_calisan_sayisi)*100)

Esleri_Calisiyor_Olan_Calisan_Yuzde=((int(Esi_Calismakta_Olan_Calisan_Sayisi)/int(Evli_Calisan_Sayisi))*100)

bakmakla_yukumlu_olunan_cocuk_say_ortalama=float(int(bakmakla_yukumlu_olunan_cocuk_say)/int(cocugu_olan_calisan_sayisi))

engelli_calisan_yuzde=((int(engelli_calisan_say)/toplam_calisan_sayisi)*100)

print("=======================================================İSTATİSTİKSEL BİLGİLER=============================================================")
print("                                                                                              ")
print("Tüm çalışanlara bir ayda ödenen aylık toplam net ücret tutarı:" , float("{0:.2f}".format(bir_ayda_odenen_aylik_toplam_net_ucret_tutari)),"TL")
print("Devlete aktarılan aylık toplam gelir vergisi tutarı:" , float("{0:.2f}".format(devlete_aktarilan_aylik_toplam_gelir_vergisi_tutari)),"TL")
print("                                                                                              ")
print("Tüm çalışanların aylık toplam brüt ücretlerinin ortalaması:" , float("{0:.2f}".format(Tum_calisanlar_aylik_toplam_burut_ucret_ortalama)),"TL")
print("Tüm çalışanların aylık toplam net ücretlerinin ortalaması:" , float("{0:.2f}".format(Tum_calisanlar_aylik_toplam_net_ucret_ortalama)),"TL")
print("                                                                                              ")
print("----------Bir Ayda Tedavüldeki Her Para Türünden Toplam Kaçar Adet Gerektiği----------")
print("----------BANKNOTLAR-------------")
print("   200'lük Toplam Banknot Sayısı:" , ikiyuzluk_banknot_sayisi_bir_ay_toplam)
print("   100'lük Toplam Banknot Sayısı:" , yuzluk_banknot_sayisi_bir_ay_toplam)
print("   50'lik Toplam Banknot Sayısı:" , ellilik_banknot_sayisi_bir_ay_toplam)
print("   20'lik Toplam Banknot Sayısı:" , yirmilik_banknot_sayisi_bir_ay_toplam)
print("   10'luk Toplam Banknot Sayısı:" , onluk_banknot_sayisi_bir_ay_toplam)
print("   5'lik Toplam Banknot Sayısı:" , beslik_banknot_sayisi_bir_ay_toplam)
print("                                                                                              ")
print("----------MADENİ PARALAR----------")
print("   1'lik Toplam Madeni Para Sayısı:" , bir_lira_madeni_para_sayisi_bir_ay_toplam)
print("   50 Kuruş'luk Toplam Madeni Para Sayısı:" , elli_kurus_madeni_para_sayisi_bir_ay_toplam)
print("   25 Kuruş'luk Toplam Madeni Para Sayısı:" , yirmibes_kurus_madeni_para_sayisi_bir_ay_toplam)
print("   10 Kuruş'luk Toplam Madeni Para Sayısı:" , on_kurus_madeni_para_sayisi_bir_ay_toplam)
print("   5 Kuruş'luk Toplam Madeni Para Sayısı:" , bes_kurus_madeni_para_sayisi_bir_ay_toplam)
print("   1 Kuruş'luk Toplam Madeni Para Sayısı:" , bir_kurus_madeni_para_sayisi_bir_ay_toplam)
print("                                                                                              ")
print("1500 TL’nin Altında Aylık Net Ücret Alan Çalışanların Sayısı:" , bin_besyuz_tl_alti_aylik_net_ucret_alan_calisan_sayisi)
print("                                                                                              ")
print("Yüzde 15 Vergi Kesintisine Dahil Edilen Çalışan Sayısı:" , int(yuzde_15_gelir_vergisi_calisan_sayisi))
print("Yüzde 20 Vergi Kesintisine Dahil Edilen Çalışan Sayısı:" , int(yuzde_20_gelir_vergisi_calisan_sayisi))
print("Yüzde 27 Vergi Kesintisine Dahil Edilen Çalışan Sayısı:" , int(yuzde_27_gelir_vergisi_calisan_sayisi))
print("Yüzde 35 Vergi Kesintisine Dahil Edilen Çalışan Sayısı:" , int(yuzde_35_gelir_vergisi_calisan_sayisi))
print("                                                                                              ")
print("Yüzde 15 Vergi Kesintisine Dahil Edilen Çalışan Sayısı Yüzdesi:" , float("{0:.2f}".format(yuzde_15_gelir_vergisi_calisan_yuzde)))
print("Yüzde 20 Vergi Kesintisine Dahil Edilen Çalışan Sayısı Yüzdesi:" , float("{0:.2f}".format(yuzde_20_gelir_vergisi_calisan_yuzde)))
print("Yüzde 27 Vergi Kesintisine Dahil Edilen Çalışan Sayısı Yüzdesi:" , float("{0:.2f}".format(yuzde_27_gelir_vergisi_calisan_yuzde)))
print("Yüzde 35 Vergi Kesintisine Dahil Edilen Çalışan Sayısı Yüzdesi:" , float("{0:.2f}".format(yuzde_35_gelir_vergisi_calisan_yuzde)))
print("                                                                                              ")
print("-----Aylık Toplam Brüt Ücreti En Yüksek Olan Çalışanın:-----")
print("     1----TC:",En_Yuksek_Aylik_Toplam_Brut_Ucret_TC)
print("     2----Ad Soyad:",En_Yuksek_Aylik_Toplam_Brut_Ucret_Ad_Soyad)
print("     3----Aylık Toplam Brüt Ücreti:",En_Yuksek_Aylik_Toplam_Brut_Ucret)
print("     4----Aylık Toplam Net Ücreti:",float("{0:.2f}".format(En_Yuksek_Aylik_Toplam_Brut_Ucret_Aylik_Net_Ucreti)))
print("     5----Gelir Vergi Kesintisi:",float("{0:.2f}".format(En_Yuksek_Aylik_Toplam_Brut_Ucret_Gelir_Vergi_Kesintisi)))
print("                                                                                              ")
print("-----Aylık Net Ücreti En Yüksek Olan Çalışanın:-----")
print("     1----TC:",En_Yuksek_Aylik_Net_Ucret_TC)
print("     2----Ad Soyad:",En_Yuksek_Aylik_Net_Ucret_Ad_Soyad)
print("     3----Aylık Toplam Brüt Ücreti:",En_Yuksek_Aylik_Net_Ucret_Toplam_Brut_Ucret)
print("     4----Aylık Toplam Net Ücreti:",float("{0:.2f}".format(En_Yuksek_Aylik_Net_Ucret_Aylik_Net_Ucreti)))
print("     5----Gelir Vergi Kesintisi:",float("{0:.2f}".format(En_Yuksek_Aylik_Net_Ucret_Gelir_Vergi_Kesintisi)))
print("                                                                                              ")
print("Evli Çalışan Sayısı Yüzdesi:" , float("{0:.2f}".format(Evli_Calisan_Sayisi_Yuzde)))
print("Bekar Çalışan Sayısı Yüzdesi:" , float("{0:.2f}".format(Bekar_Calisan_Sayisi_Yuzde)))
print("                                                                                              ")
print("Evli Olan Çalışanların İçinde, Eşleri De Çalışanların Yüzdesi:" , float("{0:.2f}".format(Esleri_Calisiyor_Olan_Calisan_Yuzde)))
print("Çalışanların Bakmakla Yükümlü Oldukları Çocuk Sayısının Ortalaması:" , float("{0:.2f}".format(bakmakla_yukumlu_olunan_cocuk_say_ortalama)))
print("                                                                                              ")
print("Bakmakla Yükümlü Olduğu Çocuk Sayısı 3’ten Fazla Olan Çalışanların Sayısı:" , cocuk_sayisi_ucten_fazla_olan_calisan_say)
print("                                                                                              ")
print("Engelli Çalışanların Sayısı:" , engelli_calisan_say)
print("Engelli Çalışanların Yüzdesi:" , float("{0:.2f}".format(engelli_calisan_yuzde)))
