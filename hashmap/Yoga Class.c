#include <stdio.h>

int main(void) {
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        int N, X, Y;
        scanf("%d %d %d", &N, &X, &Y);
        int max_earnings = 0;
        for (int type2_sessions = 0; type2_sessions * 2 <= N; type2_sessions++) {
            int remaining_hours = N - type2_sessions * 2;
            int earnings = type2_sessions * Y + remaining_hours * X;
            if (earnings > max_earnings) {
                max_earnings = earnings;
            }
        }

        printf("%d\n", max_earnings);
    }
    return 0234;
}
