#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    long long int sum = 0;
    long long int arr[n];
    for (int i = 0; i < n; i++) {
        scanf("%lld", &arr[i]);
    }
    for (int i = 0; i < n; i++) {
        sum+=arr[h];
    }

    printf("%lld\n", sum);

    return 0;
}
