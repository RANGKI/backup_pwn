#include <stdio.h>
#include <string.h>
#include <stdlib.h>

__attribute__((constructor)) void init(){
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
}

char sh[8] = "/bin/sh\0";

int main(){
	char bof[0x100];
	unsigned long ovt = 0;
	puts("start your pwn journey here (easy)");
	gets(bof);

	if (ovt > 0) {
		system(sh);
	} else {
		exit(0);
	}
	return 0;
}
