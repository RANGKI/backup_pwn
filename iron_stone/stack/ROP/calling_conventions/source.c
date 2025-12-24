//gcc source.c -o vuln-32 -no-pie -fno-stack-protector -m32
//gcc source.c -o vuln-64 -no-pie -fno-stack-protector

#include <stdio.h>

void vuln(int check) {
    if(check == 0xdeadbeef) {
        puts("Nice!");
    } else {
        puts("Not nice!");
    }
}

int main() {
    vuln(0xdeadbeef);
    vuln(0xdeadc0de);
}