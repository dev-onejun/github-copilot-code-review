#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    //malloc a large buffer and copy in 100 characters from stdin
    char* buf = malloc(1024);
    //-copilot next line-
    //copy 100 characters from stdin into buf
    fgets(buf, 100, stdin);
    //print the buffer
    printf("%s", buf);
    return 0;
}
