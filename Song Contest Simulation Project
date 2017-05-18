#include <stdio.h>
#include <stdlib.h>

int menu();
int menu2();
void yeni_yarisma_duzenle(void);
int son_duzenlenen_yarisma_istatistikleri();
void sadece_koc_puanlamasi_dikkate_alindiginda_genel_durum_listele(int,int*[]);
void sadece_seyircilerin_puanlamasi_dikkate_alindiginda_genel_durum_listele(int,int*[]);
void yarismacilarin_her_hafta_aldiklari_toplam_puanlari_listele(int,int,int*,int*);
void yarismacilarin_her_koctan_aldiklari_toplam_puanlari_listele(int,int,int,int);
int *global_koc_puan_dizi_genel,global_yarismaci_say,*global_yarismaci_no,*global_koc_puan_dizi_genel_yedek,*global_seyirci_puan_dizi_genel_yedek,*global_seyirci_puan_dizi_genel,*global_yarismaci_no2;
int global_hafta_say;



int main()
{
  int secenek;
  char eminlik;

     secenek=menu();
     switch(secenek)
     {
       case 1:
         yeni_yarisma_duzenle();
         break;
       case 2:
         son_duzenlenen_yarisma_istatistikleri();
         break;
       case 3:
          printf("Programdan cikmak istiyor musunuz(e/E-h/H):\n");
          scanf("%s",&eminlik);
          if(eminlik=='e' || eminlik=='E')
                system("cls");
          else if(eminlik=='h' || eminlik=='H')
                return menu();
          break;
     }
    return 0;
}



int menu()
{
     int sec;

       do{
      printf("\n\n-------ANA MENU-------\n\n");
       printf("1)Yeni Yarisma Duzenleme\n\n");
        printf("2)Son Duzenlenen Yarismanin Istatistiklerini Goruntuleme\n\n");
         printf("3)Cikis\n\n");
         printf("Seciminizi  giriniz:");
         scanf("%d",&sec);
       }while(sec<1 || sec>3);
    return sec;


}

int menu2()
{
           int secim;
       do{
      printf("\n-------ISTATISTIK ALT MENU-------\n\n");
       printf("1)Sadece Koclarin Puanlamasi Dikkate Alindiginda Genel Durumun Listelenmesi\n\n");
        printf("2)Sadece Seyircilerin Puanlamasi Dikkate Alindiginda Genel Durumun Listelenmesi\n\n");
         printf("3)Yarismacilarin Her Hafta Aldiklari Toplam Puanlarin Listelenmesi\n\n");
         printf("4)Yarismacilarin Her Koctan Aldiklari Toplam Puanlarin Listelenmesi\n\n");
         printf("5)Ana Menu\n\n");
         printf("Seciminizi  giriniz:");
         scanf("%d",&secim);
       }while(secim<1 || secim>5);
    return secim;


}


void yeni_yarisma_duzenle(void)
{
    int yarismaci_say=0,devam_hafta_say=0,puan_verilen_yarismaci=0,koc_puan=0,son_seyirci_puan=0;
    int *koc_puan_dizi,*seyirci_puan_dizi,i,j,v,g,f,gl,seyirci_puan_verilen_yarismaci=0,seyirci_puan=0,koc_sayisi=0;
    int *koc_puan_dizi_son,*seyirci_puan_dizi_son,* yarismaci_hafta_toplam_puan_dizi,*yarismaci_no,*yarismaci_hafta_toplam_puan_dizi_kopya;
    int *koc_puan_dizi_genel,*seyirci_puan_dizi_genel,*yarismaci_no_genel,* yarismaci_hafta_toplam_puan_dizi_genel,*yarismaci_hafta_toplam_puan_dizi_genel_kopya,*koc_puan_dizi_son_liste,*seyirci_puan_dizi_son_liste;
    int *koc_puan_dizi_genel_liste,*seyirci_puan_dizi_genel_liste;
    int her_haftanin_toplam_puanlarini_tutan_dizi[devam_hafta_say][yarismaci_say];
    int *birincilik_say,sectigi;

   do{
    printf("Yarismaci sayisini giriniz:");
    scanf("%d",&yarismaci_say);
     while(yarismaci_say<5 || yarismaci_say>20 )
     {
            printf("\nHatali yarismaci sayisi girisi.\n");
              printf("\nYarismaci sayisini giriniz:");
               scanf("%d",&yarismaci_say);
     }

       koc_sayisi=yarismaci_say;
       global_yarismaci_say=yarismaci_say;

       birincilik_say = (int *) malloc((yarismaci_say*sizeof(int)));
       for(f=0;f<yarismaci_say;f++)
       {
           birincilik_say[f]=0;
       }



       yarismaci_hafta_toplam_puan_dizi_genel = (int *) malloc((yarismaci_say*sizeof(int)));
       for(f=0;f<yarismaci_say;f++)
       {
           yarismaci_hafta_toplam_puan_dizi_genel[f]=0;
       }


         global_seyirci_puan_dizi_genel=(int*)malloc((yarismaci_say *sizeof(int)));
         for(f=0;f<yarismaci_say;f++)
           {
           global_seyirci_puan_dizi_genel[f]=0;
           }


         global_seyirci_puan_dizi_genel_yedek=(int*)malloc((yarismaci_say *sizeof(int)));
         for(f=0;f<yarismaci_say;f++)
           {
           global_seyirci_puan_dizi_genel_yedek[f]=0;
           }




        global_koc_puan_dizi_genel=(int*)malloc((yarismaci_say *sizeof(int)));
         for(f=0;f<yarismaci_say;f++)
           {
           global_koc_puan_dizi_genel[f]=0;
           }

         global_koc_puan_dizi_genel_yedek=(int*)malloc((yarismaci_say *sizeof(int)));
         for(f=0;f<yarismaci_say;f++)
           {
           global_koc_puan_dizi_genel_yedek[f]=0;
           }


        global_yarismaci_no=(int*)malloc((yarismaci_say *sizeof(int)));//1.istatistikteki koc puani icin
         for(f=0;f<yarismaci_say;f++)
           {
           global_yarismaci_no[f]=0;
           }

           global_yarismaci_no2=(int*)malloc((yarismaci_say *sizeof(int)));//2.istatistik icin
         for(f=0;f<yarismaci_say;f++)
           {
           global_yarismaci_no2[f]=0;
           }




       yarismaci_hafta_toplam_puan_dizi_genel_kopya = (int *) malloc((yarismaci_say*sizeof(int)));
       for(f=0;f<yarismaci_say;f++)
       {
           yarismaci_hafta_toplam_puan_dizi_genel_kopya[f]=0;
       }



       yarismaci_no_genel=(int*)malloc((yarismaci_say*sizeof(int)));
         for(f=0;f<yarismaci_say;f++)
       {
           yarismaci_no_genel[f]=0;
       }

       seyirci_puan_dizi_genel=(int*)malloc((yarismaci_say *sizeof(int)));
         for(f=0;f<yarismaci_say;f++)
       {
           seyirci_puan_dizi_genel[f]=0;
       }

       koc_puan_dizi_genel=(int*)malloc((yarismaci_say *sizeof(int)));
         for(f=0;f<yarismaci_say;f++)
       {
           koc_puan_dizi_genel[f]=0;
       }

       yarismaci_hafta_toplam_puan_dizi_kopya = (int *) malloc((yarismaci_say*sizeof(int)));
       for(f=0;f<yarismaci_say;f++)
       {
           yarismaci_hafta_toplam_puan_dizi_kopya[f]=0;
       }



       yarismaci_no = (int *) malloc((yarismaci_say*sizeof(int)));
       for(f=0;f<yarismaci_say;f++)
       {
           yarismaci_no[f]=0;
       }


       koc_puan_dizi_son_liste=(int*)malloc((yarismaci_say*sizeof(int)));
       for(f=0;f<yarismaci_say;f++)
       {
           koc_puan_dizi_son_liste[f]=0;
       }

       seyirci_puan_dizi_son_liste=(int*)malloc((yarismaci_say*sizeof(int)));
       for(f=0;f<yarismaci_say;f++)
       {
           seyirci_puan_dizi_son_liste[f]=0;
       }

       koc_puan_dizi_genel_liste=(int*)malloc((yarismaci_say*sizeof(int)));
       for(f=0;f<yarismaci_say;f++)
       {
           koc_puan_dizi_genel_liste[f]=0;
       }

      seyirci_puan_dizi_genel_liste=(int*)malloc((yarismaci_say*sizeof(int)));
       for(f=0;f<yarismaci_say;f++)
       {
           seyirci_puan_dizi_genel_liste[f]=0;
       }



       yarismaci_hafta_toplam_puan_dizi = (int *) malloc((yarismaci_say*sizeof(int)));
       for(f=0;f<yarismaci_say;f++)
       {
           yarismaci_hafta_toplam_puan_dizi[f]=0;
       }


       koc_puan_dizi = (int *) malloc((yarismaci_say*sizeof(int)));//yarismaci sayisi kadar elemanli bir KOCLAIN puanlarini tutan dizi olusturdum.
       koc_puan_dizi_son = (int *) malloc((yarismaci_say*sizeof(int)));
       int k=0;
       for(k=0;k<yarismaci_say;k++)
       {
           koc_puan_dizi[k]=0;         //Burada dinamik dizimin butun elemanlarini 0 yaptim
           koc_puan_dizi_son[k]=0; //Cunku ilerde bir kocun ayni yarismaciya puan vermesini engelleyecegim,yani dizimizin o elemani artik sifir degerinden farkli olmussa bu degere koc puan vermistir olcak daha once

       }


       seyirci_puan_dizi=(int *) malloc((yarismaci_say*sizeof(int)));//yarismaci sayisi kadar elemanli bir SEYIRCILERIN puanlarini tutan dizi olusturdum
       seyirci_puan_dizi_son=(int *) malloc((yarismaci_say*sizeof(int)));
       int p=0;
       for(p=0;p<yarismaci_say;p++)
       {
           seyirci_puan_dizi[p]=0;//Burada dinamik dizimin butun elemanlarini 0 yaptim
           seyirci_puan_dizi_son[p]=0;
       }                      //Cunku ilerde bir seyircinin ayni yarismaciya puan vermesini engelleyecegim,yani dizimizin o elemani artik sifir degerinden farkli olmussa bu degere koc puan vermistir olcak daha once


       printf("\nHafta sayisini giriniz:");
        scanf("%d",&devam_hafta_say);
         while(devam_hafta_say<3 )
          {
            printf("\nHatali devam haftasi sayisi girisi.\n");
              printf("\nHafta sayisini giriniz:");
               scanf("%d",&devam_hafta_say);
          }


       global_hafta_say=devam_hafta_say;//bu sayi ilerde 3.istatistikte olusturacagimiz cok boyutlu dizi icin lazim olacak.

     for(v=1;v<=devam_hafta_say;v++)
     {



        printf("\n\nKoclarin yarismacilara verdikleri puanlar\n");
        printf("------------------------------------------");

     for(i=1;i<=yarismaci_say;i++)
     {
          printf("\n\n-----%d.Koc icin-----",i);

          for(j=0;j<3;j++)//3 seferlik dondurma icin for
          {
          printf("\nPuan verilen yarismaciyi giriniz:");
           scanf("%d",&puan_verilen_yarismaci);

           while(puan_verilen_yarismaci<1||puan_verilen_yarismaci>yarismaci_say)//puani 5 yarismaci varken tutup da 50.yarismaciya verilmesini engelledik
                {
                 printf("\nBu kadar cok yarismaci yoktur.");
                 printf("\nPuan verilen yarismaciyi giriniz:");
                 scanf("%d",&puan_verilen_yarismaci);
              }


          while(i==puan_verilen_yarismaci)//Burda kendi yarismacisina puan veremiyor
              {
                 printf("\nBu koc,bu yarismaciya puan veremez");
                 printf("\nPuan verilen yarismaciyi giriniz:");
                 scanf("%d",&puan_verilen_yarismaci);
              }

          while(koc_puan_dizi[puan_verilen_yarismaci-1]!=0)//Burda puan verdigi bir yarismaciya bir daha puan veremiyor
              {
                 printf("\nBu koc,bu yarismaciya daha once puan vermistir.");
                 printf("\nPuan verilen yarismaciyi giriniz:");
                 scanf("%d",&puan_verilen_yarismaci);
              }


                 while(i==puan_verilen_yarismaci)//tekrar koyduk,cunku koc mesela daha once puan verdigi yarismaciya tekrar puan verirse hata cikiyor,ardindan hemen kocun kendi yarismacisina puan vermeyi denersek kabul ediyordu bu olmadiginda.Simdi oyle birsey yok.
              {
                 printf("\nBu koc,bu yarismaciya puan veremez");
                 printf("\nPuan verilen yarismaciyi giriniz:");
                 scanf("%d",&puan_verilen_yarismaci);
              }


             while(puan_verilen_yarismaci<1||puan_verilen_yarismaci>yarismaci_say)//tekrar koyduk.cunku mesela diyelim kullanici once kocun daha once puan verdigi bir yarismaci girdi hata,sonra kendi yarismacisini girdi hata,sonra mesela 5 yarismaci varken 53 girdiginde kabul etmemesini saglattik burada.
                {
                 printf("\nBu kadar cok yarismaci yoktur.");
                 printf("\nPuan verilen yarismaciyi giriniz:");
                 scanf("%d",&puan_verilen_yarismaci);
              }



                  printf("\nVerilen puani giriniz:");
                   scanf("%d",&koc_puan);

          while(koc_puan<1 || koc_puan >3)//Burda kendi yarismacisina puan veremiyor
             {
                 printf("\nBu puan,yarismacilara verilemez");
                 printf("\nVerilen puani giriniz:");
                   scanf("%d",&koc_puan);
             }


              koc_puan_dizi[puan_verilen_yarismaci-1]=koc_puan;//Yarismaciya baska koclardan gelen puani atadik.Dizinin o elemanina atiyoruz.


          }//Koclar 3 yarismaciya puan verebildi,3 kez donduruyoruz yani,onun for'u.

                int s=0;
                for(s=0;s<yarismaci_say;s++)                                                    //-1 yaptim cunku diziler 0.elemandan basliyor.
                {
                  koc_puan_dizi_son[s]+=koc_puan_dizi[s];
                }//Burada dizimizi bir baska diziye sonra kullanma icin kopyaladik.Cunku koc_puan_diziyi tekrar sifirlayacagiz ki ikinci koc puan girerken 1.kocun girdigi yarismaci 2.koc icin puan girilmis yarismaci olarak gorulmesin makina tarafindan.


               for(k=0;k<yarismaci_say;k++)
                   {
                     koc_puan_dizi[k]=0; //Burada dinamik dizimin butun elemanlarini 0 yaptik tekrar.

                   }

     }//Koc ve sayisinin for'u.




        printf("\n\nSeyircilerin yarismacilara verdikleri puanlar\n");
         printf("------------------------------------------");


        for(j=0;j<3;j++)//3 seferlik dondurma icin for
          {
          printf("\nPuan verilen yarismaciyi giriniz:");
           scanf("%d",&seyirci_puan_verilen_yarismaci);

            while(seyirci_puan_verilen_yarismaci<1||seyirci_puan_verilen_yarismaci>yarismaci_say)//puani 5 yarismaci varken tutup da 50.yarismaciya verilmesini engelledik
                {
                 printf("\nBu kadar cok yarismaci yoktur.");
                 printf("\nPuan verilen yarismaciyi giriniz:");
                 scanf("%d",&seyirci_puan_verilen_yarismaci);
              }


          while(seyirci_puan_dizi[seyirci_puan_verilen_yarismaci-1]!=0)//Burda puan verdigi bir yarismaciya bir daha puan veremiyor
              {
                 printf("\nSeyirci,bu yarismaciya daha once puan vermistir.");
                 printf("\nPuan verilen yarismaciyi giriniz:");
                 scanf("%d",&seyirci_puan_verilen_yarismaci);
              }


                  printf("\nVerilen puani giriniz:");
                   scanf("%d",&seyirci_puan);

          while(seyirci_puan<1 || seyirci_puan >3)//Burda kendi yarismacisina puan veremiyor
             {
                 printf("\nBu puan,yarismacilara verilemez");
                 printf("\nVerilen puani giriniz:");
                   scanf("%d",&seyirci_puan);
             }
              son_seyirci_puan=((koc_sayisi-1)*seyirci_puan);


              seyirci_puan_dizi[seyirci_puan_verilen_yarismaci-1]=son_seyirci_puan;// Yarismaciya seyirciden gelen puani atiyor,artik seyirci hangi yarismaciya veriyorsa dizinin o elemanina atiyoruz
                                                                                   //-1 olayi var cunku diziler 0.elemandan basliyor.

          }//Seyircinin verebilecegi 3 puan kisitini saglatan for

              int l;
                for(l=0;l<yarismaci_say;l++)                                                    //-1 yaptim cunku diziler 0.elemandan basliyor.
                {
                  seyirci_puan_dizi_son[l]+=seyirci_puan_dizi[l];
                }

                int m;
                for(m=0;m<yarismaci_say;m++)
                   {
                     seyirci_puan_dizi[m]=0; //Burada dinamik dizimin butun elemanlarini 0 yaptik tekrar.

                   }


              int d=0,tut,tur;
              for(d=0;d<yarismaci_say;d++)
              {
                yarismaci_hafta_toplam_puan_dizi[d]+=(koc_puan_dizi_son[d]+seyirci_puan_dizi_son[d]);
              }

              for(d=0;d<yarismaci_say;d++)//degerlerimizi burada kopyaladik.
              {
                yarismaci_hafta_toplam_puan_dizi_kopya[d]+=yarismaci_hafta_toplam_puan_dizi[d];
              }

          //**********************************Burda bir cok boyutlu diziye,
                for(d=0;d<yarismaci_say;d++)
                     {                                                                                        //sirayla butun haftalarda olusan
                       her_haftanin_toplam_puanlarini_tutan_dizi[v-1][d]+=yarismaci_hafta_toplam_puan_dizi[d];  //toplam puan dizilerini atayacagiz ki
                                                                                                                      //3.istatistik icin kullanabilelim kaybolmadan.
                     }//v-1dedik cunku v 1 den baslıyor dizinini 0.elemanina atama yapmaliyiz ilk.


          //**********************************


              //Simdi bu dizide en buyuk elemani bulalim o bulunan elemanin sirasini,bir dizi daha olusturulmustu ekstra ona atalim.
              int n,z=0,sil,b,dondur=0,sirasi=0,buyuk=0,asil_sirasi=0;

               for(dondur=0;dondur<yarismaci_say;dondur++)
                {
                  printf("\nislemden sonra gelen. ");
                   printf("\n------------------");
                for(i=0;i<yarismaci_say;i++)
                {
                    printf("\n%d",yarismaci_hafta_toplam_puan_dizi_kopya[i]);

                }
              printf("\n------------------");


                for(n=0 ; n<yarismaci_say ; n++)
                 {

                   if(n!=yarismaci_say-1)
                    {
                   int df;
                   for(df=0;df<yarismaci_say;df++)
                   {

                    int sp;
                    for(sp=0;sp<yarismaci_say;sp++)//bu dongude diziyi bir kere dolasip en buyugunu buluyor ilk.
                     {
                     if((yarismaci_hafta_toplam_puan_dizi_kopya[sp]>yarismaci_hafta_toplam_puan_dizi[(sp+1)])&&(yarismaci_hafta_toplam_puan_dizi_kopya[sp]>buyuk)&&(yarismaci_hafta_toplam_puan_dizi_kopya[sp]!=yarismaci_hafta_toplam_puan_dizi_kopya[yarismaci_say-1]))
                            {
                              buyuk = yarismaci_hafta_toplam_puan_dizi_kopya[sp];
                              sirasi=sp;//dizi elemani 0 dan basladigi icin 0 dan atiyor yarismaci sayisina.arti bir yaptigimizda tam yarismacinin sayisina denk geliyor
                              sil=buyuk;
                              asil_sirasi=sirasi;
                              if(sp==0)
                                {
                                 birincilik_say[asil_sirasi]++;
                                }

                            }
                    else if((yarismaci_hafta_toplam_puan_dizi_kopya[sp]>yarismaci_hafta_toplam_puan_dizi[(sp+1)])&&(yarismaci_hafta_toplam_puan_dizi_kopya[sp]>=buyuk)&&(yarismaci_hafta_toplam_puan_dizi_kopya[sp]==yarismaci_hafta_toplam_puan_dizi_kopya[yarismaci_say-1]))
                            {
                                if(koc_puan_dizi_son[sp]>koc_puan_dizi_son[yarismaci_say-1])
                                {
                                  asil_sirasi=sp;
                                 if(sp==0)
                                   {
                                     birincilik_say[asil_sirasi]++;
                                   }
                                }
                                if(koc_puan_dizi_son[sp]<koc_puan_dizi_son[yarismaci_say-1])
                                     {
                                      asil_sirasi=(yarismaci_say-1);
                                      if(sp==0)
                                        {
                                          birincilik_say[asil_sirasi]++;
                                        }
                                     }



                                if(koc_puan_dizi_son[sp]==koc_puan_dizi_son[yarismaci_say-1])
                                 {
                                  if(sp<(yarismaci_say-1))
                                    {
                                     asil_sirasi=sp;
                                      if(sp==0)
                                       {
                                           birincilik_say[asil_sirasi]++;
                                       }
                                    }
                                  else
                                   {
                                        asil_sirasi=(yarismaci_say-1);
                                         if(sp==0)
                                          {
                                             birincilik_say[asil_sirasi]++;
                                          }
                                   }
                                 }

                             }
                     else

                        if((yarismaci_hafta_toplam_puan_dizi_kopya[yarismaci_say-1]>yarismaci_hafta_toplam_puan_dizi_kopya[0])&&(yarismaci_hafta_toplam_puan_dizi_kopya[yarismaci_say-1]>buyuk))
                         {
                          buyuk = yarismaci_hafta_toplam_puan_dizi_kopya[yarismaci_say-1];
                          sirasi=(yarismaci_say-1);//dizi elemani 0 dan basladigi icin 0 dan atiyor yarismaci sayisina.arti bir yaptigimizda tam yarismacinin sayisina denk geliyor
                          sil=buyuk;
                          asil_sirasi=sirasi;
                          if(sp==0)
                             {
                                 birincilik_say[asil_sirasi]++;
                             }
                         }

                     }//sp for'unun bitisi icin.En buyugu donduren ve bulduran alan.bu bittiginde en buyuk elimizde oluyor.


              }//df foru icin.
                printf("\n*************");//silinecekler kontrol icin
                 printf("\n%d",asil_sirasi);
                 printf("\n*************");



                     }

                     buyuk=0;//en son elemani da bulmasi icin bunu yaptik.
                }//bu for diziyi dolasip en buyuk elemani bulduruyor


                yarismaci_no[z]+=asil_sirasi;//sonra olusturdugumuz bir dizide en buyuk elemanin diger dizide hangi sirada oldugunu tuttuk
                koc_puan_dizi_son_liste[z]+=koc_puan_dizi_son[asil_sirasi];
                seyirci_puan_dizi_son_liste[z]+=seyirci_puan_dizi_son[asil_sirasi];


             int nm;
             for (nm=0;nm<yarismaci_say;nm++)
                   {
                     if (yarismaci_hafta_toplam_puan_dizi_kopya[nm]==sil&&nm==asil_sirasi)
                       {
                         yarismaci_hafta_toplam_puan_dizi_kopya[nm]=0;
                       }
                   }

                   int r;
                      for (r=0;r<yarismaci_say+1;r++)
                        {
                         yarismaci_hafta_toplam_puan_dizi_kopya[r]+= yarismaci_hafta_toplam_puan_dizi_kopya[r];
                        }

                for(i=0;i<5;i++)//silinecekler kontrol icin
                {
                    printf("\n%d",yarismaci_hafta_toplam_puan_dizi_kopya[i]);//silinecekler kontrol icin

                }

              printf("\n------------------");//silinecek


                z++;

               }//dondur for'unun bitisi.

              for(tur=1;tur<=yarismaci_say-1;tur++)
              {
                 for(d=0;d<=yarismaci_say-2;d++)
                 {
                    if(yarismaci_hafta_toplam_puan_dizi[d+1]>yarismaci_hafta_toplam_puan_dizi[d])
                    {
                       tut=yarismaci_hafta_toplam_puan_dizi[d+1];
                       yarismaci_hafta_toplam_puan_dizi[d+1]=yarismaci_hafta_toplam_puan_dizi[d];
                       yarismaci_hafta_toplam_puan_dizi[d]=tut;   //burda yarisma puani buyuk olani yer degistirerek dizimizi siraliyoruz.
                    }
                 }
              }
          printf("\n%d. haftanin sonuclari:",v);//o haftanin sonucunu cikaracak burasi
          printf("\n------------------------");
          printf("\n\n%s%14s%14s%18s%19s","Sira No","Yarismaci No","Koc Puani","Seyirci Puani","Toplam Puan");
          printf("\n%s%13s%15s%18s%20s","-------","-----------","---------","-------------","------------");

          for(g=0;g<yarismaci_say;g++)
          {
             printf("\n\n%d         %5d      %9d  %14d  %19d",g,yarismaci_no[g],koc_puan_dizi_son_liste[g],seyirci_puan_dizi_son_liste[g],yarismaci_hafta_toplam_puan_dizi[g]);
          }


              int don;
              for(don=0;don<yarismaci_say;don++)
              {
                koc_puan_dizi_genel[don]+=(koc_puan_dizi_son[don]);
                global_koc_puan_dizi_genel[don]+=(koc_puan_dizi_son[don]);//ikinci menu 1.istatistikte kullanmak icin global bir dizimize atýyoruz bunu.
                global_koc_puan_dizi_genel_yedek[don]+=(koc_puan_dizi_son[don]);//yedegini aldik sonra istatistik menusunde siralatacagiz puanari onun icin.Diger bir usteki de ayni dizi oluyor fakat onu sifirlayarak kullanacagimiz icin islem sonunda hepsi sira donusecek bunu kullanamayiz en son siralamada.
              }

                for(don=0;don<yarismaci_say;don++)
              {
                seyirci_puan_dizi_genel[don]+=(seyirci_puan_dizi_son[don]);
                global_seyirci_puan_dizi_genel[don]+=(seyirci_puan_dizi_son[don]);
                global_seyirci_puan_dizi_genel_yedek[don]+=(seyirci_puan_dizi_son[don]);
              }


            int pl;

            for(pl=0;pl<yarismaci_say;pl++)
             {
               seyirci_puan_dizi[pl]=0;//Burada dinamik dizimin butun elemanlarini 0 yaptim
               seyirci_puan_dizi_son[pl]=0;
              }

              for(pl=0;pl<yarismaci_say;pl++)
             {
               koc_puan_dizi[pl]=0;//Burada dinamik dizimin butun elemanlarini 0 yaptim
               koc_puan_dizi_son[pl]=0;
              }

              for(pl=0;pl<yarismaci_say;pl++)
             {
               yarismaci_hafta_toplam_puan_dizi[pl]=0;
             }

             for(pl=0;pl<yarismaci_say;pl++)
              {
                yarismaci_no[pl]=0;
              }

              for(pl=0;pl<yarismaci_say;pl++)
              {
                koc_puan_dizi_son_liste[pl]=0;
              }

               for(pl=0;pl<yarismaci_say;pl++)
              {
                seyirci_puan_dizi_son_liste[pl]=0;
              }


         }//koc ve seyircileri icine alan buyuk for

//*************************************************************************************************
               int dns;
                for(dns=0;dns<yarismaci_say;dns++)
              {
                yarismaci_hafta_toplam_puan_dizi_genel[dns]+=(koc_puan_dizi_genel[dns]+seyirci_puan_dizi_genel[dns]);
              }

                 for(dns=0;dns<yarismaci_say;dns++)//kopyaladik burda
              {
                yarismaci_hafta_toplam_puan_dizi_genel_kopya[dns]+=(yarismaci_hafta_toplam_puan_dizi_genel[dns]);

              }
         int nl,zl=0,silinen,donduren=0,sirasi2=0,buyuk2=0,asil_sirasi2=0;

           for(donduren=0;donduren<yarismaci_say;donduren++)
                {

                for(nl=0 ; nl<yarismaci_say ; nl++)
                 {

                   if(nl!=yarismaci_say-1)
                    {
                   int dft;
                   for(dft=0;dft<yarismaci_say;dft++)
                   {

                    int spt;
                    for(spt=0;spt<yarismaci_say;spt++)//bu dongude diziyi bir kere dolasip en buyugunu buluyor ilk.
                     {
                     if((yarismaci_hafta_toplam_puan_dizi_genel_kopya[spt]>yarismaci_hafta_toplam_puan_dizi_genel[(spt+1)])&&(yarismaci_hafta_toplam_puan_dizi_genel_kopya[spt]>buyuk2)&&(yarismaci_hafta_toplam_puan_dizi_genel_kopya[spt]!=yarismaci_hafta_toplam_puan_dizi_genel_kopya[yarismaci_say-1]))
                            {
                              buyuk2 = yarismaci_hafta_toplam_puan_dizi_genel_kopya[spt];
                              sirasi2=spt;//dizi elemani 0 dan basladigi icin 0 dan atiyor yarismaci sayisina.arti bir yaptigimizda tam yarismacinin sayisina denk geliyor
                              silinen=buyuk2;
                              asil_sirasi2=sirasi2;


                            }
                    else if((yarismaci_hafta_toplam_puan_dizi_genel_kopya[spt]>yarismaci_hafta_toplam_puan_dizi_genel[(spt+1)])&&(yarismaci_hafta_toplam_puan_dizi_genel_kopya[spt]>=buyuk2)&&(yarismaci_hafta_toplam_puan_dizi_genel_kopya[spt]==yarismaci_hafta_toplam_puan_dizi_genel_kopya[yarismaci_say-1]))
                            {
                                if(koc_puan_dizi_genel[spt]>koc_puan_dizi_genel[yarismaci_say-1])
                                asil_sirasi2=spt;

                                   else if(koc_puan_dizi_genel[spt]<koc_puan_dizi_genel[yarismaci_say-1])
                                     asil_sirasi2=(yarismaci_say-1);



                               else if(koc_puan_dizi_genel[spt]==koc_puan_dizi_genel[yarismaci_say-1])
                                 {
                                  if(spt<(yarismaci_say-1))
                                     asil_sirasi2=spt;
                                  else
                                    asil_sirasi2=(yarismaci_say-1);
                                 }

                             }
                     else

                        if((yarismaci_hafta_toplam_puan_dizi_genel_kopya[yarismaci_say-1]>yarismaci_hafta_toplam_puan_dizi_genel_kopya[0])&&(yarismaci_hafta_toplam_puan_dizi_genel_kopya[yarismaci_say-1]>buyuk2))
                         {
                          buyuk2 = yarismaci_hafta_toplam_puan_dizi_genel_kopya[yarismaci_say-1];
                          sirasi2=(yarismaci_say-1);//dizi elemani 0 dan basladigi icin 0 dan atiyor yarismaci sayisina.arti bir yaptigimizda tam yarismacinin sayisina denk geliyor
                          silinen=buyuk2;
                          asil_sirasi2=sirasi2;
                         }

                     }//sp for'unun bitisi icin.En buyugu donduren ve bulduran alan.bu bittiginde en buyuk elimizde oluyor.


              }//dft foru icin.



                     }

                     buyuk2=0;//en son elemani da bulmasi icin bunu yaptik.
                }//bu for diziyi dolasip en buyuk elemani bulduruyor


                yarismaci_no_genel[zl]+=asil_sirasi2;//sonra olusturdugumuz bir dizide en buyuk elemanin diger dizide hangi sirada oldugunu tuttuk
                koc_puan_dizi_genel_liste[zl]+=koc_puan_dizi_genel[asil_sirasi2];
                seyirci_puan_dizi_genel_liste[zl]+=seyirci_puan_dizi_genel[asil_sirasi2];


             int nmt;
             for (nmt=0;nmt<yarismaci_say;nmt++)
                   {
                     if (yarismaci_hafta_toplam_puan_dizi_genel_kopya[nmt]==silinen&&nmt==asil_sirasi2)
                       {
                         yarismaci_hafta_toplam_puan_dizi_genel_kopya[nmt]=0;
                       }
                   }

                   int rl;
                      for (rl=0;rl<yarismaci_say+1;rl++)
                        {
                         yarismaci_hafta_toplam_puan_dizi_genel_kopya[rl]+= yarismaci_hafta_toplam_puan_dizi_genel_kopya[rl];
                        }


                zl++;
               }//donduren for'unun bitisi.

//**********************************************************************************************************************

              int turla,dn=0,tutucu;
              for(turla=1;turla<=yarismaci_say-1;turla++)
              {
                 for(dn=0;dn<=yarismaci_say-2;dn++)
                 {
                    if(yarismaci_hafta_toplam_puan_dizi_genel[dn+1]>yarismaci_hafta_toplam_puan_dizi_genel[dn])
                    {
                       tutucu=yarismaci_hafta_toplam_puan_dizi_genel[dn+1];
                       yarismaci_hafta_toplam_puan_dizi_genel[dn+1]=yarismaci_hafta_toplam_puan_dizi_genel[dn];
                       yarismaci_hafta_toplam_puan_dizi_genel[dn]=tutucu;   //burda yarisma puani buyuk olani yer degistirerek dizimizi siraliyoruz.
                    }
                 }
              }


          printf("\n%d. hafta sonunda genel durum:",(v-1));//o haftanin sonucunu cikaracak burasi
          printf("\n-------------------------------");
          printf("\n\n%s%14s%14s%18s%19s","Sira No","Yarismaci No","Koc Puani","Seyirci Puani","Toplam Puan");
          printf("\n%s%13s%15s%18s%20s","-------","-----------","---------","-------------","------------");

          for(gl=0;gl<yarismaci_say;gl++)
          {
             printf("\n\n%d         %5d      %9d  %14d  %19d",gl,yarismaci_no_genel[gl],koc_puan_dizi_genel_liste[gl],seyirci_puan_dizi_genel_liste[gl],yarismaci_hafta_toplam_puan_dizi_genel[gl]);
          }
           sectigi=menu();
         }while(sectigi==1);


    if(sectigi==2)
    {

     int secilen;
      do{
      secilen=menu2();

       if(secilen==1)
          sadece_koc_puanlamasi_dikkate_alindiginda_genel_durum_listele(yarismaci_say, koc_puan_dizi_genel[yarismaci_say]);

       else if(secilen==2)
         sadece_seyircilerin_puanlamasi_dikkate_alindiginda_genel_durum_listele(yarismaci_say,seyirci_puan_dizi_genel[yarismaci_say]);

       //else if(secilen==3)
       //yarismacilarin_her_hafta_aldiklari_toplam_puanlari_listele(yarismaci_say,devam_hafta_say,her_haftanin_toplam_puanlarini_tutan_dizi[10][yarismaci_say],birincilik_say[yarismaci_say]);

     else if(secilen==4)
         //yarismacilarin_her_koctan_aldiklari_toplam_puanlari_listele(secim);

       if(secilen==5)
         return menu();

     }while(secilen>=1&&secilen<=5);

    }

   if(sectigi==3)
      system("cls");


}//fonksiyon bitisi


int son_duzenlenen_yarisma_istatistikleri()
{
  int sec;
   sec=menu2();
   return sec;
}//fonksiyon sonu.

void sadece_koc_puanlamasi_dikkate_alindiginda_genel_durum_listele( int yarismaciSay, int * koc_puan_dizi_genell[])
{
   int n,z=0,f,sil,b,dondur=0,sirasi=0,buyuk=0,asil_sirasi=0;
   int *koc_puan_dizi_genel_yedek,*yarismaciNo;

           yarismaciNo = (int *) malloc((yarismaciSay*sizeof(int)));
          for(f=0;f<yarismaciSay;f++)
             {
               yarismaciNo[f]=0;
             }

         koc_puan_dizi_genel_yedek = (int *) malloc((yarismaciSay*sizeof(int)));
           for(f=0;f<yarismaciSay;f++)
               {
                 koc_puan_dizi_genel_yedek[f]=0;
               }


                for(f=0;f<yarismaciSay;f++)
               {
                 koc_puan_dizi_genel_yedek[f]+=koc_puan_dizi_genell[f];
               }


              for(dondur=0;dondur<yarismaciSay;dondur++)
                {

                for(n=0 ; n<yarismaciSay ; n++)
                 {

                   if(n!=yarismaciSay-1)
                    {
                   int df;
                   for(df=0;df<yarismaciSay;df++)
                   {

                    int sp;
                    for(sp=0;sp<yarismaciSay;sp++)//bu dongude diziyi bir kere dolasip en buyugunu buluyor ilk.
                     {
                     if((*koc_puan_dizi_genell[sp]>*koc_puan_dizi_genell[(sp+1)])&&(*koc_puan_dizi_genell[sp]>buyuk)&&(*koc_puan_dizi_genell[sp]!=*koc_puan_dizi_genell[yarismaciSay-1]))
                            {
                              buyuk = *koc_puan_dizi_genell[sp];
                              sirasi=sp;//dizi elemani 0 dan basladigi icin 0 dan atiyor yarismaci sayisina.arti bir yaptigimizda tam yarismacinin sayisina denk geliyor
                              sil=buyuk;
                              asil_sirasi=sirasi;


                            }
                    else if((*koc_puan_dizi_genell[sp]>*koc_puan_dizi_genell[(sp+1)])&&(*koc_puan_dizi_genell[sp]>=buyuk)&&(*koc_puan_dizi_genell[sp]==*koc_puan_dizi_genell[yarismaciSay-1]))
                            {
                                  if(sp<(yarismaciSay-1))
                                     asil_sirasi=sp;

                             }
                     else

                        if((*koc_puan_dizi_genell[yarismaciSay-1]>*koc_puan_dizi_genell[0])&&(*koc_puan_dizi_genell[yarismaciSay-1]>buyuk))
                         {
                          buyuk = *koc_puan_dizi_genell[yarismaciSay-1];
                          sirasi=(yarismaciSay-1);//dizi elemani 0 dan basladigi icin 0 dan atiyor yarismaci sayisina.arti bir yaptigimizda tam yarismacinin sayisina denk geliyor
                          sil=buyuk;
                          asil_sirasi=sirasi;
                         }

                     }//sp for'unun bitisi icin.En buyugu donduren ve bulduran alan.bu bittiginde en buyuk elimizde oluyor.


              }//df foru icin.

                     }

                     buyuk=0;//en son elemani da bulmasi icin bunu yaptik.
                }//bu for diziyi dolasip en buyuk elemani bulduruyor


                yarismaciNo[z]+=asil_sirasi;//sonra olusturdugumuz bir dizide en buyuk elemanin diger dizide hangi sirada oldugunu tuttuk


             int nm;
             for (nm=0;nm<yarismaciSay;nm++)
                   {
                     if (*koc_puan_dizi_genell[nm]==sil&&nm==asil_sirasi)
                       {
                         *koc_puan_dizi_genell[nm]=0;//burda sifirlaniyor ya bu dizi o nedenle yedegini tutmaliyiz sonra siralatma icin
                       }
                   }

                   int r;
                      for (r=0;r<yarismaciSay+1;r++)
                        {
                         *koc_puan_dizi_genell[r]+=*koc_puan_dizi_genell[r];
                        }

                z++;

               }
printf("*************girdi**************");
               /* int turla,dn=0,tutucu,gl=0;
              for(turla=1;turla<=yarismaciSay-1;turla++)
              {
                 for(dn=0;dn<=yarismaciSay-2;dn++)
                 {
                    if(koc_puan_dizi_genel_yedek[dn+1]>koc_puan_dizi_genel_yedek[dn])
                    {
                       tutucu=koc_puan_dizi_genel_yedek[dn+1];
                       koc_puan_dizi_genel_yedek[dn+1]=koc_puan_dizi_genel_yedek[dn];
                       koc_puan_dizi_genel_yedek[dn]=tutucu;   //burda yarisma puani buyuk olani yer degistirerek dizimizi siraliyoruz.
                    }
                 }
              }

          printf("\nSadece Koclarin Puanlamasina Gore Genel Durum");//o haftanin sonucunu cikaracak burasi
          printf("\n-----------------------------------------------");
          printf("\n\n%s%14s%21s","Sira No","Yarismaci No","Puan");
          printf("\n%s%13s%23s","-------","-----------","-------");

          for(gl=0;gl<yarismaciSay;gl++)
          {
             printf("\n\n%d         %5d       %19d",gl,yarismaciNo[gl],koc_puan_dizi_genel_yedek[gl]);
          }*/



}

void sadece_seyircilerin_puanlamasi_dikkate_alindiginda_genel_durum_listele(int yarismaciSay,int *seyirci_puan_dizi_genel[])
{
  int n,z=0,f,sil,b,dondur=0,sirasi=0,buyuk=0,asil_sirasi=0;
   int *seyirci_puan_dizi_genel_yedek,*yarismaciNo;

           yarismaciNo = (int *) malloc((yarismaciSay*sizeof(int)));
          for(f=0;f<yarismaciSay;f++)
             {
               yarismaciNo[f]=0;
             }


          seyirci_puan_dizi_genel_yedek = (int *) malloc((yarismaciSay*sizeof(int)));
          for(f=0;f<yarismaciSay;f++)
             {
              seyirci_puan_dizi_genel_yedek[f]=0;
             }

               for(f=0;f<yarismaciSay;f++)
               {
                  seyirci_puan_dizi_genel_yedek[f]+=seyirci_puan_dizi_genel[f];
               }

               for(dondur=0;dondur<yarismaciSay;dondur++)
                {

                for(n=0 ; n<yarismaciSay ; n++)
                 {

                   if(n!=yarismaciSay-1)
                    {
                   int df;
                   for(df=0;df<yarismaciSay;df++)
                   {

                    int sp;
                    for(sp=0;sp<yarismaciSay;sp++)//bu dongude diziyi bir kere dolasip en buyugunu buluyor ilk.
                     {
                     if((seyirci_puan_dizi_genel[sp]>seyirci_puan_dizi_genel[(sp+1)])&&(seyirci_puan_dizi_genel[sp]>buyuk)&&(seyirci_puan_dizi_genel[sp]!=seyirci_puan_dizi_genel[yarismaciSay-1]))
                            {
                              buyuk = seyirci_puan_dizi_genel[sp];
                              sirasi=sp;//dizi elemani 0 dan basladigi icin 0 dan atiyor yarismaci sayisina.arti bir yaptigimizda tam yarismacinin sayisina denk geliyor
                              sil=buyuk;
                              asil_sirasi=sirasi;


                            }
                    else if((seyirci_puan_dizi_genel[sp]>seyirci_puan_dizi_genel[(sp+1)])&&(seyirci_puan_dizi_genel[sp]>=buyuk)&&(seyirci_puan_dizi_genel[sp]==seyirci_puan_dizi_genel[yarismaciSay-1]))
                            {
                                  if(sp<(yarismaciSay-1))
                                     asil_sirasi=sp;

                             }
                     else

                        if((seyirci_puan_dizi_genel[yarismaciSay-1]>seyirci_puan_dizi_genel[0])&&(seyirci_puan_dizi_genel[yarismaciSay-1]>buyuk))
                         {
                          buyuk = seyirci_puan_dizi_genel[yarismaciSay-1];
                          sirasi=(yarismaciSay-1);//dizi elemani 0 dan basladigi icin 0 dan atiyor yarismaci sayisina.arti bir yaptigimizda tam yarismacinin sayisina denk geliyor
                          sil=buyuk;
                          asil_sirasi=sirasi;
                         }

                     }//sp for'unun bitisi icin.En buyugu donduren ve bulduran alan.bu bittiginde en buyuk elimizde oluyor.


              }//df foru icin.

                     }

                     buyuk=0;//en son elemani da bulmasi icin bunu yaptik.
                }//bu for diziyi dolasip en buyuk elemani bulduruyor


                yarismaciNo[z]+=asil_sirasi;//sonra olusturdugumuz bir dizide en buyuk elemanin diger dizide hangi sirada oldugunu tuttuk


             int nm;
             for (nm=0;nm<yarismaciSay;nm++)
                   {
                     if (seyirci_puan_dizi_genel[nm]==sil&&nm==asil_sirasi)
                       {
                         seyirci_puan_dizi_genel[nm]=0;//burda sifirlaniyor ya bu dizi o nedenle yedegini tutmaliyiz sonra siralatma icin
                       }
                   }

                   int r;
                      for (r=0;r<yarismaciSay+1;r++)
                        {
                         *seyirci_puan_dizi_genel[r]+=*seyirci_puan_dizi_genel[r];
                        }

                z++;

               }

                int turla,dn=0,tutucu,gl=0;
              for(turla=1;turla<=yarismaciSay-1;turla++)
              {
                 for(dn=0;dn<=yarismaciSay-2;dn++)
                 {
                    if(seyirci_puan_dizi_genel_yedek[dn+1]>seyirci_puan_dizi_genel_yedek[dn])
                    {
                       tutucu=seyirci_puan_dizi_genel_yedek[dn+1];
                       seyirci_puan_dizi_genel_yedek[dn+1]=seyirci_puan_dizi_genel_yedek[dn];
                       seyirci_puan_dizi_genel_yedek[dn]=tutucu;   //burda yarisma puani buyuk olani yer degistirerek dizimizi siraliyoruz.
                    }
                 }
              }

          printf("\nSadece Seyircilerin Puanlamasina Gore Genel Durum");//o haftanin sonucunu cikaracak burasi
          printf("\n-----------------------------------------------");
          printf("\n\n%s%14s%21s","Sira No","Yarismaci No","Puan");
          printf("\n%s%13s%23s","-------","-----------","-------");

          for(gl=0;gl<yarismaciSay;gl++)
          {
             printf("\n\n%d         %5d       %19d",gl,yarismaciNo[gl],seyirci_puan_dizi_genel_yedek[gl]);
          }


}

  /*void yarismacilarin_her_hafta_aldiklari_toplam_puanlari_listele(int yarismaciSay,int haftaSay,int istatistik_haftalik_toplam_puan[10][],int birincilikSay[])
           {

              int il, jl, kl, ll;
                  printf("\nYarismacilarin Her Hafta Aldiklari Toplam Puanlar"
                          "\nYarismaci No");
                   for(il=0;il<haftaSay;il++)
                    {
                       printf(" %d.Hafta",il+1);
                    }
                   printf(" 1.lik Sayisi \n------------");
                   for(jl=0;jl<haftaSay;jl++)
                    {
                       printf(" -------");
                     }
                   printf(" -----------");

                  for(kl=0;kl<yarismaciSay;kl++)
                    {
                      printf("\n%7d  ",kl+1);
                      for(ll=0;ll<3;ll++)
                        {
                           printf("%8d",istatistik_haftalik_toplam_puan[ll][kl]);
                        }

                     printf("%11d",birincilikSay[kl]);

                      }




           }//fonksiyon bitisi.*/

