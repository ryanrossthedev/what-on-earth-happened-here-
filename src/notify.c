#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    // Expecting: notify <title> <message>
    if (argc < 3) {
        printf("Usage: %s <title> <message>\n", argv[0]);
        return 1;
    }

    char command[512];
    // Safely construct the desktop notification command
    snprintf(command, sizeof(command), "notify-send \"%s\" \"%s\"", argv[1], argv[2]);

    int result = system(command);
    
    return result;
}