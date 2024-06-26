class Solution {
    public int solution(int[][] triangle) {
        int l = triangle.length;
        int ans = 0;
        //DP에 알맞게 1. 큰 문제를 작은 문제로 나누기 2. memorization을 통한 값 갱신 및 기록
        //전체 층이 아니라 한 층만 내려가서 최댓값을 구해본다고 가정
        //1층, 2층을 제외하고 3층부터 최댓값을 구하려는 경우는
        //1. 왼쪽으로만 내려가기 2. 오른쪽으로만 내려가기
        //3. 2층에서 자기 idx, 자기 idx - 1 중 더 큰 값과 더하기
        for(int i = 1; i < l; i++)
            //층 별 크기를 다 돌며 층의 모든 원소에 대한 최댓값
            for(int j = 0; j < triangle[i].length; j++) {
                //1. 왼쪽으로만 더하기
                if(j == 0) triangle[i][j] += triangle[i - 1][j];
                //2. 오른쪽으로만 더하기
                else if(j == i) triangle[i][j] += triangle[i - 1][j - 1];
                //3. 그 외
                else {
                    triangle[i][j] += Math.max(triangle[i - 1][j], triangle[i - 1][j - 1]);
                }
                //한 층을 내려갈 때마다 그 층별 최댓값 갱신
                ans = Math.max(ans, triangle[i][j]);
            }
        return ans;
    }
}