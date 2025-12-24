#include <stdio.h>
#include <string.h>
#include <stdlib.h>


__attribute__((constructor)) void init(){
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
}

char sh[8];

void win(){
	strcpy(sh, "/bi");
	strcpy(sh, "n/");
	strcpy(sh, "sh");
	system(sh);
}

int main(){
	char bof[0x100];
	puts("start your ctf journey from here (easy)");
	gets(bof);
	return 0;
}
