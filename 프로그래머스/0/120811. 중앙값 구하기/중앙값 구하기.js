function solution(array) {
    let answer = 0;
    array.sort(function (a, b) {
        return a - b;
    });
    let x = Math.trunc(array.length/2);
    answer = array[x]
    return answer;
}