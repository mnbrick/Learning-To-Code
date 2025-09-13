#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt the user for change owed, in cents
    int cents;
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);

    // Calculate how many quarters you should give customer
    // Subtract the value of those quarters from cents
    int quarters = (cents / 25);
    cents = (cents - quarters * 25);

    // Calculate how many dimes you should give customer
    // Subtract the value of those dimes from remaining cents
    int dimes = (cents / 10);
    cents = (cents - dimes * 10);

    // Calculate how many nickels you should give customer
    // Subtract the value of those nickels from remaining cents
    int nickels = (cents / 5);
    cents = (cents - nickels * 5);

    // Calculate how many pennies you should give customer
    // Subtract the value of those pennies from remaining cents
    int pennies = (cents);

    // Sum the number of quarters, dimes, nickels, and pennies used
    // Print that sum
    int change = (quarters + dimes + nickels + pennies);
    printf("%i\n", change);
}
