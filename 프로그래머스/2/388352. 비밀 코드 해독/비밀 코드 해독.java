import java.util.*;
class Solution {
    public int solution(int n, int[][] q, int[] ans) {
        int answer = 0;
        // q 대신 사용할 set List
        List<Set<Integer>> ques = new ArrayList<>();
        for (int[] qu : q) {
            Set<Integer> set = new HashSet<>();
            for(int num : qu) {
                set.add(num);
            }
            ques.add(set);
        }
        int[] arr = new int[n];
        for (int i = 1; i <= n; i++) {
            arr[i-1] = i;
        }
        List<List<Integer>> combination = comb(arr, 5);
        for (List<Integer> com : combination) {
            // 해당 조합이 모든 ques와 ans를 만족하는지 판단할 flag
            boolean flag = true;
            for (int i = 0; i < ans.length; i++) {
                // 시스템 응답 일치 개수
                int target = ans[i];
                Set<Integer> targetSet = ques.get(i);
                int cnt = 0;
                for (int num : com) {
                    if (targetSet.contains(num)) cnt++;
                }
                if (cnt != target) {
                    flag = false;
                }
                if (!flag) break;
            }
            // flag면 ans++
            if (flag) answer++;
        }
        
        return answer;
    }
    
    public List<List<Integer>> comb(int[] arr, int r) {
        List<List<Integer>> result = new ArrayList<>();
        dfs(arr,0,r,new ArrayList<>(),result);
        return result;
    }
    
    public static void dfs(int[] arr, int start, int r, List<Integer> chosen,
                               List<List<Integer>> result) {
            if (chosen.size() == r) {
                result.add(new ArrayList<>(chosen));
                return;
            }
            
            for (int i = start; i < arr.length; i++) {
                chosen.add(arr[i]);
                dfs(arr,i+1,r,chosen,result);
                chosen.remove(chosen.size()-1);
            }
        }
}