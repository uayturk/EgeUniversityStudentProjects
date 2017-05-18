#include <stdio.h>
#include <stdlib.h>

#define MAX_HASH 100
#define MAX_DERS 80

struct ogrenci{
    int ogr_no;
    char ad_soyad[31];
    int sinif;
    int kredi_say;
    float agir_not_ort;
    struct ogrenci *sonraki;
};

struct alan_ogr{
    int puan;
    int numara;
    struct alan_ogr *noya_gore_sonraki;
    struct alan_ogr *puana_gore_onceki;
    struct alan_ogr *puana_gore_sonraki;
};

struct ders{
    int ders_kodu;
    char ders_adi[26];
    int kredi;
    int ogr_say;
    float genel_not_ort;
    struct alan_ogr ogr;
};

int hash_fonksiyon(int ogr_no);
int menu_goruntule();
int ogrenci_no_al();
int donem_al();
int ders_kodu_al();
struct ogrenci *hash_arama(struct ogrenci *ilk_ptr,int aranan);
void hash_sirali_ekle(struct ogrenci **ilk_ptr,struct ogrenci *eklenen);
void dairesel_ekle(struct alan_ogr *liste_basi,struct alan_ogr *eklenen);
struct alan_ogr *dairesel_arama(struct alan_ogr *liste_basi,int aranan_no);
void derse_gore_listele(struct alan_ogr *liste_basi,struct ogrenci *ilk_hashler[]);
void daireselden_cikar(struct alan_ogr *liste_basi,struct alan_ogr *cikarilacak);
void daireselden_sil(struct ders *ptr[],int no);
void hashden_sil(struct ogrenci **ilk_ptr,int no);
void baraja_gore_yuksek(struct alan_ogr *liste_basi,struct ogrenci *ilk_hashler[],int baraj);
void baraja_gore_alcak(struct alan_ogr *liste_basi,struct ogrenci *ilk_hashler[],int baraj);
void ogrenciye_gore_listele(struct ders *ptr[],int no);
void sinif_listele(struct ogrenci *ilk_ptr[],int sinif);

int main()
{
    int secenek,i,ogr_no,hash,donem,ders_kod,kontrol_ders=0,puan,toplam_kredi,yeni_puan,cikar_puan,baraj,sinif;
    char cevap;
    struct ders *ptr_liste[MAX_DERS]={NULL};
    struct ogrenci *bir_ogrenci;
    struct ogrenci *hash_listesi[MAX_HASH]={NULL};
    struct alan_ogr *yeni_alan;

    do{
        secenek=menu_goruntule();
        switch (secenek){
            case 1:
                ogr_no=ogrenci_no_al();
                hash=hash_fonksiyon(ogr_no);

                if (hash_arama(hash_listesi[hash-1],ogr_no)==NULL){//ogrenci numarasi araniyor
                    bir_ogrenci=malloc(sizeof(struct ogrenci));//gerekli bellek ayriliyor
                    bir_ogrenci->ogr_no=ogr_no;
                    bir_ogrenci->kredi_say=0;
                    bir_ogrenci->agir_not_ort=0;
                    printf("Ogrencinin adi soyadini giriniz:\n");
                    fflush(stdin);
                    gets(bir_ogrenci->ad_soyad);
                    printf("Ogrencinin sinifini giriniz:\n");
                    scanf("%d",&bir_ogrenci->sinif);
                    hash_sirali_ekle(&hash_listesi[hash-1],bir_ogrenci);//hash listesine ekleme yapiliyor
                    printf("Ogrenci eklendi.\n");
                }
                else
                    printf("Girdiginiz numaraya ait bir ogrenci kaydi zaten var!\n");
                break;
            case 2:
                donem=donem_al();
                for (i=(donem*10-10);i<donem*10;i++){//kullanicidan alinan donem ile ders icin uygun yer araniyor
                    if (ptr_liste[i]==NULL){
                        printf("Dersin kodu:%d\n",i+10);hash_arama
                        ptr_liste[i]=malloc(sizeof(struct ders));//gerekli bellek ayriliyor
                        ptr_liste[i]->ogr.noya_gore_sonraki=&ptr_liste[i]->ogr;//ders listesine bagli bagli listeler icin ilklemeler yapiliyor
                        ptr_liste[i]->ogr.puana_gore_onceki=&ptr_liste[i]->ogr;
                        ptr_liste[i]->ogr.puana_gore_sonraki=&ptr_liste[i]->ogr;
                        ptr_liste[i]->ders_kodu=i+10;//gerekli bilgiler ayrilan adrese ataniyor
                        ptr_liste[i]->ogr_say=0;
                        ptr_liste[i]->genel_not_ort=0;
                        printf("Dersin adini giriniz:\n");
                        fflush(stdin);
                        gets(ptr_liste[i]->ders_adi);
                        printf("Dersin kredisini giriniz:\n");
                        scanf("%d",&ptr_liste[i]->kredi);
                        printf("Ders eklendi.\n");
                        kontrol_ders=1;
                        break;
                    }
                }
                if (kontrol_ders==0)//eger o donem icin bos ders kayit sahasi yoksa bir uyari mesaji yazdiriliyor
                    printf("Bu donem butun ders kayitlari dolu!\n");
                break;
            case 3:
                ders_kod=ders_kodu_al();
                if (ptr_liste[ders_kod-10]==NULL)//girilen ders kodunun dolu olup olmadigi kontrol ediliyor
                    printf("Bu ders koduna ait ders kaydi bulunmamaktadir!\n");
                else{
                    do{
                        ogr_no=ogrenci_no_al();
                        hash=hash_fonksiyon(ogr_no);
                        bir_ogrenci=hash_arama(hash_listesi[hash-1],ogr_no);//girilen ogrenci numarasinin dolu olup olmadigi kontrol ediliyor
                        if(bir_ogrenci==NULL)
                            printf("Bu numarali ogrenci kaydi bulunmamaktadir!\n");
                        else{
                            printf("Alinan notu giriniz:\n");
                            scanf("%d",&puan);
                            yeni_alan=malloc(sizeof(struct alan_ogr));//dersi alacak ogrenci icin gerekli bellek ataniyor
                            yeni_alan->numara=ogr_no;
                            yeni_alan->puan=puan;//gerekli atamalar yapiliyor
                            bir_ogrenci->agir_not_ort=(bir_ogrenci->kredi_say*bir_ogrenci->agir_not_ort+ptr_liste[ders_kod-10]->kredi*puan)/(bir_ogrenci->kredi_say+ptr_liste[ders_kod-10]->kredi);
                            //degisecek olan bilgiler degistiriliyor
                            bir_ogrenci->kredi_say+=ptr_liste[ders_kod-10]->kredi;
                            ptr_liste[ders_kod-10]->genel_not_ort=(ptr_liste[ders_kod-10]->genel_not_ort*ptr_liste[ders_kod-10]->ogr_say+puan)/(ptr_liste[ders_kod-10]->ogr_say+1);
                            ptr_liste[ders_kod-10]->ogr_say++;
                            dairesel_ekle(&ptr_liste[ders_kod-10]->ogr,yeni_alan);//olusan kayit bagli listeye ekleniyor
                        }

                        printf("Baska ogrenci var mi?\n");
                        fflush(stdin);
                        scanf("%c",&cevap);//baska ogrenci olup olmadigi kontrol ediliyor
                    }while (cevap=='e' || cevap=='E');
                }
                break;
            case 4:
                ders_kod=ders_kodu_al();
                if (ptr_liste[ders_kod-10]==NULL)
                    printf("Bu ders koduna ait ders kaydi bulunmamaktadir!\n");
                else{
                    ogr_no=ogrenci_no_al();
                    hash=hash_fonksiyon(ogr_no);
                    bir_ogrenci=hash_arama(hash_listesi[hash-1],ogr_no);
                    if(bir_ogrenci==NULL)
                        printf("Bu numarali ogrenci kaydi bulunmamaktadir!\n");
                    else{
                        yeni_alan=dairesel_arama(&ptr_liste[ders_kod-10]->ogr,ogr_no);//ogrencinin bu derse kayitli olup olmadigi kontrol ediliyor
                        if (yeni_alan==NULL)
                            printf("Bu numarali ogrencinin bu derse kaydi bulunmamaktadir!\n");
                        else{
                            daireselden_cikar(&ptr_liste[ders_kod-10]->ogr,yeni_alan);//eski not listeden cikariliyor
                            printf("Ogrencinin yeni notunu giriniz:\n");
                            scanf("%d",&yeni_puan);
                            cikar_puan=ptr_liste[ders_kod-10]->kredi*yeni_alan->puan;
                            bir_ogrenci->agir_not_ort=(bir_ogrenci->agir_not_ort*bir_ogrenci->kredi_say-cikar_puan+ptr_liste[ders_kod-10]->kredi*yeni_puan)/bir_ogrenci->kredi_say;
                            ptr_liste[ders_kod-10]->genel_not_ort=(ptr_liste[ders_kod-10]->ogr_say*ptr_liste[ders_kod-10]->genel_not_ort-yeni_alan->puan+yeni_puan)/ptr_liste[ders_kod-10]->ogr_say;
                            yeni_alan->puan=yeni_puan;//gerekli degisiklikler yapiliyor
                            dairesel_ekle(&ptr_liste[ders_kod-10]->ogr,yeni_alan);//yeni puan bagli listeye ekleniyor
                            printf("Ogrencinin notu basariyla guncellendi.\n");
                        }
                    }
                }
                break;
            case 5:
                ogr_no=ogrenci_no_al();
                hash=hash_fonksiyon(ogr_no);
                bir_ogrenci=hash_arama(hash_listesi[hash-1],ogr_no);
                if (bir_ogrenci==NULL)
                    printf("Bu numarali ogrenci kaydi bulunmamaktadir!\n");
                else{
                    daireselden_sil(ptr_liste,ogr_no);//silinecek ogrenci kayitli oldugu derslerin bagli listelerinden siliniyor
                    hashden_sil(&hash_listesi[hash-1],ogr_no);//hash listesinden siliniyor
                    printf("Ogrenci basariyla silinmistir.\n");
                }
                break;
            case 6:
                ders_kod=ders_kodu_al();
                if (ptr_liste[ders_kod-10]==NULL)
                    printf("Bu ders koduna ait ders kaydi bulunmamaktadir!\n");
                else{
                    printf("Ders Kodu   Ders Adi   Kredi   Ogrenci Say   Not Ort\n");
                    printf("---------   --------   -----   -----------   -------\n");
                    printf("%-11d %-11s %-11d %-11d %-11.2f\n",ptr_liste[ders_kod-10]->ders_kodu,ptr_liste[ders_kod-10]->ders_adi,ptr_liste[ders_kod-10]->kredi,ptr_liste[ders_kod-10]->ogr_say,ptr_liste[ders_kod-10]->genel_not_ort);
                    printf("\nDersi Alan Ogrenciler:\n");
                    printf("Ogr No   Ad Soyad   Sinif   Notu\n");
                    printf("------   --------   -----   ----\n");
                    derse_gore_listele(&ptr_liste[ders_kod-10]->ogr,hash_listesi);//dersi alan ogrenciler listeleniyor
                }
                break;
            case 7:
                ders_kod=ders_kodu_al();
                if (ptr_liste[ders_kod-10]==NULL)
                    printf("Bu ders koduna ait ders kaydi bulunmamaktadir!\n");
                else{
                    printf("Bilgilerini gormek istediginiz ogrenciler icin baraj notu girin:\n");
                    scanf("%d",&baraj);
                    printf("\nNotu Yuksek Olan Ogrenciler:\n");
                    printf("Ogr No   Ad Soyad   Sinif   Notu\n");
                    printf("------   --------   -----   ----\n");
                    baraja_gore_yuksek(&ptr_liste[ders_kod-10]->ogr,hash_listesi,baraj);//girilen sinir degeri kosuluna uyan ogrenciler listeleniyor
                }
                break;
            case 8:
                ders_kod=ders_kodu_al();
                if (ptr_liste[ders_kod-10]==NULL)
                    printf("Bu ders koduna ait ders kaydi bulunmamaktadir!\n");
                else{
                    printf("Bilgilerini gormek istediginiz ogrenciler icin baraj notu girin:\n");
                    scanf("%d",&baraj);
                    printf("\nNotu Dusuk Olan Ogrenciler:\n");
                    printf("Ogr No   Ad Soyad   Sinif   Notu\n");
                    printf("------   --------   -----   ----\n");
                    baraja_gore_alcak(&ptr_liste[ders_kod-10]->ogr,hash_listesi,baraj);//girilen sinir degeri kosuluna uyan ogrenciler listeleniyor
                }
                break;
            case 9:
                donem=donem_al();
                toplam_kredi=0;
                printf("Ders Kodu   Ders Adi   Kredi   Ogrenci Say   Not Ort\n");
                printf("---------   --------   -----   -----------   -------\n");
                for (i=(donem*10-10);i<donem*10;i++){//girilen donemde olan dersler taraniyor
                    if (ptr_liste[i]==NULL)
                        break;
                    printf("%-11d %-11s %-11d %-11d %-11.2f\n",ptr_liste[i]->ders_kodu,ptr_liste[i]->ders_adi,ptr_liste[i]->kredi,ptr_liste[i]->ogr_say,ptr_liste[i]->genel_not_ort);
                    toplam_kredi+=ptr_liste[i]->kredi;//derslerin kredi toplamlari bulunuyor
                }
                printf("\nDerslerin kredi toplami:%d\n",toplam_kredi);
                break;
            case 10://girilen ogrenciye ait bilgiler gosteriliyor
                ogr_no=ogrenci_no_al();
                hash=hash_fonksiyon(ogr_no);
                bir_ogrenci=hash_arama(hash_listesi[hash-1],ogr_no);
                if (bir_ogrenci==NULL)
                    printf("Bu numarali ogrenci kaydi bulunmamaktadir!\n");
                else{
                    printf("Ogrenci No   Ogrenci Adi   Sinifi   Toplam Kredisi    Not Ort\n");
                    printf("----------   -----------   ------   --------------    -------\n");
                    printf("%-13d %-14s %-13d %-12d %.2f\n",bir_ogrenci->ogr_no,bir_ogrenci->ad_soyad,bir_ogrenci->sinif,bir_ogrenci->kredi_say,bir_ogrenci->agir_not_ort);
                }
                break;
            case 11:
                ogr_no=ogrenci_no_al();
                hash=hash_fonksiyon(ogr_no);
                bir_ogrenci=hash_arama(hash_listesi[hash-1],ogr_no);
                if (bir_ogrenci==NULL)
                    printf("Bu numarali ogrenci kaydi bulunmamaktadir!\n");
                else{
                    printf("Ogrenci No   Ogrenci Adi   Sinifi   Toplam Kredisi    Not Ort\n");
                    printf("----------   -----------   ------   --------------    -------\n");
                    printf("%-13d %-14s %-13d %-12d %.2f\n",bir_ogrenci->ogr_no,bir_ogrenci->ad_soyad,bir_ogrenci->sinif,bir_ogrenci->kredi_say,bir_ogrenci->agir_not_ort);
                    printf("\nAldigi Dersler:\n");
                    printf("Ders Kodu   Ders Adi   Kredi   Notu\n");
                    printf("---------   --------   -----   ----\n");
                    ogrenciye_gore_listele(ptr_liste,ogr_no);//girilen ogrencinin aldigi derslerin bilgileri listeleniyor
                }
                break;
            case 12:
                printf("Ogrencilerini gormek istediginiz sinif numarasini giriniz:\n");
                scanf("%d",&sinif);
                printf("Ogrenci No   Ogrenci Adi   Sinifi   Toplam Kredisi    Not Ort\n");
                printf("----------   -----------   ------   --------------    -------\n");
                sinif_listele(hash_listesi,sinif);//girilen sinifta olan ogrenciler listeleniyor
                break;
        }

    }while (secenek!=13);

    return 0;
}

int hash_fonksiyon(int ogr_no)//ogrenci no suna gore hash bulan fonksiyon
{
    int hash_no;

    hash_no=(ogr_no-1)/100+1;

    return hash_no;
}

int menu_goruntule()
{
    int secim;

    printf("\n1.Yeni bir ogrencinin eklenmesi:\n");
    printf("2.Yeni bir dersin eklenmesi:\n");
    printf("3.Bir dersi alan ogrencilerin notlarinin eklenmesi:\n");
    printf("4.Bir dersi alan bir ogrencinin notunun guncellenmesi:\n");
    printf("5.Bir ogrencinin silinmesi:\n");
    printf("6.Bir dersin bilgilerinin ve o dersi alan ogrencilerin listelenmesi:\n");
    printf("7.Bir dersi alan ogrencilerden,notu belirli bir notun ustunde olan ogrencilerin listelenmesi:\n");
    printf("8.Bir dersi alan ogrencilerden,notu belirli bir notun altinda olan ogrencilerin listelenmesi:\n");
    printf("9.Bir donemin derslerinin listelenmesi:\n");
    printf("10.Bir ogrencinin bilgilerinin listelenmesi:\n");
    printf("11.Bir ogrencinin bilgilerinin ve aldigi derslerin listelenmesi:\n");
    printf("12.Bir sinifta okuyan ogrencilerin listelenmesi:\n");
    printf("13.Cikis\n");
    scanf("%d",&secim);

    return secim;
}

struct ogrenci *hash_arama(struct ogrenci *ilk_ptr,int aranan)//girilen ogr no sunu mevcut hash listesinde arayan fonksiyon
{
    struct ogrenci *gecici;

    gecici=ilk_ptr;
    while (gecici!=NULL && gecici->ogr_no<=aranan){
        if (gecici->ogr_no==aranan)
            return gecici;
        gecici=gecici->sonraki;
    }
    return NULL;
}

int ogrenci_no_al()
{
    int no;

    do{
        printf("Ogrenci numarasini giriniz:\n");
        scanf("%d",&no);
    }while (no<1 || no>10000);

    return no;
}

int donem_al()
{
    int no;

    do{
        printf("Donem numarasini giriniz:\n");
        scanf("%d",&no);
    }while (no<1 || no>8);

    return no;
}

int ders_kodu_al()
{
    int kod;

    do{
        printf("Ders kodunu giriniz:\n");
        scanf("%d",&kod);
    }while (kod<10 || kod>89);

    return kod;
}

void hash_sirali_ekle(struct ogrenci **ilk_ptr,struct ogrenci *eklenen)//verileri alinan ogrencinin hash listesine ekletildigi fonksiyon
{
    struct ogrenci *gecici,*onceki;

    if (*ilk_ptr==NULL){
        eklenen->sonraki=NULL;
        *ilk_ptr=eklenen;
    }
    else if ((*ilk_ptr)->ogr_no>eklenen->ogr_no){
        eklenen->sonraki=*ilk_ptr;
        *ilk_ptr=eklenen;
    }
    else{
        onceki=*ilk_ptr;
        gecici=(*ilk_ptr)->sonraki;
        while (gecici!=NULL && gecici->ogr_no<eklenen->ogr_no){
            onceki=gecici;
            gecici=gecici->sonraki;
        }
        eklenen->sonraki=gecici;
        onceki->sonraki=eklenen;
    }
}

void dairesel_ekle(struct alan_ogr *liste_basi,struct alan_ogr *eklenen)//ogrencinin aldigi nota gore dersin bagli listelerine ekletildigi fonksiyon
{
    struct alan_ogr *onceki,*gecici;

    onceki=liste_basi;
    gecici=liste_basi->noya_gore_sonraki;

    while (gecici!=liste_basi && gecici->numara<eklenen->numara){
        onceki=gecici;
        gecici=gecici->noya_gore_sonraki;
    }
    eklenen->noya_gore_sonraki=gecici;
    onceki->noya_gore_sonraki=eklenen;

    gecici=liste_basi->puana_gore_sonraki;
    while (gecici!=liste_basi && gecici->puan<eklenen->puan)
        gecici=gecici->puana_gore_sonraki;
    eklenen->puana_gore_onceki=gecici->puana_gore_onceki;
    eklenen->puana_gore_sonraki=gecici;
    gecici->puana_gore_onceki->puana_gore_sonraki=eklenen;
    gecici->puana_gore_onceki=eklenen;
}

struct alan_ogr *dairesel_arama(struct alan_ogr *liste_basi,int aranan_no)//ogr noya gore bir dersi alan ogrenciler icinde o ogrencinin aratildigi fonksiyon
{
    struct alan_ogr *gecici;

    gecici=liste_basi->noya_gore_sonraki;
    while (gecici!=liste_basi && gecici->numara<=aranan_no){
        if (gecici->numara==aranan_no)
            return gecici;
        gecici=gecici->noya_gore_sonraki;
    }
    return NULL;
}

void derse_gore_listele(struct alan_ogr *liste_basi,struct ogrenci *ilk_hashler[])
{
    struct alan_ogr *gecici;
    struct ogrenci *gecici2;
    int hash;

    gecici=liste_basi->noya_gore_sonraki;
    while (gecici!=liste_basi){
        hash=hash_fonksiyon(gecici->numara);
        gecici2=ilk_hashler[hash-1];
        while (gecici2!=NULL){
            if (gecici->numara==gecici2->ogr_no)
                printf("%-8d %-11s %-8d %-10d\n",gecici->numara,gecici2->ad_soyad,gecici2->sinif,gecici->puan);
            gecici2=gecici2->sonraki;
        }
        gecici=gecici->noya_gore_sonraki;
    }
}

void daireselden_cikar(struct alan_ogr *liste_basi,struct alan_ogr *cikarilacak)
{//verileri alinan ogrencinin ilgili oldugu derslerin bagli listelerinden cikarildigi fonksiyon
    struct alan_ogr *gecici,*onceki;

    onceki=liste_basi;
    gecici=liste_basi->noya_gore_sonraki;
    while (gecici!=liste_basi && gecici->numara<cikarilacak->numara){
        onceki=gecici;
        gecici=gecici->noya_gore_sonraki;
    }
    onceki->noya_gore_sonraki=gecici->noya_gore_sonraki;
    cikarilacak->puana_gore_onceki->puana_gore_sonraki=cikarilacak->puana_gore_sonraki;
    cikarilacak->puana_gore_sonraki->puana_gore_onceki=cikarilacak->puana_gore_onceki;
}

void daireselden_sil(struct ders *ptr[],int no)
{//verileri alinan ogrencinin ilgili oldugu derslerin bagli listelerinden silindigi fonksiyon
    struct alan_ogr *silinecek;
    int i;

    for (i=0;i<MAX_DERS;i++){
        if (ptr[i]!=NULL){
            silinecek=dairesel_arama((&ptr[i]->ogr),no);
            if (silinecek!=NULL){
                daireselden_cikar((&ptr[i]->ogr),silinecek);
                if (ptr[i]->ogr_say==1)
                    ptr[i]->genel_not_ort=0;
                else
                    ptr[i]->genel_not_ort=(ptr[i]->genel_not_ort*ptr[i]->ogr_say-silinecek->puan)/(ptr[i]->ogr_say-1);
                ptr[i]->ogr_say--;
                free(silinecek);
            }
        }
    }
}

void hashden_sil(struct ogrenci **ilk_ptr,int no)
{//ogr nosuna gore ogrenciyi bagli oldugu hash listesinden silen fonksiyon
    struct ogrenci *onceki,*gecici;

    gecici=*ilk_ptr;
    if ((*ilk_ptr)->ogr_no==no){
        *ilk_ptr=(*ilk_ptr)->sonraki;
        free(gecici);
    }
    else{
        onceki=*ilk_ptr;
        gecici=(*ilk_ptr)->sonraki;
        while (gecici!=*ilk_ptr && gecici->ogr_no!=no){
            onceki=gecici;
            gecici=gecici->sonraki;
        }
        onceki->sonraki=gecici->sonraki;
        free(gecici);
    }
}

void baraja_gore_yuksek(struct alan_ogr *liste_basi,struct ogrenci *ilk_hashler[],int baraj)
{//alinan sinir degerine gore ogrencilerin listelendigi fonksiyon
    struct alan_ogr *gecici;
    struct ogrenci *gecici2;
    int hash,top_ogr=0,basarili=0;

    gecici=liste_basi->puana_gore_onceki;
    while (gecici!=liste_basi){
        if (gecici->puan>baraj){
            basarili++;
            hash=hash_fonksiyon(gecici->numara);
            gecici2=ilk_hashler[hash-1];
            while (gecici2!=NULL){
                if (gecici->numara==gecici2->ogr_no)
                    printf("%-8d %-11s %-8d %-10d\n",gecici->numara,gecici2->ad_soyad,gecici2->sinif,gecici->puan);
                gecici2=gecici2->sonraki;
            }
        }
        top_ogr++;
        gecici=gecici->puana_gore_onceki;
    }
    printf("\nNotu %d'nin ustunde olan ogr sayisi:%d ve yuzdesi:%.2f dir.\n",baraj,basarili,(float)basarili*100/top_ogr);
}

void baraja_gore_alcak(struct alan_ogr *liste_basi,struct ogrenci *ilk_hashler[],int baraj)
{//alinan sinir degerine gore ogrencilerin listelendigi fonksiyon
    struct alan_ogr *gecici;
    struct ogrenci *gecici2;
    int hash,top_ogr=0,basarisiz=0;

    gecici=liste_basi->puana_gore_sonraki;
    while (gecici!=liste_basi){
        if (gecici->puan<baraj){
            basarisiz++;
            hash=hash_fonksiyon(gecici->numara);
            gecici2=ilk_hashler[hash-1];
            while (gecici2!=NULL){
                if (gecici->numara==gecici2->ogr_no)
                    printf("%-8d %-11s %-8d %-10d\n",gecici->numara,gecici2->ad_soyad,gecici2->sinif,gecici->puan);
                gecici2=gecici2->sonraki;
            }
        }
        top_ogr++;
        gecici=gecici->puana_gore_sonraki;
    }
    printf("\nNotu %d'nin altinda olan ogr sayisi:%d ve yuzdesi:%.2f dir.\n",baraj,basarisiz,(float)basarisiz*100/top_ogr);
}

void ogrenciye_gore_listele(struct ders *ptr[],int no)
{
    struct ders *gecici;
    struct alan_ogr *gecici2;
    int i;

    for (i=0;i<MAX_DERS;i++){
        gecici=ptr[i];
        if (gecici!=NULL){
            gecici2=ptr[i]->ogr.noya_gore_sonraki;
            while (gecici2!=&(ptr[i]->ogr)){
                if (gecici2->numara==no){
                    printf("%-11d %-11s %-7d %-10d\n",gecici->ders_kodu,gecici->ders_adi,gecici->kredi,gecici2->puan);
                    break;
                }
                gecici2=gecici2->noya_gore_sonraki;
            }
        }
    }
}

void sinif_listele(struct ogrenci *ilk_ptr[],int sinif)
{//alinan sinif numarasina gore ogrencilerin listelendigi fonksiyon
    struct ogrenci *gecici;
    int i,sinif_say=0,basarisiz=0;
    float top_ort=0;

    for (i=0;i<MAX_DERS;i++){
        gecici=ilk_ptr[i];
        while (gecici!=NULL){
            if (gecici->sinif==sinif){
                sinif_say++;
                top_ort+=gecici->agir_not_ort;
                printf("%-13d %-14s %-13d %-12d %.2f\n",gecici->ogr_no,gecici->ad_soyad,gecici->sinif,gecici->kredi_say,gecici->agir_not_ort);
                if (gecici->agir_not_ort<60)
                    basarisiz++;
            }
            gecici=gecici->sonraki;
        }
    }
    printf("\nSinifin ogrenci sayisi:%d\n",sinif_say);
    printf("Sinifin genel not ortalamasi:%.2f\n",top_ort/sinif_say);
    printf("Donemlik agirlikli not ort u 60'in altinda olan ogr sayisi:%d ve yuzdesi:%.2f\n",basarisiz,(float)basarisiz*100/sinif_say);
}
