import java.util.*;
import java.io.*;

class Main {
    static class Pair {
        int rank, startidx;
        Pair(int rank, int startidx) {
            this.rank = rank;
            this.startidx = startidx;
        }
        public int getRank() {
            return rank;
        }
        public int getStartidx() {
            return startidx;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());
        for(int i = 0; i < num; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            //Object 담을 수 있는 queue 생성
            Queue<Pair> queue = new LinkedList<>();
            int n = Integer.parseInt(st.nextToken());
            //목표 인덱스
            int m = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            //몇 번째에 나가는지 셀 변수
            int cnt = 0;
            //큐에 넣는 반복문
            for(int j = 0; j < n; j++) {
                //pair 생성 후 queue에 넣기
                int rank = Integer.parseInt(st.nextToken());
                Pair pair = new Pair(rank, j);
                queue.offer(pair);
            }
            //큐에서 peek부터 뽑아가며 중요도를 비교
            while (!queue.isEmpty()) {
                Pair cur = queue.poll();
                boolean Check = true;
                for(Pair p : queue) {
                    if(p.getRank() > cur.getRank()) {
                        Check = false;
                        break;
                    }
            }
                if(Check) {
                    cnt++;
                    if(cur.getStartidx() == m) {
                        System.out.println(cnt);
                        break;
                    }
                }
                else queue.offer(cur);
            }
        }
    }
}