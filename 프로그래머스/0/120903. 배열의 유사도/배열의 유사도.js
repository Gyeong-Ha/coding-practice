function solution(s1, s2) {
    let answer = 0;
    let arr = [];
    arr = s1.filter(x => s2.includes(x));
    answer = arr.length
    return answer;
}