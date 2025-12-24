// gcc -fno-stack-protector -z execstack -o password password.c 

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

__attribute__((naked)) void pop(){
	__asm__(
		"pop %rdi\nret\n"
		"pop %rsi\nret\n"
        "pop %rdx\nret\n"
		"pop %rcx\nret\n"
        "pop %r8\nret\n"
		);
}

void secret(long first, long second, long third, long fourth, long fifth) {
    char s[104];
    FILE *stream;

    stream = fopen("flag.txt", "r");
    if (!stream) {
        puts("flag.txt not found");
        exit(-1);
    }

    if (first == 0xdeadbeefdeadbeef && 
        second == 0xc0debabec0debabe && 
        third == 0x4141414141414141 && 
        fourth == 0x4242424242424242 && 
        fifth == 0x4343434343434343) {
        
        fgets(s, 100, stream);
        fclose(stream);
        printf("Wow, how did you get here? Here's the flag:\n%s\n", s);
    }
}

void questions() {
    char exp[64];  
    char temp[32]; 

    printf("Enter password\n: ");
    scanf("%31s", temp);
    if (strcmp(temp, "password") != 0) {
        printf("Error\n");
        exit(1);
    }

    printf("Password is incorrect\n: ");
    scanf("%31s", temp);
    if (strcmp(temp, "incorrect") != 0) {
        printf("Error\n");
        exit(1);
    }

    printf("Try again\n: ");
    scanf("%31s", temp);
    if (strcmp(temp, "again") != 0) {
        printf("Error\n");
        exit(1);
    }

    printf("Please try again later\n: ");
    scanf(" %31[^\n]", temp);
    if (strcmp(temp, "again later") != 0) {
        printf("Error\n");
        exit(1);
    }

    while (getchar() != '\n'); 

    printf("What percentage do you remember the password?\n: ");
    gets(temp); 
    printf("like this? ");
    printf(temp);
    printf("\n");
    
    printf("Please try ......\n: ");
    gets(exp);
}

int main() {
    setbuf(stdout, NULL); 
    questions();
    return 0;
}
