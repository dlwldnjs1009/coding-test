#include<stdio.h>

int main() {
    int a = 0;
    int cnt = 0;
    scanf("%d", &a);
    
    while (a > 0) {
        if (a % 5 == 0) {
            cnt += a / 5;
            a =0;
            break;
        }
        else {
            a -= 3;
            cnt++;
        }
    }
    
    if (a < 0) printf("%d\n", -1);
    else printf("%d\n", cnt);
    
    return 0;
}