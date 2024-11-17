import java.util.*;
class Solution {
    public long solution(int[] queue1, int[] queue2) {
        long sum1 = 0;
        long sum2 = 0;
        long avg = 0;
        long limit = 0;
        Queue<Integer> q1 = new LinkedList<>();
        Queue<Integer> q2 = new LinkedList<>();
        for(int i : queue1) {
            sum1 += i;
            q1.offer(i);
            limit++;
        }
        for(int i : queue2) {
            sum2 += i;
            q2.offer(i);
            limit++;
        }
        // 한 쪽 queue당 가져야할 목표값
        avg = (sum1 + sum2);
        // 모든 원소가 한 바퀴 돌 때까지의 최대 횟수
        limit *= 2;
        if(avg % 2 == 1) return -1;
        avg /= 2;
        long cnt = 0;
        while(limit > cnt) {
            // 밸런스 안 맞으면 불가능한 q
            if(q1.isEmpty() || q2.isEmpty()) {
                return -1;
            }
            if(avg == sum1) {
                return cnt;
            }
            
            if(sum1 > sum2) {
                int num = q1.poll();
                if(num > avg) return -1;
                sum1 -= num;
                sum2 += num;
                q2.offer(num);
                cnt++;
            }
            else if(sum1 < sum2) {
                int num = q2.poll();
                if(num > avg) return -1;
                sum1 += num;
                sum2 -= num;
                q1.offer(num);
                cnt++;
            }
        }
        return -1;
    }
}