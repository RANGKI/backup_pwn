#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *gets(char *s);

int Clannad(){
  system("/bin/sh");
}

int vuln(){
  char buffer[64];
  printf("Welcome to the world of dango daikazoku\n");
  printf("enter a dango:");
  gets(buffer);
}

int main(){
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stdin, 0, 2, 0);
  setvbuf(stderr, 0, 2, 0);

  vuln();
  printf("Hello\n");
  return 0;
}
