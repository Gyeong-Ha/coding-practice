function solution(numbers) {
    let total = 0
    for (let n of numbers) {
        total += n
    }
    return total / numbers.length;
}