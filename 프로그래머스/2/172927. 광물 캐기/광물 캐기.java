class Solution {
    int[] p5 = {1,5,25};
    int ans;
    int ml;
    int[] mines;
    public int solution(int[] picks, String[] mine) {
        ans = Integer.MAX_VALUE;
        ml = mine.length;
        mines = new int[ml];
        for (int i = 0; i < ml; i++) {
            if (mine[i].equals("diamond")) {
                mines[i] = 0;
            } else if (mine[i].equals("iron")) {
                mines[i] = 1;
            } else mines[i] = 2;
        }
        
        // hp, idx, picks
        dfs(0,0,picks);
        return ans;
    }
    
    public void dfs(int hp, int idx, int[] picks) {
        if (ans <= hp) return;
        if ((picks[0] == 0 && picks[1] == 0 && picks[2] == 0) || idx >= ml) {
            ans = Math.min(ans,hp);
            return;
        }
        
        for (int g = 0; g < 3; g++) {
            if (picks[g] == 0) continue;
            
            picks[g] -= 1;
            int use = 0;
            int end = Math.min(ml,idx+5);
            for (int i = idx; i < end; i++) {
                int v = g - mines[i];
                if (v < 0) v = 0;
                use += p5[v];
            }
            dfs(hp+use,idx+5,picks);
            picks[g] += 1;
        }
    }
}