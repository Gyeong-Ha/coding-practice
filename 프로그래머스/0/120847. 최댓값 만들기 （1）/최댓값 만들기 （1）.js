function solution(numbers) {
    let answer = 0;
    let numbers_sorted = numbers.sort((a, b) => b - a);
    let first = numbers_sorted[0];
    let second = numbers_sorted[1];
    answer = first * second;
    return answer;
}