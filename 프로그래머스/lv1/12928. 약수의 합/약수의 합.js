function solution(n) {
    let sum = 0
    let result = []
    for(let i = 1; i<n+1;i++){
        if(n%i==0 && (n/i)>=i){
            if(i==(n/i)){
                result.push(i)
                continue
            }
            result.push(i)
            result.push((n/i))
        }
    }
    
    for(let j of result){
        sum += j
    }
    
    var answer = sum;
    return answer;
}