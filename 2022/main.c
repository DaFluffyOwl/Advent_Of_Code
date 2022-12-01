#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int main(){
    FILE *fptr;
    fptr = fopen("input.txt", "r");
    int str[700];
    char buffer[50];
    int i = 2;
    int j = 0;


    while(buffer[1] != EOF){
        buffer[0] = buffer[1];
        buffer[1] = fgetc(fptr);
        //printf("%c", buffer[1]);
        if(buffer[0] == '\n' && buffer[1] == '\n'){
            printf("Here");
            buffer[i] = 'e';
            for(int j = 2; buffer[j] != 'e'; j++){
                printf("%c", buffer[j]);
            }
        }
        else{
            buffer[i] = buffer[1];
            //printf("%c", buffer[i]);
            i++;
        }
    }
    
}

int chartoint(char *c, int len){
    
}