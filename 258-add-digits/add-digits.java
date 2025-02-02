class Solution {
    public int addDigits(int num) {
       while (num >=10){
            num = sumd(num);
        }
        return num; 
    }
    static int sumd(int n){
        int sum = 0;
        
        while (n !=0) {
            int digit = n % 10;
            sum = sum + digit;
            n = n/10;   
        }
        return sum;
    }
}