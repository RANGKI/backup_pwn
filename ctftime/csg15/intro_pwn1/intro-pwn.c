#include <stdio.h>
#include <stdlib.h>

// --------------------------------------------------- SETUP


void ignore_me_init_buffering()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

// --------------------------------------------------- VULNERABLE FUNCTION

void win()
{
    system("echo no cat /flag for you");
}

void vuln() {
    char name[16];
    printf("What is your name?\n");
    gets(name);
    printf("Hello %s!\nI have a present for you: %d\n", name, 0xc35f);
}

// --------------------------------------------------- MAIN

int main(int argc, char **argv)
{
    (void)argc;
    (void)argv;

	ignore_me_init_buffering();

    vuln();
    return 0;
}
