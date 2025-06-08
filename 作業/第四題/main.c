#include <stdio.h>

// 宣告外部組合語言函數
extern int mul3(int a, int b, int c);

int main() {
    int result = mul3(3, 2, 5);
    printf("mul3(3,2,5) = %d\n", result);
    return 0;
}
