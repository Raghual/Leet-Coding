Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


int reverse(int x){
    long long int rev_num=0;
        while(x!=0){
            rev_num=rev_num*10+(x%10);
            x/=10;
            }
    if(rev_num<-2147483648 || rev_num>2147483647)return 0;
    return rev_num;
}
