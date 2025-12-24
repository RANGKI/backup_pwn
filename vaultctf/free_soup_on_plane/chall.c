#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void soup_order_card(FILE *fp) {
    printf("Stewardess: Let's see what's in your soup order card...\n");
    ssize_t n = read(0, fp, 0x100);
    printf("Stewardess: Hmm, read %zd mysterious bytes from your card!\n", n);
}

void chef_serve_soup(FILE *fp) {
    char *buffer = malloc(0x100);
    printf("Chef: Scooping some soup into your bowl...\n");
    fread(buffer, 1, sizeof(buffer), fp);
    printf("Chef: Enjoy your free soup!\n");
}

void copilot_share_recipe(FILE *fp) {
    char *buffer = malloc(0x100);
    printf("Co-Pilot: Broadcasting the soup recipe to the whole plane...\n");
    fwrite(buffer, 1, sizeof(buffer), fp);
    printf("Co-Pilot: Soup recipe shared with everyone onboard!\n");
}

int main() {
    int choice;
    setvbuf(stdin, NULL, 2, 0);
    setvbuf(stdout, NULL, 2, 0);
    FILE *fp = fopen("/tmp/recipe.txt", "w+");

    while (1) {
        printf("\n🛫 Welcome to Free Soup on Plane 🛫\n");
        printf("What would you like to do?\n");
        printf("1. Give your soup order card to the stewardess\n");
        printf("2. Ask the chef for a free bowl of soup\n");
        printf("3. Ask the co-pilot to share the soup recipe\n");
        printf("4. Land the plane and exit\n");
        printf("Your choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                soup_order_card(fp);
                break;
            case 2:
                chef_serve_soup(fp);
                break;
            case 3:
                copilot_share_recipe(fp);
                break;
            case 4:
                printf("Captain: Thank you for flying with Free Soup Airlines. Goodbye!\n");
                return 0;
            default:
                printf("Stewardess: Sorry, that's not a valid selection.\n");
        }
    }
}
// gcc chall.c -o chall -no-pie -fno-stack-protector -Wl,-z,relro,-z,now