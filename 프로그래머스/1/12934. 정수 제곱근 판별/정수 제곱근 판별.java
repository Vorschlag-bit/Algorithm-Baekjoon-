class Solution {
    public long solution(long n) {
        long answer = -1;
        long s = (long) Math.sqrt(n);
        if (s*s == n) answer = (s+1)*(s+1);
        return answer;
    }
}