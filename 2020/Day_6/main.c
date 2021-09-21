#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXLINE 2232

int part_one(char *s);

int main(){
    FILE *fptr;
    fptr = fopen("input.txt", "r");

    char answers[MAXLINE];
    char buffer[MAXLINE];
    int answer_count = 0;

    while(fgets(buffer, MAXLINE, fptr)){
        if(strcmp("\n", buffer)){
            strcat(answers, buffer);
        }
        else{
            answer_count += part_one(answers);
            memset(answers, MAXLINE, 0);
        }
    }
}

int part_one(char *s){
    char answer[MAXLINE];
    memset(answer, 0, MAXLINE);
    int _answer_count = 0;
    
    
}