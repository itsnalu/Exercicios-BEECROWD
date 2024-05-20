#include <iostream>

using namespace std;

int main(){
    long long int numero;

    cin >> numero;
    cout << numero << endl;

    while(numero >= 10){
        int unidade;
        unidade = numero % 10;
        numero = numero / 10;
        numero = numero * 3 + unidade;
        cout << numero << endl;
    }


    return 0;
}