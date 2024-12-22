function solution(num_list) {
    let answer = [];
    let even_list = [];
    let odd_list = [];
    for (let num of num_list) {
        if (num % 2 == 0) {
            even_list.push(num);
        } else {
            odd_list.push(num);
        };
    };
    answer.push(even_list.length);
    answer.push(odd_list.length);
    return answer;
}