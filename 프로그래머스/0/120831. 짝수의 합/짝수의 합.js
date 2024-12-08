function solution(n) {
    let answer = 0;
    let i = 0;
    do {
        i += 1;
        if (i % 2 === 0) {
            answer += i;
        }
    } while (i < n)
    return answer;
}