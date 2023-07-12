function solution(n)
{
    let arr1 = String(n)
    let result = arr1.split("")
    let sum = 0
    
    for(let i of result){
        sum += Number(i)
    }

    return sum;
}