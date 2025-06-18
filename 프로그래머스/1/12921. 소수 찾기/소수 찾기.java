class Solution {
    public int solution(int n) {
        int answer = 0;
        for (int i = 1; i <= n; i++) {
            if (check(i)) answer++;
        }
        return answer;
    }
    
    public boolean check(int n) {
        if(n == 1) return false;
        if(n == 2) return true;
        int t = (int) Math.sqrt(n);
        for (int i = 2; i <= t; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}