import java.util.*;

class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        String name = sc.next();
        int n = sc.nextInt();

        int l = 0;
        int o = 0;
        int v = 0;
        int e = 0;
        
        for(int i = 0; i < name.length(); i++){
            if(name.charAt(i)=='L')
                l++;
            if(name.charAt(i)=='O')
                o++;
            if(name.charAt(i)=='V')
                v++;
            if(name.charAt(i)=='E')
                e++;
        }
        //for문 돌 때마다 초기화해야 할 개수 넣을 변수 생성
        
        String[] arr = new String[n+1];
        
        for(int i = 1; i <= n; i++){
            arr[i] = sc.next();
        }
        
        int pro = -1;
        String team = "";
        
        //이름 전부를 도는 반복문
        for(int i = 1; i <= n; i++){
            int ln = l;
            int on = o;
            int vn = v;
            int en = e;
            //한 이름에서 love검사하는 반복문
            int len = arr[i].length();
            for(int j = 0; j < len; j++){
                if(arr[i].charAt(j)=='L')
                    ln++;
                if(arr[i].charAt(j)=='O')
                    on++;
                if(arr[i].charAt(j)=='V')
                    vn++;
                if(arr[i].charAt(j)=='E')
                    en++;
            }
            int newpro = ((ln+on)*(ln+vn)*(ln+en)*(on+vn)*(on+en)*(vn+en))%100;
                if(newpro > pro){
                    pro = newpro;
                    team = arr[i];
                }
                else if(newpro == pro){
                    if(team.compareTo(arr[i]) > 0)
                    team = arr[i];
                }
        }
        System.out.print(team);
    }
}