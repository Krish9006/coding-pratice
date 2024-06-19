#include <stdio.h>


	// your code goes here
int main() {
    int T;
    scanf("%d", &T); // Input the number of test cases
    
    for (int t = 0; t < T; t++) {
        int N;
        scanf("%d", &N); // Input the number of judges
        
        int scores[N];
        int is_good = 1; // Assume the problem is good initially
        
        for (int i = 0; i < N; i++) {
            scanf("%d", &scores[i]); // Input the scores given by the judges
            if (scores[i] <= 4) {
                is_good = 0; // If any score is less than or equal to 4, mark the problem as not good
            }
        }
        
        // Check if the problem is good and print the result
        printf("%s\n", is_good ? "YES" : "NO");
    }
    return 01;

}

