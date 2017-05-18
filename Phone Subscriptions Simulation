#include <stdio.h>
#include <stdlib.h>

struct Aboneler
{
  char ad_soyad[26];
  char birim_adi[31];
  int abone_tip;
  int on_odenmis_kontor_say;


};

struct Gorusmeler
{
  int arayan_dahili_tel_no;
  char aranan_dis_hat_tel_no[11];
  int tarih;
  int baslangic_saati;
  int baslangic_dakikasi;
  int sure;

};

typedef struct Aboneler Abone;
typedef struct Gorusmeler Gorusme;
int menu();
void bir_abone_listele(FILE*);//2
void bir_abone_bilgisi_ve_o_ay_yapilan_dis_hat_gorusmelerini_listele(FILE*,FILE*);//3
void bir_birimdeki_abonelerin_bilgilerinin_listelenmesi(FILE*);//4
void abone_tipine_gore_abone_say_ve_yuzde_listelenmesi(FILE*);//6
void bir_gun_yapilan_gorusmeler_listelenmesi(FILE*,FILE*);//7
void gune_gore_gorusme_sayisilarinini_ve_surelerinin_listelenmesi(FILE*);//5
void kontor_yuklemesi_gereken_aboneler(FILE*);
void bir_abone_kontor_yuklemesi(FILE*);//10
void yapilan_dis_hat_gorusmelerine_iliskin_kayit_eklenmesi(FILE*,FILE*);//9
void yeni_abone_eklemesi(FILE*);//9
void bir_abone_kaydi_silinmesi(FILE*,FILE*);//
void sporcu_lisans_siralama(int[],int[],int[],char[],char[],int);
void sporcu_il_siralama(int[],int);
void yer_degistirme(int *,int *);
void char_yer_degistirme(char *,char *);



int main()
{

  int sec;
  FILE *abonelerptr;
  abonelerptr=fopen("aboneler.dat","a+");//aboneler.dat dosyasini okuyup guncellemek icin dosyayi actik.
  if((abonelerptr=fopen("aboneler.dat","a+"))==NULL)
  printf("Aboneler dosyasi acilamadi.\n");
  FILE *gorusmelerptr;
  gorusmelerptr=fopen("gorusmeler.txt","a+");//gorusmeler.txt dosyasini okuyup guncellemek icin dosyayi actik.
  if((gorusmelerptr=fopen("gorusmeler.txt","a+"))==NULL)
  printf("Gorusmeler dosyasi acilamadi.\n");

    switch(sec=menu())
  {
    case 1:
      bir_abone_listele(abonelerptr);
      break;
    case 2:
      bir_abone_bilgisi_ve_o_ay_yapilan_dis_hat_gorusmelerini_listele(abonelerptr,gorusmelerptr);
      break;
    case 3:
      bir_birimdeki_abonelerin_bilgilerinin_listelenmesi(abonelerptr);
      break;
    case 4:
      abone_tipine_gore_abone_say_ve_yuzde_listelenmesi(abonelerptr);
      break;
    case 5:
      bir_gun_yapilan_gorusmeler_listelenmesi(abonelerptr,gorusmelerptr);
      break;
    case 6:
      gune_gore_gorusme_sayisilarinini_ve_surelerinin_listelenmesi(gorusmelerptr);
      break;
    case 7:
      kontor_yuklemesi_gereken_aboneler(abonelerptr);
      break;
    case 8:
      bir_abone_kontor_yuklemesi(abonelerptr);
      break;
    case 9:
      yapilan_dis_hat_gorusmelerine_iliskin_kayit_eklenmesi(abonelerptr,gorusmelerptr);
      break;
    case 10:
      yeni_abone_eklemesi(abonelerptr);
      break;
    case 11:
      bir_abone_kaydi_silinmesi(abonelerptr,gorusmelerptr);
      break;
  }
   fclose(abonelerptr);
   fclose(gorusmelerptr);
    return 0;

}

int menu(void)
{
  int secim;
    printf("\n\n1)Bir abonenin bilgilerinin listelenmesi\n"
           "2)Bir abonenin bilgilerinin ve o ay yapmýs oldugu dis hat gorusmelerinin listelenmesi\n"
           "3)Bir birimdeki abonelerin bilgilerinin listelenmesi\n"
           "4)Abone tipine gore abone sayilarinin ve yuzdelerinin listelenmesi\n"
           "5)Bir gun yapilan gorusmelerin listelenmesi\n"
           "6)Gune gore gorusme sayilarinin ve surelerinin listelenmesi\n"
           "7)Dis hat gorusmesi yapabilmek icin kontor yuklemesi gereken abonelerin listelenmesi\n"
           "8)Bir abonenin kontor yuklemesi.\n"
           "9)Yapilan dis hat gorusmelerine iliskin kayitlarin eklenmesi\n"
           "10)Yeni bir abonenin eklenmesi\n"
           "11)Bir abonenin kaydinin silinmesi\n\n");
           do
           {
             scanf("%d",&secim);
           }while(secim<1 || secim>11);
           return secim;
}

void bir_abone_listele(FILE*abonelerptr)
{
  Abone birAbone;
  int dahili_tel_no,eldeki_dosya_no;
    printf("\nAbonenin dahili no'sunu giriniz:");
    scanf("%d",&dahili_tel_no);

    eldeki_dosya_no=dahili_tel_no-100;

     printf("\nTel No       Ad Soyad           Birimi                    Tip          Kontor\n");
       printf("----------   ------------      -------------------        ----         --------  ");

      fseek(abonelerptr,eldeki_dosya_no*sizeof(Abone),SEEK_SET);
        fread(&birAbone,sizeof(Abone),1,abonelerptr);
          printf("\n%d          %10s        %s        %d            %d\n",dahili_tel_no,birAbone.ad_soyad,birAbone.birim_adi,birAbone.abone_tip,birAbone.on_odenmis_kontor_say);

    main();
}

void bir_abone_bilgisi_ve_o_ay_yapilan_dis_hat_gorusmelerini_listele(FILE*abonelerptr,FILE*gorusmelerptr)
{
   Abone birAbone;
   Gorusme birGorusme;
   int bitis_saat,ilk_saat,bitis_dakika,top_gorusme_sayisi=0,top_gunduz_gorusme_suresi,top_gece_gorusme_suresi,top_harcadigi_kontor_miktari;
   int dahili_tel_no,eldeki_dosya_no,aranan_tel_no,gun_no,baslangic,bitis;
   int gunduz_harcanan_kontor,toplam_gunduz_harcanan_kontor=0,gunduz_gorusme_suresi,toplam_gunduz_gorusme_suresi=0;
    int toplam_gece_harcanan_kontor=0,gece_harcanan_kontor,gece_gorusme_suresi,toplam_gece_gorusme_suresi=0, toplam_harcanan_kontor=0;
    int arayan_dahili_tel_no,tarih,baslangic_saati,baslangic_dakikasi,sure;
    char aranan_dis_hat_tel_no[11];
    printf("\nAbonenin dahili no'sunu giriniz:");
    scanf("%d",&dahili_tel_no);

    eldeki_dosya_no=dahili_tel_no-100;

     printf("\nTel No       Ad Soyad           Birimi                    Tip          Kontor\n");
       printf("----------   ------------      -------------------        ----         --------  ");

      fseek(abonelerptr,eldeki_dosya_no*sizeof(Abone),SEEK_SET);//Bir dosyadaki belirli bir byte'ı bulur.
        fread(&birAbone,sizeof(Abone),1,abonelerptr);
         printf("\n%d          %10s        %s        %d            %d\n",dahili_tel_no,birAbone.ad_soyad,birAbone.birim_adi,birAbone.abone_tip,birAbone.on_odenmis_kontor_say);


       printf("\n\nDis Hat Gorusmeleri:");
       printf("\nAranan Tel No     Gun No      Baslangic      Bitis\n");
        printf("--------------  ------------  ---------     --------  ");

         while(!feof(gorusmelerptr))
           {
             fscanf(gorusmelerptr,"%d\n%s\n%d\n%d\n%d\n%d\n",&arayan_dahili_tel_no,&aranan_dis_hat_tel_no,&tarih,&baslangic_saati,&baslangic_dakikasi,&sure);

               if(dahili_tel_no==arayan_dahili_tel_no)
                {
                 ilk_saat=baslangic_saati;
                 if(baslangic_saati<=20&&baslangic_saati>=8)//gunduz gorusmeleri icin hesaplamalar
                   {

                    gunduz_harcanan_kontor=sure*3;
                    toplam_gunduz_harcanan_kontor+=gunduz_harcanan_kontor;
                    gunduz_harcanan_kontor==0;

                    gunduz_gorusme_suresi=sure;
                    toplam_gunduz_gorusme_suresi+=gunduz_gorusme_suresi;
                    gunduz_gorusme_suresi==0;
                    top_gorusme_sayisi++;

                      if((sure+baslangic_dakikasi)>59)
                      {
                         baslangic_saati++;
                         bitis_saat=baslangic_saati;
                         bitis_dakika=((sure+baslangic_dakikasi)-60);
                      }
                      else
                      {
                         bitis_saat=baslangic_saati;
                         bitis_dakika=sure+baslangic_dakikasi;

                      }


                    }//gunduz isini bitirdik


                   if(baslangic_saati>20&&baslangic_saati<24||baslangic_saati<8&&baslangic_saati>=0)//gece gorusmeleri icin hesaplamalar
                   {

                    gece_harcanan_kontor=sure*2;
                    toplam_gece_harcanan_kontor+=gece_harcanan_kontor;
                    gece_harcanan_kontor==0;

                    gece_gorusme_suresi=sure;
                    toplam_gece_gorusme_suresi+=gece_gorusme_suresi;
                    gece_gorusme_suresi==0;
                     top_gorusme_sayisi++;
                      if((sure+baslangic_dakikasi)>59)
                      {
                         baslangic_saati++;

                         if(baslangic_saati>=24)
                           {
                             bitis_saat=(baslangic_saati-24);
                             bitis_dakika=((sure+baslangic_dakikasi)-60);
                           }
                          else
                           {
                             bitis_saat=baslangic_saati;
                             bitis_dakika=((sure+baslangic_dakikasi)-60);
                           }

                      }
                      else
                      {
                         bitis_saat=baslangic_saati;
                         bitis_dakika=sure+baslangic_dakikasi;

                      }



                    }//gece isini bitirdik.

                  toplam_harcanan_kontor+=(toplam_gunduz_harcanan_kontor+toplam_gece_harcanan_kontor);

                  printf("\n%8s           %d        %2d : %2d    %3d : %3d\n",aranan_dis_hat_tel_no,tarih,ilk_saat,baslangic_dakikasi,bitis_saat,bitis_dakika);
                  baslangic_saati=0;
                }

           }//while sonu

          printf("\n-----------------------------------------------------------");

          printf("\nToplam Gorusme Sayisi:%d\n",top_gorusme_sayisi);
          printf("Toplam Gunduz Gorusme Suresi:%d\n",toplam_gunduz_gorusme_suresi);
           printf("Toplam Gece Gorusme Suresi:%d\n",toplam_gece_gorusme_suresi);
            printf("Toplam Harcadigi Kontor:%d\n",toplam_harcanan_kontor);

            main();
}

void bir_birimdeki_abonelerin_bilgilerinin_listelenmesi(FILE*abonelerptr)
{
   Abone birAbone;
   int dahili_tel_no,i;
    char cevap[31];


    printf("Hangi birimin aboneleri goruntulensin?\n");
      fflush(stdin);
       gets(cevap);

        printf("\n%s Biriminin Aboneleri:\n"
           "Tel No    Ad Soyad               Birim                  Tip         Kontor\n"
           "------  --------------          -------                 -------     --------\n",cevap);


      for(i=0;i<900;i++) //aboneler.txt'nin sonuna kadar donduruluyor.
        {

            fseek(abonelerptr,i*sizeof(Abone),SEEK_SET);
            fread(&birAbone,sizeof(Abone),1,abonelerptr);
            if(strcmp(cevap,birAbone.birim_adi)==0)
            printf("    %d         %s       %-4s        %d             %d\n",(i+100),birAbone.ad_soyad,birAbone.birim_adi,birAbone.abone_tip,birAbone.on_odenmis_kontor_say);

        }
    main();

}

void abone_tipine_gore_abone_say_ve_yuzde_listelenmesi(FILE*abonelerptr)
{
   Abone birAbone;
   int i;
   float dizi2[5]={0};
   int dizi1[5]={0};
   char AboneTipi[5][10]={"Akademik","Idari","Diger","Yonetici","Bos"};


        for(i=0;i<900;i++) //aboneler.txt'nin sonuna kadar donduruluyor.
        {

            fseek(abonelerptr,i*sizeof(Abone),SEEK_SET);
            fread(&birAbone,sizeof(Abone),1,abonelerptr);
            if((birAbone.abone_tip)==1)//Akademik
             dizi1[0]++;

               if((birAbone.abone_tip)==2)//Idari
                dizi1[1]++;

                 if((birAbone.abone_tip)==4)//Diger
                  dizi1[2]++;

                   if((birAbone.abone_tip)==3)//Yonetici
                    dizi1[3]++;

                      if((birAbone.abone_tip)==0)//Bos
                       dizi1[4]++;

        }

        dizi2[0]=(((float)dizi1[0]/900)*100);
        dizi2[1]=(((float)dizi1[1]/900)*100);
        dizi2[2]=(((float)dizi1[2]/900)*100);
        dizi2[3]=(((float)dizi1[3]/900)*100);
        dizi2[4]=(((float)dizi1[4]/900)*100);

        printf(
           "Abone Tipi     Abone Sayisi        Yuzde   \n"
           "----------     ------------       -------   \n");
           for(i=0;i<5;i++)
           {
             printf(" %s           %d                %.2f\n",AboneTipi[i],dizi1[i],(float)dizi2[i]);

             if(i==3)
                printf("-------------------------------------------\n");
           }

    main();
}

void bir_gun_yapilan_gorusmeler_listelenmesi(FILE*abonelerptr,FILE*gorusmelerptr)
{
   Abone birAbone;
   Gorusme birGorusme;
   int cevap,tarih,arayan_dahili_tel_no,baslangic_saati,baslangic_dakikasi,sure;
   char ad_soyad[26];
   char aranan_dis_hat_tel_no[11];

    printf("Hangi Gunun Gorusmeleri Goruntulensin?\n");
    scanf("%d",&cevap);
    printf("\n%d. Gunun Gorusmeleri:\n"
           "Arayan Tel No     Arayan Ad Soyad      Aranan Tel No     Baslangic     Sure (dk)"
           "-------------     ---------------      -------------     ---------     ---------\n",cevap);
       while(!feof(gorusmelerptr)) //gorusmeler.txt'nin sonuna kadar donduruluyor.
    {
        fscanf(gorusmelerptr,"%d\n%s\n%d\n%d\n%d\n%d\n",&arayan_dahili_tel_no,&aranan_dis_hat_tel_no,&tarih,&baslangic_saati,&baslangic_dakikasi,&sure);

        if(cevap==tarih) //Istenilen gun dosyadakiyle ayniysa,
        {
            fseek(abonelerptr,(arayan_dahili_tel_no-100)*sizeof(Abone),SEEK_SET);
            fread(&birAbone,sizeof(Abone),1,abonelerptr);
            strcpy(ad_soyad,birAbone.ad_soyad);

            printf("%d                  %s             %s      %d:%d           %d\n",arayan_dahili_tel_no,ad_soyad,aranan_dis_hat_tel_no,baslangic_saati,baslangic_dakikasi,sure);

        }
    }

    main();
}

void gune_gore_gorusme_sayisilarinini_ve_surelerinin_listelenmesi(FILE*gorusmelerptr)
{
  Gorusme birGorusme;
   int tarih,arayan_dahili_tel_no,baslangic_saati,baslangic_dakikasi,sure,aranan_dis_hat_tel_no;
   int top_gorusme_say[31]={0},i,top_gorusme_suresi[31]={0},aylik_top_gorusme_say=0,aylik_top_gorusme_suresi=0;
   float ort_gorusme_suresi[31]={0};
      printf("\n Gunun Gorusme istatistikleri:\n"
           "Gun      Top Gor Sayisi      Top Gor Suresi(dk)    Ortalama Gor Suresi(dk)\n"
           "-----    --------------     ------------------     ----------------------\n");
       while(!feof(gorusmelerptr)) //gorusmeler.txt'nin sonuna kadar donduruluyor.
        {
        fscanf(gorusmelerptr,"%d\n%s\n%d\n%d\n%d\n%d\n",&arayan_dahili_tel_no,&aranan_dis_hat_tel_no,&tarih,&baslangic_saati,&baslangic_dakikasi,&sure);

        for(i=0;i<31;i++)
         {
           if(tarih==i+1)
             {
               top_gorusme_say[i]++;
               top_gorusme_suresi[i]+=sure;
               ort_gorusme_suresi[i]=((float)top_gorusme_suresi[i]/top_gorusme_say[i]);
                aylik_top_gorusme_say++;
                aylik_top_gorusme_suresi+=sure;
             }

         }

       }

        for(i=0;i<31;i++)
           {
               printf("%d              %d                    %d                    %.2f \n",i+1,top_gorusme_say[i],top_gorusme_suresi[i],(float)ort_gorusme_suresi[i]);

           }

            printf("----------------------------------------------\n");
             printf("Aylik toplam gorusme sayisi:%d\n",aylik_top_gorusme_say);
               printf("Aylik toplam gorusme suresi:%d\n",aylik_top_gorusme_suresi);
    main();
}

void kontor_yuklemesi_gereken_aboneler(FILE*abonelerptr)
{
   Abone birAbone;
   int i;


        printf("\nKontor Yuklemesi Gereken Aboneler:\n"
           "Tel No    Ad Soyad               Birim              Tip         Kontor\n"
           "------  --------------          -------            -------     --------\n");


      for(i=0;i<900;i++) //aboneler.txt'nin sonuna kadar donduruluyor.
        {

            fseek(abonelerptr,i*sizeof(Abone),SEEK_SET);
            fread(&birAbone,sizeof(Abone),1,abonelerptr);
            if((birAbone.on_odenmis_kontor_say)<-100)
            printf(" %d     %s          %s      %7d             %-5d\n",(i+100),birAbone.ad_soyad,birAbone.birim_adi,birAbone.abone_tip,birAbone.on_odenmis_kontor_say);

        }
    main();
}

void bir_abone_kontor_yuklemesi(FILE*abonelerptr)
{
    Abone birAbone;
     int dahili_tel_no,eldeki_dosya_no,yuklenen_kontor,i;

         do{ printf("\nAbonenin dahili no'sunu giriniz:");
            scanf("%d",&dahili_tel_no);
            eldeki_dosya_no=dahili_tel_no-100;


               fseek(abonelerptr,eldeki_dosya_no*sizeof(Abone),SEEK_SET);
               fread(&birAbone,sizeof(Abone),1,abonelerptr);

               if(birAbone.abone_tip==0)
                   printf("Bu dahili no'ya sahip abone bulunamadi.\n");
             }while(birAbone.abone_tip==0);

                    if(birAbone.abone_tip!=0)
                        {
                         printf("Aboneye yuklenecek kontor miktarini giriniz:\n");
                         scanf("%d",&yuklenen_kontor);
                         birAbone.on_odenmis_kontor_say=yuklenen_kontor;//yeni yuklenen kontoru ekledik
                         fseek(abonelerptr,eldeki_dosya_no*sizeof(Abone),SEEK_SET);
                          fwrite(&birAbone,sizeof(Abone),1,abonelerptr); //Bilgileri dosyada guncelliyoruz.

                         }

           printf("\nTel No       Ad Soyad           Birimi                  Tip         Yeni Kontor\n"
                  "----------   ------------      -------------------      ----        ------------  ");

           printf("\n%d          %10s        %s        %d            %d\n",dahili_tel_no,birAbone.ad_soyad,birAbone.birim_adi,birAbone.abone_tip,birAbone.on_odenmis_kontor_say);


          main();

}

void  yapilan_dis_hat_gorusmelerine_iliskin_kayit_eklenmesi(FILE*abonelerptr,FILE*gorusmelerptr)
{
    Abone birAbone;
    Gorusme birGorusme;
    char aranan_dis_hat_tel_no[11];
    int gun_no,baslangic_saat,baslangic_dakika,sure,eldeki_dosya_no,dahili_tel_no,i,arayan_tel_no;
    int harcanan_kontor=0,ilk_kontor=0,secim;
   do{
    do
    {
        printf("\nAbonenin dahili no'sunu giriniz:");
        scanf("%d",&dahili_tel_no);
        eldeki_dosya_no=dahili_tel_no-100;

        for(i=0; i<900; i++)
        {
            fseek(abonelerptr,eldeki_dosya_no*sizeof(Abone),SEEK_SET);
            fread(&birAbone,sizeof(Abone),1,abonelerptr);
        }
        if(birAbone.abone_tip==0)
            printf("Bu dahili no'ya sahip abone bulunamadi.\n");
        else if(birAbone.on_odenmis_kontor_say<-100)
            printf("Bu dahili no'ya sahip abonenin kontoru gorusme icin yetersizdir.Bedava yok oyle!\n");
    }
    while(birAbone.abone_tip==0||birAbone.on_odenmis_kontor_say<-100);

    if(birAbone.abone_tip!=0)
    {
        printf("Aranan Dis Hat Tel No'yu Giriniz:");
        scanf("\n%s",aranan_dis_hat_tel_no);
        printf("Gun Numarasini Giriniz:");
        scanf("\n%d",&gun_no);
        printf("Baslangic Saatini Giriniz:");
        scanf("\n%d",&baslangic_saat);
        printf("Baslangic Dakikasini Giriniz:");
        scanf("\n%d",&baslangic_dakika);
        printf("Konusma Suresini Giriniz:");
        scanf("\n%d",&sure);

        fprintf(gorusmelerptr,"%d %s %d %d %d %d\n",dahili_tel_no,aranan_dis_hat_tel_no,gun_no,baslangic_saat,baslangic_dakika,sure);


      if(baslangic_saat<=20&&baslangic_saat>=8)//kontor guncellenmeleri
      {
         ilk_kontor=birAbone.on_odenmis_kontor_say;
         harcanan_kontor=sure*3;
         birAbone.on_odenmis_kontor_say=ilk_kontor-harcanan_kontor;
          fseek(abonelerptr,eldeki_dosya_no*sizeof(Abone),SEEK_SET);//belirli byte'imizi bulup..
           fwrite(&birAbone,sizeof(Abone),1,abonelerptr); //Bilgileri dosyada guncelliyoruz.

      }

      else if(baslangic_saat>20&&baslangic_saat<24||baslangic_saat<8&&baslangic_saat>=0)
      {
        ilk_kontor=birAbone.on_odenmis_kontor_say;
        harcanan_kontor=sure*2;
         birAbone.on_odenmis_kontor_say=ilk_kontor-harcanan_kontor;
         fseek(abonelerptr,eldeki_dosya_no*sizeof(Abone),SEEK_SET);//belirli byte'imizi bulup..
           fwrite(&birAbone,sizeof(Abone),1,abonelerptr); //Bilgileri dosyada guncelliyoruz.

      }


    }

    printf("\nYeni Dosyamiz\n"
           "Arayan tel no  Aranan dis hat tel no  Tarih      Bas. Saat Dakika    Sure\n"
           "-------------  ---------------------  -----      ------------------  ----\n");

    rewind(gorusmelerptr);
    fscanf(gorusmelerptr,"%d %s %d %d %d %d",&arayan_tel_no,aranan_dis_hat_tel_no,&gun_no,&baslangic_saat,&baslangic_dakika,&sure);
    while(!feof(gorusmelerptr)) //gorusmeler.txt'nin sonuna kadar donduruluyor.
    {
        printf("%d                 %s          %d            %d:%d           %d\n",arayan_tel_no,aranan_dis_hat_tel_no,gun_no,baslangic_saat,baslangic_dakika,sure);
        fscanf(gorusmelerptr,"%d %s %d %d %d %d",&arayan_tel_no,aranan_dis_hat_tel_no,&gun_no,&baslangic_saat,&baslangic_dakika,&sure);


    }

    printf("Baska hat gorusme kaydi eklemek istiyor musunuz?(Evet Icin:1,Hayir Icin:0):\n");
    scanf("%d",&secim);

   }while(secim==1);

    if(secim==0)
     main();


}


void yeni_abone_eklemesi(FILE*abonelerptr)
{
   Abone birAbone;

   int dahili_tel_no,i,k,eldeki_dosya_no;
  do{
   printf("Abonenin dahili telefon numarasini giriniz:");
   scanf("%d",&dahili_tel_no);
   eldeki_dosya_no=dahili_tel_no-100;

   for(i=0;i<900;i++)
   {
     fseek(abonelerptr,eldeki_dosya_no*sizeof(Abone),SEEK_SET);
     fread(&birAbone,sizeof(Abone),1,abonelerptr);

      k=0;
      if(birAbone.abone_tip!=0)
      {
         printf("Bu abone mevcuttur,lutfen baska bir dahili numara giriniz:\n");
         k=1;
         break;
      }
   }
  }while(k==1);

  if(birAbone.abone_tip==0)
{
    printf("Abonenin adi-soyadini giriniz:");
     fflush(stdin);
      gets(birAbone.ad_soyad);
    printf("\nAbonenin birim adini giriniz:");
     fflush(stdin);
      gets(birAbone.birim_adi);
    printf("\nAbone birim tipini(1:Akademik,2:Idari,3:Yonetici,4:Diger,0: Bos) giriniz:");
     scanf("%d",&birAbone.abone_tip);
    printf("Abonenin on odenmis kontor sayisini giriniz:");
     scanf("%d",&birAbone.on_odenmis_kontor_say);

      fseek(abonelerptr,eldeki_dosya_no*sizeof(Abone),SEEK_SET);//O adresi bulduk
        fwrite(&birAbone,sizeof(Abone),1,abonelerptr);// Bilgileri dosyada guncelledik.
  }


         rewind(abonelerptr);
         printf("\nYeni Eklenen Abonemizin Bilgileri\n");
         printf("\nTel No       Ad Soyad           Birimi                Tip          Kontor\n");
         printf("----------   ------------      -------------        -----         --------  ");
          printf("\n%d          %s        %s               %d            %d\n",dahili_tel_no,birAbone.ad_soyad,birAbone.birim_adi,birAbone.abone_tip,birAbone.on_odenmis_kontor_say);


    main();


}

void  bir_abone_kaydi_silinmesi(FILE*abonelerptr,FILE*gorusmelerptr)
{
    FILE *yeni_dosya;//YENİ BİR DOSYA OLUSTURDUK ILK.AMACI ARANAN DEGER BULUNUNCA ONU BIR BIT ATLAYIP,GERI KALANI DA YAZDIKTAN SONRA YENI SILINMIS DOSYAMIZI ELDE ETMEK.
    Abone birAbone;
    Gorusme birGorusme;
    int dahili_tel_no,i,k,eldeki_dosya_no;
    int tarih,arayan_dahili_tel_no,baslangic_saati,baslangic_dakikasi,sure;
    char aranan_dis_hat_tel_no[11];
    do
    {
        printf("Abonenin dahili telefon numarasini giriniz:");
        scanf("%d",&dahili_tel_no);
        eldeki_dosya_no=dahili_tel_no-100;
        for(i=0; i<900; i++)
        {
            fseek(abonelerptr,eldeki_dosya_no*sizeof(Abone),SEEK_SET);//Dosyayi okuyup kontrol ediyoruz abone var mi yok mu
            fread(&birAbone,sizeof(Abone),1,abonelerptr);
            k=0;
            if(birAbone.abone_tip==0)
            {
                printf("Bu abone mevcut degildir,lutfen baska bir dahili numara giriniz:\n");
                k=1;
                break;
            }
        }
    }
    while(k==1);
    yeni_dosya=fopen("gorusmeler1.txt","w");
    rewind(gorusmelerptr);//dosya aktif konumunu basa aliyorum.
    fscanf(gorusmelerptr,"%d %s %d %d %d %d",&arayan_dahili_tel_no,aranan_dis_hat_tel_no,&tarih,&baslangic_saati,&baslangic_dakikasi,&sure);
    while(!feof(gorusmelerptr))
    {
        if(dahili_tel_no!=arayan_dahili_tel_no)
        {
            fprintf(yeni_dosya,"%d %s %d %d %d %d\n",arayan_dahili_tel_no,aranan_dis_hat_tel_no,tarih,baslangic_saati,baslangic_dakikasi,sure);
        }
        fscanf(gorusmelerptr,"%d %s %d %d %d %d",&arayan_dahili_tel_no,aranan_dis_hat_tel_no,&tarih,&baslangic_saati,&baslangic_dakikasi,&sure);
    }
    fclose(yeni_dosya);
    fclose(gorusmelerptr);
    remove("gorusmeler.txt");
    rename("gorusmeler1.txt","gorusmeler.txt");
    gorusmelerptr = fopen("gorusmeler.txt","a+");
    main();
}
