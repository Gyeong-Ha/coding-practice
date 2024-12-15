function solution(n) {
    let answer = 0;
    n_str = n.toString();
    let i = 0;
    do {
        answer += Number(n_str[i])
        i += 1
    } while (i < n_str.length)
    return answer;
}