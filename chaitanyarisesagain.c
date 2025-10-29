#include <stdio.h>

int main() {
    int inputtemp;
    char corf;
    float outputtemp;

    printf("Enter your source temperature (e.g., 32C or 100F): ");
    scanf("%d%c", &inputtemp, &corf);

    switch(corf) {
        case 'F':
        case 'f':
            outputtemp = (inputtemp - 32) * 5.0 / 9.0;
            printf("%.2fC\n", outputtemp);
            break;

        case 'C':
        case 'c':
            outputtemp = (inputtemp * 9.0 / 5.0) + 32;
            printf("%.2fF\n", outputtemp);
            break;

        default:
            printf("Invalid input. Please use format like 32C or 100F.\n");
            break;
    }

    return 0;
}
