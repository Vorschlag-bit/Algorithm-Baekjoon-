import java.util.*;
class Solution {
    public int solution(String[] friends, String[] gifts) {
        int ans = 0;
        // 기록 없거나 주고 받은 게 같다면 선물지수가 더 큰 사람이 받기
        // 선물지수까지 같다면 선물 교환 x
        // 선물 준 사람, 선물 받은 사람 리스트 map
        Map<String, List<String>> giver = new HashMap<>();
        // 선물 준 사람, 선물 지수 map
        Map<String, Integer> giftCnt = new HashMap<>();
        // 초기화
        for (String person : friends) {
            giver.put(person, new ArrayList<>());
            giftCnt.put(person, 0);
        }
        // 선물등록
        for (String str : gifts) {
            String[] s = str.split(" ");
            String give = s[0];
            String given = s[1];
            giver.get(give).add(given);
            // 준 사람은 + 1
            giftCnt.put(give, giftCnt.get(give) + 1);
            // 받은 사람은 - 1
            giftCnt.put(given, giftCnt.get(given) - 1);
        }
        
        // 준 사람을 기준으로 모든 사람들과 비교하면서 받은 선물 계산
        for (String give : friends) {
            int cnt = 0;
            for (String given : friends) {
                // 자기 자신은 패스
                if (give.equals(given)) continue;
                // 주고 받은 선물 계산
                // give가 given에게 준 선물
                int g1 = 0;
                for (String person : giver.get(give)) {
                    if (person.equals(given)) g1++;
                }
                // given이 giver에게 준 선물
                int g2 = 0;
                for (String person : giver.get(given)) {
                    if (person.equals(give)) g2++;
                }
                if (g1 > g2) cnt++;
                else if (g1 == g2) {
                    // 선물 지수 비교
                    int p1 = giftCnt.get(give);
                    int p2 = giftCnt.get(given);
                    if (p1 > p2) cnt++;
                    
                } else continue; // 적다면 패스
            }
            ans = Math.max(ans, cnt);
        }
        
        return ans;
    }
}