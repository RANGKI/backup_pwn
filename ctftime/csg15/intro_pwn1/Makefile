CC = gcc
CFLAGS = -Wall -Wextra -g -std=c99 -g -fno-stack-protector -no-pie

intro-pwn: intro-pwn.c
	$(CC) $(CFLAGS) -o intro-pwn intro-pwn.c

clean:
	rm -f intro-pwn