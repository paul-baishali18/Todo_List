#include<stdio.h>
int main()
{
    float c,f;
    printf("enter temp in celcius:");
    scanf("%f",&c);
    f=((9.0/5)*c)+32;
    printf("temp in fah: %f",f);
    return 0;

}