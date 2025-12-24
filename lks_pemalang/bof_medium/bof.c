#include <stdio.h>
#include <string.h>
#include <stdlib.h>


__attribute__((naked)) void help(){
	__asm__(
		"pop %rdi\nret\n"
		"pop %rsi\nret\n"
		"pop %rdx\nret\n"
		);
}

__attribute__((constructor)) void init(){
	setbuf(stdin, NULL);
	setbuf(stdout, NULL);
}

char sh[8];

void win(unsigned int a, unsigned int b, unsigned int c){
	if (a != 0xdeadbeef) exit(0);
	strcpy(sh, "/bi");
	if (b != 0xfacebeeb) exit(0);
	strcpy(sh, "n/");
	if (c != 0xdeadface) exit(0);
	strcpy(sh, "sh");
	system(sh);
}

int main(){
	char bof[0x100];
	puts("start your ctf journey from here (medium)");
	gets(bof);
	return 0;
}
