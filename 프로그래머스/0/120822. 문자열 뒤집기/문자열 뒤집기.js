function solution(my_string) {
    let answer = '';
    let splitString = my_string.split("");
    let reverseString = splitString.reverse();
    let joinArray = reverseString.join("");
    answer = joinArray
    return answer;
}