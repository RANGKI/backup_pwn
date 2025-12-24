// gcc source.c -o vuln-32 -no-pie -z execstack -m32
// gcc source.c -o vuln-64 -no-pie -z execstack

#include <stdio.h>

void vuln() {
    char buffer[20];

    puts("Give me the input");

    gets(buffer);
}

int main() {
    vuln();

    return 0;
}