#include <stdio.h>

void win() {
puts("win");
}

void vuln() {
int lol = 29330203;

char buffer[60];
puts("Overflow me: ");
gets(buffer);


}

int main(int argc, char **argv) {
vuln();
return 0;
}