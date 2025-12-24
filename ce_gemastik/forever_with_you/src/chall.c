#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

#define MAX_MEMORIES 100
#define MAX_MEMORY_SIZE 0x500

void init()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    alarm(30);
}

void menu()
{
    puts("\n===================================");
    puts("      Our Precious Memories 💌     ");
    puts("===================================");
    puts("1. 📝 Record a new memory with Elysia");
    puts("2. 💭 Reminisce about a memory");
    puts("3. 💔 Let go of a memory");
    puts("4. 🚶 Walk into the future with her");
    puts("===================================");
}

void record_memory(void **memories)
{
    int sz;
    printf("How long is your new memory? ");
    scanf("%d", &sz);
    if (sz <= 0 || sz > MAX_MEMORY_SIZE)
    {
        puts("Your memory feels a bit... empty. 💔");
        return;
    }
    char *new_memory = malloc(sz + 1);
    if (new_memory == NULL)
    {
        puts("Your mind feels a bit hazy...");
        return;
    }

    printf("Describe your new memory with her: ");
    read(0, new_memory, MAX_MEMORY_SIZE - 1);

    for (int i = 0; i < MAX_MEMORIES; i++)
    {
        if (memories[i] == NULL)
        {
            memories[i] = new_memory;
            printf("You've carefully stored the memory at slot %d. 🗃️\n", i);
            return;
        }
    }
    free(new_memory);
    puts("Your heart is too full to hold any more new memories. ❤️");
}

void reminisce_memory(void **memories)
{
    int idx;
    printf("Which memory do you want to look back on? ");
    scanf("%d", &idx);

    if (idx < 0 || idx >= MAX_MEMORIES + 1 || memories[idx] == NULL)
    {
        puts("That memory feels a bit fuzzy... 🤔");
    }
    else
    {
        printf("\n-- Memory %d --\n", idx);
        printf("%s\n", (char *)memories[idx]);
        printf("-- End of Memory --\n");
    }
}

void let_go_of_memory(void **memories)
{
    int idx;
    printf("Which memory do you need to let go of? ");
    scanf("%d", &idx);

    if (idx < 0 || idx >= MAX_MEMORIES || memories[idx] == NULL)
    {
        puts("You can't seem to recall that one... ❓");
    }
    else
    {
        free(memories[idx]);
        puts("The memory fades away... 💨");
    }
}

int main(int argc, char const *argv[])
{
    void *memories[MAX_MEMORIES];
    memset(memories, 0, sizeof(memories));
    int choice;
    init();
    puts("You decide to keep a diary of your time with Elysia. 📔");
    while (1)
    {
        menu();
        printf("> ");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            record_memory(memories);
            break;
        case 2:
            reminisce_memory(memories);
            break;
        case 3:
            let_go_of_memory(memories);
            break;
        case 4:
            puts("You close the diary, ready for what comes next. 💕");
            puts("Elysia smiles at you, and you both walk into the future together. 🌅");
            return 0;
        default:
            puts("An unfamiliar feeling... 😵‍💫");
            break;
        }
    }
    return 0;
}