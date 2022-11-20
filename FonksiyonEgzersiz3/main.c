#include <stdio.h>
#include <stdlib.h>

int faktoriyel(int sayim)
{

    int i;
    int sonuc=1;

    for(i=1;i<=sayim;i++)
    {
        sonuc=sonuc*i;
    }
    return sonuc;
}





int main()
{
   /*Klavyeden girilen bir tamsayının faktoriyelini fonksiyon kullanarak hesaplayan C programını yazınız
    */
    int sayi;
    printf("Lutfen bir sayi griniz");
    scanf("%d",&sayi);
    printf("%d! = %d",sayi,faktoriyel(sayi));
    return 0;
}
