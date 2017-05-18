#include <stdio.h>
#include <stdlib.h>

int main()
{
   int bilyesayisi,yeni_bilye_sayisi=0,i,j,agirlik1,agirlik3,agirlik2,agirlik4,hatalikutusay=0,iadebilyesayisi=0,kabuledilenbiylesayisi=0,birbilye_daha_agir_olan_kutusay=0,birbilye_daha_hafif_olan_kutusay=0;
    int farkliagirlik=0,devamliagirlik=0,devamliagirlik2=0,devamliagirlik3=0,tumbilyeleresitagirlikkutusu=0,birbilyeagirlikfarklikutusu=0;
     int en_agir_tumbilyeleresitagirlikkutusu=0,en_hafif_agirlik=0,en_hafif_agirlik_olan_kutu_birbilye_agirlik=0,en_hafif_agirlik_olan_kutu_bilyesay=0,en_cok_tumbilyeleresitagirlikkutusu_bilyesay=0,en_cok_tumbilyeleresitagirlikkutusu_bilyesay_birbilye_agirlik=0;
    char secim;
    float hatalikutuyuzde,hatasizkutusay=0,float_tanimli_agirlik3=0,float_tanimli_agirlik1=0,float_tanimli_agirlik2=0,geciciagirlik1=0,geciciagirlik2=0,tekseferlikagirlik=0,tekseferlikagirlik2=0,agir_olan_bilyeler_yuzdeleri_toplami_ort=0,hafif_olan_bilyeler_yuzdeleri_toplami_ort=0,agir_olan_bilyeler_fark_degerleri_ort=0,hafif_olan_bilyeler_fark_degerleri_ort=0,agir_olan_bilyeler_fark_degerleri=0,hafif_olan_bilyeler_fark_degerleri=0,hafif_olan_bilye_yuzdesi=0,agir_olan_bilye_yuzdesi=0,agir_olan_bilyeler_yuzdeleri_toplami=0;
    float hafif_olan_bilyeler_yuzdeleri_toplami=0,toplamhatasizkutusay=0,kutusayisi=0,tumbilyeleresitagirlikyuzde=0,birbilyedahaagiryuzde=0,birbilyedahahafifyuzde=0;
    float birkutu_ici_bilyeler_agirliklari_farki_hafif=0,birkutu_ici_bilyeler_agirliklari_farki_agir=0,elde_birkutu_ici_bilyeler_agirliklari_farki_hafif=0,elde_birkutu_ici_bilyeler_agirliklari_farki_agir=0;
    float hafif_fark_degerinin_en_buyuk_oldugu_deger=0,agir_fark_degerinin_en_buyuk_oldugu_deger=0,hafif_fark_degerinin_en_buyuk_oldugu_deger_yuzde=0,agir_fark_degerinin_en_buyuk_oldugu_deger_yuzde=0;
    float hafif_fark_degerinin_en_buyuk_oldugu_yuzde=0,agir_fark_degerinin_en_buyuk_oldugu_yuzde=0;
    do{

      printf("Bir kutu icersindeki bilye sayisini giriniz:");
         scanf("%d",&bilyesayisi);
     while(bilyesayisi<10)
     {
            printf("Hatali bilye sayisi girisi.\n");

              printf("Bir kutu icersindeki bilye sayisini giriniz:");
              scanf("%d",&bilyesayisi);
     }

        kutusayisi++;

          printf("\n1.bilyenin miligram cinsinden agirligi giriniz:");
           scanf("%d",&agirlik1);

  while(agirlik1<=0)
         {
           printf("Hatali agirlik sayisi girisi.");
           printf("\n1.bilyenin miligram cinsinden agirligi giriniz:");
           scanf("%d",&agirlik1);

         }


           printf("\n2.bilyenin miligram cinsinden agirligi giriniz:");//Kontrolleri yapttirdim buralarda.Agirliga negetif deger girilemesin diye.
            scanf("%d",&agirlik2);
         while(agirlik2<=0)
            {
              printf("Hatali agirlik sayisi girisi.");
              printf("\n2.bilyenin miligram cinsinden agirligi giriniz:");
              scanf("%d",&agirlik2);

            }



                     for(i=3;i<=bilyesayisi;i++)
                     {

                         printf("\n%d.bilyenin miligram cinsinden agirligi giriniz:",i);
                          scanf("%d",&agirlik3);
                           while(agirlik3<=0)
                                {
                                    printf("Hatali agirlik sayisi girisi.");
                                   printf("\n%d.bilyenin miligram cinsinden agirligi giriniz:",i);
                                    scanf("%d",&agirlik3);

                                }

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        /*If 1*/          if(agirlik3==agirlik1 && agirlik3==agirlik2 && agirlik1==agirlik2)//Mesela bastan girilen sayilarimiz esitse burada devamli girilmesi gereken agirligimizi belirliyoruz,sonra tek sefere mahsus bir farkli agirlik girilmesine izin veriyoruz.
                            {
                                devamliagirlik=agirlik3;

                                  do {
                                             i++;

                                            printf("\n%d.bilyenin miligram cinsinden agirligi giriniz:",i);
                                              scanf("%d",&agirlik3);

                                           while(agirlik3<=0)
                                           {
                                              printf("Hatali agirlik sayisi girisi.");
                                              printf("\n%d.bilyenin miligram cinsinden agirligi giriniz:",i);
                                              scanf("%d",&agirlik3);

                                           }
                                   } while(agirlik3==devamliagirlik&&i<bilyesayisi);

                                  ///////////////////////////////
                                         if(agirlik3!=devamliagirlik)//Bu if icinde tek seferlik farkli agirlikta bilye almasina izin veriyoruz.
                                             {
                                                                     //agirlik esit degilse direk buraya girsin diuoruz.mesela 10 bilyelik kutuda 10.bilye agirsa yine buraya giriyor arttiriyor agir olani
                                                    tekseferlikagirlik=agirlik3;

                                                        do{                        //bilyesayisindan kucukse hala ve agirlik devamli agirliga esitse giriyor.
/*Bu do while icinde bir kere farkli */                    i++;
/*deger girilip o farkli deger alindiktan sonra */
/*surekli devamliagirlik girilirse bilye */              while(agirlik3<=0)
                                                            {
                                                             printf("Hatali agirlik sayisi girisi.");
                                                             printf("\n%d.bilyenin miligram cinsinden agirligi giriniz:",i);
                                                             scanf("%d",&agirlik3);

                                                             }
                                                              printf("\n%d.bilyenin miligram cinsinden agirligi giriniz:",i);//Sonra burda yeniden agirlik soruyoruz..
/*sayisi bitene kadar agirlik alinip sonlaniyor*/               scanf("%d",&agirlik3);


                                                 }while(agirlik3==devamliagirlik && i<bilyesayisi);


                                                         if(agirlik3>tekseferlikagirlik)//tek seferlik agirlik kucuk girildiyse bu if icindeki islemler yapilsin istedim
                                                             {
                                                                birkutu_ici_bilyeler_agirliklari_farki_hafif=(agirlik3-tekseferlikagirlik);
                                                                float_tanimli_agirlik3=agirlik3;//bunu yuzdeleri hesaplatmak icin gecici tanimladik
                                                                if(birkutu_ici_bilyeler_agirliklari_farki_hafif>elde_birkutu_ici_bilyeler_agirliklari_farki_hafif)
                                                                    {
                                                                           hafif_fark_degerinin_en_buyuk_oldugu_deger=birkutu_ici_bilyeler_agirliklari_farki_hafif;
                                                                           hafif_fark_degerinin_en_buyuk_oldugu_deger_yuzde=((birkutu_ici_bilyeler_agirliklari_farki_hafif/float_tanimli_agirlik3)*100);

                                                                    }
                                                             }

                                                             elde_birkutu_ici_bilyeler_agirliklari_farki_hafif=birkutu_ici_bilyeler_agirliklari_farki_hafif;

                                                           if(agirlik3<tekseferlikagirlik)
                                                               {
                                                                  birkutu_ici_bilyeler_agirliklari_farki_agir=(tekseferlikagirlik-agirlik3);
                                                                   float_tanimli_agirlik3=agirlik3;
                                                                if(birkutu_ici_bilyeler_agirliklari_farki_agir>elde_birkutu_ici_bilyeler_agirliklari_farki_agir)
                                                                {
                                                                             agir_fark_degerinin_en_buyuk_oldugu_deger=birkutu_ici_bilyeler_agirliklari_farki_agir;

                                                                            agir_fark_degerinin_en_buyuk_oldugu_yuzde=((birkutu_ici_bilyeler_agirliklari_farki_agir/float_tanimli_agirlik3)*100);

                                                                }


                                                               }
                                                             elde_birkutu_ici_bilyeler_agirliklari_farki_agir=birkutu_ici_bilyeler_agirliklari_farki_agir;

                                                             //Eger bundan sonra girilen agirlik3 esit olmazsa devamliagirliga hata veriyor.
                                             if(agirlik3!=devamliagirlik)//Eger yeni alinan agirlik devamliagirligimiza esit degilse kutuyu hatali sayiyoruz
                                                {
                                                       printf("Hatali kutu.\n");
                                                       hatalikutusay++;
                                                       iadebilyesayisi+=bilyesayisi;
                                                       break;

                                                }
                                                else if(i==bilyesayisi&&agirlik3==devamliagirlik&&tekseferlikagirlik>devamliagirlik)
                                                {
                                                     birbilye_daha_agir_olan_kutusay++;
                                                     agir_olan_bilyeler_fark_degerleri+=(tekseferlikagirlik-devamliagirlik);
                                                     agir_olan_bilye_yuzdesi=((tekseferlikagirlik/devamliagirlik)*100);
                                                    agir_olan_bilyeler_yuzdeleri_toplami+=agir_olan_bilye_yuzdesi;
                                                     kabuledilenbiylesayisi+=bilyesayisi;
                                                     hatasizkutusay++;


                                                }
                                                 else if(i==bilyesayisi&&agirlik3==devamliagirlik&&tekseferlikagirlik<devamliagirlik)
                                                {
                                                     birbilye_daha_hafif_olan_kutusay++;
                                                     hafif_olan_bilyeler_fark_degerleri+=(devamliagirlik-tekseferlikagirlik);
                                                     hafif_olan_bilye_yuzdesi=((tekseferlikagirlik/devamliagirlik)*100);
                                                     hafif_olan_bilyeler_yuzdeleri_toplami+=agir_olan_bilye_yuzdesi;
                                                     kabuledilenbiylesayisi+=bilyesayisi;
                                                     hatasizkutusay++;


                                                }

                                        }


                                       ////////////////////////////////////////////////////////////

                                                   else if(agirlik3!=devamliagirlik)//Zaten farkli ya da tekseferlik agirlik girerse kutu hatali uyarisi veriyor.

                                                     {
                                                     printf("Hatali kutu.");
                                                      hatalikutusay++;
                                                      iadebilyesayisi+=bilyesayisi;
                                                      break;
                                                     }
                                           /////////////////////////////////


                                      else if(i==bilyesayisi)//tum bilye agirigi esit girilirse
                                       {
                                              kabuledilenbiylesayisi+=bilyesayisi;
                                            hatasizkutusay++;

                                            if(agirlik3==devamliagirlik)
                                            {
                                                tumbilyeleresitagirlikkutusu++;

                                                 if(yeni_bilye_sayisi<bilyesayisi)//yeni girdik simdi mesela bir bilye sayisi,eger o elde tutulan yeni_bilye_sayisindan buyukse,yeni_bilye_sayisini atiyoru buyuk olani.
                                                 {             //Icinde tum bilyeler esit kutudaki icinde en cok bilyeler olan kutu icin yapildi burasi
                                                    en_cok_tumbilyeleresitagirlikkutusu_bilyesay=bilyesayisi;
                                                    en_cok_tumbilyeleresitagirlikkutusu_bilyesay_birbilye_agirlik=agirlik3;
                                                 }
                                                 //Buranin altindaki kodlarda tum bilyelerin esit agirlikta oldugu kutular arasinda,en hafif agrlikli olan

                                                  if(en_hafif_agirlik>agirlik3)//Bu ilk basta buyuk agirlik girilirse isletilen kisim oluyor
                                                 {
                                                    en_hafif_agirlik_olan_kutu_bilyesay=bilyesayisi;
                                                    en_hafif_agirlik_olan_kutu_birbilye_agirlik=agirlik3;
                                                 }

                                                 else  if(en_hafif_agirlik<agirlik3)//Bu ilk basta kucuk agirlik girilirse isletilen kisim oluyor
                                                 {
                                                    en_hafif_agirlik_olan_kutu_bilyesay=yeni_bilye_sayisi;
                                                    en_hafif_agirlik_olan_kutu_birbilye_agirlik=en_hafif_agirlik;
                                                 }


                                            }

                                             yeni_bilye_sayisi=bilyesayisi;//her yenib bilye girisinde buraya atıyoruz eldeki bilye sayisini,bu tutuluyor yukardan asagi gelene dek tekrar program
                                             en_hafif_agirlik=agirlik3;
                                         }




               /* If 1 son*/               }

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                          else if(agirlik3==agirlik1 || agirlik3==agirlik2 && agirlik1!=agirlik2)//ilk iki agirlik mesela farkli girilmis ise 3.agirlik illaki biri olacagi icin bu else if icinde bu durumu saglattim.
                            {
                                   devamliagirlik2=agirlik3;//agirlik3 neyse artik devamliagirlik o olmak zorunda
                                   geciciagirlik1=agirlik1;
                                   geciciagirlik2=agirlik2;//Bunlari float yuzdeyi hesaplatmak icin atadık
                                   do{
                                          i++;
                                           printf("\n%d.bilyenin miligram cinsinden agirligi giriniz:",i);
                                           scanf("%d",&agirlik3);

                                            while(agirlik3<=0)
                                           {
                                              printf("Hatali agirlik sayisi girisi.");
                                              printf("\n%d.bilyenin miligram cinsinden agirligi giriniz:",i);
                                              scanf("%d",&agirlik3);

                                           }


                                   } while(agirlik3==devamliagirlik2 && i<bilyesayisi);

                                         ////////////Alttaki iki if ilk girilen sayi icin hafif agirlik girisi icin kullaniliyor
                                                     if(agirlik1>agirlik2&&agirlik3==agirlik1)//tek seferlik agirlik kucuk girildiyse bu if icindeki islemler yapilsin istedim
                                                             {
                                                                birkutu_ici_bilyeler_agirliklari_farki_hafif=(agirlik1-agirlik2);
                                                                float_tanimli_agirlik3=agirlik3;
                                                                if(birkutu_ici_bilyeler_agirliklari_farki_hafif>elde_birkutu_ici_bilyeler_agirliklari_farki_hafif)
                                                                     {
                                                                               hafif_fark_degerinin_en_buyuk_oldugu_deger=birkutu_ici_bilyeler_agirliklari_farki_hafif;
                                                                               hafif_fark_degerinin_en_buyuk_oldugu_deger_yuzde=((birkutu_ici_bilyeler_agirliklari_farki_hafif/float_tanimli_agirlik3)*100);

                                                                     }
                                                             }
                                                             elde_birkutu_ici_bilyeler_agirliklari_farki_hafif=birkutu_ici_bilyeler_agirliklari_farki_hafif;

                                                       if(agirlik2>agirlik1&&agirlik3==agirlik2)
                                                      {
                                                              birkutu_ici_bilyeler_agirliklari_farki_hafif=(agirlik2-agirlik1);
                                                              float_tanimli_agirlik3=agirlik3;
                                                                if(birkutu_ici_bilyeler_agirliklari_farki_hafif>elde_birkutu_ici_bilyeler_agirliklari_farki_hafif)
                                                                     {
                                                                             hafif_fark_degerinin_en_buyuk_oldugu_deger=birkutu_ici_bilyeler_agirliklari_farki_hafif;
                                                                             hafif_fark_degerinin_en_buyuk_oldugu_deger_yuzde=((birkutu_ici_bilyeler_agirliklari_farki_hafif/float_tanimli_agirlik3)*100);

                                                                     }
                                                      }
                                                      elde_birkutu_ici_bilyeler_agirliklari_farki_hafif=birkutu_ici_bilyeler_agirliklari_farki_hafif;

                                      /////////////Alttaki iki if agir girisler icin

                                                           if(agirlik1<agirlik2&&agirlik3==agirlik1)
                                                               {
                                                                  birkutu_ici_bilyeler_agirliklari_farki_agir=(agirlik2-agirlik1);
                                                                  float_tanimli_agirlik2=agirlik2;
                                                                  float_tanimli_agirlik3=agirlik3;

                                                                if(birkutu_ici_bilyeler_agirliklari_farki_agir>elde_birkutu_ici_bilyeler_agirliklari_farki_agir)
                                                                     {
                                                                           agir_fark_degerinin_en_buyuk_oldugu_deger=birkutu_ici_bilyeler_agirliklari_farki_agir;
                                                                             agir_fark_degerinin_en_buyuk_oldugu_yuzde=((birkutu_ici_bilyeler_agirliklari_farki_agir/float_tanimli_agirlik3)*100);

                                                                     }

                                                               }
                                                             elde_birkutu_ici_bilyeler_agirliklari_farki_agir=birkutu_ici_bilyeler_agirliklari_farki_agir;

                                                           if(agirlik2<agirlik1&&agirlik3==agirlik2)
                                                              {
                                                              birkutu_ici_bilyeler_agirliklari_farki_agir=(agirlik1-agirlik2);
                                                                float_tanimli_agirlik2=agirlik2;
                                                                float_tanimli_agirlik1=agirlik1;
                                                                if(birkutu_ici_bilyeler_agirliklari_farki_agir>elde_birkutu_ici_bilyeler_agirliklari_farki_agir)
                                                                    {
                                                                          agir_fark_degerinin_en_buyuk_oldugu_deger=birkutu_ici_bilyeler_agirliklari_farki_agir;
                                                                           agir_fark_degerinin_en_buyuk_oldugu_yuzde=((birkutu_ici_bilyeler_agirliklari_farki_agir/float_tanimli_agirlik3)*100);
                                                                    }

                                                             }
                                                              elde_birkutu_ici_bilyeler_agirliklari_farki_agir=birkutu_ici_bilyeler_agirliklari_farki_agir;

                                                  //////////////////////////////////agir girisler son


                                       if(i==bilyesayisi&&devamliagirlik2==agirlik3)
                                       {
                                             if(devamliagirlik2<agirlik2 || devamliagirlik2<agirlik1)
                                          {
                                                          birbilye_daha_agir_olan_kutusay++;

                                                          if(devamliagirlik2<agirlik1)//devamli agirligimiz agirlik1 den kucukse burayı kullaniyoruz.bu islemleri buyuk agirlik hangisi onu belirlemek icin yaptim.
                                                                {
                                                                agir_olan_bilyeler_fark_degerleri+=(geciciagirlik1-devamliagirlik2);
                                                                 agir_olan_bilye_yuzdesi=((geciciagirlik1/devamliagirlik2)*100);
                                                                  agir_olan_bilyeler_yuzdeleri_toplami+=agir_olan_bilye_yuzdesi;
                                                                }

                                                          else if(devamliagirlik2<agirlik2)//devamli agirligimiz agirlik2 den kucukse burayı kullaniyoruz.bu islemleri buyuk agirlik hangisi onu belirlemek icin yaptim.
                                                                {
                                                                agir_olan_bilyeler_fark_degerleri+=(geciciagirlik2-devamliagirlik2);
                                                                 agir_olan_bilye_yuzdesi=((geciciagirlik2/devamliagirlik2)*100);
                                                                  agir_olan_bilyeler_yuzdeleri_toplami+=agir_olan_bilye_yuzdesi;
                                                                }
                                          }

                                           else if(devamliagirlik2>agirlik2||devamliagirlik2>agirlik1)
                                            {
                                                   birbilye_daha_hafif_olan_kutusay++;//kucuk olarak girilen agirlik daha girilemedigi icin bu sartta bir hafif bilye olan kutuyu arttiriyorum.

                                                     if(devamliagirlik2>agirlik2)
                                                     {
                                                                     hafif_olan_bilyeler_fark_degerleri+=(devamliagirlik2-geciciagirlik2);
                                                                     hafif_olan_bilye_yuzdesi=((geciciagirlik2/devamliagirlik2)*100);
                                                                     hafif_olan_bilyeler_yuzdeleri_toplami+=hafif_olan_bilye_yuzdesi;
                                                     }

                                                      else if(devamliagirlik2>agirlik1)
                                                     {
                                                                     hafif_olan_bilyeler_fark_degerleri+=(devamliagirlik2-geciciagirlik1);
                                                                     hafif_olan_bilye_yuzdesi=((geciciagirlik1/devamliagirlik2)*100);
                                                                     hafif_olan_bilyeler_yuzdeleri_toplami+=hafif_olan_bilye_yuzdesi;
                                                     }

                                            }

                                              birbilyeagirlikfarklikutusu++;
                                              kabuledilenbiylesayisi+=bilyesayisi;
                                              hatasizkutusay++;

                                              break;

                                       }

                                            else if(agirlik3!=devamliagirlik2)
                                           {
                                                  printf("Hatali kutu\n");
                                                   hatalikutusay++;
                                                   iadebilyesayisi+=bilyesayisi;
                                                    break;
                                           }


                            }
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                           else if (agirlik3!=agirlik1 && agirlik3!=agirlik2 && agirlik1==agirlik2)//Mesela burda 3. agirlik ilk ikisine esit olmazsa ve ilk iki agirlik ayniysa durumunda sadece 3.agirligi 1 sefere mahsus alma olayý gerceklestiriliyor.

                                {
                                       tekseferlikagirlik2=agirlik3;//3.agirlik girisi farkli oldugu icin bunu atadik bir gecici yere
                                       devamliagirlik3=agirlik1;//agirlik1 ya da agirlik2 degeri devamli agirlik oluyor bu sartta.Ve kilit agirlik agirlik 3.
                                  do {
                                          i++;

                                            printf("\n%d.bilyenin miligram cinsinden agirligi giriniz:",i);
                                              scanf("%d",&agirlik3);

                                           while(agirlik3<=0)
                                           {
                                              printf("Hatali agirlik sayisi girisi.");
                                              printf("\n%d.bilyenin miligram cinsinden agirligi giriniz:",i);
                                              scanf("%d",&agirlik3);

                                           }


                                   }while(agirlik3==devamliagirlik3 && i<bilyesayisi);
                            /////////////////////////////////////////////////////////////////////////////////////
                                        //burda agirlik2,agirlik3 de kullanilabilirdi sabit agirlik oluyor o cunku girislerden dolayi
                                         if(agirlik1>tekseferlikagirlik2)//tek seferlik agirlik kucuk girildiyse bu if icindeki islemler yapilsin istedim
                                                             {
                                                                birkutu_ici_bilyeler_agirliklari_farki_hafif=(agirlik1-tekseferlikagirlik2);
                                                                float_tanimli_agirlik1=agirlik1;
                                                                if(birkutu_ici_bilyeler_agirliklari_farki_hafif>elde_birkutu_ici_bilyeler_agirliklari_farki_hafif)
                                                                      {
                                                                            hafif_fark_degerinin_en_buyuk_oldugu_deger=birkutu_ici_bilyeler_agirliklari_farki_hafif;
                                                                             hafif_fark_degerinin_en_buyuk_oldugu_deger_yuzde=((birkutu_ici_bilyeler_agirliklari_farki_hafif/float_tanimli_agirlik1)*100);

                                                                      }

                                                             }

                                                             elde_birkutu_ici_bilyeler_agirliklari_farki_hafif=birkutu_ici_bilyeler_agirliklari_farki_hafif;

                                                           if(agirlik1<tekseferlikagirlik2)
                                                               {
                                                                  birkutu_ici_bilyeler_agirliklari_farki_agir=(tekseferlikagirlik2-agirlik1);
                                                                  float_tanimli_agirlik1=agirlik1;
                                                                if(birkutu_ici_bilyeler_agirliklari_farki_agir>elde_birkutu_ici_bilyeler_agirliklari_farki_agir)
                                                                      {
                                                                            agir_fark_degerinin_en_buyuk_oldugu_deger=birkutu_ici_bilyeler_agirliklari_farki_agir;
                                                                            agir_fark_degerinin_en_buyuk_oldugu_yuzde=((birkutu_ici_bilyeler_agirliklari_farki_agir/float_tanimli_agirlik1)*100);
                                                                      }

                                                               }
                                                             elde_birkutu_ici_bilyeler_agirliklari_farki_agir=birkutu_ici_bilyeler_agirliklari_farki_agir;
                                  ////////////////////////////////////////////////////////////Bu iflerle agirlik ya da hafiflik olarak en buyuk frk degeri bulundu



                                          if(i==bilyesayisi&&agirlik3==devamliagirlik3)
                                                {
                                                        if(tekseferlikagirlik2<devamliagirlik3)
                                                          {
                                                          birbilye_daha_hafif_olan_kutusay++;//eger alinan agirlk3 degeri bizim devamli agirligimizdan kucukse hafif bilye var demektir o arttir.
                                                          hafif_olan_bilyeler_fark_degerleri+=(devamliagirlik3-tekseferlikagirlik2);
                                                          hafif_olan_bilye_yuzdesi=((tekseferlikagirlik2/devamliagirlik3)*100);
                                                          hafif_olan_bilyeler_yuzdeleri_toplami+=hafif_olan_bilye_yuzdesi;

                                                          }
                                                        else if(tekseferlikagirlik2>devamliagirlik3)
                                                          {
                                                          birbilye_daha_agir_olan_kutusay++;
                                                          agir_olan_bilyeler_fark_degerleri+=(tekseferlikagirlik2-devamliagirlik3);
                                                          agir_olan_bilye_yuzdesi=((tekseferlikagirlik2/devamliagirlik3)*100);
                                                          agir_olan_bilyeler_yuzdeleri_toplami+=agir_olan_bilye_yuzdesi;
                                                          }
                                                        birbilyeagirlikfarklikutusu++;
                                                        kabuledilenbiylesayisi+=bilyesayisi;
                                                        hatasizkutusay++;

                                                        break;
                                                     }
                                 else if(agirlik3!=devamliagirlik3)//Eger yeni alinan agirlik devamliagirligimiza esit degilse kutuyu hatali sayiyoruz
                                                {
                                                       printf("Hatali kutu.\n");
                                                       hatalikutusay++;
                                                       iadebilyesayisi+=bilyesayisi;

                                                       break;
                                                }




                                       }

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                            else

                                  {
                                          printf("hatali kutu.\n");
                                         hatalikutusay++;
                                         iadebilyesayisi+=bilyesayisi;
                                         break;
                                  }


                     }

                     printf("Baska kutu girisi var mi(Evet(E ya da e)/Hayir(H ya da h)):");
                     scanf("%s",&secim);


    }while(secim=='E' || secim=='e');

    if(secim=='H'|| secim=='h')
    {
           hatalikutuyuzde=((hatalikutusay/kutusayisi)*100);

           tumbilyeleresitagirlikyuzde=((tumbilyeleresitagirlikkutusu/hatasizkutusay)*100);
           birbilyedahaagiryuzde=((birbilye_daha_agir_olan_kutusay/hatasizkutusay)*100);
           birbilyedahahafifyuzde=((birbilye_daha_hafif_olan_kutusay/hatasizkutusay)*100);
           agir_olan_bilyeler_fark_degerleri_ort=(agir_olan_bilyeler_fark_degerleri/hatasizkutusay);
           hafif_olan_bilyeler_fark_degerleri_ort=(hafif_olan_bilyeler_fark_degerleri/hatasizkutusay);
           agir_olan_bilyeler_yuzdeleri_toplami_ort=(agir_olan_bilyeler_yuzdeleri_toplami/hatasizkutusay);
           hafif_olan_bilyeler_yuzdeleri_toplami_ort=(hafif_olan_bilyeler_yuzdeleri_toplami/hatasizkutusay);


           printf("Hatali kutu sayisi=%d",hatalikutusay);
           printf("\nHatali kutularin yuzdesi=%.2f",hatalikutuyuzde);
           printf("\nKabul edilen bilye sayisi=%d",kabuledilenbiylesayisi);
           printf("\nIade edilen bilye sayisi=%d",iadebilyesayisi);
           printf("\n");
           printf("\nTum bilyelerin esit agirlikta oldugu kutu sayisi=%d",tumbilyeleresitagirlikkutusu);
            printf("\n");
           printf("\nTum bilyelerin esit agirlikta oldugu kutularin,\nuretim hatasi olmayan kutular icindeki yuzdesi=%.2f",tumbilyeleresitagirlikyuzde);
            printf("\n");
           printf("\nBir bilye daha agir olan kutu sayisi=%d",birbilye_daha_agir_olan_kutusay);
            printf("\n");
           printf("\nBir bilyenin daha agir oldugu kutularin,\nuretim hatasi olmayan kutular icindeki yuzdesi=%.2f",birbilyedahaagiryuzde);
            printf("\n");
           printf("\nBir bilye daha hafif olan kutu sayisi=%d",birbilye_daha_hafif_olan_kutusay);
            printf("\n");
           printf("\nBir bilyenin daha hafif oldugu kutularin,\nuretim hatasi olmayan kutular icindeki yuzdesi=%.2f",birbilyedahahafifyuzde);
            printf("\n");
           printf("\nBir bilyenin daha agir olgugu kutulardaki,agir olan bilyelerin,\nagirlik farki degerlerinin ortalamasi=%.2f",agir_olan_bilyeler_fark_degerleri_ort);
            printf("\n");
           printf("\nBir bilyenin daha hafif olgugu kutulardaki,hafif olan bilyelerin,\nagirlik farki degerlerinin ortalamasi=%.2f",hafif_olan_bilyeler_fark_degerleri_ort);
            printf("\n");
           printf("\nBir bilyenin daha agir olgugu kutulardaki,agir olan bilyelerin,\nagirlik farki yuzdelerinin ortalamasi=%.2f",agir_olan_bilyeler_yuzdeleri_toplami_ort);
           printf("\n");
           printf("\nBir bilyenin daha hafif olgugu kutulardaki,hafif olan bilyelerin,\nagirlik farki yuzdelerinin ortalamasi=%.2f",hafif_olan_bilyeler_yuzdeleri_toplami_ort);
            printf("\n");
           printf("\nTum bilyeler esit agirlikta olan kutularda,\nicinde en cok bilye olan kutudaki bilye sayisi=%d",en_cok_tumbilyeleresitagirlikkutusu_bilyesay);
            printf("\n");
           printf("\nTum bilyeler esit agirlikta olan kutularda,\nicinde en cok bilye olan kutudaki bir bilyenin agirligi=%d",en_cok_tumbilyeleresitagirlikkutusu_bilyesay_birbilye_agirlik);
            printf("\n");
           printf("\nTum bilyeler esit agirlikta olan kutularda,\nicinde en hafif bilyeler olan kutudaki bilye sayisi=%d",en_hafif_agirlik_olan_kutu_bilyesay);
             printf("\n");
           printf("\nTum bilyeler esit agirlikta olan kutularda,\nicinde en hafif bilyeler olan kutudaki bir bilye agirligi=%d",en_hafif_agirlik_olan_kutu_birbilye_agirlik);
            printf("\n");
           printf("\nFarkli olan bilyenin agirliginin,\ndiger bilyelerin agirligiyla arasindaki farkin degerinin,\nen buyuk oldugu farkin degeri(Hafif)= - %.f",hafif_fark_degerinin_en_buyuk_oldugu_deger);
            printf("\n");
           printf("\nFarkli olan bilyenin agirliginin,\ndiger bilyelerin agirligiyla arasindaki farkin degerinin,\nen buyuk oldugu farkin degeri(Agir)= + %.f",agir_fark_degerinin_en_buyuk_oldugu_deger);
            printf("\n");
            printf("\nFarkli olan bilyenin agirliginin,\ndiger bilyelerin agirligiyla arasindaki farkin degerinin,\nen buyuk oldugu farkin yuzdesi=%.2f.( hafif bilye bulunan kutu icin).",hafif_fark_degerinin_en_buyuk_oldugu_deger_yuzde);
           printf("\n");
            printf("\nFarkli olan bilyenin agirliginin,\ndiger bilyelerin agirligiyla arasindaki farkin degerinin,\nen buyuk oldugu farkin yuzdesi=%.2f.(agir bilye bulunan kutu icin).",agir_fark_degerinin_en_buyuk_oldugu_yuzde);
           printf("\n");
            printf("\nFarkli olan bilyenin agirliginin,\ndiger bilyelerin agirligiyla arasindaki farkin yuzdesinin,\nen buyuk oldugu farkin degeri=%.2f(agir).",agir_fark_degerinin_en_buyuk_oldugu_deger);
           printf("\n");
            printf("\nFarkli olan bilyenin agirliginin,\ndiger bilyelerin agirligiyla arasindaki farkin yuzdesinin,\nen buyuk oldugu farkin yuzdesi %.2f(agir).",agir_fark_degerinin_en_buyuk_oldugu_yuzde);
             printf("\n");
            printf("\nFarkli olan bilyenin agirliginin,\ndiger bilyelerin agirligiyla arasindaki farkin yuzdesinin,\nen buyuk oldugu farkin degeri %.2f(hafif).",hafif_fark_degerinin_en_buyuk_oldugu_deger);
           printf("\n");
            printf("\nFarkli olan bilyenin agirliginin,\ndiger bilyelerin agirligiyla arasindaki farkin yuzdesinin,\nen buyuk oldugu farkin yuzdesi %.2f(hafif).", hafif_fark_degerinin_en_buyuk_oldugu_deger_yuzde);

    }

    return 0;
}



