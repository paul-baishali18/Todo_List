#include <stdio.h>
#include <stdlib.h>
#include <time.h>   // For seeding the random number generator
#include <ctype.h>  // For tolower() function

/**
 * @brief Gets the computer's random choice.
 * @return int 0 for Rock, 1 for Paper, 2 for Scissors
 */
int getComputerChoice() {
    // rand() % 3 generates a number between 0, 1, or 2
    return rand() % 3;
}

/**
 * @brief Gets the user's choice and validates it.
 * @return int 0 for Rock, 1 for Paper, 2 for Scissors, -1 for invalid
 */
int getUserChoice() {
    char choice;
    printf("Enter your choice (r for rock, p for paper, s for scissors): ");
    scanf(" %c", &choice); // Notice the space before %c to consume whitespace

    choice = tolower(choice); // Convert to lowercase

    if (choice == 'r') {
        return 0; // Rock
    } else if (choice == 'p') {
        return 1; // Paper
    } else if (choice == 's') {
        return 2; // Scissors
    } else {
        printf("Invalid choice. Please try again.\n");
        return -1; // Invalid input
    }
}

/**
 * @brief Prints the name of the choice based on its integer value.
 * @param choice The integer choice (0, 1, or 2).
 */
void printChoice(int choice) {
    switch (choice) {
        case 0: printf("Rock"); break;
        case 1: printf("Paper"); break;
        case 2: printf("Scissors"); break;
    }
}

/**
 * @brief Determines and prints the winner of the round.
 * @param user The user's choice (0, 1, or 2).
 * @param comp The computer's choice (0, 1, or 2).
 */
void determineWinner(int user, int comp) {
    printf("You chose: ");
    printChoice(user);
    printf("\nComputer chose: ");
    printChoice(comp);
    printf("\n\n");

    // Logic for winning
    // (user - comp + 3) % 3 is a common trick for this game's logic
    // Result 0 = Tie
    // Result 1 = User wins
    // Result 2 = Computer wins
    
    int result = (user - comp + 3) % 3;

    if (result == 0) {
        printf("It's a tie! 🤝\n");
    } else if (result == 1) {
        // User wins (Rock > Scissors, Paper > Rock, Scissors > Paper)
        printf("You win! 🎉\n");
    } else { // result == 2
        // Computer wins
        printf("You lose. 😟\n");
    }
}

int main() {
    char playAgain = 'y';
    
    // Seed the random number generator *once* at the start of the program
    srand(time(NULL));

    while (playAgain == 'y' || playAgain == 'Y') {
        int userChoice = -1;
        
        // Loop until user gives valid input
        while (userChoice == -1) {
            userChoice = getUserChoice();
        }

        int compChoice = getComputerChoice();

        determineWinner(userChoice, compChoice);

        printf("----------------------------------\n");
        printf("Do you want to play again? (y/n): ");
        scanf(" %c", &playAgain);
        
        // Clear the input buffer in case of multiple character entries
        while (getchar() != '\n'); 
    }

    printf("\nThanks for playing! 👋\n");
    return 0;
}