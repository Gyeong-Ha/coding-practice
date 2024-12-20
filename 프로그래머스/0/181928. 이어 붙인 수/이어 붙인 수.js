function solution(num_list) {
    let answer = 0;
    let odd_list = [];
    let even_list = [];
    for (let num of num_list) {
        if (num % 2 === 1) {
            odd_list.push(num)
        } else {
            even_list.push(num)
        }
    } 
    answer = Number(odd_list.join(''))+Number(even_list.join(''));
    return answer;
}