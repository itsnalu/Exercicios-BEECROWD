#include <stdio.h>
#include <stdlib.h>


int main(){

    int testes, tamanho, soma, i, numero;

    scanf("%d", &testes);

    while (testes > 0)
    {
        soma = 0;
        scanf("%d", &tamanho);

        for(i = 0; i < tamanho; i++){
            
            scanf("%d", &numero);

            if (numero <0){
                numero = abs(numero);
            }

            soma+= numero;
        }

        printf("%d\n", soma);
        testes--;
    }
    
    
    return 0;
}

