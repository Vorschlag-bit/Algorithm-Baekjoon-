import java.util.*;
import java.io.*;

class Board{
    int x;
    int y;

    public Board(int x, int y){
        this.x = x;
        this.y = y;
    }
}

class Main{
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        ArrayList<Board> list = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            list.add(new Board(x, y));
        }

        Collections.sort(list, new Comparator<Board>() {
            @Override
            public int compare(Board b1, Board b2) {
                if(b1.y == b2.y)
                    return b1.x - b2.x;
                return b1.y - b2.y;
            }
        });
        StringBuilder sb = new StringBuilder();
        for(Board board : list) {
            sb.append(board.x + " ").append(board.y).append('\n');
        }
        System.out.println(sb);
    }
}