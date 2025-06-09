import java.util.*;
class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] ans = {6,6,5,4,3,2,1};
        int cnt_0 = (int) Arrays.stream(lottos).filter(x -> x == 0).count();
        int c = 0;
        for (int l : lottos) {
            for(int n : win_nums) {
                if (n == l) c++;
            }
        }
        return new int[] {ans[cnt_0+c],ans[c]};
    }
}