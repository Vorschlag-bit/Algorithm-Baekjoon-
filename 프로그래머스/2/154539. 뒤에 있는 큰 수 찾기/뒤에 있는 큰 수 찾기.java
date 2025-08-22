import java.util.*;
class Pair {
    int idx;
    int value;
    public Pair(int idx, int value) {
        this.idx = idx;
        this.value = value;
    }
}
class Solution {
    public int[] solution(int[] numbers) {
        int l = numbers.length;
        int[] answer = new int[l];
        // -1로 다 초기화
        for (int i = 0; i < l; i++) answer[i] = -1;
        Deque<Pair> stack = new ArrayDeque<>();
        for (int i = 0; i < l; i++) {
            int v = numbers[i];
            while(!stack.isEmpty() && stack.peekLast().value < v) {
                Pair p = stack.pollLast();
                int idx = p.idx;
                answer[idx] = v;
            }
            stack.add(new Pair(i,v));
        }
        return answer;
    }
}