class Solution {
    fun n2dec(str: String, base: Int): Int {
        var num = 0
        for (chr in str) {
            val digit = chr - '0'
            num = num * base + digit
        }
        return num
    }
    
    fun dec2n(n: Int, base: Int): String {
        if (n == 0) return "0"
        var num = n
        var digit = ""
        while (num > 0) {
            val r = num % base
            digit = r.toString() + digit
            num /= base
        }
        return digit
    }
    
    fun solution(exp: Array<String>): List<String> {
        var ans = mutableListOf<String>()
        var x = mutableListOf<String>()
        // set을 사용해서 가능한 진수를 모두 저장(2-9)
        // 2,3,4 5,6,7 8,9
        val s = mutableSetOf<Int>()
        var minN = 2
        for (ex in exp) {
            val sp = ex.split(" ")
            val n1 = sp[0]
            val op = sp[1]
            val n2 = sp[2]
            val r = sp[4]
 
            for (chr in n1) {
                val num = chr - '0'
                minN = maxOf(minN,num+1)
            }
            for (chr in n2) {
                val num = chr - '0'
                minN = maxOf(minN,num+1)
            }
            if (r != "X") {
                for (chr in r) {
                    val num = chr - '0'
                    minN = maxOf(minN,num+1)
                }
            } else {
                x.add(ex)
            }
        }
        var candid = (minN..9).toList()
        for (ex in exp) {
            val sp = ex.split(" ")
            val valid = mutableListOf<Int>()
            val n1 = sp[0]
            val op = sp[1]
            val n2 = sp[2]
            val r = sp[4]
            if (r == "X") continue
            for (base in candid) {
                val n1_d = n2dec(n1,base)
                val n2_d = n2dec(n2,base)
                val n3_d = n2dec(r,base)
                when (op) {
                    "+" -> {
                        if (n1_d + n2_d == n3_d) valid.add(base)
                    }
                    "-" -> {
                        if (n1_d - n2_d == n3_d) valid.add(base)
                    }
                }
            }
            candid = candid.filter { it in valid }
        }
        for (ex in x) {
            val sp = ex.split(" ")
            val valid = mutableListOf<Int>()
            val n1 = sp[0]
            val op = sp[1]
            val n2 = sp[2]
            val r = sp[4]
            val cnt = mutableSetOf<String>()
            for (base in candid) {
                val n1_d = n2dec(n1,base)
                val n2_d = n2dec(n2,base)
                if (op == "+") {
                    cnt.add(dec2n(n1_d+n2_d,base))
                } else {
                    cnt.add(dec2n(n1_d-n2_d,base))
                }
            }
            if (cnt.size == 1) {
                val num = cnt.first()
                ans.add("$n1 $op $n2 = $num")
            } else {
                ans.add("$n1 $op $n2 = ?")
            }
        }
        return ans.toList()
    }
}