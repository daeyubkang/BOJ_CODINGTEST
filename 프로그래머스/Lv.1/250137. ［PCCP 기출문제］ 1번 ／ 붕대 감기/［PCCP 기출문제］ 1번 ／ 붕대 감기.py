def solution(bandage, health, attacks):
    answer = 0
    maxHealth = health
    
    for i in range(len(attacks)):
        health -= attacks[i][1]
        if health <= 0:
            return -1
        if(len(attacks)-1 != i):
            num1 = attacks[i+1][0] - attacks[i][0] - 1
            health += (num1 * bandage[1]) + (num1//bandage[0]*bandage[2])
            if (health > maxHealth):
                health = maxHealth
    
    return health