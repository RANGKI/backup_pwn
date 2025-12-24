#include <stdio.h>

void init()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

int main(int argc, char const *argv[])
{
    init();
    char your_promise[64];
    puts("You stand before Elysia, your heart full.");
    puts("You look into her eyes and make an unbreakable promise... ");
    gets(your_promise);
    return 0;
}