#include <stdio.h>

void vuln() {
    char buffer[100];
    gets(buffer);
}

int main() {
    vuln();
    return 0;
}