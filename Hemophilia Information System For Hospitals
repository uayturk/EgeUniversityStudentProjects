hemofilihastaA=0
hemofilihastaB=0
hemofilihastaagir=0
hemofilihastaorta=0
hemofilihastahafif=0
inhibitorhemofiliA=0
inhibitorhemofiliB=0
profilaksiuygulananhepatitA=0
profilaksiuygulananhepatitB=0
ortahemofiliprofilaksiuygulanansay=0
plazmakaynaklıhemofiliA=0
plazmakaynaklıhemofiliB=0
rekombinanthemofiliA=0
rekombinanthemofiliB=0
hemofiliAhastalarindaplazmakaynaklifaktoryuzde=0
hemofiliBhastalarindaplazmakaynaklifaktoryuzde=0
hemofiliAhastalarindarekombinantfaktoryuzde=0
hemofiliBhastalarindarekombinantfaktoryuzde=0
toplamdorthaftalikrekombinantfaktor9ilacmiktar=0
toplamdorthaftalikplazmakaynaklifaktor9ilacmiktar=0
toplamdorthaftalikrekombinantfaktor8ilacmiktar=0
toplamdorthaftalikplazmakaynaklifaktor8ilacmiktar=0

dorthaftaiktoplamilac=0

toplamdorthaftalikrekombinantfaktor9ilacbinlik=0
toplamdorthaftalikrekombinantfaktor9ilacbesyuzluk=0
toplamdorthaftalikrekombinantfaktor9ilacikiyuzellilik=0

toplamdorthaftalikplazmakaynaklifaktor9ilacbinlik=0
toplamdorthaftalikplazmakaynaklifaktor9ilacbesyuzluk=0
toplamdorthaftalikplazmakaynaklifaktor9ilacikiyuzellilik=0

toplamdorthaftalikrekombinantfaktor8ilacbinlik=0
toplamdorthaftalikrekombinantfaktor8ilacbesyuzluk=0
toplamdorthaftalikrekombinantfaktor8ilacikiyuzellilik=0

toplamdorthaftalikplazmakaynaklifaktor8ilacbinlik=0
toplamdorthaftalikplazmakaynaklifaktor8ilacbesyuzluk=0
toplamdorthaftalikplazmakaynaklifaktor8ilacikiyuzellilik=0

SGKdorthaftalikilfaktorilactutar=0
SGKbiryillikfaktorilactutar=0

ortalamabirhastaiçinkarsilananyillikilacmiktar=0
toplam4haftalıkgenelilactoplam=0
yillikgenelilactoplam=0
ortamalabirhastaicinkarsilananyilliktutar=0

ilacmiktarienyuksekhemofiliB=0
ilacmiktarienyuksekhemofiliA=0

dorthaftalikilactutariencokhastaB=0
dorthaftalikilactutar=0
dorthaftalikilactutariencokhastaA=0

hemofilihastasıAtutarmiktar=0
hemofilihastasıBtutarmiktar=0

while(True):
    hastaTC= input("Hastanın TC kimlik numarasını giriniz:")
    HastaADSoyad= input("Hastanın Ad-Soyadını giriniz:")

    hastalıktipi=input("Hemofili hastalığının tipini giriniz(A/a/B/b):")
    while(str(hastalıktipi)!="A" and str(hastalıktipi)!="a" and str(hastalıktipi)!="B" and str(hastalıktipi)!="b"):
       print("Hastalık tipini yanlış harfle belirttiniz!")
       hastalıktipi=input("Hemofili hastalığının tipini giriniz(A/a/B/b):")

    if(str(hastalıktipi)=="A" or str(hastalıktipi)=="a"):
        hemofilihastaA=hemofilihastaA+1
    elif(str(hastalıktipi)=="B" or str(hastalıktipi)=="b"):
        hemofilihastaB=hemofilihastaB+1
    kandakifaktormiktar=input("Kandaki ilgili faktör miktarı (ünite): ")
    while(float(kandakifaktormiktar)<0 or float(kandakifaktormiktar)>=50):
       print("Kandaki ilgili faktor miktarını yanlış girdiniz!")
       kandakifaktormiktar=input("Kandaki ilgili faktör miktarı (ünite): ")

    karsiantikor=input("Kandaki ilgili faktör proteinine karşı üretilen antikor miktarı (ünite):")
    while(float(karsiantikor)<0):
       print("Kandaki ilgili faktör proteinine karşı üretilen antikor miktarını yanlış girdiniz!")
       karsiantikor=input("Kandaki ilgili faktör proteinine karşı üretilen antikor miktarı (ünite):")

    kandakipıhtılasmafaktormiktar=(float(kandakifaktormiktar)/float(karsiantikor))

    if(float(kandakipıhtılasmafaktormiktar)<float(0.01)):
        if(float(karsiantikor)<=5):
           print("Hastalık ağır şiddettedir.")
           hemofilihastaagir=hemofilihastaagir+1
           if(str(hastalıktipi)=="A" or str(hastalıktipi)=="a"):
               profilaksiuygulananhepatitA=profilaksiuygulananhepatitA+1
           elif(str(hastalıktipi)=="B" or str(hastalıktipi)=="b"):
               profilaksiuygulananhepatitB=profilaksiuygulananhepatitB+1
           hastalıksiddet=str("Ağır")
           hastakilosu=input("Hastanın kilosunu giriniz:")
           faktorilacturu=input("Kullanacağı faktör ilacının türü (P/p/R/r):")
           if(str(faktorilacturu)=="R" or str(faktorilacturu)=="r"):
               turadi=str("Rekombinant faktör-8/faktör-9")
               if(str(hastalıktipi)=="A" or str(hastalıktipi)=="a"):#Burada ağır hemofiliA hastalarındaki rekombinant faktör ilacı kullanan yuzdesini bulmak için rekombinant kullanan hemofiliA hasta sayılarını saptadık
                   rekombinanthemofiliA=rekombinanthemofiliA+1
               elif(str(hastalıktipi)=="B" or str(hastalıktipi)=="b"):#Burada da ağır hemofiliB hastalarındaki rekombinant faktör ilacı kullanan yuzdesini bulmak için rekombinant kullanan hemofiliB hasta sayılarını saptadık
                   rekombinanthemofiliB=rekombinanthemofiliB+1

           elif(str(faktorilacturu)=="P" or str(faktorilacturu)=="p"):
               turadi=str("Plazma kaynaklı faktör-8/faktör-9")
               if(str(hastalıktipi)=="A" or str(hastalıktipi)=="a"):#Burada ağır hemofiliA hastalarındaki plazma kaynaklı faktör ilacı kullanan yuzdesini bulmak için plazma kaynaklı faktör kullanan hemofiliA hasta sayılarını saptadık
                   plazmakaynaklıhemofiliA=plazmakaynaklıhemofiliA+1
               elif(str(hastalıktipi)=="B" or str(hastalıktipi)=="b"):#Burada da ağır hemofiliB hastalarındaki plazma kaynaklı faktör ilacı kullanan yuzdesini bulmak için plazma kaynaklı faktör kullanan hemofiliB hasta sayılarını saptadık
                   plazmakaynaklıhemofiliB=plazmakaynaklıhemofiliB+1
           while(str(faktorilacturu)!="P" and str(faktorilacturu)!="p" and str(faktorilacturu)!="R" and str(faktorilacturu)!="r"):
               print("Kullanacağı faktör ilacının türünü yanlış harfle belirttiniz!")
               faktorilacturu=input("Kullanacağı faktör ilacının türü (P/p/R/r):")
        else:
            print("Hastalık ağır şiddettedir fakat inhibitör varlığı nedeniyle hastaya profilaksi uygulanamayacaktır.")
            hemofilihastaagir=hemofilihastaagir+1
            if(str(hastalıktipi)=="A" or str(hastalıktipi)=="a"):
               inhibitorhemofiliA=inhibitorhemofiliA+1
            elif(str(hastalıktipi)=="B" or str(hastalıktipi)=="b"):
               inhibitorhemofiliB=inhibitorhemofiliB+1
            hastalıksiddet=str("Ağır")

    elif(float(kandakipıhtılasmafaktormiktar)==float(0.01) or ( float(kandakipıhtılasmafaktormiktar)>float(0.01) and float(kandakipıhtılasmafaktormiktar)<float(0.05))):
        if(float(karsiantikor)<5):
            print("Hastalık orta şiddettedir.")
            hemofilihastaorta=hemofilihastaorta+1
            hastalıksiddet=str("Orta")
            kanamasayisi=input("Son 1 yılda meydana gelen kanama sayısı:")
            while(int(kanamasayisi)<0):
                print("Kanama sayısını yanlış girdiniz!")
                kanamasayisi=input("Son 1 yılda meydana gelen kanama sayısı:")

            aylikortalamakanamamiktari=(int(kanamasayisi)/12)

            if(float(aylikortalamakanamamiktari)>3):
                if(str(hastalıktipi)=="A" or str(hastalıktipi)=="a"):
                    profilaksiuygulananhepatitA=profilaksiuygulananhepatitA+1
                elif(str(hastalıktipi)=="B" or str(hastalıktipi)=="b"):
                    profilaksiuygulananhepatitB=profilaksiuygulananhepatitB+1

                ortahemofiliprofilaksiuygulanansay=ortahemofiliprofilaksiuygulanansay+1

                hastakilosu=input("Hastanın kilosunu giriniz:")
                faktorilacturu=input("Kullanacağı faktör ilacının türü (P/p/R/r):")
                if(str(faktorilacturu)=="R" or str(faktorilacturu)=="r"):
                    turadi=str("Rekombinant faktör-8/faktör-9")
                    if(str(hastalıktipi)=="A" or str(hastalıktipi)=="a"):#Burada orta hemofiliA hastalarındaki rekombinant faktör ilacı kullanan yuzdesini bulmak için rekombinant kullanan hemofiliA hasta sayılarını saptadık
                       rekombinanthemofiliA=rekombinanthemofiliA+1
                    elif(str(hastalıktipi)=="B" or str(hastalıktipi)=="b"):#Burada da orta hemofiliB hastalarındaki rekombinant faktör ilacı kullanan yuzdesini bulmak için rekombinant kullanan hemofiliB hasta sayılarını saptadık
                       rekombinanthemofiliB=rekombinanthemofiliB+1

                elif(str(faktorilacturu)=="P" or str(faktorilacturu)=="p"):
                    turadi=str("Plazma kaynaklı faktör-8/faktör-9")
                    if(str(hastalıktipi)=="A" or str(hastalıktipi)=="a"):#Burada ağır hemofiliA hastalarındaki plazma kaynaklı faktör ilacı kullanan yuzdesini bulmak için plazma kaynaklı faktör kullanan hemofiliA hasta sayılarını saptadık
                       plazmakaynaklıhemofiliA=plazmakaynaklıhemofiliA+1
                    elif(str(hastalıktipi)=="B" or str(hastalıktipi)=="b"):#Burada da ağır hemofiliB hastalarındaki plazma kaynaklı faktör ilacı kullanan yuzdesini bulmak için plazma kaynaklı faktör kullanan hemofiliB hasta sayılarını saptadık
                       plazmakaynaklıhemofiliB=plazmakaynaklıhemofiliB+1
                while(str(faktorilacturu)!="P" and str(faktorilacturu)!="p" and str(faktorilacturu)!="R" and str(faktorilacturu)!="r"):
                    print("Kullanacağı faktör ilacının türünü yanlış harfle belirttiniz!")
                    faktorilacturu=input("Kullanacağı faktör ilacının türü (P/p/R/r):")
            else:
                print("Aylık ortalama kanama miktarı 3'ten fazla olmadığı için hastaya profilaksi uygulanamayacaktır.")
        else:
           print("Hastalık orta şiddettedir fakat inhibitör varlığı nedeniyle hastaya profilaksi uygulanamayacaktır.")
           hemofilihastaorta=hemofilihastaorta+1
           if(str(hastalıktipi)=="A" or str(hastalıktipi)=="a"):
               inhibitorhemofiliA=inhibitorhemofiliA+1
           elif(str(hastalıktipi)=="B" or str(hastalıktipi)=="b"):
               inhibitorhemofiliB=inhibitorhemofiliB+1
           hastalıksiddet=str("Orta")

    elif(float(kandakipıhtılasmafaktormiktar)==float(0.05) or float(kandakipıhtılasmafaktormiktar)>float(0.05) and float(kandakipıhtılasmafaktormiktar)<float(0.5)):
        print("Kanama hafif şiddettedir.")
        hemofilihastahafif=hemofilihastahafif+1
        hastalıksiddet=str("Hafif")


    print("Hasta TC:",hastaTC)
    print("Hasta Ad-Soyad:",HastaADSoyad)
    print("Hastalığın tipi:",hastalıktipi)
    print("Hastalık Şiddeti:",hastalıksiddet)
    if(str(hastalıksiddet)=="Ağır" and float(karsiantikor)<=5 or str(hastalıksiddet)=="Orta" and int(aylikortalamakanamamiktari)>3):
        print("Hastaya profilaksi uygulanacaktır.")
        print("Kullanacağı faktör ilacı türü:",turadi)

        if(str(hastalıktipi)=="A" or str(hastalıktipi)=="a" ):
            print("Hastanın haftada kaç kez ilaç kullanacak:",int(3))

            gerekliartis=(float(0.4)-float(kandakifaktormiktar))#önce %40'a çıkacak sekilde oldugu için kandaki gerekli artışı bulduk.
            unitekilogramliartis=(float(gerekliartis)*int(hastakilosu))#Sonra kilo başına 1 ünitelik verildiği için kaç kiloya hasta o kilo ile gerekli artışı çarptım ki sonrasında bunu ((Kandaki ilgili faktör miktarı)*0.02(hemofiliA artışı))'ye bölüp kaç ünite alınması gerek ona ulaşacağım

            birimartis=(float(kandakifaktormiktar)*float(0.02))#Burada işte mesela hastanın Kandaki ilgili faktör miktarı=0.1 ise 0.1*0.02=0.0002 birim artış oluyor kilo başına.Yeni kandaki miktar bu örnek için 0,1002'e çıktı mesela.

            kullanilmasigerekenminilacmiktar=(float(unitekilogramliartis)/float(birimartis))#Burada da en son bölünce işte o kaç kiloysa hasta onun gerekli artış ile çarpılmış halini,birim artışımıza bize hastanın kaç ünite kullanması gerektiğini veriyor.Yazınızdan anladığım bu yani,umarım doğrudur diğer projede daha açık ve anlaşılır yazarsanız sevinirim.

            ilacmiktarienyuksekhemofiliA=dorthaftaiktoplamilac
            dorthaftalikilactutariencokhastaB=dorthaftalikilactutar
            print("Bir seferde kullanması gereken minimum ilaç miktarı (ünite):",round(kullanilmasigerekenminilacmiktar,2))

            if(int(kullanilmasigerekenminilacmiktar)>1000):#önce alınması gereken ilac miktarı 1000'den buyukse buraya soktuk ve her binlik için alınacak tam bir 1000 ünitelik 1 flakonu tuttuk
                binliktam=(int(kullanilmasigerekenminilacmiktar)/1000)#Örnek üzerinden mantığı anlatalım.Mesela burada örnegin bir seferde min.1770 ünite kullancak hasta.
                if((int(kullanilmasigerekenminilacmiktar)%1000)!=0):#Sonra modunu aldık 770 kaldi
                    kalanmiktar1=(int(kullanilmasigerekenminilacmiktar)%1000)#Kalanı kalanmiktar1 diye bir degiskene atadık
                    if(int(kalanmiktar1)>500):#kalanmiktar1 770 yani 500 den buyuk
                        besyuzluktam=(int(kalanmiktar1)/500)#770/500 yapıp,...
                        besyuzlukflakon=int(besyuzluktam)
                        if((int(kalanmiktar1)%500)!=0):#sonra 770 modunu aldık
                            kalanmiktar2=(int(kalanmiktar1)%500)#modu yani 270'i atadık kalanmiktar2 diye yeni bir degiskene.
                            if(kalanmiktar2>250):#son olarak 250 lik flakon hesabı için büyük küçük kontrollerini sağladık.
                                ikiyuzelliliktam=(int(kalanmiktar2)/250)#270/250 yapıp..
                                ikiyuzellilikflakon=int(ikiyuzelliliktam)
                                if((int(kalanmiktar2)%250)!=0):
                                    ikiyuzellilikflakon=ikiyuzellilikflakon+1#kalan varsa birşey yine 250 lik flakan almak zorundayız
                                    binlikflakon=int(binliktam)
                                    besyuzlukflakon=int(besyuzluktam)
                            else:
                               ikiyuzellilikflakon=1 #eger kalan mesela 170 falansa 250lik almalıyız 1 tane yine
                               besyuzlukflakon=int(besyuzluktam)
                               binlikflakon=int(binliktam)
                    else:#Bu kısım kalan direk 500den küçük birşeyse olasılığı için
                        if(int(kalanmiktar1)>250):
                            ikiyuzellilikflakon=2 #eger kalan 450 gibi birseyse 2 tane 250lik flakon ünite almak lazım oluyor
                        else:
                            ikiyuzellilikflakon=1#eger kalan 50 gibi birseyse 2 tane 250lik flakon ünite almak lazım oluyor
                        binlikflakon=int(binliktam)
                        besyuzlukflakon=0
                else:
                    binlikflakon=int(binliktam)#Eger 1000 ünitelik tam alınabiliyorsa yani alınacak ünite tam 1000'in katlarına denk geliyorsa direk buraya geliyor.
                    besyuzlukflakon=0
                    ikiyuzellilikflakon=0
            else:#eger direk 1000den küçük gelirse alınacak ünite
                binlikflakon=0
                if(int(kullanilmasigerekenminilacmiktar)>500):#kalanmiktar1 770 yani 500 den buyuk
                        besyuzluktam=(int(kullanilmasigerekenminilacmiktar)/500)#770/500 yapıp,...
                        besyuzlukflakon=int(besyuzluktam)
                        if((int(kullanilmasigerekenminilacmiktar)%500)!=0):#sonra 770 modunu aldık
                            kalanmiktar2=(int(kullanilmasigerekenminilacmiktar)%500)#modu yani 270'i atadık kalanmiktar2 diye yeni bir degiskene.
                            if(kalanmiktar2>250):#son olarak 250 lik flakon hesabı için büyük küçük kontrollerini sağladık.
                                ikiyuzelliliktam=(int(kalanmiktar2)/250)#270/250 yapıp..
                                ikiyuzellilikflakon=int(ikiyuzelliliktam)
                                if((int(kalanmiktar2)%250)!=0):
                                    ikiyuzellilikflakon=ikiyuzellilikflakon+1#kalan varsa birşey yine 250 lik flakan almak zorundayız
                                    besyuzlukflakon=int(besyuzluktam)
                            else:
                               ikiyuzellilikflakon=1 #eger kalan mesela 170 falansa 250lik almalıyız 1 tane yine
                               besyuzlukflakon=int(besyuzluktam)
                else:#Bu kısım kalan direk 500den küçük birşeyse olasılığı için
                    if(int(kullanilmasigerekenminilacmiktar)>250):
                        ikiyuzellilikflakon=2 #eger kalan 450 gibi birseyse 2 tane 250lik flakon ünite almak lazım oluyor
                    else:
                        ikiyuzellilikflakon=1#eger kalan 50 gibi birseyse 2 tane 250lik flakon ünite almak lazım oluyor
                    besyuzlukflakon=0

            birseferdekullanacagiilacmiktar=((int(binlikflakon)*int(1000))+(int(besyuzlukflakon)*int(500))+(int(ikiyuzellilikflakon)*int(250)))


            print("Bir seferde kullanacağı ilaç miktarı (ünite):",int(birseferdekullanacagiilacmiktar))
            print("Binlik ünite:",int(binlikflakon))
            print("Besyüzlük ünite:",int(besyuzlukflakon))
            print("İkiyüzellilik ünite:",int(ikiyuzellilikflakon))

            dorthaftaiktoplamilac=(int(birseferdekullanacagiilacmiktar)*3*4)#Hemofili-A hastaları haftada 3 kez kullanıyordu.4 haftada 12 ile çarpımı kadar ünite ilaç gerekir.
            dorthaftalikbinlikunitemiktar=(int(binlikflakon)*3*4)
            dorthaftalikbesyuzlukunitemiktar=(int(besyuzlukflakon)*3*4)
            dorthaftalikikiyuzellilikunitemiktar=(int(ikiyuzellilikflakon)*3*4)

            print("Hastanın 4 haftalık toplam ilaç miktarı (ünite):",dorthaftaiktoplamilac)
            print("Hastanın 4 haftalık binlik ünite miktarı:",dorthaftalikbinlikunitemiktar)
            print("Hastanın 4 haftalık beşyüzlük ünite miktarı:",dorthaftalikbesyuzlukunitemiktar)
            print("Hastanın 4 haftalık ikiyüzellilik ünite miktarı:",dorthaftalikikiyuzellilikunitemiktar)

            if(str(faktorilacturu)=="R" or str(faktorilacturu)=="r"):
                dorthaftalikilactutar=(float(dorthaftaiktoplamilac)*(1.5))
                SGKdorthaftalikilfaktorilactutar=(SGKdorthaftalikilfaktorilactutar+int(dorthaftalikilactutar))
                toplamdorthaftalikrekombinantfaktor8ilacmiktar=(toplamdorthaftalikrekombinantfaktor8ilacmiktar+dorthaftaiktoplamilac)
                toplamdorthaftalikrekombinantfaktor8ilacbinlik=(toplamdorthaftalikrekombinantfaktor8ilacbinlik+int(dorthaftalikbinlikunitemiktar))
                toplamdorthaftalikrekombinantfaktor8ilacbesyuzluk=(toplamdorthaftalikrekombinantfaktor8ilacbesyuzluk+int(dorthaftalikbesyuzlukunitemiktar))
                toplamdorthaftalikrekombinantfaktor8ilacikiyuzellilik=(toplamdorthaftalikrekombinantfaktor8ilacikiyuzellilik+int(dorthaftalikikiyuzellilikunitemiktar))

            elif(str(faktorilacturu)=="P" or str(faktorilacturu)=="p"):
                dorthaftalikilactutar=(float(dorthaftaiktoplamilac)*(1.25))
                SGKdorthaftalikilfaktorilactutar=(SGKdorthaftalikilfaktorilactutar+int(dorthaftalikilactutar))
                toplamdorthaftalikplazmakaynaklifaktor8ilacmiktar=(toplamdorthaftalikplazmakaynaklifaktor8ilacmiktar+dorthaftaiktoplamilac)
                toplamdorthaftalikplazmakaynaklifaktor8ilacbinlik=(toplamdorthaftalikplazmakaynaklifaktor8ilacbinlik+int(dorthaftalikbinlikunitemiktar))
                toplamdorthaftalikplazmakaynaklifaktor8ilacbesyuzluk=(toplamdorthaftalikplazmakaynaklifaktor8ilacbesyuzluk+int(dorthaftalikbesyuzlukunitemiktar))
                toplamdorthaftalikplazmakaynaklifaktor8ilacikiyuzellilik=(toplamdorthaftalikplazmakaynaklifaktor8ilacikiyuzellilik+int(dorthaftalikikiyuzellilikunitemiktar))

            print("4 haftalık ilaç tutarı:",float(dorthaftalikilactutar))

            if(int(ilacmiktarienyuksekhemofiliA)<int(dorthaftaiktoplamilac)):
                ilacmiktarienyuksekhemofiliATC=hastaTC
                ilacmiktarienyuksekhemofiliAAdSoyad=HastaADSoyad
                ilacmiktarienyuksekhemofiliAhastaliksiddet=hastalıksiddet
                ilacmiktarienyuksekhemofiliAkilo=hastakilosu
                ilacmiktarienyuksekhemofiliAilacturu=turadi
                ilacmiktarienyuksekhemofiliA4haftalikilacmiktar=birseferdekullanacagiilacmiktar
                ilacmiktarienyuksekhemofiliA4haftalikilactutar=dorthaftalikilactutar

            if(int(dorthaftalikilactutariencokhastaA)<int(dorthaftalikilactutar)):
                hemofilihastasıAtutarmiktar=dorthaftalikilactutar#Bunu hemofili B hastasının tutarıyla karsılastırıp hangisi yuksekse onun atamalarını yaptıracagız.
                dorthaftalikilactutariencokhastaATC=hastaTC
                dorthaftalikilactutariencokhastaAAdSoyad=HastaADSoyad
                dorthaftalikilactutariencokhastaahastaliksiddet=hastalıksiddet
                dorthaftalikilactutariencokhastaAkilo=hastakilosu
                dorthaftalikilactutariencokhastaAilacturu=turadi
                dorthaftalikilactutariencokhastaA4haftalikilacmiktar=birseferdekullanacagiilacmiktar
                dorthaftalikilactutariencokhastaA4haftalikilactutar=dorthaftalikilactutar



        elif(str(hastalıktipi)=="B" or str(hastalıktipi)=="b"):
            print("Hastanın haftada kaç kez ilaç kullanacak:",int(2))

            gerekliartis=(float(0.4)-float(kandakifaktormiktar))
            unitekilogramliartis=(float(gerekliartis)*int(hastakilosu))

            birimartis=(float(kandakifaktormiktar)*float(0.01))

            kullanilmasigerekenminilacmiktar=(float(unitekilogramliartis)/float(birimartis))

            ilacmiktarienyuksekhemofiliB=dorthaftaiktoplamilac
            dorthaftalikilactutariencokhastaB=dorthaftalikilactutar

            print("Bir seferde kullanması gereken minimum ilaç miktarı (ünite):",round(kullanilmasigerekenminilacmiktar,2))

            if(int(kullanilmasigerekenminilacmiktar)>1000):#önce alınması gereken ilac miktarı 1000'den buyukse buraya soktuk ve her binlik için alınacak tam bir 1000 ünitelik 1 flakonu tuttuk
                binliktam=(int(kullanilmasigerekenminilacmiktar)/1000)#Örnek üzerinden mantığı anlatalım.Mesela burada örnegin bir seferde min.1770 ünite kullancak hasta.
                if((int(kullanilmasigerekenminilacmiktar)%1000)!=0):#Sonra modunu aldık 770 kaldi
                    kalanmiktar1=(int(kullanilmasigerekenminilacmiktar)%1000)#Kalanı kalanmiktar1 diye bir degiskene atadık
                    if(int(kalanmiktar1)>500):#kalanmiktar1 770 yani 500 den buyuk
                        besyuzluktam=(int(kalanmiktar1)/500)#770/500 yapıp,...
                        besyuzlukflakon=int(besyuzluktam)
                        if((int(kalanmiktar1)%500)!=0):#sonra 770 modunu aldık
                            kalanmiktar2=(int(kalanmiktar1)%500)#modu yani 270'i atadık kalanmiktar2 diye yeni bir degiskene.
                            if(kalanmiktar2>250):#son olarak 250 lik flakon hesabı için büyük küçük kontrollerini sağladık.
                                ikiyuzelliliktam=(int(kalanmiktar2)/250)#270/250 yapıp..
                                ikiyuzellilikflakon=int(ikiyuzelliliktam)
                                if((int(kalanmiktar2)%250)!=0):
                                    ikiyuzellilikflakon=ikiyuzellilikflakon+1#kalan varsa birşey yine 250 lik flakan almak zorundayız
                                    binlikflakon=int(binliktam)
                                    besyuzlukflakon=int(besyuzluktam)
                            else:
                               ikiyuzellilikflakon=1 #eger kalan mesela 170 falansa 250lik almalıyız 1 tane yine
                               besyuzlukflakon=int(besyuzluktam)
                               binlikflakon=int(binliktam)
                    else:#Bu kısım kalan direk 500den küçük birşeyse olasılığı için
                        if(int(kalanmiktar1)>250):
                            ikiyuzellilikflakon=2 #eger kalan 450 gibi birseyse 2 tane 250lik flakon ünite almak lazım oluyor
                        else:
                            ikiyuzellilikflakon=1#eger kalan 50 gibi birseyse 2 tane 250lik flakon ünite almak lazım oluyor
                        binlikflakon=int(binliktam)
                        besyuzlukflakon=0
                else:
                    binlikflakon=int(binliktam)#Eger 1000 ünitelik tam alınabiliyorsa yani alınacak ünite tam 1000'in katlarına denk geliyorsa direk buraya geliyor.
                    besyuzlukflakon=0
                    ikiyuzellilikflakon=0
            else:#eger direk 1000den küçük gelirse alınacak ünite
                binlikflakon=0
                if(int(kullanilmasigerekenminilacmiktar)>500):#kalanmiktar1 770 yani 500 den buyuk
                        besyuzluktam=(int(kullanilmasigerekenminilacmiktar)/500)#770/500 yapıp,...
                        besyuzlukflakon=int(besyuzluktam)
                        if((int(kullanilmasigerekenminilacmiktar)%500)!=0):#sonra 770 modunu aldık
                            kalanmiktar2=(int(kullanilmasigerekenminilacmiktar)%500)#modu yani 270'i atadık kalanmiktar2 diye yeni bir degiskene.
                            if(kalanmiktar2>250):#son olarak 250 lik flakon hesabı için büyük küçük kontrollerini sağladık.
                                ikiyuzelliliktam=(int(kalanmiktar2)/250)#270/250 yapıp..
                                ikiyuzellilikflakon=int(ikiyuzelliliktam)
                                if((int(kalanmiktar2)%250)!=0):
                                    ikiyuzellilikflakon=ikiyuzellilikflakon+1#kalan varsa birşey yine 250 lik flakan almak zorundayız
                                    besyuzlukflakon=int(besyuzluktam)
                            else:
                               ikiyuzellilikflakon=1 #eger kalan mesela 170 falansa 250lik almalıyız 1 tane yine
                               besyuzlukflakon=int(besyuzluktam)
                else:#Bu kısım kalan direk 500den küçük birşeyse olasılığı için
                    if(int(kullanilmasigerekenminilacmiktar)>250):
                        ikiyuzellilikflakon=2 #eger kalan 450 gibi birseyse 2 tane 250lik flakon ünite almak lazım oluyor
                    else:
                        ikiyuzellilikflakon=1#eger kalan 50 gibi birseyse 2 tane 250lik flakon ünite almak lazım oluyor
                    besyuzlukflakon=0

            birseferdekullanacagiilacmiktar=((int(binlikflakon)*int(1000))+(int(besyuzlukflakon)*int(500))+(int(ikiyuzellilikflakon)*int(250)))


            print("Bir seferde kullanacağı ilaç miktarı (ünite):",int(birseferdekullanacagiilacmiktar))
            print("Binlik ünite:",int(binlikflakon))
            print("Besyüzlük ünite:",int(besyuzlukflakon))
            print("İkiyüzellilik ünite:",int(ikiyuzellilikflakon))

            print("Bir seferde kullanacağı ilaç miktarı (ünite):",int(birseferdekullanacagiilacmiktar))
            print("Binlik ünite:",int(binlikflakon))
            print("Besyüzlük ünite:",int(besyuzlukflakon))
            print("İkiyüzellilik ünite:",int(ikiyuzellilikflakon))

            dorthaftaiktoplamilac=(int(birseferdekullanacagiilacmiktar)*2*4)#Hemofili-B hastaları haftada 2 kez kullanıyordu.4 haftada 12 ile çarpımı kadar ünite ilaç gerekir.
            dorthaftalikbinlikunitemiktar=(int(binlikflakon)*2*4)
            dorthaftalikbesyuzlukunitemiktar=(int(besyuzlukflakon)*2*4)
            dorthaftalikikiyuzellilikunitemiktar=(int(ikiyuzellilikflakon)*2*4)

            print("Hastanın 4 haftalık toplam ilaç miktarı (ünite):",dorthaftaiktoplamilac)
            print("Hastanın 4 haftalık binlik ünite miktarı:",dorthaftalikbinlikunitemiktar)
            print("Hastanın 4 haftalık beşyüzlük ünite miktarı:",dorthaftalikbesyuzlukunitemiktar)
            print("Hastanın 4 haftalık ikiyüzellilik ünite miktarı:",dorthaftalikikiyuzellilikunitemiktar)

            if(str(faktorilacturu)=="R" or str(faktorilacturu)=="r"):#hepatit B için burası burada faktor9 için işlem yaptırıyoruz
                dorthaftalikilactutar=(float(dorthaftaiktoplamilac)*(1.5))
                SGKdorthaftalikilfaktorilactutar=(SGKdorthaftalikilfaktorilactutar+int(dorthaftalikilactutar))
                toplamdorthaftalikrekombinantfaktor9ilacmiktar=(toplamdorthaftalikrekombinantfaktor9ilacmiktar+dorthaftaiktoplamilac)
                toplamdorthaftalikrekombinantfaktor9ilacbinlik=(toplamdorthaftalikrekombinantfaktor9ilacbinlik+int(dorthaftalikbinlikunitemiktar))
                toplamdorthaftalikrekombinantfaktor9ilacbesyuzluk=(toplamdorthaftalikrekombinantfaktor9ilacbesyuzluk+int(dorthaftalikbesyuzlukunitemiktar))
                toplamdorthaftalikrekombinantfaktor9ilacikiyuzellilik=(toplamdorthaftalikrekombinantfaktor9ilacikiyuzellilik+int(dorthaftalikikiyuzellilikunitemiktar))
            elif(str(faktorilacturu)=="P" or str(faktorilacturu)=="p"):
                dorthaftalikilactutar=(float(dorthaftaiktoplamilac)*(1.25))
                SGKdorthaftalikilfaktorilactutar=(SGKdorthaftalikilfaktorilactutar+int(dorthaftalikilactutar))
                toplamdorthaftalikplazmakaynaklifaktor9ilacmiktar=(toplamdorthaftalikplazmakaynaklifaktor9ilacmiktar+dorthaftaiktoplamilac)
                toplamdorthaftalikplazmakaynaklifaktor9ilacbinlik=(toplamdorthaftalikplazmakaynaklifaktor9ilacbinlik+int(dorthaftalikbinlikunitemiktar))
                toplamdorthaftalikplazmakaynaklifaktor9ilacbesyuzluk=(toplamdorthaftalikplazmakaynaklifaktor9ilacbesyuzluk+int(dorthaftalikbesyuzlukunitemiktar))
                toplamdorthaftalikplazmakaynaklifaktor9ilacikiyuzellilik=(toplamdorthaftalikplazmakaynaklifaktor9ilacikiyuzellilik+int(dorthaftalikikiyuzellilikunitemiktar))

            print("4 haftalık ilaç tutarı:",float(dorthaftalikilactutar))

            if(int(ilacmiktarienyuksekhemofiliB)<int(dorthaftaiktoplamilac)):
                ilacmiktarienyuksekhemofiliBTC=hastaTC
                ilacmiktarienyuksekhemofiliBAdSoyad=HastaADSoyad
                ilacmiktarienyuksekhemofiliBhastaliksiddet=hastalıksiddet
                ilacmiktarienyuksekhemofiliBkilo=hastakilosu
                ilacmiktarienyuksekhemofiliBilacturu=turadi
                ilacmiktarienyuksekhemofiliB4haftalikilacmiktar=birseferdekullanacagiilacmiktar
                ilacmiktarienyuksekhemofiliB4haftalikilactutar=dorthaftalikilactutar

            if(int(dorthaftalikilactutariencokhastaB)<int(dorthaftalikilactutar)):
                hemofilihastasıBtutarmiktar=dorthaftalikilactutar#Bunu hemofili A hastasının tutarıyla karsılastırıp hangisi yuksekse onun atamalarını yaptıracagız.
                dorthaftalikilactutariencokhastaBTC=hastaTC
                dorthaftalikilactutariencokhastaBAdSoyad=HastaADSoyad
                dorthaftalikilactutariencokhastaBhastaliksiddet=hastalıksiddet
                dorthaftalikilactutariencokhastaBkilo=hastakilosu
                dorthaftalikilactutariencokhastaBilacturu=turadi
                dorthaftalikilactutariencokhastaB4haftalikilacmiktar=birseferdekullanacagiilacmiktar
                dorthaftalikilactutariencokhastaB4haftalikilactutar=dorthaftalikilactutar

    baskahasta=input("Başka hasta var mı?(E/e/H/h)")
    while(str(baskahasta)!="E" and str(baskahasta)!="e" and str(baskahasta)!="H" and str(baskahasta)!="h"):
        print("Hatalı harf girişi!!")
        baskahasta=input("Başka hasta var mı?(E/e/H/h)")

    if(str(baskahasta)=="H" or str(baskahasta)=="h"):
        break

if(hemofilihastasıBtutarmiktar>hemofilihastasıAtutarmiktar):
    dorthaftalikilactutariencokhastaSONTC=dorthaftalikilactutariencokhastaBTC
    dorthaftalikilactutariencokhastaSONAdSoyad=dorthaftalikilactutariencokhastaBAdSoyad
    dorthaftalikilactutariencokhastaSONhastaliktip=str("Hemofili-B")
    dorthaftalikilactutariencokhastaSONsiddet=dorthaftalikilactutariencokhastaBhastaliksiddet
    dorthaftalikilactutariencokhastaSONkilo=dorthaftalikilactutariencokhastaBkilo
    dorthaftalikilactutariencokhastaSONturu=dorthaftalikilactutariencokhastaBilacturu
    dorthaftalikilactutariencokhastaSON4haftalikilacmiktar=dorthaftalikilactutariencokhastaB4haftalikilacmiktar
    orthaftalikilactutariencokhastaSON4haftalikilactutar=dorthaftalikilactutariencokhastaB4haftalikilactutar

elif(hemofilihastasıBtutarmiktar<hemofilihastasıAtutarmiktar):
    dorthaftalikilactutariencokhastaSONTC=dorthaftalikilactutariencokhastaATC
    dorthaftalikilactutariencokhastaSONAdSoyad=dorthaftalikilactutariencokhastaAAdSoyad
    dorthaftalikilactutariencokhastaSONhastaliktip=str("Hemofili-A")
    dorthaftalikilactutariencokhastaSONsiddet=dorthaftalikilactutariencokhastaahastaliksiddet
    dorthaftalikilactutariencokhastaSONkilo=dorthaftalikilactutariencokhastaAkilo
    dorthaftalikilactutariencokhastaSONturu=dorthaftalikilactutariencokhastaAilacturu
    dorthaftalikilactutariencokhastaSON4haftalikilacmiktar=dorthaftalikilactutariencokhastaA4haftalikilacmiktar
    orthaftalikilactutariencokhastaSON4haftalikilactutar=dorthaftalikilactutariencokhastaA4haftalikilactutar


toplamprofilaksiuygulananhastasayisi=(int(profilaksiuygulananhepatitA)+int(profilaksiuygulananhepatitB))
toplamhastasay=(int(hemofilihastaA)+int(hemofilihastaB))

toplam4haftalıkgenelilactoplam=(toplamdorthaftalikplazmakaynaklifaktor8ilacmiktar+toplamdorthaftalikrekombinantfaktor8ilacmiktar+toplamdorthaftalikplazmakaynaklifaktor9ilacmiktar+toplamdorthaftalikrekombinantfaktor9ilacmiktar)
yillikgenelilactoplam=(int(toplam4haftalıkgenelilactoplam*12))
ortalamabirhastaiçinkarsilananyillikilacmiktar=(yillikgenelilactoplam/toplamprofilaksiuygulananhastasayisi)

ortamalabirhastaicinkarsilananyilliktutar=(SGKbiryillikfaktorilactutar/toplamprofilaksiuygulananhastasayisi)

agirhastayuzde=((int(hemofilihastaagir)/toplamhastasay)*100)
ortahastayuzde=((int(hemofilihastaorta)/toplamhastasay)*100)
hafifhastayuzde=((int(hemofilihastahafif)/toplamhastasay)*100)

inhibitorhemoAyuzde=((int(inhibitorhemofiliA)/hemofilihastaA)*100)
inhibitorhemoByuzde=((int(inhibitorhemofiliB)/hemofilihastaB)*100)

profilaksiuygulananhepatitAyuzde=((int(profilaksiuygulananhepatitA)/toplamprofilaksiuygulananhastasayisi)*100)
profilaksiuygulananhepatitByuzde=((int(profilaksiuygulananhepatitB)/toplamprofilaksiuygulananhastasayisi)*100)

ortasiddethemofilihastaprofilaksiuygulananyuzde=((int(ortahemofiliprofilaksiuygulanansay)/hemofilihastaorta)*100)

hemofiliAhastalarindaplazmakaynaklifaktoryuzde=((int(plazmakaynaklıhemofiliA)/profilaksiuygulananhepatitA)*100)
hemofiliBhastalarindaplazmakaynaklifaktoryuzde=((int(plazmakaynaklıhemofiliB)/profilaksiuygulananhepatitB)*100)
hemofiliAhastalarindarekombinantfaktoryuzde=((int(rekombinanthemofiliA)/profilaksiuygulananhepatitA)*100)
hemofiliBhastalarindarekombinantfaktoryuzde=((int(rekombinanthemofiliB)/profilaksiuygulananhepatitB)*100)

SGKbiryillikfaktorilactutar=(int(SGKdorthaftalikilfaktorilactutar)*12)

print("Hemofili A hasta sayısı:",hemofilihastaA)
print("Hemofili B hasta sayısı:",hemofilihastaB)
print("Toplam hasta sayısı:",toplamhastasay)
print("--------------------------------")
print("Agir hasta yüzdesi: %",float(agirhastayuzde))
print("Agir hasta sayısı:",int(hemofilihastaagir))
print("Orta şiddetli hasta yüzdesi: %",float(ortahastayuzde))
print("Orta şiddette hasta sayısı:",int(hemofilihastaorta))
print("Hafif şiddette hasta yüzdesi: %",float(hafifhastayuzde))
print("Hafif şiddette hasta sayısı:",int(hemofilihastahafif))
print("--------------------------------")
print(" Hemofili-A hastalarında inhibitör varlığı yüzdesi: %",float(inhibitorhemoAyuzde))
print(" Hemofili-B hastalarında inhibitör varlığı yüzdesi: %",float(inhibitorhemoByuzde))
print("--------------------------------")
print("Profilaksi uygulanan Hemofili-A hastalarının sayısı:",profilaksiuygulananhepatitA)
print("Profilaksi uygulanan Hemofili-B hastalarının sayısı:",profilaksiuygulananhepatitB)
print("Profilaksi uygulanan Hemofili-A hastalarının yüzdesi:%",float(profilaksiuygulananhepatitAyuzde))
print("Profilaksi uygulanan Hemofili-B hastalarının yüzdesi:%",float(profilaksiuygulananhepatitByuzde))
print("--------------------------------")
print("Hastalığının şiddeti orta olan hemofili hastaları içinde, profilaksi uygulanan hastaların yüzdesi:%",float(ortasiddethemofilihastaprofilaksiuygulananyuzde))

print("Profilaksi uygulanan Hemofili-A hastaları içinde:")
print("Plazma kaynaklı faktör ilacı kullanan hastaların yüzdeleri:%",float(hemofiliAhastalarindaplazmakaynaklifaktoryuzde))
print("Rekombinant faktör ilacı kullanan hastaların yüzdeleri:%",float(hemofiliAhastalarindarekombinantfaktoryuzde))
print("--------------------------------")
print("Profilaksi uygulanan Hemofili-B hastaları içinde:")
print("Plazma kaynaklı faktör ilacı kullanan hastaların yüzdeleri:%",float(hemofiliBhastalarindaplazmakaynaklifaktoryuzde))
print("Rekombinant faktör ilacı kullanan hastaların yüzdeleri:%",float(hemofiliBhastalarindarekombinantfaktoryuzde))
print("--------------------------------")
print("Profilaksi uygulaması için tedarik edilmesi gereken 4 haftalık toplam:")
print("1-4 Haftalık plazma kaynaklı faktör-8 miktar(ünite):",toplamdorthaftalikplazmakaynaklifaktor8ilacmiktar)
print("2-4 Haftalık rekombinant faktör-8 miktar(ünite):",toplamdorthaftalikrekombinantfaktor8ilacmiktar)
print("3-4 Haftalık plazma kaynaklı faktör-9 miktar(ünite):",toplamdorthaftalikplazmakaynaklifaktor9ilacmiktar)
print("4-4 Haftalık rekombinant faktör-9 miktar(ünite):",toplamdorthaftalikrekombinantfaktor9ilacmiktar)
print("---------------Faktör-8--------------")
print("1-4 Haftalık plazma kaynaklı faktör-8 binlik:",toplamdorthaftalikplazmakaynaklifaktor8ilacbinlik)
print("2-4 Haftalık plazma kaynaklı faktör-8 besyuzluk:",toplamdorthaftalikplazmakaynaklifaktor8ilacbesyuzluk)
print("3-4 Haftalık plazma kaynaklı faktör-8 ikiyuzellilik:",toplamdorthaftalikplazmakaynaklifaktor8ilacikiyuzellilik)
print("5-4 Haftalık rekombinant faktör-8 binlik:",toplamdorthaftalikrekombinantfaktor8ilacbinlik)
print("6-4 Haftalık rekombinant faktör-8 besyüzlük:",toplamdorthaftalikrekombinantfaktor8ilacbesyuzluk)
print("7-4 Haftalık rekombinant faktör-8 ikiyüzellilik:",toplamdorthaftalikrekombinantfaktor8ilacikiyuzellilik)
print("---------------Faktör-9--------------")
print("1-4 Haftalık plazma kaynaklı faktör-9 binlik:",toplamdorthaftalikplazmakaynaklifaktor9ilacbinlik)
print("2-4 Haftalık plazma kaynaklı faktör-9 besyuzluk:",toplamdorthaftalikplazmakaynaklifaktor9ilacbesyuzluk)
print("3-4 Haftalık plazma kaynaklı faktör-9 ikiyuzellilik:",toplamdorthaftalikplazmakaynaklifaktor9ilacikiyuzellilik)
print("5-4 Haftalık rekombinant faktör-9 binlik:",toplamdorthaftalikrekombinantfaktor9ilacbinlik)
print("6-4 Haftalık rekombinant faktör-9 besyüzlük:",toplamdorthaftalikrekombinantfaktor9ilacbesyuzluk)
print("7-4 Haftalık rekombinant faktör-9 ikiyüzellilik:",toplamdorthaftalikrekombinantfaktor9ilacikiyuzellilik)
print("--------------------------------")
print("SGK’nın karşıladığı 4 haftalık faktör ilacı tutarı:",SGKdorthaftalikilfaktorilactutar)
print("SGK’nın karşıladığı 1 yıllık faktör ilacı tutarı:",SGKbiryillikfaktorilactutar)
print("--------------------------------")
print("SGK’nın profilaksi uygulaması kapsamında ortalama olarak 1 hasta için karşıladığı yıllık toplam ilaç miktarı (ünite):",int(ortalamabirhastaiçinkarsilananyillikilacmiktar))
print("SGK’nın profilaksi uygulaması kapsamında ortalama olarak 1 hasta için karşıladığı yıllık toplam tutar:",ortamalabirhastaicinkarsilananyilliktutar)
print("--------------4 haftalık ilaç kullanım miktarı en çok olan Hemofili-A Hasta bilgileri------------------")
print("1-Hastanın TC kimlik no:",int(ilacmiktarienyuksekhemofiliATC))
print("2-Hastanın Adı-Soyadı:",str(ilacmiktarienyuksekhemofiliAAdSoyad))
print("3-Hastanın hastalık şiddeti:",ilacmiktarienyuksekhemofiliAhastaliksiddet)
print("4-Hastanın kullandığı ilaç türü:",ilacmiktarienyuksekhemofiliAilacturu)
print("5-Hastanın 4 haftalık ilaç kullanım miktarı:",ilacmiktarienyuksekhemofiliA4haftalikilacmiktar)
print("6-Hastanın 4 haftalık ilaç kullanım miktarı tutarı:",ilacmiktarienyuksekhemofiliA4haftalikilactutar)
print("7-Hastanın kilosu:", ilacmiktarienyuksekhemofiliAkilo)
print("--------------4 haftalık ilaç kullanım miktarı en çok olan Hemofili-B Hasta bilgileri------------------")
print("1-Hastanın TC kimlik no:",int(ilacmiktarienyuksekhemofiliBTC))
print("2-Hastanın Adı-Soyadı:",str(ilacmiktarienyuksekhemofiliBAdSoyad))
print("3-Hastanın hastalık şiddeti:",ilacmiktarienyuksekhemofiliBhastaliksiddet)
print("4-Hastanın kullandığı ilaç türü:",ilacmiktarienyuksekhemofiliBilacturu)
print("5-Hastanın 4 haftalık ilaç kullanım miktarı:",ilacmiktarienyuksekhemofiliB4haftalikilacmiktar)
print("6-Hastanın 4 haftalık ilaç kullanım miktarı tutarı:",ilacmiktarienyuksekhemofiliB4haftalikilactutar)
print("7-Hastanın kilosu:", ilacmiktarienyuksekhemofiliBkilo)
print("--------------4 haftalık ilaç tutarı en çok olan hastanın------------------")
print("1-Hastanın TC kimlik no:",int(dorthaftalikilactutariencokhastaSONTC))
print("2-Hastanın Adı-Soyadı:",str(dorthaftalikilactutariencokhastaSONAdSoyad))
print("3-Hastanın kilosu:",dorthaftalikilactutariencokhastaSONkilo)
print("4-Hastanın hastalık tipi:",dorthaftalikilactutariencokhastaSONhastaliktip)
print("5-Hastanın hastalık şiddeti:",dorthaftalikilactutariencokhastaSONsiddet)
print("6-Hastanın kullandığı ilaç türü:",dorthaftalikilactutariencokhastaSONturu)
print("7-Hastanın 4 haftalık ilaç kullanım miktarı:",dorthaftalikilactutariencokhastaSON4haftalikilacmiktar)
print("8-Hastanın 4 haftalık ilaç kullanım miktarı tutarı:",orthaftalikilactutariencokhastaSON4haftalikilactutar)

