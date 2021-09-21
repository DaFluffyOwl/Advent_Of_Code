#include <stdio.h> 
#include <stdlib.h>



char str[323][35];


int get_tree_count(int right, int down, int len){
    int x = 0;
    int y = 0;
    unsigned long tree_count = 0;

    while(x < len + 1){
        if(str[x][y%31] == '#'){
            tree_count++;
        }
        y += right;
        x += down;
    }
    return tree_count;
}



int main(){
    FILE *fptr;
    fptr = fopen("input.txt", "r");

    char c;
    int i = 0;
    int j = 0;
    int file_len = 0;
    unsigned long trees = 0;

    while((c = fgetc(fptr)) != EOF){
        if(c == '\n'){
            i++;
            j = 0;
            file_len++;
        }
        else{
            str[i][j++] = c;
        }
    }

    trees += get_tree_count(3, 1, file_len);
    printf("There are %lu trees\n", trees);

    /*Right 1, down 1.
    Right 3, down 1.
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.*/

    unsigned long trees2 = 1;

    trees2 *= get_tree_count(1, 1, file_len);
    trees2 *= get_tree_count(3, 1, file_len);
    trees2 *= get_tree_count(5, 1, file_len);
    trees2 *= get_tree_count(7, 1, file_len);
    trees2 *= get_tree_count(1, 2, file_len);
    printf("There are %lu trees (multiplied)\n", trees2);



    fclose(fptr);
}