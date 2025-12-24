#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// --------------------------------------------------- SETUP

void ignore_me_init_buffering()
{
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

// --------------------------------------------------- VULNERABLE FUNCTION

int bug = 0;
void vuln()
{
    char name[1024];
    printf("What is your name?\n");
    int number_read = read(STDIN_FILENO, name, sizeof(name) - 1);
    name[number_read-1] = 0;
    printf("Thank you ");
    printf(name);
    printf("!\n");
    if(bug){
        printf("Oh, you got here somehow, you must have triggered a bug.. Here is the flag: ");
        system("cat /flag");
        exit(0);
    }
    printf("But our flag is in another branch!\n");
}

// --------------------------------------------------- MAIN

int main(int argc, char **argv)
{
    (void)argc;
    (void)argv;
    ignore_me_init_buffering();

    vuln();
}