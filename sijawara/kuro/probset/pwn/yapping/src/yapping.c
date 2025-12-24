//gcc -no-pie -fstack-protector -z execstack -o yapping yapping.c

#include <stdio.h>
#include <stdlib.h>
#include <sys/ptrace.h>
#include <unistd.h>

void anti_hacker() {
    if (ptrace(PTRACE_TRACEME, 0, NULL, NULL) == -1) {
        printf("I thought you were better than this, lil hacker!\n");
        exit(1);
    }
}

void flag() {
    char s[104];
    FILE *stream;

    stream = fopen("flag.txt", "r");
    if (!stream) {
        puts("flag.txt not found");
        exit(-1);
    }

    fgets(s, 100, stream);
    fclose(stream);
    printf("Nih flag:\n%s\n", s);
}

void exploit() {
    char buffer[64];

    while(1) {
        printf("Mana yapping nya? ");
        gets(buffer);
        

        if (strncmp(buffer, "exit", 4) == 0) {
            break;
        }
        else {
            printf("oaoaoaoa");
            printf(buffer);
            printf("\n");
        }
    }

    printf("Udah yapping nya? ");
    gets(buffer);
}

int main() {
    setbuf(stdout, NULL); 
    anti_hacker();
    exploit();
    return 0;
}
