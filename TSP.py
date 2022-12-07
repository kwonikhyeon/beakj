# field : 0 <= x <= 200 / 0 <= y <= 200
# start point : (0,0)
# count of city : 20

from queue import Empty
import sys
import random
import math
import numpy as np
import copy
import turtle as t
import time

# 깊이 제한
sys.setrecursionlimit(10**6)

# 도시 위치 선정 (0,0에서 다른 도시 좌표로의 이동 상황_default : 지정된 위치 반환 / 'random' : 랜덤 위치 반환)
def setCityPosition(cityCount, mode):
    cityPosition = [(0,0)]
    # 지정된 도시 출력
    if mode == 3:
        cityPosition = [(0,0), (1, 0), (5, 0), (3, 2)]
    elif mode == 5:
        cityPosition = [(0, 0), (111, 156), (6, 33), (24, 95), (32, 122), (8, 86)]
    elif mode == 7:
        cityPosition = [(0, 0), (46, 74), (80, 151), (159, 131), (111, 33), (173, 196), (38, 117), (18, 49)]
    elif mode == 20:
        cityPosition = [(0,0), (116, 180), (191, 57), (91, 67), (143, 87), (76, 129), 
                        (15, 119), (27, 172), (198, 44), (119, 64), (161, 80), 
                        (41, 47), (60, 105), (195, 14), (1, 21), (42, 91), 
                        (26, 87), (185, 139), (67, 92), (6, 186), (183, 149)]
    # 랜덤 도시 출력
    elif mode == 'random':
        for i in range(cityCount):
            position = (random.randint(0,200), random.randint(0,200))
            while position in cityPosition:
                position = (random.randint(0,200), random.randint(0,200))
            cityPosition.append(position)
    else:
        print('Error : wrong parameter entered')

    return cityPosition

# 기준 도시로부터 다른 도시로의 거리 반환(return : n*n metrix / n : 1+도시개수)
def calculateCost(cityPosition):
    # 0 : start point
    # list index : 0 ~ 도시개수
    cityCost = []
    for i, (x1, y1) in enumerate(cityPosition):
        buffer = []
        for j, (x2, y2) in enumerate(cityPosition):
            if i == j:
                cost = 0
            else:
                cost = round(math.sqrt((x1-x2)**2 + (y1-y2)**2), 4)
            buffer.append(cost)
        cityCost.append(buffer)
    return cityCost

# 비용(거리) 합 계산
def sumCost(cityCost, visited):
    totalCost = 0
    for i in range(len(visited)-1):
        totalCost += cityCost[visited[i]][visited[i+1]]
    totalCost += cityCost[visited[i+1]][0]
    return totalCost

# DFS 재귀함수
def dfs(notVisited, visited, cityCost, minDist):
    global minRoot
    if len(notVisited) == 0 and len(visited) == cityCount+1:
        calcDist = sumCost(cityCost, visited)
        if minDist > calcDist:
            minDist = calcDist
            minRoot = visited
        return minDist, minRoot

    for i in notVisited:
        nextNotVisited = copy.deepcopy(notVisited)
        nextNotVisited.remove(i)
        nextVisited = copy.deepcopy(visited)
        nextVisited.append(i)
        minDist, minRoot = dfs(nextNotVisited, nextVisited, cityCost, minDist)

    return minDist, minRoot

# DFS 실행함수
def findPathAsDFS(cityCost):
    notVisited = [i for i in range(1, cityCount+1)]
    visited = [0]
    maxDistance = math.sqrt(200**2) * cityCount
    minDist, minRoot = dfs(notVisited, visited, cityCost, maxDistance)
    print('[ DFS OPTIMIZED ROOT ] :', minRoot+[0])
    print('[ DFS OPTIMIZED COST ] :', minDist)
    return minRoot

# ------------------------------------------------------------------------------------------
# 유전자 생성 함수(0세대 유전자 및 자식 유전자)
def generateGene(parant1 = [], parant2 = [], generation = 0):
    cutRange = cityCount//3
    # 0세대 생성
    if generation == 0:
        gene = [i for i in range(1, cityCount+1)]
        random.shuffle(gene)
        return gene
    # 교차 연산을 통한 후세대 생성(Order CrossOver)
    p1_head = parant1[:cutRange]
    p1_body = parant1[cutRange:-cutRange]
    p1_tail = parant1[-cutRange:]
    p2_head = parant2[:cutRange]
    p2_body = parant2[cutRange:-cutRange]
    p2_tail = parant2[-cutRange:]
    # 자식 1 생성
    a1 = p2_tail + p2_head + p2_body
    for element in p1_body:
        a1.remove(element)
    c1 = a1[:cutRange] + p1_body + a1[-cutRange:]
    # 자식 2 생성(자식 1의 body부분 Inverse)
    p1_body_reverse = list(reversed(p1_body))
    c2 = a1[:cutRange] + p1_body_reverse + a1[-cutRange:]
    # 자식 3 생성
    a2 = p1_tail + p1_head + p1_body
    for element in p2_body:
        a2.remove(element)
    c3 = a2[:cutRange] + p2_body + a2[-cutRange:]
    # 자식 4 생성(자식 2의 body부분 Inverse)
    p2_body_reverse = list(reversed(p2_body))
    c4 = a2[:cutRange] + p2_body_reverse + a2[-cutRange:]
    
    newGene = [c1, c2, c3, c4]
    # 돌연변이 유전자(확률 : 0.005)
    for i in range(len(newGene)):
        if random.randint(1,1000) <= 5:
            random.shuffle(newGene[i])
    return newGene

# 평가함수
def calcFitness(gene, cityCost):
    gene = [0]+gene
    totalCost = sumCost(cityCost, gene)
    maxDistance = math.sqrt(200**2) * cityCount
    fitValue = 1/(totalCost**2) * maxDistance
    return fitValue

def findPathAsGenetic(cityCost):
    epoch = 300000   # 최대 반복 횟수
    # 5개의 0세대 유전자 생성
    gene0 = []
    for i in range(5):
        sample = generateGene()
        while sample in gene0:
            sample = generateGene()    
        gene0.append(sample)
    
    tempGene = gene0
    generation = 1
    # 세대 수 만큼 반복
    while generation < epoch:
        # fit value 계산 및 normalize
        fitValue = []
        for gene in tempGene:
            fitValue.append(calcFitness(gene, cityCost))
        fitValue = np.array(fitValue)*(1/sum(fitValue))
        
        # RouletteWheel 생성
        fitRouletteWheel = [0]*len(fitValue)
        for i in range(len(fitValue)):
            count = i
            fitRouletteWheel[i] = fitValue[i]
            while count != 0:
                count -= 1
                fitRouletteWheel[i] += fitValue[count]
        fitRouletteWheel = np.array(fitRouletteWheel)    
        
        # 확률 기반 우성 유전자 2개를 부모 유전자로 지정
        p1 = min(np.where(fitRouletteWheel>random.random())[0])
        p2 = min(np.where(fitRouletteWheel>random.random())[0])
        while p2 == p1:
            p2 = min(np.where(fitRouletteWheel>random.random())[0])
        
        nextGene = generateGene(tempGene[p1], tempGene[p2], generation)
        c5 = tempGene[np.argmax(fitValue)] # 이전 세대의 우성 유전자 다음 세대로 전달
        nextGene.append(c5)

        generation += 1
        tempGene = nextGene
    
    fitValue = []
    for gene in tempGene:
        fitValue.append(calcFitness(gene, cityCost))
    fitValue = np.array(fitValue)*(1/sum(fitValue))
    minRoot = [0] + tempGene[np.argmax(fitValue)]
    minCost = sumCost(cityCost, minRoot)
    print('[ GENETIC OPTIMIZED ROOT ] :', minRoot+[0])
    print('[ GENETIC OPTIMIZED COST ] :', minCost)
    return minRoot

if __name__ == '__main__':
    cityCount = 7 # 도시 개수 선정
    p = setCityPosition(cityCount, 'random')
    pp = calculateCost(p)
    print('-----------------------------------------------------------------')
    startTime = time.time()
    dfs_root = findPathAsDFS(pp)
    endTime = time.time()
    dfsDuration = endTime - startTime
    print('-----------------------------------------------------------------')
    startTime = time.time()
    genetic_root = findPathAsGenetic(pp)
    endTime = time.time()
    geneticDuration = endTime - startTime
    print('-----------------------------------------------------------------')
    print('[ Duration ]\n', 'DFS : ', dfsDuration, '\n', 'GENETIC :', geneticDuration)
    print('-----------------------------------------------------------------')

    # 그래픽으로 확인
    t.width(5)
    t.pencolor('blue')
    for i in range(cityCount+1):
        t.goto(p[dfs_root[i]])
        t.dot(20)
    t.goto((0,0))

    t.width(1)
    t.pencolor('red')
    for i in range(cityCount+1):
        t.goto(p[genetic_root[i]])
        t.dot(10)
    t.goto((0,0))

    t.exitonclick()