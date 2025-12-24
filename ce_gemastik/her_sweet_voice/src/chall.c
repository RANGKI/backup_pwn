#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <signal.h>

void timeout_handler(int signum)
{
    puts("\nYou pause for a moment, gathering your thoughts...");
    exit(1);
}

void init()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    signal(SIGALRM, timeout_handler);
    alarm(60);
}

void menu()
{
    puts("1. Hear her sweet voice ❤️");
    puts("2. Listen to her soft singing~ 🎶");
    puts("3. Give her a hug 🤗");
    puts("4. Exit ❌");
}

int main(int argc, char const *argv[])
{
    init();
    short choice = 0;
    int keyToHerHeart = 0;
    char input[100];

    puts("You go on a second date with Elysia. ❤️");
    puts("You are sitting on a bench in the park, enjoying the beautiful weather together.");
    puts("You can hear her sweet voice, and you want to cherish this moment.");
    puts("What will you do?");
    while (true)
    {
        menu();
        fputs("> ", stdout);
        scanf("%lld", &choice);
        switch (choice)
        {
        case 1:
            puts("You hear her sweet voice, and it makes you feel warm inside. ❤️");
            puts("You want to cherish this moment forever.");
            break;
        case 2:
            puts("You listen to her soft singing, and it fills your heart with joy. 🎶");
            puts("You want to cherish this moment forever.");
            break;
        case 3:
            puts("You hugged her tightly, and she smiled at you. ❤️");
            // Explanation:
            /*
            1 = I
            4 = Love
            3 = You
            24 = 24
            7 = 7
            keyToHearHeart = I Love You 24/7
            */
            if (keyToHerHeart == 143247)
            {
                printf("You braced yourself and whispered to her: ");
                scanf("%s", input);
            }
            break;
        case 4:
            puts("You said goodbye to her. This concludes today's date! ❤️");
            return 0;
        default:
            puts("Elysia looks at you with a confused expression. ❓");
        }
    }

    return 0;
}
