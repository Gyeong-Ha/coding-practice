function solution(a, b) {
    let answer = 0;
    let x = Number(a.toString() + b.toString());
    let y = Number(b.toString() + a.toString());
    if (x > y) {
        answer = x
    } else {
        answer = y
    }
    return answer;
}