function solution(my_string, n) {
    let answer = '';
    let length = my_string.length;
    let x = '';
    let i = 0;
    do {
        x = my_string.charAt(i);
        answer += x.repeat(n);
        i += 1;
    } while (i <= length)

    return answer;
}