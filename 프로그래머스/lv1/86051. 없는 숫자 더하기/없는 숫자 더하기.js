function solution(numbers) {
    let answer = 0
    let arr1 = []
    
    for(let i = 1; i<10;i++){
        let flag = false
        for(let j of numbers){
            if(i==j){
                flag = true
                break
            }
        }
        if(flag == false){
            arr1.push(i)
        }
    }
    
    for(let i of arr1){
        answer += i
    }
    return answer;
}