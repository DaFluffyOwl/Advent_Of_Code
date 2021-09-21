#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#define MAXLINE 965
#define SEAT_ROW 127
#define SEAT_COLUMN 8

int part_one(char *s);
int part_two(char *s);
int average_of_two(int a, int b);
int is_max(int n);

int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

int main(){
    FILE *fptr;
    fptr = fopen("input.txt", "r");
    char seat[MAXLINE];
    int ID = 0;
    int max = 0;
    int my_seat = 0;
    int all_ID[MAXLINE];
    int x = 0;


    while(fgets(seat, MAXLINE, fptr)){
        ID = part_one(seat);
        all_ID[x] = part_one(seat);
        x++;    
        if(ID > max){
            max = ID;
        }
    }
    qsort(all_ID, MAXLINE, sizeof(int), cmpfunc);
    int temp = 13; //13 is minumum seat id
    int id = 0; 
    for(int i = 0; i < MAXLINE; i++){
        id = all_ID[i];
        if(temp + 1 != id){
            my_seat = temp+1;
        }
        else{
            temp = id;
        }
    }
    
    printf("Max seat ID is: %d\n", max);
    printf("My seat ID is: %d\n", my_seat);
}


int part_one(char *s){
    int index_row_max = SEAT_ROW;
    int index_row_min = 0;
    int index_column_max = SEAT_COLUMN;
    int index_column_min = 0;
    int row = 0;
    int column = 0; 

    for(int i = 0; i < strlen(s); i++){
        if(s[i] == 'F'){
            index_row_max = average_of_two(index_row_max, index_row_min);
        }
        if(s[i] == 'B'){
            index_row_min = average_of_two(index_row_max, index_row_min);
        }
        if(s[i] == 'L'){
            index_column_max = average_of_two(index_column_max, index_column_min);
        }
        if(s[i] == 'R'){
            index_column_min = average_of_two(index_column_max, index_column_min);
        }
    }
    row = average_of_two(index_row_max, index_row_min) + 1;
    column = average_of_two(index_column_max, index_column_min);
    return (row * 8) + column;
}

int average_of_two(int a, int b){
    return (a + b)/2;
}