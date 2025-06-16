class Solution {
    public int solution(int n) {
        int cnt = dec2n(n);
        int ans = 0;
        for (int i = n+1; i < 1000000000; i++) {
            if (cnt == dec2n(i)) {
                ans = i;
                break;
            }
        }
        return ans;
    }
    public int dec2n(int n) {
        int cnt = 0;
        while (n > 0) {
            int r = n % 2;
            if (r == 1) cnt++;
            n /= 2;
        }
        return cnt;
    }
}