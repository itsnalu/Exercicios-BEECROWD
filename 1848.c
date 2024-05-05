#include <stdio.h>
#include <math.h>

void main ()
{

    char v[10];
    int numero, olhos;

    olhos = 3;
    while (olhos--)
    {

        numero = 0;
        while (scanf(" %[^\n]", v), v[0] != 'c')
            for (int i = 3; i >= 0; --i)
                if (v[i] == '*')
                    numero += pow(2, (2-i));

        printf("%d\n", numero);

    }

}