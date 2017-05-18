#include <stdio.h>
#include <stdlib.h>
struct Sporcular
{
  int lisans;
  char tc_no[11];
  char ad_soyad[30];
  int plaka_kod;
  int UKD_puan;
};
struct Turnuva
{
  int turnuva_no;
  char turnuva_adi[40];
  char turnuva_tarihi[10];
  char turnuva_sehir[15];
};
typedef struct Sporcular Oyuncular;
typedef struct Turnuva Turnuvalar;
int menu();
void yeni_oyuncu_ekle(FILE*);
void bir_oyuncu_listele(FILE*);
void il_guncelleme(FILE*);
void biten_turnuva_bilgi_aktar(FILE*,FILE*,FILE*,FILE*,FILE*);
void bir_il_oyuncu_listele(FILE*);
void sporcu_lisans_siralama(int[],int[],int[],char[],char[],int);
void sporcu_il_siralama(int[],int);
void yer_degistirme(int *,int *);
void char_yer_degistirme(char *,char *);
void bir_il_oyuncu_sayisi(FILE*);
void siyah_beyaz(FILE *);
int main()
{
  int sec;
  FILE *sporcularptr;
  sporcularptr=fopen("sporcular.dat","a+");//sporcular.dat dosyasini okuyup guncellemek icin dosyayi actik.
  if((sporcularptr=fopen("sporcular.dat","a+"))==NULL)
  printf("Sporcular dosyasi acilamadi.\n");
  FILE *turnuvalarptr;
  turnuvalarptr=fopen("turnuvalar.dat","a+");//turnuvalar.dat dosyasini okuyup guncellemek icin dosyayi actik.
  if((turnuvalarptr=fopen("turnuvalar.dat","a+"))==NULL)
  printf("Turnuvalar dosyasi acilamadi.\n");
  FILE *tum_maclarptr;
  tum_maclarptr=fopen("tum_maclar.txt","a+");//tum_maclar.txt dosyasini okuyup guncellemek icin dosyayi actik.
  if((tum_maclarptr=fopen("tum_maclar.txt","a+"))==NULL)
  printf("Tum maclar dosyasi acilamadi.\n");
  FILE *turnuva_genelptr;
  turnuva_genelptr=fopen("turnuva_genel.txt","r");//turnuva_genel.txt dosyasini okuyup guncellemek icin dosyayi actik.
  if((turnuva_genelptr=fopen("turnuva_genel.txt","r"))==NULL)
  printf("Turnuva genel dosyasi acilamadi.\n");
  FILE *turnuva_maclarptr;
  turnuva_maclarptr=fopen("turnuva_maclar.txt","r");//turnuva_maclar.txt dosyasini okuyup guncellemek icin dosyayi actik.
  if((turnuva_maclarptr=fopen("turnuva_maclar.txt","r"))==NULL)
  printf("Turnuva maclar dosyasi acilamadi.\n");
  switch(sec=menu())
  {
    case 1:
      biten_turnuva_bilgi_aktar(turnuva_genelptr,turnuva_maclarptr,tum_maclarptr,turnuvalarptr,sporcularptr);
      break;
    case 2:
      bir_oyuncu_listele(sporcularptr);
      break;
    case 3:
      break;
    case 4:
      bir_il_oyuncu_listele(sporcularptr);
      break;
    case 5:
      break;
    case 6:
      bir_il_oyuncu_sayisi(sporcularptr);
      break;
    case 7:
      break;
    case 8:
    siyah_beyaz(tum_maclarptr);
      break;
    case 9:
      yeni_oyuncu_ekle(sporcularptr);
      break;
    case 10:
      il_guncelleme(sporcularptr);
      break;
    case 11:
      break;
  }
   fclose(sporcularptr);
   fclose(turnuvalarptr);
   fclose(tum_maclarptr);
   fclose(turnuva_genelptr);
   fclose(turnuva_maclarptr);
    return 0;
}
int menu(void)
{
  int secim;
    printf("\n\n1)Biten bir turnuvaya iliskin bilgilerin sisteme aktarilmasi\n"
           "2)Bir oyuncunun bilgilerinin listelenmesi\n"
           "3)Bir oyuncunun bilgilerinin ve katildigi turnuvalarda oynadigi maclarin listelenmesi\n"
           "4)Bir ildeki tum oyuncularin listelenmesi\n"
           "5)UKD puani en yuksek 10 oyuncunun listelenmesi\n"
           "6)Illerdeki oyuncu sayisinin listelenmesi\n"
           "7)Bir turnuvanin bilgilerinin ve turnuvada oynanan maclarin listelenmesi\n"
           "8)Tum maclardaki beyaz-siyah karsilastirmasi\n"
           "9)Yeni bir oyuncunun eklenmesi\n"
           "10)Bir oyuncunun ilinin guncellenmesi\n"
           "11)Cikis\n\n");
           do
           {
             scanf("%d",&secim);
           }while(secim<1 || secim>11);
           return secim;
}
void yeni_oyuncu_ekle(FILE *sporcularptr)
{
  Oyuncular birOyuncu;
  int yeni_lisans,i,k,ukd=0;
  do{
   printf("Eklenecek oyuncunun lisans numarasini giriniz:");
   scanf("%d",&yeni_lisans);
   for(i=0;i<9999;i++)
   {
     fseek(sporcularptr,i*sizeof(Oyuncular),SEEK_SET);
     fread(&birOyuncu,sizeof(Oyuncular),1,sporcularptr);
      k=0;
      if(birOyuncu.lisans==yeni_lisans)
      {
         printf("Bu lisans numarali oyuncu mevcut,lutfen baska numara giriniz:\n");
         k=1;
         break;
      }
   }
  }while(k==1);
   printf("Oyuncunun adi-soyadini giriniz:");
   fflush(stdin);
    gets(birOyuncu.ad_soyad);
   printf("\nOyuncunun TC kimlik no'sunu giriniz:");
   fflush(stdin);
    gets(birOyuncu.tc_no);
   printf("Il plaka kodunu giriniz:");
    scanf("%d",&birOyuncu.plaka_kod);
    birOyuncu.UKD_puan=ukd;
    birOyuncu.lisans=yeni_lisans;
    fseek(sporcularptr,(yeni_lisans-1)*sizeof(Oyuncular),SEEK_SET);
    fwrite(&birOyuncu,sizeof(Oyuncular),1,sporcularptr);// Bilgileri dosyada guncelliyor.
    rewind(sporcularptr);
    main();
}
void bir_oyuncu_listele(FILE*sporcularptr)
{
  Oyuncular birOyuncu;
  char tc_num[11];
  int i;
    printf("\nOyuncunun TC kimlik no'sunu giriniz:");
    fflush(stdin);
    gets(tc_num);
       printf("\nLisans No       TC Kimlik No       Ad Soyad       Ili       UKD Puani\n");
       printf("----------   ------------        -----------      ----       ----------  ");
   for(i=0;i<9999;i++)
   {
     fseek(sporcularptr,i*sizeof(Oyuncular),SEEK_SET);
     fread(&birOyuncu,sizeof(Oyuncular),1,sporcularptr);
       if(strcmp(tc_num,birOyuncu.tc_no)==0)
        break;
   }
   printf("\n%-10d    %7s           %7s    %7d        %10d",birOyuncu.lisans,birOyuncu.tc_no,birOyuncu.ad_soyad,birOyuncu.plaka_kod,birOyuncu.UKD_puan);
    main();
}
void il_guncelleme(FILE*sporcularptr)
{
    Oyuncular birOyuncu;
    int il_plaka,lisans,i;
    printf("Ilini guncellemek istediginiz oyuncunun lisans numarasini giriniz:");
    scanf("%d",&lisans);
    for(i=0;i<9999;i++)
   {
     fseek(sporcularptr,i*sizeof(Oyuncular),SEEK_SET);
     fread(&birOyuncu,sizeof(Oyuncular),1,sporcularptr);
       if(birOyuncu.lisans==lisans)
        {
          printf("Yeni il plaka kodunu giriniz: \n");
          scanf("%d",&il_plaka);
          birOyuncu.plaka_kod=il_plaka;
          fseek(sporcularptr,i*sizeof(Oyuncular),SEEK_SET);
          fwrite(&birOyuncu,sizeof(Oyuncular),1,sporcularptr);
          break;
        }
        else
        printf("Bu lisans numarasina sahip sporcu bulunamadi.\n");
   }
    main();
}
void biten_turnuva_bilgi_aktar(FILE*turnuva_genelptr,FILE*turnuva_maclarptr,FILE*tum_maclarptr,FILE*turnuvalarptr,FILE*sporcularptr)
{
  Turnuvalar birTurnuva;
  Oyuncular birOyuncu;
   char turnuva_ad[40],turnuva_tarih[10],turnuva_sehir[15];
   int lisans_no[9000],i=0,tur_no,beyaz_lisans,siyah_lisans,sonuc,turnuva_no=1;
   float UKD_ort,beyaz_UKD_degisim,siyah_UKD_degisim;
    fscanf(turnuva_genelptr,"%s\n%s\n%s\n%f\n",turnuva_ad,turnuva_tarih,turnuva_sehir,&UKD_ort);
  while(!feof(turnuva_genelptr))
    {
      fscanf(turnuva_genelptr,"%d\n",&lisans_no[i]);
      i++;
    }
     fscanf(turnuva_maclarptr,"%d\n%d\n%d\n%d\n%f\n%f\n",&tur_no,&beyaz_lisans,&siyah_lisans,&sonuc,&beyaz_UKD_degisim,&siyah_UKD_degisim);
     while(!feof(sporcularptr))
     {
       fseek(sporcularptr,sizeof(Oyuncular),SEEK_SET);
       fread(&birOyuncu,sizeof(Oyuncular),1,sporcularptr);
       if(beyaz_lisans==birOyuncu.lisans)
       {
         birOyuncu.UKD_puan+=beyaz_UKD_degisim;
           if(birOyuncu.UKD_puan<1000)
           birOyuncu.UKD_puan=0;
       }
       if(siyah_lisans==birOyuncu.lisans)
       {
         birOyuncu.UKD_puan+=siyah_UKD_degisim;
          if(birOyuncu.UKD_puan<1000)
           birOyuncu.UKD_puan=0;
       }
     }
    rewind(turnuva_genelptr);
    rewind(turnuva_maclarptr);
    birTurnuva.turnuva_no=turnuva_no;
    strcpy(birTurnuva.turnuva_adi,turnuva_ad);
    strcpy(birTurnuva.turnuva_tarihi,turnuva_tarih);
    strcpy(birTurnuva.turnuva_sehir,turnuva_sehir);
    fwrite(&birTurnuva,sizeof(Turnuvalar),1,turnuvalarptr);//Dogrudan(rastgele) erisimli dosyaya fwrite fonk.ile yazdirma yaptik.
    fprintf(tum_maclarptr,"&d\n&d\n&d\n&d\n&d\n&.3f\n&.3f",&turnuva_no,&tur_no,&beyaz_lisans,&siyah_lisans,&sonuc,&beyaz_UKD_degisim,&siyah_UKD_degisim);
    turnuva_no++;
    main();
}
void bir_il_oyuncu_listele(FILE*sporcularptr)
{
  Oyuncular birOyuncu;
  int oyuncu_il_plaka_kod,lisans_dizi[20]={0},plaka_dizi[20]={0},UKD_dizi[20],oyuncu_say=0,j,i;
  char TC_dizi[20],ad_soyad_dizi[20];
       printf("Oyuncularini gormak istediginiz ilin plaka kodunu giriniz:");
        scanf("%d",&oyuncu_il_plaka_kod);
    while(!feof(sporcularptr))
    {
      fread(&birOyuncu,sizeof(Oyuncular),1,sporcularptr);
        while( oyuncu_il_plaka_kod==birOyuncu.plaka_kod) //Eger aranan kodla dosyadaki kod eslesirse donguden cikiliyor.
            {
              lisans_dizi[oyuncu_say]=birOyuncu.lisans;
            plaka_dizi[oyuncu_say]=birOyuncu.plaka_kod;
            UKD_dizi[oyuncu_say]=birOyuncu.UKD_puan;
            strcpy(&TC_dizi[oyuncu_say],birOyuncu.tc_no);
            strcpy(&ad_soyad_dizi[oyuncu_say],birOyuncu.ad_soyad);
            oyuncu_say++;
            }
    }
       printf("\n\nLisans No      TC Numarasi      Adi Soyadi      Plaka No      UKD Puani\n");
        printf("--------      ------------      ----------      --------      ---------\n");
       sporcu_lisans_siralama(lisans_dizi,plaka_dizi,UKD_dizi,TC_dizi,ad_soyad_dizi,oyuncu_say);
          for(j=1;j<oyuncu_say-1;j++)
                {
                  fseek(sporcularptr,j*sizeof(Oyuncular),SEEK_SET); //Takim sayisi kadar dondurulerek bilgiler okutuluyor.
                  fread(&birOyuncu,sizeof(Oyuncular),1,sporcularptr);
                  printf("%-10d     %6s        %10s     %8d           %2d\n",lisans_dizi[oyuncu_say],birOyuncu.tc_no,birOyuncu.ad_soyad,plaka_dizi[j],birOyuncu.UKD_puan);
                }
      /* while(!feof(sporcularptr))
       {
          fread(&birOyuncu,sizeof(Oyuncular),1,sporcularptr);
          if(birOyuncu.plaka_kod==oyuncu_il_plaka_kod)
          {
            lisans_dizi[oyuncu_say]=birOyuncu.lisans;
            plaka_dizi[oyuncu_say]=birOyuncu.plaka_kod;
            UKD_dizi[oyuncu_say]=birOyuncu.UKD_puan;
            strcpy(&TC_dizi[oyuncu_say],birOyuncu.tc_no);
            strcpy(&ad_soyad_dizi[oyuncu_say],birOyuncu.ad_soyad);
            oyuncu_say++;
          }
       }
       printf("\n\nLisans No      TC Numarasi      Adi Soyadi      Plaka No      UKD Puani\n");
        printf("--------      ------------      ----------      --------      ---------\n");
sporcu_lisans_siralama(lisans_dizi,plaka_dizi,UKD_dizi,TC_dizi,ad_soyad_dizi,oyuncu_say);
for(j=0;j<oyuncu_say-1;j++)
                {
                  fseek(sporcularptr,j*sizeof(Oyuncular),SEEK_SET); //Takim sayisi kadar dondurulerek bilgiler okutuluyor.
                  fread(&birOyuncu,sizeof(Oyuncular),1,sporcularptr);
                  printf("%-10d     %6s        %10s     %8d           %2d\n",lisans_dizi[j],birOyuncu.tc_no,birOyuncu.ad_soyad,plaka_dizi[j],birOyuncu.UKD_puan);
                }*/
    main();
}
void yer_degistirme(int *gecici1,int *gecici2)
{
    int gecici_sayi;
    gecici_sayi=*gecici1;
    *gecici1=*gecici2;
    *gecici2=gecici_sayi;
}
void char_yer_degistirme(char *gecici1,char *gecici2)
{
    char gecici_sayi;
    gecici_sayi=*gecici1;
    *gecici1=*gecici2;
    *gecici2=gecici_sayi;
}
void sporcu_lisans_siralama(int lisans_dizi[],int plaka_dizi[],int UKD_dizi[],char TC_dizi[],char ad_soyad_dizi[],int sporcu_say)
{
    int j,gecis_say=0,switched;
    do
    {
        switched=0; //Degisim yapilip yapilmadigini anlamak icin bu degiskeni kullaniyoruz.
        gecis_say++; //Degistirilen sporculari tekrar donguye sokmamak icin bu degiskeni kullaniyoruz.
        for(j=0;j<sporcu_say-gecis_say;j++)
        {
            if(lisans_dizi[j]>lisans_dizi[j+1]) //Sporculari diziler yardimiyla toplu olarak yerleri degistiriyoruz.
            {
                yer_degistirme(&lisans_dizi[j],&lisans_dizi[j+1]);
                yer_degistirme(&plaka_dizi[j],&plaka_dizi[j+1]);
                yer_degistirme(&UKD_dizi[j],&UKD_dizi[j+1]);
                char_yer_degistirme(&TC_dizi[j],&TC_dizi[j+1]);
                char_yer_degistirme(&ad_soyad_dizi[j],&ad_soyad_dizi[j+1]);
                switched=1;
            }
        }
    }while(switched==1);
}
void sporcu_il_siralama(int plaka_dizi[],int sporcu_say)
{
    int j,gecis_say=0,switched;
    do
    {
        switched=0; //Degisim yapilip yapilmadigini anlamak icin bu degiskeni kullaniyoruz.
        gecis_say++; //Degistirilen sporculari tekrar donguye sokmamak icin bu degiskeni kullaniyoruz.
        for(j=0;j<sporcu_say-gecis_say;j++)
        {
            if(plaka_dizi[j]>plaka_dizi[j+1]) //Sporculari diziler yardimiyla toplu olarak yerleri degistiriyoruz.
            {
                yer_degistirme(&plaka_dizi[j],&plaka_dizi[j+1]);
                switched=1;
            }
        }
    }while(switched==1);
}
void bir_il_oyuncu_sayisi(FILE*sporcularptr)
{
  Oyuncular birOyuncu;
   int lisans_dizi[20],plaka_dizi[20],oyuncu_say=0,iller[81]={0},j,k, toplamiller=0;
    while(!feof(sporcularptr))
       {
         fread(&birOyuncu,sizeof(Oyuncular),1,sporcularptr);
            plaka_dizi[oyuncu_say]=birOyuncu.plaka_kod;
            iller[birOyuncu.plaka_kod]++;
            oyuncu_say++;
       }
       sporcu_il_siralama( plaka_dizi, oyuncu_say);
       for(k=0;k<81;k++)
            {
              if(iller[k]!=0)
              {
                toplamiller++;
              }
            }
        printf("Plaka No      Oyuncu Sayisi\n");
        printf("--------      -------------\n");
       for(j=0;j<oyuncu_say-1;j++)
       {
             printf("%d              %d\n",plaka_dizi[j],iller[plaka_dizi[j]]);
       }
    main();
}
void siyah_beyaz(FILE *tum_maclarptr)
{
    int turnuva_no,tur_no,beyaz,siyah,sonuc;
    float beyaz_ukd,siyah_ukd,toplam_puan_siyah=0,toplam_puan_beyaz=0,toplam_ukd_beyaz=0,toplam_ukd_siyah=0;
    printf("                     Beyaz Oynayanlar  Siyah Oynayanlar"
           "                     ----------------  ----------------");
    while(!feof(tum_maclarptr))
    {
        fscanf(tum_maclarptr,"%d\n%d\n%d\n%d\n%d\n%f\n%f\n",&turnuva_no,&tur_no,&beyaz,&siyah,&sonuc,&beyaz_ukd,&siyah_ukd);
        if(sonuc==1)
        {
            toplam_puan_beyaz+=1;
        }
        else if(sonuc==2)
        {
            toplam_puan_siyah+=1;
        }
        else
        {
            toplam_puan_beyaz+=(0.5);
            toplam_puan_siyah+=(0.5);
        }
        toplam_ukd_beyaz+=beyaz_ukd;
        toplam_ukd_siyah+=siyah_ukd;
    }
    printf("Toplam Mac Puani     %-16f  %16f"
           "Toplam UKD Deðisimi  %-16f  %16f",toplam_puan_beyaz,toplam_puan_siyah,toplam_ukd_beyaz,toplam_ukd_siyah);
}

void bir_oyuncu_butun_bilgiler(FILE *sporcularptr,FILE *tum_maclarptr,FILE *turnuvalarptr)
{
    Oyuncular birOyuncu;
    Turnuvalar birTurnuva;
    int lisans_bir_oyuncu,flag=0,turnuva_numarasi,tur_no,beyaz_lisans,siyah_lisans,sonuc,i;
    float beyaz_UKD_degisim,siyah_UKD_degisim,rakip_UKD,tek_UKD_degisim,toplam_UKD_degisim=0,mac_puani,toplam_mac_puani=0;
    char rakip_isim[30];
    do
    {
        printf("Bilgilerini gormek istediginiz oyuncunun lisans numarasini giriniz:");
        scanf("%d",&lisans_bir_oyuncu);

      for(i=0;i<9999;i++)
      {
        fread(&birOyuncu,sizeof(Oyuncular),1,sporcularptr);
        if(birOyuncu.lisans==0)
        {
            printf("Boyle bir oyuncu bulunmamaktadir.\n");
            flag++;
        }
        if(lisans_bir_oyuncu==birOyuncu.lisans)
        break;
      }
    }while(flag==1);
    printf("Lisans No  TC Kimlik No  Ad Soyad              Ili  UKD Puani\n"
           "---------  ------------  --------------------- ---  ---------\n"
           "%-9d  %12s  %21s %3d  %9d\n\n",birOyuncu.lisans,birOyuncu.tc_no,birOyuncu.ad_soyad,birOyuncu.plaka_kod,birOyuncu.UKD_puan);
    printf("Katildigi Turnuvalar ve Oynadigi Maclar:\n");
    while(!feof(tum_maclarptr))
    {
        fscanf(tum_maclarptr,"%d\n%d\n%d\n%d\n%d\n%f\n%f\n",&turnuva_numarasi,&tur_no,&beyaz_lisans,&siyah_lisans,&sonuc,&beyaz_UKD_degisim,&siyah_UKD_degisim);
        if(birOyuncu.lisans==beyaz_lisans || birOyuncu.lisans==siyah_lisans)
        {
            fseek(turnuvalarptr,(turnuva_numarasi)*sizeof(Turnuvalar),SEEK_SET);
            fread(&birTurnuva,sizeof(Turnuvalar),1,turnuvalarptr);
            printf("Turnuva Adi: %s\n"
                   "Turnuva Tarihi: %s\n"
                   "Turnuva Sehri: %s\n",birTurnuva.turnuva_adi,birTurnuva.turnuva_tarihi,birTurnuva.turnuva_sehir);
            if(birOyuncu.lisans==beyaz_lisans)
            {
                fseek(sporcularptr,(siyah_lisans)*sizeof(Oyuncular),SEEK_SET);
                fread(&birOyuncu,sizeof(Oyuncular),1,sporcularptr);
                strcpy(rakip_isim,birOyuncu.ad_soyad);
                rakip_UKD=birOyuncu.UKD_puan;
                tek_UKD_degisim=beyaz_UKD_degisim;
                if(sonuc==1)
                {
                    mac_puani++;
                }
                else if(sonuc==0)
                {
                    mac_puani=mac_puani+0.5;
                }
            }
            if(birOyuncu.lisans==siyah_lisans)
            {
                fseek(sporcularptr,(beyaz_lisans)*sizeof(Oyuncular),SEEK_SET);
                fread(&birOyuncu,sizeof(Oyuncular),1,sporcularptr);
                strcpy(rakip_isim,birOyuncu.ad_soyad);
                rakip_UKD=birOyuncu.UKD_puan;
                tek_UKD_degisim=siyah_UKD_degisim;
                if(sonuc==2)
                {
                    mac_puani++;
                }
                else if(sonuc==0)
                {
                    mac_puani=mac_puani+0.5;
                }
            }
            printf("Tur No  Rakip Ad Soyad    Rakip UKD  Mac Puani  UKD Degisimi\n"
                   "------  ----------------  ---------  ---------  ------------\n"
                   "%-6d  %16s  %9f  %9f  %12f\n",tur_no,rakip_isim,rakip_UKD,mac_puani,tek_UKD_degisim);
            toplam_UKD_degisim+=tek_UKD_degisim;
            toplam_mac_puani+=mac_puani;
        }
    }
    printf("Toplam Mac Puani: %f\n"
           "Toplam UKD Degisimi: %f\n",toplam_mac_puani,toplam_UKD_degisim);
}
