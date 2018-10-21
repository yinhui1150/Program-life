/*
 * just for pratice
*/
#if 0

#include <stdio.h>
#include <stdlib.h>
#define MAX_LINE_NUM  200
void main()
{
    char c;
    char buf[MAX_LINE_NUM];
    int i;

    i = 0;
    while((c = getchar()) != EOF) {
        if (c == ' ') {
            buf[i] = '\n';
        } else {
            buf[i] = c;
        }
        
        i++;
    }
    buf[i - 2] = '\0';
    puts(buf);
}
#endif

#if 0 /* 该程序读入一组文本行，并把 最长的文本行打印出来*/

#include <stdio.h>
#define MAXLINE 1000 /* 每行最长以及文件最长的行数 */


static int getline(char s[], int lim)
{
    int c, i;

    for (i = 0; (i < lim - 1) && ((c = getchar()) != EOF) && c != '\n'; i++) {
        s[i] = c;
    }

    if (c == '\n') {
        s[i] = c;
        i++;
    } 

    s[i] = '\0';
    return i;
}

void copy(char to[], char from[])
{
    int i;
    i = 0;
    while((to[i] = from[i]) != '\0') {
        i++;
    }
}
    
void main()
{
    int max;
    int len;
    char line[MAXLINE];
    char longest[MAXLINE];

    max = 0;
    while((len = getline(line, MAXLINE)) > 0) {
        if (len > max) {
            max = len;
            copy(longest, line);
        }
    }

    if (max != 0) {
        printf("longest string is  %s.\n", longest);
    }
    return;
    
}
#endif

#if 1
#include<stdio.h>

#define MAXLINE 1000

char pattern[] = "ould";
static int my_get_line(char s[], int lim)
{
    int c, i;

    for (i = 0; (i < lim - 1) && ((c = getchar()) != EOF) && c != '\n'; i++) {
        s[i] = c;
    }

    if (c == '\n') {
        s[i] = c;
        i++;
    } 

    s[i] = '\0';
    return i;
}

int strindex(char s[], char t[])
{
    int i, j, k;

    for (i = 0; s[i] != '\0'; i++) {
        for (j = i, k = 0; t[k] != '\0' && s[j] == t[k]; j++, k++) {
            ;
        }

        if (k > 0 && t[k] == '\0') {
            return i;
        }
    }

    return -1;
}

void main()
{
    char line[MAXLINE];

    while(my_get_line(line, MAXLINE) > 0) {      
        if (strindex(line, pattern) >= 0) {
            printf("%s", line);
        }
    }

    return;
}
#endif

