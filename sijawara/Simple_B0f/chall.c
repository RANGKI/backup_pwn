#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#define SECRET_PASS "SMKN7Semarang"

typedef enum
{
  no,
  yes
} Bool;

void flushBuffers()
{
  fflush(NULL);
}

void flag()
{
  system("/bin/cat flag.txt");
  flushBuffers();
}

Bool isPasswordCorrect(char *input)
{
  return (strncmp(input, SECRET_PASS, strlen(SECRET_PASS)) == 0) ? yes : no;
}

void authentication()
{
  Bool authenticationOpen = no;
  char inputPass[64];

  puts("Selamat datang di permainan BINARY EXPLOITATION\n");

  puts("langkah pertama masukkan password terlebih dahulu:");
  flushBuffers();

  scanf("%s", inputPass);

  if (authenticationOpen == no)
  {
    puts("Maaf password yang anda masukkan salah!");
    flushBuffers();
    return;
  }

  if (isPasswordCorrect(inputPass) == yes)
  {
    puts("Langkah pertama telah diselesaikan anda berhasil masuk.\nFLAG:");
    flag();
  }
  else
  {
    puts("ERROR, INCORRECT PASSWORD!");
    flushBuffers();
  }
}

int main()
{
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);

  authentication();

  return 0;
}