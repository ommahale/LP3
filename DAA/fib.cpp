#include <iostream>
using namespace std;

int fibonacci(int n){
    if (n <= 1)
        return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int n;

    cout << "Enter number of terms in the series: ";
    cin >> n;

    cout << "Fibonacci Series: ";
    for (int i = 0; i < n; i++) {
        cout << fibonacci(i) << " ";
    }

    return 0;
}


#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter the number of terms you want in the Fibonacci series: ";
    cin >> n;

    int first = 0, second = 1, next;

    cout << "Fibonacci Series without Recursion: ";

    for (int i = 0; i < n; i++) {
        if (i <= 1) {
            next = i;
        } else {
            next = first + second;
            first = second;
            second = next;
        }
        cout << next << " ";
    }

    return 0;
}
