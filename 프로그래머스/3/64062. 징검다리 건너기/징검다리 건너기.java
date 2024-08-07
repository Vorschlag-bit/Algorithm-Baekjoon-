class Solution {
    public int solution(int[] stones, int k) {
        int start = 1;
        int end = 200000000;
        while(start <= end) {
            int mid = (start + end) / 2;
            if(check(stones, k, mid)) {
                start = mid + 1;
            }
            else end = mid - 1;
        }
        return end;
    }
    boolean check(int[] stones, int k, int person) {
        int count = 0;
        for(int stone : stones) {
            if(stone - person < 0) count++;
            else count = 0;
            if(count >= k) return false;
        }
        return true;
    }
}