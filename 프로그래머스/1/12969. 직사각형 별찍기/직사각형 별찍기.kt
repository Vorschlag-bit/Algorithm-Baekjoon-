fun main(args: Array<String>) {
    val (m, n) = readLine()!!.split(' ').map(String::toInt)
    val list = mutableListOf<String>()
    for (i in 0 until n) {
        list.add("*".repeat(m))
    }
    print(list.joinToString("\n"))
}