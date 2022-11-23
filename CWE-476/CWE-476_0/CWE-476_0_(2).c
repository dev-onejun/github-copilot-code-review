
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char name[100];
    int status;
} person;

int main(int argc, char *argv[]) {
    //allocate a new person and set status to 0
    //-copilot next line-
    person *p = malloc(sizeof(person));
    p->status = 0;
    return 0;
}
