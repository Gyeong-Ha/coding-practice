function solution(n, k) {
    let answer = 0
    let x = 0
    if (n < 10) {
        answer = 12000*n + 2000*k
    } else {
        x = Math.floor(n / 10)
        console.log(x)
        answer = 12000*n + 2000*k - 2000*x
    }
    return answer;
}