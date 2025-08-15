class Solution {
public:
    int reverse(int x) {
        long long temp = 0;
        while(x!=0){
            long long rev = x % 10;
            temp = temp*10 +rev;
            x/=10;
            if(temp > 2147483647 || temp < -2147483647){
            return 0;
        }
        }
        return temp;

    }
};