def solution(answers):
    
    case1 = [1,2,3,4,5]
    case2 = [2,1,2,3,2,4,2,5]
    case3 = [3,3,1,1,2,2,4,4,5,5]
          
    score = [0, 0, 0]
    for i, answer in enumerate(answers):
        if case1[i % 5] == answer:
            score[0] += 1
        if case2[i % 8] == answer:
            score[1] += 1
        if case3[i % 10] == answer:
            score[2] += 1
            
    max_score = max(score)
    
    # print(max_score)
    
    # for i, score in enumerate(score):
    #     if score == max_score:
    #         print(i+1)
            
    return [i+1 for i,score in enumerate(score) if score == max_score]
        
