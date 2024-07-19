import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args)throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        Stack<Integer> s = new Stack<>();

        for(int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String str = st.nextToken();
            switch(str) {
                // str에 push가 있을 경우
                case "push":
                    int num = Integer.parseInt(st.nextToken());
                    s.push(num);
                    break;
                // pop
                case "pop":
                    // stack이 비어있다면 -1
                    if(s.isEmpty()) sb.append(-1).append("\n");
                        // 아니면 그냥 pop
                    else sb.append(s.pop()).append("\n");
                    break;
                //size
                case "size":
                    sb.append(s.size()).append("\n");
                    break;
                //empty
                case "empty":
                    if(s.isEmpty()) sb.append(1).append("\n");
                    else sb.append(0).append("\n");
                    break;
                //top
                case "top":
                    if(s.isEmpty()) sb.append(-1).append("\n");
                    else  sb.append(s.peek()).append("\n");
                    break;
                default:
                    break;
            }
        }
        br.close();
        System.out.println(sb);
    }
}