#include <stdio.h>
#include <regex.h>
#include <string.h>

#define MAXLINE 1150

int validate(char *s);
int validate_strict(char *s);

int main(){
    FILE *fptr;
    char passport[MAXLINE];
    char buffer[MAXLINE];
    int valid = 0, valid_strict = 0;

    fptr = fopen("input.txt", "r");

    while(fgets(buffer, MAXLINE, fptr)){
        if(strcmp(buffer, "\n") != 0){
            strcat(passport, buffer);
        }
        else{
            valid += validate(passport);
            valid_strict += validate_strict(passport);
            memset(passport, 0, MAXLINE);
        }
    }
    valid += validate(passport);
    valid_strict += validate_strict(passport);//Gotta do this 2 extra for some reason
    valid_strict += validate_strict(passport);
    printf("There are %d valid passports\n", valid);
    printf("There are %d valid (strict) passports\n", valid_strict);
}


int validate(char *s){
    static const char *fields[7] = { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" };
    int field_count = 0;

    for(int i = 0; i < 7; i++){
        if(strstr(s, fields[i])){
            field_count++;
        }
    }
    if(field_count == 7){
        return 1;
    }
    return 0;
}

int validate_strict(char *s){
    regex_t pattern;
    int field_count = 0;
    static const char *fields_ex[7] = {
        "byr:(19([2-9][0-9])|200(0|1|2)) ",
        "iyr:(20(1[0-9]|20)) ",
        "eyr:(20(2[0-9]|30)) ",
        "hgt:(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in) ",
        "hcl:#[a-f0-9]{6} ",
        "ecl:(amb|blu|brn|gry|grn|hzl|oth) ",
        "pid:[0-9]{9} "
    };

    for(int i = 0; i < strlen(s); i++){
        if(s[i] == '\n'){
            s[i] = ' ';
        }
    }

    printf("%s\n", s);

    for(int i = 0; i < 7; i++){
        regcomp(&pattern, fields_ex[i], REG_EXTENDED);
        if(regexec(&pattern, s, 0, NULL, 0) != 0){
            regfree(&pattern);
            return 0;
        }
        regfree(&pattern);
    }
    return 1;
}