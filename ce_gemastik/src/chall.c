#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <signal.h>
#include <sys/types.h>

#define MAX_SIZE 256

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

void elysia()
{
    puts("Elysia smiles softly, her eyes sparkling with warmth.");
    system("/bin/sh");
}

void her_embrace()
{
    printf("Elysia pulls you into a warm, gentle embrace...\n\n");
    printf("She whispers, 'What do you want to say to me?'\n> ");

    char thoughts[MAX_SIZE];
    if (fgets(thoughts, sizeof(thoughts) * 2, stdin) == NULL)
    {
        puts("You didn't say anything. And it leaves Elysia feeling a bit sad.");
        return;
    }
}

int main(int argc, char const *argv[])
{
    init();
    her_embrace();
    return 0;
}
