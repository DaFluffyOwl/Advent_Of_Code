#include <stdio.h> 
#include <stdlib.h>

int part_one(int min, int max, char c, char *password){
    int count = 0;
    while(*password){
        if(*password == c){
            count++;
        }
        password++;
    }
    if(count < min || count > max){
        return 0;
    }
    else{
        return 1;
    }
}

int part_two(int index_min, int index_max, char c, char* password){
    if(password[index_min - 1] == c ^ password[index_max - 1] == c){
        return 1;
    }
    else{
        return 0;
    }
}

int main() {
    FILE *fptr;
    fptr = fopen("input.txt", "r");

    int min, max;
    char c;
    char str[50];

    int valid_sled = 0;
    int valid_toboggan = 0;

     while(fscanf(fptr, "%d-%d %c: %s", &min, &max, &c, str) == 4){
         valid_sled += part_one(min, max, c, str);
         valid_toboggan += part_two(min, max, c, str);
     }
     
     printf("There are %d valid sleds\n", valid_sled);
     printf("There are %d valid toboggans\n", valid_toboggan);
     fclose("input.txt");
 }
