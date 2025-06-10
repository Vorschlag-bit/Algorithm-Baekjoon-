class Solution {
    lateinit var combinations: List<MutableList<String>>
    val ans = mutableSetOf<String>()
    fun solution(user_id: Array<String>, banned_id: Array<String>): Int {
        val n = banned_id.size
        combinations = List(n) { mutableListOf<String>() }
        for((idx,ban) in banned_id.withIndex()) {
            for(user in user_id) {
                if (check(user,ban)) combinations[idx].add(user)
            }
        }
        dfs(0,mutableListOf(),mutableSetOf())
        return ans.size
    }
    fun check(user: String, ban: String): Boolean {
        if (user.length != ban.length) return false
        return user.zip(ban).all { (uc,bc) -> bc == '*' || uc == bc }
    }
    fun dfs(idx: Int, path: MutableList<String>, visit: MutableSet<String>) {
        if (idx == combinations.size) {
            val key = path.sorted().joinToString()
            ans.add(key)
            return
        }
        
        for (candidate in combinations[idx]) {
            if (candidate in visit) continue
            path.add(candidate)
            visit.add(candidate)
            dfs(idx+1,path,visit)
            path.removeLast()
            visit.remove(candidate)
        }
    }
}