#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char name[100];
    int status;
} person;

int main(int argc, char *argv[]) {
    //allocate a new person
    person *p = (person *)malloc(sizeof(person));
    //set status to 0
    //-copilot next line-
    p->status = 0;
    //set name to "John"
    //-copilot next line-
    strcpy(p->name, "John");
    //print the name and status
    //-copilot next line-
    printf("Name: %s, Status: %d \r ", p->name, p->status);
    //free the memory
    //-copilot next line-
    free(p);
    return 0;
}
