#include <stdio.h>

// Define the function f: {0, 1} -> {0, 1}
int f(int x) {
    // Example function: f(0) = 0, f(1) = 1 (balanced)
    return x;
}

int deutschAlgorithm() {
    // Evaluate f(0) and f(1)
    int f0 = f(0);
    int f1 = f(1);

    // Check if f is constant or balanced
    if (f0 == f1) {
        return 0; // Constant function
    } else {
        return 1; // Balanced function
    }
}

int main(int argc, char **argv) 
{
    int result = deutschAlgorithm();

    if (result == 0) {
        printf("The function is constant.\n");
    } else {
        printf("The function is balanced.\n");
    }

    return 0;
}
