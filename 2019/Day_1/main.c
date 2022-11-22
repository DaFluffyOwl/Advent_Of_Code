#include <stdio.h>
#include <stdlib.h>
#include <math.h>

FILE *fptr;
int t_mass = 0;
int Question_2(int m);

int main(){
    fptr = fopen("input.txt", "r");
    char s[700];
    int mass = 0;
    int Q_1 = 0;
    int Q_2 = 0;

    while(fgets(s, 700, fptr)){
        mass = atoi(s);
        Q_1 += (mass/3)-2;
        Q_2 += Question_2(mass);
        t_mass = 0;
    }
    printf("%d\n", Q_2);
    fclose(fptr);
}


int Question_2(int m){
    int fuel = 0;

    fuel = floor(((m/3)-2));
    if(fuel > 0){
        t_mass = t_mass + fuel;
        Question_2(fuel);
    }
    else{
        return t_mass;
    }
}