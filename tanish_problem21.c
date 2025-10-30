#include <stdio.h>

int main()
{
    float c;
    printf("Celcius value is: ");
    scanf("%f", &c);
    printf("Fahrenheit is: %f\n", (c*9.0/5.0)+32.0);
    return 0;
}
