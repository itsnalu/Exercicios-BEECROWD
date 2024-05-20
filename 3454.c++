#include <iostream>
#include <string>

using namespace std;

int main() {
    string jogada;
    cin >> jogada;

    if (jogada == "XOX") {
        cout << "*" << endl;
    } else if (jogada == "XXO" || jogada == "OXX") {
        cout << "Alice" << endl;
    } else {
        cout << "?" << endl;
    }

    return 0;
}
