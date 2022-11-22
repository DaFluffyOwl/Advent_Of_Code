#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int StrtoInt(char *arr, FILE *ptr, int size);

int main(){
    FILE *fptr;

    fptr = fopen("input.txt", "r");
    int MAX_CHAR = 0;
    
    /*while(fgetc(fptr) != EOF){
        MAX_CHAR++;
    } */

    char s[441];
    StrtoInt(s, fptr, 441);
    

    fclose(fptr);
}

int StrtoInt(char *arr, FILE *ptr, int size){
    int x = 0;
    while (fgets(arr, size, ptr))
    {
        while(arr[x] != '\0'){
            if(arr[x] != ','){
                printf("%d ", (int)(arr[x]));
                }
                x++;
            }
        }

}