#Author of code : ufukatakanyuksel

def menu():
   print("----------MENU----------")
   print("1.Fal Bakma Oyunu")
   print("2. Blackjack (21) Oyunu")
   print("3.Çıkış")

   secim = input("Lütfen oynamak istediğiniz oyunu seçiniz:")
   while(int(secim)!=1 and int(secim)!=2 and int(secim)!=3 ):
       print("Seçiminizi yanlış girdiniz!")
       secim = input("Lütfen oynamak istediğiniz oyunu seçiniz:")

   if (int(secim) == 1):
       falbakmaoyunu(secim)
   elif(int(secim)== 2):
       blackjackoyunu(secim)

def blackjackoyunu(numara):

    while(True):

          kartlar=[ "Kupa As","Karo As","Sinek As","Maça As","Kupa İkili","Karo İkili","Sinek İkili","Maça İkili","Kupa Üçlü","Karo Üçlü","Sinek Üçlü","Maça Üçlü","Kupa Dörtlü","Karo Dörtlü","Sinek Dörtlü","Maça Dörtlü","Kupa Beşli","Karo Beşli","Sinek Beşli","Maça Beşli", "Kupa Altılı","Karo Altılı","Sinek Altılı","Maça Altılı", "Kupa Yedili","Karo Yedili","Sinek Yedili","Maça Yedili","Kupa Sekizli","Karo Sekizli","Sinek Sekizli","Maça Sekizli", "Kupa Dokuzlu","Karo Dokuzlu","Sinek Dokuzlu","Maça Dokuzlu","Kupa Onlu","Karo Onlu","Sinek Onlu","Maça Onlu","Kupa Vale","Karo Vale","Sinek Vale","Maça Vale" ,"Kupa Kız","Karo Kız","Sinek Kız","Maça Kız","Kupa Papaz","Karo Papaz","Sinek Papaz","Maça Papaz"]
          yeni_deste=[]
          numara_liste=[]
          as_ozel_durum_numara_liste=[]
          dagatici_kartlar=[]
          dagatici_kartlar_numara=[]
          oyuncu_kartlar=[]
          oyuncu_kartlar_numara=[]
          oyuncutoplam=0
          oyuncutoplam2=0
          dagaticitoplam=0
          j=1
          k=1
          secim=str
          kazanan=0
          oyuncu_blackjack=0#ikisi de 1'e eşitlenirse şayet aşağıda blackjack yapmış olur ikiside ve bu ikisi eşit ise birbirine oyun berabere diyeceğiz
          dagatici_blackjack=2
          toplamı_21_dagatici=3
          toplamı_21_oyuncu=4
          import random# randomu kullanmak için import

          for i in range(0,52):

              kart=random.choice(kartlar)#burada random olarak tipleri ve sayilarını sectirip kart isimi bir değişkene atadım
              kartlar.remove(kart)# kartlardan seçilen elemanı kaldırdım ki aynı kartı seçmesin iki kere

              if (str(kart)=="Kupa As" or  str(kart)=="Karo As" or str(kart)=="Sinek As" or str(kart)=="Maça As"):# bu if-elif yığınında da işte hangisi geldiyse string şeklindeki sayılardan, numara listemize o string şeklindeki sayının sayısal halini atıyoruz.
                  numara_liste.append(1)
                  as_ozel_durum_numara_liste.append(11)
              elif (str(kart)=="Kupa İkili" or str(kart)=="Karo İkili" or str(kart)=="Sinek İkili" or str(kart)=="Maça İkili"):
                  numara_liste.append(2)
              elif (str(kart)=="Kupa Üçlü" or str(kart)=="Karo Üçlü" or str(kart)=="Sinek Üçlü" or str(kart)=="Maça Üçlü"):
                  numara_liste.append(3)
              elif (str(kart)=="Kupa Dörtlü" or str(kart)=="Karo Dörtlü" or str(kart)=="Sinek Dörtlü" or str(kart)=="Maça Dörtlü"):
                  numara_liste.append(4)
              elif (str(kart)=="Kupa Beşli" or str(kart)=="Karo Beşli" or str(kart)=="Sinek Beşli" or str(kart)=="Maça Beşli"):
                  numara_liste.append(5)
              elif (str(kart)=="Kupa Altılı" or str(kart)=="Karo Altılı" or str(kart)=="Sinek Altılı" or str(kart)=="Maça Altılı"):
                  numara_liste.append(6)
              elif (str(kart)=="Kupa Yedili" or str(kart)=="Karo Yedili" or str(kart)=="Sinek Yedili" or str(kart)=="Maça Yedili"):
                  numara_liste.append(7)
              elif (str(kart)=="Kupa Sekizli" or str(kart)=="Karo Sekizli" or str(kart)=="Sinek Sekizli" or str(kart)=="Maça Sekizli"):
                  numara_liste.append(8)
              elif (str(kart)=="Kupa Dokuzlu" or str(kart)=="Karo Dokuzlu" or str(kart)=="Sinek Dokuzlu" or str(kart)=="Maça Dokuzlu"):
                  numara_liste.append(9)
              elif (str(kart)=="Kupa Onlu" or str(kart)=="Karo Onlu" or str(kart)=="Sinek Onlu" or str(kart)=="Maça Onlu"):
                  numara_liste.append(10)
              elif (str(kart)=="Kupa Vale" or str(kart)=="Karo Vale" or str(kart)=="Sinek Vale" or str(kart)=="Maça Vale"):
                  numara_liste.append(10)
              elif (str(kart)=="Kupa Kız" or str(kart)=="Karo Kız" or str(kart)=="Sinek Kız" or str(kart)=="Maça Kız"):
                  numara_liste.append(10)
              elif (str(kart)=="Kupa Papaz" or str(kart)=="Karo Papaz" or str(kart)=="Sinek Papaz" or str(kart)=="Maça Papaz"):
                  numara_liste.append(10)

              yeni_deste.append(kart)#randon sectirdiğim her kartı atıyorum oluşturdugum desteye


          for i in range(0,2):

              dagaticikart=random.choice(yeni_deste)#dagaticiya destemden random bir kart seciyorum
              dagaticikartindex=yeni_deste.index(dagaticikart)#sonra bu secilen kart kaçıncı sırada bunu bulayım ki sonra numaraları tuttugum listenin o sırasındaki sayı elemanımı senkron sekilde cekebileyim.
              dagatici_kartlar.append(dagaticikart)#sonra bunu dagaticimn kartlarını tutacak olan listeye attım
              dagatici_kartlar_numara.append(numara_liste[dagaticikartindex])#dagaticiya gelen kartların numarasını tutacak listeye, numara listesinin dagaticikartindex'inci indexinde yer alan elemanı attım.Yani mesela karo 5 geldi,karo 5 destede 4. sırada ,yukarda karo 5'e  puan degeri olarak 4. sırada 5 atadık oradan çekeceğiz işte

              #şimdi aynı kartlar gelmesin diye o katları ve numaraları kaldıralım
              yeni_deste.remove(dagaticikart)#desteden o seçilen kartı kaldırdık
              numara_liste.pop(dagaticikartindex)#numaraları tutan desteden de o kart kacıncı indexte ise numaralar listesindeki o indexin içeriğini çıkardık.yani sayısal karşılıgını

              #Şimdi oyuncu için aynı mantığı kullanacağı aşağıda
              oyuncukart=random.choice(yeni_deste)
              oyuncukartindex=yeni_deste.index(oyuncukart)
              oyuncu_kartlar.append(oyuncukart)
              oyuncu_kartlar_numara.append(numara_liste[oyuncukartindex])

              yeni_deste.remove(oyuncukart)
              numara_liste.pop(oyuncukartindex)

          print("Dağatıcının açık kartı:",dagatici_kartlar[0])

        #Şimdi aşagıdaki if-elif-else kombinasyonunda dagatıcıya gelen ilk iki kart toplamlarını oyun şartlarına uygun senkronize edecegiz.
          if (dagatici_kartlar[0]=="Kupa As" or  dagatici_kartlar[0]=="Karo As" or dagatici_kartlar[0]=="Sinek As" or dagatici_kartlar[0]=="Maça As"):

              if(dagatici_kartlar[1]=="Kupa As" or  dagatici_kartlar[1]=="Karo As" or dagatici_kartlar[1]=="Sinek As" or dagatici_kartlar[1]=="Maça As"):
                  dagaticitoplam=1+1 #dagatıcıya ikiside as gelirse 22 eder.geçiyor 21'i. 1 olarak alırız ikisini de bu yuzden
              else:
                  dagaticitoplam=11+dagatici_kartlar_numara[1]#eger ilk kart as diğeri değilse normal as 11olarak aldık
                  if(dagaticitoplam==21):
                      #print("Dagatici Blackjack yaptı.")
                      dagatici_blackjack=1

          elif (dagatici_kartlar[1]=="Kupa As" or  dagatici_kartlar[1]=="Karo As" or dagatici_kartlar[1]=="Sinek As" or dagatici_kartlar[1]=="Maça As"):
                  dagaticitoplam=11+dagatici_kartlar_numara[0]#listemizin ikinci kartı as gelirse 11 alıyoruz toplarken.Zaten ilk eleman da 0 gelince 1+1'i yukarısı yapıyor diye burada kontrol etmedik
                  if(dagaticitoplam==21):
                      #print("Dagatici Blackjack yaptı.")
                      dagatici_blackjack=1
          else:
              dagaticitoplam=dagatici_kartlar_numara[0]+dagatici_kartlar_numara[1]#eger as gelmediyse ele direk normal topla




         #Şimdi aşağıda,oyuncu için yapacağız uygun senkronizasyonu
          if (oyuncu_kartlar[0]=="Kupa As" or  oyuncu_kartlar[0]=="Karo As" or oyuncu_kartlar[0]=="Sinek As" or oyuncu_kartlar[0]=="Maça As"):

              if (oyuncu_kartlar[1]=="Kupa As" or  oyuncu_kartlar[1]=="Karo As" or oyuncu_kartlar[1]=="Sinek As" or oyuncu_kartlar[1]=="Maça As"):
                  oyuncutoplam=11+1#oyuncu için asları avantajlı olacak şekilde aldık.
                  oyuncutoplam2=1+1#Mesela 3 As geldi ilk el sonra bi de 10'lu gelirse eder toplam 22 aşar.Oyuncu için avantajsız olur o durum olursa.Bunu o yuzden ekledik o durum olabilir diye.
              else:
                  oyuncutoplam=11+oyuncu_kartlar_numara[1]
                  oyuncutoplam2=1+oyuncu_kartlar_numara[1]# ilerde çekeceğimiz 3.karta göre As değerini 1'li şekliyle de alabiliriz
                  if(oyuncutoplam==21):
                      print("Oyuncunun kartları:",oyuncu_kartlar[0],",",oyuncu_kartlar[1],"(BlackJack)")
                      print("Oyuncu Blackjack yaptı.")
                      oyuncu_blackjack=1
                      print("Sıra dagatıcıdaa.")
                      break
              print("Oyuncunun kartları:",oyuncu_kartlar[0],",",oyuncu_kartlar[1],"( Toplam",oyuncutoplam,"ya da",oyuncutoplam2,")")
              secim=input("(K)ağıt mı, (P)as mı?:")


          elif(oyuncu_kartlar[1]=="Kupa As" or  oyuncu_kartlar[1]=="Karo As" or oyuncu_kartlar[1]=="Sinek As" or oyuncu_kartlar[1]=="Maça As"):

              oyuncutoplam=11+oyuncu_kartlar_numara[0]
              oyuncutoplam2=1+oyuncu_kartlar_numara[0]
              if(oyuncutoplam==21):
                    print("Oyuncunun kartları:",oyuncu_kartlar[0],",",oyuncu_kartlar[1],"(BlackJack)")
                    print("Oyuncu Blackjack yaptı.")
                    oyuncu_blackjack=1
                    print("Sıra dagaticida.")
                    break

              print("Oyuncunun kartları:",oyuncu_kartlar[0],",",oyuncu_kartlar[1],"( Toplam",oyuncutoplam,"ya da",oyuncutoplam2,")")
              secim=input("(K)ağıt mı, (P)as mı?:")

          else:
              oyuncutoplam=oyuncu_kartlar_numara[0]+oyuncu_kartlar_numara[1]
              print("Oyuncunun kartları:",oyuncu_kartlar[0],",",oyuncu_kartlar[1],"( Toplam:",oyuncutoplam,")")
              secim=input("(K)ağıt mı, (P)as mı?:")


          while(str(secim)=="K"):

                  oyuncukart=random.choice(yeni_deste)
                  oyuncukartindex=yeni_deste.index(oyuncukart)
                  oyuncu_kartlar.append(oyuncukart)
                  oyuncu_kartlar_numara.append(numara_liste[oyuncukartindex])

                  yeni_deste.remove(oyuncukart)
                  numara_liste.pop(oyuncukartindex)
                  j=j+1#mesela 3.bir kart eklendi ya,2. index lazım olacak bize toplarken oyuncu kart değerlerini ondan j kullandım.


                  if(oyuncu_kartlar[j]!="Kupa As" or  oyuncu_kartlar[j]!="Karo As" or oyuncu_kartlar[j]!="Sinek As" or oyuncu_kartlar[j]!="Maça As"):


                        if(oyuncu_kartlar_numara[0]==1 and oyuncu_kartlar_numara[1]==1):#Mesela iki tane As gelirse ilk kağıtlar olarak oyuncuya buraya girsin istiyoruz

                            if(int(oyuncutoplam+oyuncu_kartlar_numara[j])<21):#şimdi ya 12 ya 2 alınıyordu yaibaktık 12 alındığı halde ilk,gelen yeni kartla toplanınca hala küçükse buna girsin ve oyuncutoplamı yani büyük olanı seçerek işlem yapsın
                               print("Oyuncunun kartları:",oyuncu_kartlar,"( Toplam",oyuncutoplam+oyuncu_kartlar_numara[j],")")
                               oyuncutoplam=oyuncutoplam+oyuncu_kartlar_numara[j]
                               secim=input("(K)ağıt mı, (P)as mı?:")
                               if(str(secim)=="P"):
                                  print("Oyuncu puanı:",oyuncutoplam)# oyuncutoplam+ 'lı olanı aldık çünku oyuncutoplam bizim büyük olanımız.Oyuncu için avantajı göz önünde bulundurduk
                                  print("Sıra dagatıcıda.")
                                  break

                            elif(int(oyuncutoplam+oyuncu_kartlar_numara[j])>21):#mesela 12 ya da 2,burada 12 secik,10 gelirse 22 eder oyuncu batar.Oyuncunun avantajını düşünüyorduk,10 gelirse 2 seçilmesini sağlıyotuz burda
                               if(oyuncutoplam2+oyuncu_kartlar_numara[j]<21):#msela AS-AS-SEKİZ geldi=20,bir daha kağat  istediğimde AS+AS+SEKiz =10 etmeli oyuncu avantajı  için.
                                 print("Oyuncunun kartları:",oyuncu_kartlar)
                                 print("Oyuncu puanı:",oyuncutoplam2+oyuncu_kartlar_numara[j])#oyuncutoplamı2 ile toplamamız gerek 21'i aştığı için
                                 oyuncutoplam=oyuncutoplam2+oyuncu_kartlar_numara[j]#oyuncunun kart toplamını da ona göre güncelledik
                                 secim=input("(K)ağıt mı, (P)as mı?:")
                                 if(str(secim)=="P"):
                                    print("Oyuncu puanı:",oyuncutoplam)# oyuncutoplam+ 'lı olanı aldık çünku oyuncutoplam bizim büyük olanımız.Oyuncu için avantajı göz önünde bulundurduk
                                    print("Sıra dagatıcıda.")
                                    break

                            elif(int(oyuncutoplam+oyuncu_kartlar_numara[j])==21):
                               print("Oyuncunun kartları:",oyuncu_kartlar,"( Toplam",oyuncutoplam+oyuncu_kartlar_numara[j])
                               print("Sıra dağatıcıya geçiyor.")
                               toplamı_21_oyuncu=1
                               break


                        elif(oyuncu_kartlar_numara[0]==1 or oyuncu_kartlar_numara[1]==1):#herhangi bir oyuncu ilk kağıdı As ise buraya girsin.

                            if(int(oyuncutoplam+oyuncu_kartlar_numara[j])<21):
                                print("Oyuncunun kartları:",oyuncu_kartlar,"( Toplam",oyuncutoplam+oyuncu_kartlar_numara[j],"ya da",oyuncutoplam2+oyuncu_kartlar_numara[j],")")
                                oyuncutoplam=oyuncutoplam+oyuncu_kartlar_numara[j]
                                if(oyuncutoplam>21):
                                    print("Oyuncunun kartları:",oyuncu_kartlar,"( Toplam",oyuncutoplam2+oyuncu_kartlar_numara[j],")")#mesela toplam 25 ya da 15 geldi ya.25'i saf dışı bırakıyoruz.
                                    oyuncutoplam=oyuncutoplam2+oyuncu_kartlar_numara[j]
                                secim=input("(K)ağıt mı, (P)as mı?:")
                                if(str(secim)=="P"):
                                   print("Oyuncu puanı:",oyuncutoplam)# oyuncutoplam+ 'lı olanı aldık çünku oyuncutoplam bizim büyük olanımız.Oyuncu için avantajı göz önünde bulundurduk
                                   print("Sıra dagatıcıda.")
                                   break

                            elif(int(oyuncutoplam+oyuncu_kartlar_numara[j])>21):

                                if(oyuncutoplam2+oyuncu_kartlar_numara[j]<21):#mesela As ve 9lu geldi.Toplam 20 ya da 10.eğer sıradaki kağat mesela 9-10 gibi büyük gelirse oyuncu için As'ı 1 seçsin.Burda bunu yaptırıyoruz.
                                    print("Oyuncunun kartları:",oyuncu_kartlar,"( Toplam",oyuncutoplam2+oyuncu_kartlar_numara[j],")")
                                    oyuncutoplam2=oyuncutoplam2+oyuncu_kartlar_numara[j]
                                    oyuncutoplam=oyuncutoplam2
                                    secim=input("(K)ağıt mı, (P)as mı?:")
                                    if(str(secim)=="P"):
                                      print("Oyuncu puanı:",oyuncutoplam2)# oyuncutoplam+ 'lı olanı aldık çünku oyuncutoplam bizim büyük olanımız.Oyuncu için avantajı göz önünde bulundurduk
                                      print("Sıra dagatıcıda.")
                                      break
                                elif(oyuncutoplam2+oyuncu_kartlar_numara[j]>21):
                                    print("Oyuncunun kartları:",oyuncu_kartlar,"( ToplamM",oyuncutoplam2+oyuncu_kartlar_numara[j],")")
                                    print("Oyuncu puanı:",oyuncutoplam+oyuncu_kartlar_numara[j])# oyuncutoplam+ 'lı olanı aldık çünku oyuncutoplam bizim büyük olanımız.Oyuncu için avantajı göz önünde bulundurduk
                                    print("Oyuncu kaybetti.")

                                    kazanan=1 #kazanan 1 ise eğer dağatıcı oluyor aşağıdaki dagatıcının kar cektiği while'e hiç girmiyor.
                                    break

                            elif(int(oyuncutoplam+oyuncu_kartlar_numara[j])==21):
                                print("Oyuncunun kartları:",oyuncu_kartlar,"( Toplam",oyuncutoplam+oyuncu_kartlar_numara[j],")")
                                print("Sıra dağatıcıya geçiyor.")
                                toplamı_21_oyuncu=1
                                break



                        if(int(oyuncutoplam+oyuncu_kartlar_numara[j])<21):
                            print("Oyuncunun kartları:",oyuncu_kartlar,"( Toplam",oyuncutoplam+oyuncu_kartlar_numara[j],")")
                            oyuncutoplam=oyuncutoplam+oyuncu_kartlar_numara[j]
                            secim=input("(K)ağıt mı, (P)as mı?:")
                            if(str(secim)=="P"):
                               print("Oyuncu puanı:",oyuncutoplam)# oyuncutoplam+ 'lı olanı aldık çünku oyuncutoplam bizim büyük olanımız.Oyuncu için avantajı göz önünde bulundurduk
                               print("Sıra dagatıcıda.")
                               break

                        elif(int(oyuncutoplam+oyuncu_kartlar_numara[j])>21):
                            print("Oyuncunun kartları:",oyuncu_kartlar)
                            print("Oyuncu puanı:",oyuncutoplam+oyuncu_kartlar_numara[j])# oyuncutoplam+ 'lı olanı aldık çünku oyuncutoplam bizim büyük olanımız.Oyuncu için avantajı göz önünde bulundurduk
                            print("Oyuncu kaybetti.")
                            print("Kazanan dağatıcı")
                            kazanan=1 #kazanan 1 ise eğer dağatıcı oluyor aşağıdaki dagatıcının kar cektiği while'e hiç girmiyor.
                            break

                        elif(int(oyuncutoplam+oyuncu_kartlar_numara[j])==21):
                            print("Oyuncunun kartları:",oyuncu_kartlar,"( Toplam",oyuncutoplam+oyuncu_kartlar_numara[j])
                            print("Sıra dağatıcıya geçiyor.")
                            toplamı_21_oyuncu=1
                            break



                    #----------------------------------------------------------------

                  elif(oyuncu_kartlar[j]=="Kupa As" or  oyuncu_kartlar[j]=="Karo As" or oyuncu_kartlar[j]=="Sinek As" or oyuncu_kartlar[j]=="Maça As"):#mesela sıradaki kağıt as gelirse.




                      if(int(oyuncutoplam+11)<21):#11 secersek As'ı ne olur diye durumlara bakıyoruz
                          print("Oyuncunun kartları:",oyuncu_kartlar,"( Toplam",oyuncutoplam+11,")")
                          oyuncutoplam=oyuncutoplam+11
                          secim=input("(K)ağıt mı, (P)as mı?:")
                          if(str(secim)=="P"):
                             print("Oyuncu puanı:",oyuncutoplam)# oyuncutoplam+ 'lı olanı aldık çünku oyuncutoplam bizim büyük olanımız.Oyuncu için avantajı göz önünde bulundurduk
                             print("Sıra dagatıcıda.")
                             break

                      elif(int(oyuncutoplam+11)>21):
                          print("Oyuncunun kartları:",oyuncu_kartlar,"( Toplam",oyuncutoplam+1,")")
                          oyuncutoplam=oyuncutoplam+1#oyuncu toplamımızı güncellemeliyiz
                          secim=input("(K)ağıt mı, (P)as mı?:")
                          if(str(secim)=="P"):
                              print("Oyuncu puanı:",oyuncutoplam)# oyuncutoplam+ 'lı olanı aldık çünku oyuncutoplam bizim büyük olanımız.Oyuncu için avantajı göz önünde bulundurduk
                              print("Sıra dagatıcıda.")
                              break

                      elif(int(oyuncutoplam+11)==21):
                          print("Oyuncunun kartları:",oyuncu_kartlar,"( Toplam",oyuncutoplam+11)
                          print("Sıra dağatıcıya geçiyor.")
                          toplamı_21_oyuncu=1
                          break






          print("Dağatıcının kartları:",dagatici_kartlar[0],",",dagatici_kartlar[1],"(Toplam ",dagaticitoplam,")")

          if(dagaticitoplam==21):
              print("Dagatici Blackjack yaptı.")
              dagatici_blackjack=1
              print("Kazanan dagatici.")
              kazanan=1
              break

          while(kazanan!=1 or str(secim)=="P" or oyuncu_blackjack==1):#direk kazanan dağatıcı değilse sıra dagatıcıya geciyor burada.

                  dagaticikart=random.choice(yeni_deste)#dagaticiya destemden random bir kart seciyorum
                  dagaticikartindex=yeni_deste.index(dagaticikart)#sonra bu secilen kart kaçıncı sırada bunu bulayım ki sonra numaraları tuttugum listenin o sırasındaki sayı elemanımı senkron sekilde cekebileyim.
                  dagatici_kartlar.append(dagaticikart)#sonra bunu dagaticimn kartlarını tutacak olan listeye attım
                  dagatici_kartlar_numara.append(numara_liste[dagaticikartindex])#dagaticiya gelen kartların numarasını tutacak listeye, numara listesinin dagaticikartindex'inci indexinde yer alan elemanı attım.Yani mesela karo 5 geldi,karo 5 destede 4. sırada ,yukarda karo 5'e  puan degeri olarak 4. sırada 5 atadık oradan çekeceğiz işte

                  #şimdi aynı kartlar gelmesin diye o katları ve numaraları kaldıralım
                  yeni_deste.remove(dagaticikart)#desteden o seçilen kartı kaldırdık
                  numara_liste.pop(dagaticikartindex)
                  k=k+1

                  if(dagatici_kartlar[k]!="Kupa As" or  dagatici_kartlar[k]!="Karo As" or dagatici_kartlar[k]!="Sinek As" or dagatici_kartlar[k]!="Maça As"):

                      if(int(dagaticitoplam+dagatici_kartlar_numara[k])<21):
                          print("Dagatıcının kartları:",dagatici_kartlar,"( Toplam",dagaticitoplam+dagatici_kartlar_numara[k],")")
                          dagaticitoplam=dagaticitoplam+dagatici_kartlar_numara[k]



                      elif(int(dagaticitoplam+dagatici_kartlar_numara[k])>21):
                          print("Dagatıcının kartları:",dagatici_kartlar)
                          print("Dagatıcı puanı:",dagaticitoplam+dagatici_kartlar_numara[k])# oyuncutoplam+ 'lı olanı aldık çünku oyuncutoplam bizim büyük olanımız.Oyuncu için avantajı göz önünde bulundurduk
                          print("Dagatıcı battı.")
                          print("Oyunu Oyuncu kazandı.")
                          break

                      elif(int(dagaticitoplam+dagatici_kartlar_numara[k])==21):
                          print("Dagaticinin kartları:",dagatici_kartlar,"( Toplam",dagaticitoplam+dagatici_kartlar_numara[k],")")
                          toplamı_21_dagatici=1
                          if(toplamı_21_dagatici==1 and toplamı_21_oyuncu!=1):#eger dagatici 21'i bulup,oyuncu bulamadıysa dğatıcı kazanmalı
                              print("Dağatici oyunu kazandı.")
                          break



                  elif(dagatici_kartlar[k]=="Kupa As" or  dagatici_kartlar[k]=="Karo As" or dagatici_kartlar[k]=="Sinek As" or dagatici_kartlar[k]=="Maça As"):


                      if(int(dagaticitoplam+11)<21):#As 11 olarak alıyorduk ya hep dagatıcı için,işte 11 alındıgı halde hala küçük kalıyorsa 11 al tolarken As'ı
                          print("Dagatıcının kartları:",dagatici_kartlar,"( Toplam",dagaticitoplam+11,")")
                          dagaticitoplam=dagaticitoplam+11
                          break


                      elif(int(dagaticitoplam+11)>21):#As 11 alınık iken 21'de büyük çıkarsa dağatıcı için As'ı 1 alıyorduk
                          print("Dagatıcının kartları:",dagatici_kartlar,"( Toplam",dagaticitoplam+1,")")
                          print("Dagatıcı puanı:",dagaticitoplam+1)#Dagatıcıya yeni gelen kart As ise ve toplamı 21'i geçiyorsa As=1 plarak alacağız
                          dagaticitoplam=dagaticitoplam+1
                          break

                      elif(int(dagaticitoplam+11==21)):
                          print("Dagaticinin kartları:",dagatici_kartlar,"( Toplam",dagaticitoplam+11,")")
                          toplamı_21_dagatici=1
                          break


          if(oyuncu_blackjack==dagatici_blackjack):
              print("İki taraf da blackjack yaptı.")
              print("Oyun berabere.")

          elif(oyuncu_blackjack==1 and dagatici_blackjack!=1 and toplamı_21_dagatici==21):
              print("Oyuncu blackjack yaptığı için kazandı.")
              print("Dagaticinin kartlar toplami:21")
          elif(oyuncu_blackjack!=1 and dagatici_blackjack==1 and toplamı_21_oyuncu==21):
              print("Dagatici blackjack yaptığı için kazandı.")
              print("Oyuncunun kartlar toplami:21")
          elif(toplamı_21_oyuncu==toplamı_21_dagatici):
              print("Eldeki sayılar tolamı 21 oldu iki oyuncunun.")
              print("Oyun berabere.")
          elif(toplamı_21_dagatici==21 and toplamı_21_oyuncu!=21):
              print("Oyunu dagatici kazandı.")

          tekraroyun=input("Tekrar oynamak istiyor musunuz?(E/H):")

          while(str(tekraroyun)!="E" and str(tekraroyun)!="e" and str(tekraroyun)!="H" and str(tekraroyun)!="h"):
             print("Hatalı harf girişi!!")
             tekraroyun=input("Tekrar oynamak istiyor musunuz?(E/H):")
          if(str(tekraroyun)=="H" or str(tekraroyun)=="h"):
             menu()
             break


def falbakmaoyunu(numara):

  niyettutma = input("Niyetinizi tuttunuz mu?(e/h):")#Projede herkes kendi çıktı fortmatını oluşturabilir denmiş.Ben de asagida kartlistesi olarak bir örnek kart destesi çıktı formatı oluşturup o kart destesi örneği üzerinden simülasyonu tasarladım. Anladığım bu olduğu için random şekilde tasarlanmadım desteyi,örnek bir deste formatı üzerinden gösteriliyor bu nedenle çalıma.

  if(niyettutma == "e"):

    while(True):

       kartlar=[ "Kupa As","Karo As","Sinek As","Maça As","Kupa İkili","Karo İkili","Sinek İkili","Maça İkili","Kupa Üçlü","Karo Üçlü","Sinek Üçlü","Maça Üçlü","Kupa Dörtlü","Karo Dörtlü","Sinek Dörtlü","Maça Dörtlü","Kupa Beşli","Karo Beşli","Sinek Beşli","Maça Beşli", "Kupa Altılı","Karo Altılı","Sinek Altılı","Maça Altılı", "Kupa Yedili","Karo Yedili","Sinek Yedili","Maça Yedili","Kupa Sekizli","Karo Sekizli","Sinek Sekizli","Maça Sekizli", "Kupa Dokuzlu","Karo Dokuzlu","Sinek Dokuzlu","Maça Dokuzlu","Kupa Onlu","Karo Onlu","Sinek Onlu","Maça Onlu","Kupa Vale","Karo Vale","Sinek Vale","Maça Vale" ,"Kupa Kız","Karo Kız","Sinek Kız","Maça Kız","Kupa Papaz","Karo Papaz","Sinek Papaz","Maça Papaz"]
       yeni_deste=[]
       numara_liste=[]
       sona_eklenecek_kartlar=[] #Bunu , mesela eşleşme oldu ya eşleşme olana kadar çıkan kartları içine atmak için tasarladım.Sonra deste sonuna ekleyelim diye.
       puan_kartlar=[] #puan olacak kartlarımı tutacağım
       puan_kartlar_sayilari=[]#Puan olarak alınan kartların sayısal olarak degerlerini tutacak
       sona_eklenecek_numara=[]# burda da mesela destenin sonuna kart ekliyoruz ya o ana kadar cıkan kartların numarasını tutup numara listemin sonuna ekleyecegim
       son_eleman=str
       kirildi=0#adım adım dögüden çıkış için kullanacağım
       import random# randomu kullanmak için import

       for i in range(0,52):

           kart=random.choice(kartlar)#burada random olarak tipleri ve sayilarını sectirip kart isimi bir değişkene atadım
           kartlar.remove(kart)# kartlardan seçilen elemanı kaldırdım ki aynı kartı seçmesin iki kere

           if (str(kart)=="Kupa As" or  str(kart)=="Karo As" or str(kart)=="Sinek As" or str(kart)=="Maça As"):# bu if-elif yığınında da işte hangisi geldiyse string şeklindeki sayılardan, numara listemize o string şeklindeki sayının sayısal halini atıyoruz.
               numara_liste.append(1)
           elif (str(kart)=="Kupa İkili" or str(kart)=="Karo İkili" or str(kart)=="Sinek İkili" or str(kart)=="Maça İkili"):
               numara_liste.append(2)
           elif (str(kart)=="Kupa Üçlü" or str(kart)=="Karo Üçlü" or str(kart)=="Sinek Üçlü" or str(kart)=="Maça Üçlü"):
               numara_liste.append(3)
           elif (str(kart)=="Kupa Dörtlü" or str(kart)=="Karo Dörtlü" or str(kart)=="Sinek Dörtlü" or str(kart)=="Maça Dörtlü"):
               numara_liste.append(4)
           elif (str(kart)=="Kupa Beşli" or str(kart)=="Karo Beşli" or str(kart)=="Sinek Beşli" or str(kart)=="Maça Beşli"):
               numara_liste.append(5)
           elif (str(kart)=="Kupa Altılı" or str(kart)=="Karo Altılı" or str(kart)=="Sinek Altılı" or str(kart)=="Maça Altılı"):
               numara_liste.append(6)
           elif (str(kart)=="Kupa Yedili" or str(kart)=="Karo Yedili" or str(kart)=="Sinek Yedili" or str(kart)=="Maça Yedili"):
               numara_liste.append(7)
           elif (str(kart)=="Kupa Sekizli" or str(kart)=="Karo Sekizli" or str(kart)=="Sinek Sekizli" or str(kart)=="Maça Sekizli"):
               numara_liste.append(8)
           elif (str(kart)=="Kupa Dokuzlu" or str(kart)=="Karo Dokuzlu" or str(kart)=="Sinek Dokuzlu" or str(kart)=="Maça Dokuzlu"):
               numara_liste.append(9)
           elif (str(kart)=="Kupa Onlu" or str(kart)=="Karo Onlu" or str(kart)=="Sinek Onlu" or str(kart)=="Maça Onlu"):
               numara_liste.append(10)
           elif (str(kart)=="Kupa Vale" or str(kart)=="Karo Vale" or str(kart)=="Sinek Vale" or str(kart)=="Maça Vale"):
               numara_liste.append(11)
           elif (str(kart)=="Kupa Kız" or str(kart)=="Karo Kız" or str(kart)=="Sinek Kız" or str(kart)=="Maça Kız"):
               numara_liste.append(12)
           elif (str(kart)=="Kupa Papaz" or str(kart)=="Karo Papaz" or str(kart)=="Sinek Papaz" or str(kart)=="Maça Papaz"):
               numara_liste.append(13)

           yeni_deste.append(kart)#randon sectirdiğim her kartı atıyorum oluşturdugum desteye



       k=0#k ekledik,çünkü mesela ilk destede eşleşti herşey tamam ikinci destede eslesme olursa hata veriyor,çünkü yeni desteden ikinci seferde de ilk eşleşmenin ilk elemanı silinmeye çalışılıyor.mesela puan tablosunun k=0. elemanı silinecek ilk eşleşmede,ikici bir eşleşmede k artacak o if içinde bu kez puan kartının 1.elemanı yani k=1 silinecek böyle böyle...
       toplam_puan=0 #toplam puanı tutacağım

       while(True):

           if(kirildi==1):
               break

           for i in range(0,13):

               if( yeni_deste[i-1]==son_eleman):
                  print("Bitti,toplam puanınız:",toplam_puan)
                  print("Niyetiniz %",toplam_puan,"ihtimalle gerçekleşecek.")
                  kirildi=1 #eğer kirildi 1 ise üsteki while da kir dedim burada
                  break


               sona_eklenecek_kartlar.append(yeni_deste[i]) # ekliyoruz buraya eşleşir ihtimaline karşı.Eğer eşleşme olursa i-1 elemana kadar olanları alıp deste listemin sonuna ekleyeceğim. i. elemanı da puan diye ayıracagız,işte eşleşen elemanı yani.
               sona_eklenecek_numara.append(numara_liste[i])#işte burada o ana kadar çıkan kartların integer degerleriini bu listeye yazdım.aşagıda sıfırlayır eşlesme oldugunda güncelleyecegiz

               if(numara_liste[i]==i+1):# eşlesme olursa..
                   print(i+1,".",yeni_deste[i],"Eşleşti,saymaya yeniden başlanıyor...")
                   eslesme=1

                   for j in range(0,i): # j koyduk karışmasın diye. 0 dan i'ye kadar olan elemanlarımızı ilk kaldırıp sonra sonuna eklicez destenin
                       yeni_deste.remove(sona_eklenecek_kartlar[j]) # o index'te yazan elemanı aldık
                       numara_liste.remove(sona_eklenecek_numara[j]) # sayı karşılıklarını tutuyor oldugum listeden de o ana kadar çıkan kartlar kadar elemanı çıkardık.Tabii sayısal hallerini tutan liste bunlar

                       yeni_deste.append(sona_eklenecek_kartlar[j])# bastan kaldırdığım elemanı extend ile sona ekledim
                       numara_liste.append(sona_eklenecek_numara[j])# bastan kaldırdığım sayı seklindeki elemanımı extend ile sona ekledim


                   puan_kartlar.append(yeni_deste[0])# artık yeni destenin ilk elemanı eşleşen kartımız.Önce bunu puan kartı listesine ekleyip..(1)
                   puan_kartlar_sayilari.append(numara_liste[0])# numara versiyonlarını da aynı mantıkla.eslesen ilk numara eemanımızıouan karlar sayı versiyonu listesine ekleyip....(2)

                   toplam_puan=toplam_puan+puan_kartlar_sayilari[k]

                   yeni_deste.remove(puan_kartlar[k])#...sonra destemizden çıkararak o puan kartımızı da destemizi de güncellenmiş olarak puan kartı çıkmış olan destemle işe devam ediyorum.(1)
                   numara_liste.remove(puan_kartlar_sayilari[k])#....sonra numara versiyonu destemizden çıkararak o puan kartı numara versiyon elemanı, destemiz güncellenmiş olarak işe devam ediyorum.

                   k=k+1

                   break

               print(i+1,".",yeni_deste[i])
               devam=input()
               eslesme = 0

               if(len(yeni_deste)<13 and eslesme!=1):# 13 ten küçük ve eşleşme artık olmuyorsa buraya girdik
                   son_eleman=yeni_deste[len(yeni_deste)-1]



               if (i==12):
                   for j in range(0,13):
                       yeni_deste.remove(sona_eklenecek_kartlar[j])# sona_eklenecek_kart listemizi burda da kullanabiliriz.Zaten o 13 kartı tutacak her türlüsadece yukardaki if sağlandıgında o ana kadar tuttugu kartlar oluyor içinde o ife girdiginde.
                       numara_liste.remove(sona_eklenecek_numara[j])


           sona_eklenecek_kartlar[:]=[]# daha sonra sona eklenecek kartlar listemin tüm elemanlarını while döngüsüne tekrar giderken 0'ladım ki diğer silinen elemanları tutmaya devam etmesin.Yeni bir 13'lük tutsun.
           sona_eklenecek_numara[:]=[]# Sıfırladık işte forda işimiz bitince yine kartlardaki mantıkla



       tekraroyun=input("Tekrar oynamak istiyor musunuz?(E/H):")

       while(str(tekraroyun)!="E" and str(tekraroyun)!="e" and str(tekraroyun)!="H" and str(tekraroyun)!="h"):
          print("Hatalı harf girişi!!")
          tekraroyun=input("Tekrar oynamak istiyor musunuz?(E/H):")
       if(str(tekraroyun)=="H" or str(tekraroyun)=="h"):
          menu()
          break

  else:
    menu()#direk niyette hayır derse menuye atsın.

print("----------MENU----------")
print("1.Fal Bakma Oyunu")
print("2. Blackjack (21) Oyunu")
print("3.Çıkış")

secim = input("Lütfen oynamak istediğiniz oyunu seçiniz:")
while(int(secim)!=1 and int(secim)!=2 and int(secim)!=3 ):
     print("Seçiminizi yanlış girdiniz!")
     secim = input("Lütfen oynamak istediğiniz oyunu seçiniz:")
if (int(secim) == 1):
     falbakmaoyunu(secim)

elif(int(secim)== 2):
    blackjackoyunu(secim)









