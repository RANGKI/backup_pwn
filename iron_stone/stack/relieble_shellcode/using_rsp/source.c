#include <stdio.h>

int test = 0;

int main() {
    char input[100];

    puts("Get me with shellcode and RSP!");
    gets(input);

    if(test) {
        asm("jmp *%rsp");
        return 0;
    }
    else {
        return 0;
    }
}