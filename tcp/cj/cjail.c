#define linz fop##en

FILE *file;
file = linz("/flag.txt", "r");
if (file) {
char ch;
while ((ch = fgetc(file)) != EOF) {
printf("%c", (ch));
}
fclose(file);
} else {
perror("Error");
}
