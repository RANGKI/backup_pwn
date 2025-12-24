#define _GNU_SOURCE

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <link.h>
#include <dlfcn.h>
// intro-rop: gcc intro-rop.c -o intro-rop

// --------------------------------------------------- SETUP

void ignore_me_init_buffering()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

typedef struct ropgadget
{
    unsigned int length;
    unsigned char gadget[32];
} ropgadget_t;

typedef unsigned long long u64;

// --------------------------------------------------- ROP GADGETS
void gadget_0();
void gadget_1();
void gadget_2();
void gadget_3();
void gadget_4();
void gadget_5();
void gadget_6();
void gadget_7();
void gadget_8();
void gadget_9();
void gadget_10();
void gadget_11();
void gadget_12();
void gadget_13();
void gadget_14();
void gadget_15();
__asm(
    ".intel_syntax noprefix                     \n"
    ".global gadget_0                           \n"
    ".global gadget_1                           \n"
    ".global gadget_2                           \n"
    ".global gadget_3                           \n"
    ".global gadget_4                           \n"
    ".global gadget_5                           \n"
    ".global gadget_6                           \n"
    ".global gadget_7                           \n"
    ".global gadget_8                           \n"
    ".global gadget_9                           \n"
    ".global gadget_10                          \n"
    ".global gadget_11                          \n"
    ".global gadget_12                          \n"
    ".global gadget_13                          \n"
    ".global gadget_14                          \n"
    ".global gadget_15                          \n"

    "gadget_0:                                  \n"
    "       pop rax                             \n"
    "       ret                                 \n"

    "gadget_1:                                  \n"
    "       add rbx, r9                         \n"
    "       ret                                 \n"

    "gadget_2:                                  \n"
    "       mov rcx, qword ptr [rbx]            \n"
    "       ret                                 \n"

    "gadget_3:                                  \n"
    "       mov rax, r8                         \n"
    "       mov rbx, r9                         \n"
    "       mov rcx, r10                        \n"
    "       ret                                 \n"

    "gadget_4:                                  \n"
    "       xor rcx, rdi                        \n"
    "       xor rbx, rdi                        \n"
    "       ret                                 \n"

    "gadget_5:                                  \n"
    "       push rax                            \n"
    "       ret                                 \n"

    "gadget_6:                                  \n"
    "       xor rax, rax                        \n"
    "       xor rsi, rsi                        \n"
    "       ret                                 \n"

    "gadget_7:                                  \n"
    "       sub rax, 0x8                        \n"
    "       idiv rdi                            \n"
    "       ret                                 \n"

    "gadget_8:                                  \n"
    "       add rdi, r8                         \n"
    "       ret                                 \n"

    "gadget_9:                                  \n"
    "       nop                                 \n"
    "       ret                                 \n"

    "gadget_10:                                 \n"
    "       imul rbx, rax                       \n"
    "       ret                                 \n"

    "gadget_11:                                 \n"
    "       xor r9, r8                          \n"
    "       xor r8, r9                          \n"
    "       xor r9, r8                          \n"
    "       ret                                 \n"

    "gadget_12:                                 \n"
    "       mov rcx, rsi                        \n"
    "       add rcx, r10                        \n"
    "       ret                                 \n"

    "gadget_13:                                 \n"
    "       xor rdi, rcx                        \n"
    "       xor rsi, rcx                        \n"
    "       ret                                 \n"

    "gadget_14:                                 \n"
    "       pop rbx                             \n"
    "       push rdi                            \n"
    "       push rbx                            \n"
    "       ret                                 \n"

    "gadget_15:                                 \n"
    "       pop rbp                             \n"
    "       pop rsi                             \n"
    "       ret                                 \n"

    ".att_syntax prefix                        \n");

void *gadgets[] = {
    gadget_0,
    gadget_1,
    gadget_2,
    gadget_3,
    gadget_4,
    gadget_5,
    gadget_6,
    gadget_7,
    gadget_8,
    gadget_9,
    gadget_10,
    gadget_11,
    gadget_12,
    gadget_13,
    gadget_14,
    gadget_15,
};

// --------------------------------------------------- HELPER FUNCTIONS

// get the address of a libc function
u64 get_libc_addr(const char *func)
{
    void *handle = dlopen("libc.so.6", RTLD_LAZY);
    if (!handle)
    {
        fprintf(stderr, "Error opening libc: %s\n", dlerror());
        return 0;
    }

    u64 func_addr = (u64)dlsym(handle, func);
    if (!func_addr)
    {
        fprintf(stderr, "Error getting symbol address: %s\n", dlerror());
        dlclose(handle);
        return 0;
    }

    dlclose(handle);
    return func_addr;
}

// libc usually contains a "/bin/sh" string, this function finds it
u64 get_binsh_str()
{
    void *handle = dlopen("libc.so.6", RTLD_LAZY);
    if (!handle)
    {
        fprintf(stderr, "Error opening libc: %s\n", dlerror());
        return 0;
    }

    struct link_map *map;
    if (dlinfo(handle, RTLD_DI_LINKMAP, &map) != 0)
    {
        fprintf(stderr, "Error getting link map: %s\n", dlerror());
        dlclose(handle);
        return 0;
    }
    dlclose(handle);
    return (u64)memmem((void *)map->l_addr, 0x10000000, "/bin/sh\x00", 8);
}

// get the address of the puts GOT entry
u64 get_puts_got()
{
    void *dyn = _DYNAMIC;
    Dl_info info;
    if (dladdr(dyn, &info) == 0)
    {
        fprintf(stderr, "Error getting dynamic address: %s\n", dlerror());
    }
    u64 needle = get_libc_addr("puts");
    return (u64)memmem((void *)info.dli_fbase, 0x10000, (void *)&needle, sizeof(void *));
}

// --------------------------------------------------- Challenge

void print_stuff()
{
    u64 *new_stack = (u64 *)malloc(1024 * 1024);

    puts("Enter the index of each ROP gadget");
    puts("Finish your ROP chain with the index -1");

    signed int lastIndex = 0;
    int counter = 0;
    int maxIndex = sizeof(gadgets) / sizeof(gadgets[0]);

    u64 diff_puts_Binsh = get_binsh_str() - get_libc_addr("puts");
    u64 diff_puts_System = get_libc_addr("system") - get_libc_addr("puts");
    u64 puts_got = get_puts_got();

    while (lastIndex != -1)
    {
        printf("\n> Enter gadget index: ");
        scanf("%d", &lastIndex);

        if (lastIndex >= maxIndex || (lastIndex < 0 && lastIndex != -1))
        {
            printf("Invalid index, bye!\n");
            exit(-1);
        }

        new_stack[counter++] = (u64)gadgets[lastIndex];
    }

    printf("Lets goooo ! :)\n");
    u64 rbp = 0; // Get stack address of return pointer to overwrite it
    __asm("mov %%rbp, %0\n" : "=r"(rbp));
    rbp += 8; // Adjust for return address

    memcpy((void *)rbp, (void *)new_stack, counter * 8);

    __asm(
        ".intel_syntax noprefix\n"
        "mov rsp, %0\n"
        "mov r8, %1\n"
        "mov r9, %2\n"
        "mov r10, %3\n"
        "leave\n"
        "ret\n"
        ".att_syntax prefix\n" : : "r"(new_stack), "r"(diff_puts_System), "r"(puts_got), "r"(diff_puts_Binsh));
}

// --------------------------------------------------- MAIN

void main(int argc, char *argv[])
{
    ignore_me_init_buffering();

    print_stuff();
}