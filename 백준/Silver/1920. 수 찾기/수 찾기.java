import java.util.*;
import java.io.*;

class Main {
    static long[] arr;
    //시간복잡도를 줄이기 위한 StringBuffer 선언
    static StringBuffer sb = new StringBuffer();
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        arr = new long[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        //주어진 숫자의 범위는 int를 넘어설 수 있다
        for (int i = 0; i < n; i++) {
            arr[i] = Long.parseLong(st.nextToken());
        }
        //오름차순으로 정렬
        Arrays.sort(arr);
        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        //시간 복잡도를 n^2에서 nlogn으로 바꾸기
        for(int i = 0; i < m; i++) {
            long num = Integer.parseInt(st.nextToken());
            binary_search(0, n - 1, num);
        }
        System.out.println(sb);
    }
    //입력받은 수가 배열A에 있는지 판단하는 이진탐색
    public static void binary_search(int start, int end, long num) {
        if(start > end) {
            sb.append("0\n");
            return;
        }
        int mid = (start + end) / 2;
        if(num == arr[mid]) {
            sb.append("1\n");
            return;
        }
        //mid가 num보다 크면 mid - 1이 end가 된다
        if(arr[mid] > num) binary_search(start, mid - 1, num);
            //mid가 num보다 작으면 mid + 1가 start가 된다
        else binary_search(mid + 1, end, num);
    }
}