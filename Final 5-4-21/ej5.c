#include <stdio.h>
#include <assert.h>

#include <string.h>

void join(char destino[], char delimitador, char *cadenas[], int n) {
    // HACER: implementar la funcion
}

int main(void) {
    char *cadenas[] = { "2021", "04", "05" };
    char s[16];
    join(s, '-', cadenas, 3);
    assert(!strcmp(s, "2021-04-05"));

    // OPCIONAL: pruebas adicionales

    printf("%s: OK\n", __FILE__);
    return 0;
}
