function solution(array, n) {
    let answer = array.filter(element => n === element).length;
    return answer;
}