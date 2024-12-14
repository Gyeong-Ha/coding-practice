function solution(my_string, letter) {
    let answer = "";
    let i = 0;
    do {
        my_string = my_string.replaceAll(letter[i], "")
        i += 1;
    } while (i <= letter.length)
    answer = my_string
    return answer;
}