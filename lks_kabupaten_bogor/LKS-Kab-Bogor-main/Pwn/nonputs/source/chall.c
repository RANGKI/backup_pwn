#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

char buff[] = "echo 'Selamat Mengerjakan LKS!'";

int main()
{
    char buf[0x100];

    system(buff);
    read(0, buf, 0x1000);
    return 0;
}

// gcc -no-pie -fno-stack-protector -o chall chall.c 