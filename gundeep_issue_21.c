#include <stdio.h>

float celsius_to_fahrenheit(float c) {
    return (c * 9.0 / 5.0) + 32.0;
}

float fahrenheit_to_celsius(float f) {
    return (f - 32.0) * 5.0 / 9.0;
}

float celsius_to_kelvin(float c) {
    return c + 273.15;
}

float kelvin_to_celsius(float k) {
    return k - 273.15;
}

float fahrenheit_to_kelvin(float f) {
    return (f - 32.0) * 5.0 / 9.0 + 273.15;
}

float kelvin_to_fahrenheit(float k) {
    return (k - 273.15) * 9.0 / 5.0 + 32.0;
}

int main() {
    int choice;
    float temp, result;

    printf("🌡️ Temperature Converter\n");
    printf("1. Celsius to Fahrenheit\n");
    printf("2. Fahrenheit to Celsius\n");
    printf("3. Celsius to Kelvin\n");
    printf("4. Kelvin to Celsius\n");
    printf("5. Fahrenheit to Kelvin\n");
    printf("6. Kelvin to Fahrenheit\n");

    printf("\nEnter your choice (1-6): ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            printf("Enter temperature in Celsius: ");
            scanf("%f", &temp);
            result = celsius_to_fahrenheit(temp);
            printf("%.2f°C = %.2f°F\n", temp, result);
            break;
        case 2:
            printf("Enter temperature in Fahrenheit: ");
            scanf("%f", &temp);
            result = fahrenheit_to_celsius(temp);
            printf("%.2f°F = %.2f°C\n", temp, result);
            break;
        case 3:
            printf("Enter temperature in Celsius: ");
            scanf("%f", &temp);
            result = celsius_to_kelvin(temp);
            printf("%.2f°C = %.2f K\n", temp, result);
            break;
        case 4:
            printf("Enter temperature in Kelvin: ");
            scanf("%f", &temp);
            result = kelvin_to_celsius(temp);
            printf("%.2f K = %.2f°C\n", temp, result);
            break;
        case 5:
            printf("Enter temperature in Fahrenheit: ");
            scanf("%f", &temp);
            result = fahrenheit_to_kelvin(temp);
            printf("%.2f°F = %.2f K\n", temp, result);
            break;
        case 6:
            printf("Enter temperature in Kelvin: ");
            scanf("%f", &temp);
            result = kelvin_to_fahrenheit(temp);
            printf("%.2f K = %.2f°F\n", temp, result);
            break;
        default:
            printf("Invalid choice. Please run again.\n");
    }

    return 0;
}
