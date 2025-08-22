import java.util.*;
class Solution {
    int[] arr;
    public int[] solution(int[][] users, int[] emoticons) {
        // 1.가입자 최대, 2. 판매액 최대
        // 할인율은 10,20,30,40
        // 자신의 기준에 따라 일정 비율 이상 할인은 모두 구매
        // 구매 비용 합이 자기 기준 이상이면 구매 취소 후, 임티플 가입
        // 이모티콘별 할인율을 적용해야 하는데.. 중복순열인데
        int[] ans = new int[2];
        // 이모티콘 수
        int r = emoticons.length;
        // arr 초기화 후에 중복 순열 짜기
        arr = new int[4];
        int ansPerson = 0;
        int ansPrice = 0;
        for (int i = 1; i <= 4; i++) arr[i-1] = i*10;
        List<List<Integer>> perm = perm(arr,r);
        for (List<Integer> p : perm) {
            // 해당 p로 계산할 person과 price
            int person = 0;
            int price = 0;
            // p의 요소는 idx의 이모티콘 할인율
            // 사람마다 이모티콘 할인율 계산하기
            for (int[] user : users) {
                int ratio = user[0];
                int max = user[1];
                // 한 사람당 계산할 비용
                int eachPrice = 0;
                for (int idx = 0; idx < r; idx++) {
                    // 할인 비율
                    int saleratio = p.get(idx);
                    if (saleratio >= ratio) 
                        eachPrice += emoticons[idx]*(100-saleratio)/100;
                    // 만약 맥스 넘어서면 임티플 가입하고 break
                    if (eachPrice >= max) {
                        person++;
                        eachPrice = 0;
                        break;
                    }
                }
                // price에 eachprice 더하기
                price += eachPrice;
            }
            // 정답 계산하기
            if (person > ansPerson) {
                ansPerson = person;
                ansPrice = price;
            } else if (person == ansPerson && ansPrice < price) 
                ansPrice = price;
        }
        ans[0] = ansPerson;
        ans[1] = ansPrice;
        return ans;
    }
    
    public List<List<Integer>> perm(int[] arr, int r) {
        List<List<Integer>> result = new ArrayList<>();
        // idx, r, result, path
        dfs(0,r,result,new ArrayList<>());
        return result;
    }
    
    public void dfs(int depth, int r, List<List<Integer>> result, List<Integer> path) {
        if (path.size() == r) {
            // 깊은 복사로 전달
            result.add(new ArrayList<>(path));
            return;
        }
        
        for (int i = 0; i < arr.length; i++) {
            path.add(arr[i]);
            dfs(depth+1,r,result,path);
            path.remove(path.size()-1);
        }
    }
}