//gcc -no-pie -fno-stack-protector -z execstack -std=gnu99 -o blind blind.c

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void win() {
    FILE *f = fopen("flag.txt", "r");
    if (f == NULL) {
        printf("Flag tidak ditemukan!\n");
        exit(1);
    }
    char flag[128];
    if (fgets(flag, sizeof(flag), f)) {
        printf("Flag: %s\n", flag);
    } else {
        printf("Gagal membaca flag.\n");
    }
    fclose(f);
    exit(0);
}

void (*target)() = NULL;

void vuln() {
    char input[256];
    char buffer[512];
    
    printf("Masukkan input: ");
    fflush(stdout);
    
    if (fgets(input, sizeof(input), stdin) == NULL) {
        printf("Terjadi kesalahan membaca input.\n");
        exit(1);
    }
    input[strcspn(input, "\n")] = '\0';
    snprintf(buffer, sizeof(buffer), input);
}

int main() {
    setbuf(stdout, NULL);
    
    printf("== Blind Format String Challenge ==\n");
    printf("Cari cara untuk mengubah pointer 'target' sehingga mengarah ke fungsi 'win'\n");
    printf("kemudian flag akan dicetak.\n\n");
    
    vuln();

    if (target) {
        target();
    } else {
        printf("Tidak ada aksi yang terjadi.\n");
    }
    
    return 0;
}
