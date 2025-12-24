#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);

  char buf[136];
  char flag[49];
  char *flag_ptr = flag;
  
  gid_t gid = getegid();
  setresgid(gid, gid, gid);

  puts("Input");
  
  FILE *file = fopen("flag.txt", "r");
  if (file == NULL) {
    printf("flagnya nggak ada\n");
    exit(0);
  }
  
  fgets(flag, sizeof(flag), file);
  
  while(1) {
    fgets(buf, sizeof(buf), stdin);
    printf(buf);
  }  
  return 0;
}