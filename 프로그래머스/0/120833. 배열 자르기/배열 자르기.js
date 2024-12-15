function solution(numbers, num1, num2) {
    let answer = [];
    first = numbers.indexOf(num1)
    second = numbers.indexOf(num2)
    answer = numbers.slice(num1, num2+1)
    return answer;
}