#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main()
{
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);

    char buf[0x100] = {0};
    read(0, buf, 0x100);
    printf(buf);

    exit(0);

    return 0;
}

// gcc -no-pie -o chall chall.c 