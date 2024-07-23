import java.io.*;
import java.util.*;

class FB {
    String value;
    int idx;

    public FB(String value, int idx) {
        this.value = value;
        this.idx = idx;
    }
}

class Main{
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        ArrayList<FB> list = new ArrayList<>();

        for (int i = 0; i < 3; i++) {
            list.add(new FB(br.readLine(), i));
        }
        int idx = 0;
        int value = 0;
        for(FB fb : list){
            if(fb.value.contains("F") || fb.value.contains("B")){
                continue;
            }
            else {
                value = Integer.valueOf(fb.value);
                idx = fb.idx;
                break;
            }
        }
        int ans = 0;
        String str = "";
        // 경우에 따른 switch문
        switch(idx) {
            case 0: {
                ans = value + 3;
                break;
            }
            case 1: {
                ans = value + 2;
                break;
            }
            case 2: {
                ans = value + 1;
                break;
            }
        }
        // 단어인지 아난지 판단
        if(ans % 3 == 0 && ans % 5 == 0) str = "FizzBuzz";
        else if(ans % 3 == 0 && ans % 5 != 0) str = "Fizz";
        else if(ans % 5 == 0 && ans % 3 != 0) str = "Buzz";
        else str = ans + "";

        System.out.println(str);
    }
}