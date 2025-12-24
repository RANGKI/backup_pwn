// g++ -Wl,-z,relro,-z,now leaker.cpp -o leaker

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define messageSIZE 101
#define FLAG "CSC{tes_guys_hihi}"
#define USER "????????"
#define PASS "????????"

struct forum {
    char *post;
    forum *next;
};

void init(){
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
    alarm(10);
}

struct KoneForums {
    forum *head = NULL, *tail = NULL;
    forum *createMessage(char *message){
        forum *newPost = (forum *)malloc(sizeof(forum));
		newPost->post = (char *)malloc(sizeof(char)*messageSIZE);
		strncpy(newPost->post, message, messageSIZE - 1);
        newPost->post[messageSIZE - 1] = '\0';
		newPost->next = NULL;
        return newPost;
    }

	void post(char *message){
		forum *newMessage = createMessage(message);
		if (head == NULL) {
			head = tail = newMessage;
			return;
		}
		tail->next = newMessage;
		tail = newMessage;
	}

	void printer(int n, char *post){
		printf("%d. ", n);
		printf(post);
		puts("");
	}

	void viewPosts(){
		forum *curr = head;
		for (int n=1; curr; n++){
			printer(n, curr->post);
			curr = curr->next;
		}
	}

	void loader(char *user, char *pass){
		strcpy(user, USER);
		strcpy(pass, PASS);
	}

	void panel(char *username, char *password, char *user, char *pass){
		if ((strcmp(username, user) == 0) && (strcmp(password, pass) == 0)){
			puts("\x1b[32mAccess granted!\x1b[0m");
			printf("Flag : %s\n", FLAG);
		}
		else {
			puts("\x1b[31mAccess denied!\x1b[0m");
		}
	}
};

void koneForum(){
    short options;
	KoneForums product;
	char message[messageSIZE];
	char username[messageSIZE], password[messageSIZE], user[messageSIZE], pass[messageSIZE];

	for (;;) {
		puts("");
		puts("=== KoneForums ===");
		puts("1. Post a message");
		puts("2. View posts");
		puts("3. Admin panel");
		scanf("%1hd", &options);

		switch (options) {
			case 1:
				puts("\nEnter your message :");
				scanf(" %[^\n]", message);
				product.post(message);
				break;
			case 2:
				puts("");
				puts("Posts :");
				product.viewPosts();
				printf("Press enter to continue...");
				while (getchar() != '\n');
				getchar();
				break;
			case 3:
				puts("");
				printf("Enter your username : ");
				scanf(" %[^\n]", username);
				printf("Enter your password : ");
				scanf(" %[^\n]", password);
				product.loader(user, pass);

				product.panel(username, password, user, pass);
				printf("Press enter to continue...");
				while (getchar() != '\n');
				getchar();
				break;
			default:
				break;
		}
	}
}

int main(){
    init();
    koneForum();

    return 0;
}
