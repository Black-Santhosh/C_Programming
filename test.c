#include <stdio.h>
    

int main() {
    char b[20];
    // ✅ Correct way to initialize a char array
    char arr[] = {'s', 'w', 'w', 'g', 'h'};
    int n = sizeof(arr) / sizeof(arr[0]);

    // ✅ Use int for the loop counter
    for (int i = 0; i < n; i++) {
        if(arr[i]== arr[i-1])
        {
            int c = 0;
            for (int a = i; a < n; a++){
                b[c] = arr[i];
                c++;
            }
        }
    }
            int z = sizeof(arr);
            printf("%d\n", z);
    return 0;
}
