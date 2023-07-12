function solution(n) {
    let result = []
    for(let i =1;i<(n+1);i++){
        if(i%2==1){
            result.push("수")
        }
        else{
            result.push("박")
        }
    }
    
    var answer = result.join("");
    return answer;
}