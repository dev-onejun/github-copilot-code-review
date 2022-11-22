#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    //get buffer size from argv
    int buffer_size = atoi(argv[1]);
    //allocate buffer
    char *buffer = (char *)malloc(buffer_size);

    //-copilot next line-
    //read from stdin
    fgets(buffer, buffer_size, stdin);
    
    //print buffer
    printf("%s", buffer);

    //free buffer
    free(buffer);
    return 0;
}