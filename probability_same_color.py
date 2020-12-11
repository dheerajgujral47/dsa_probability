# -*- coding: utf-8 -*-

from collections import deque

# Calculate probability of drawing 2 balls of same color from bag
def draw_same_prob(n, total):
    net_favourable_cases = n * (n-1)/2  # nC2
    total_cases = total * (total-1)/2   # totalC2
    return net_favourable_cases/total_cases

# Calculate probability of drawing 2 balls of different color
def draw_diff_prob(m, n, total):
    net_favourable_cases = m * n  # mC1*nC1
    total_cases = total * (total-1)/2
    return net_favourable_cases/total_cases

# will return the required probability at 3rd draw
def calcProbability(a, b, c):

    draw_queue = deque()  # will contain all outcomes for every possible action
    prob = 1
    draw_queue.append([a, b, c, prob])   # the initial state of bag
    
    draw_count = 0
    
    # Run twice for 1st 2 draws to get the possible states for 3rd draw
    while(draw_count < 2):
        
        elem_count = len(draw_queue)
        
        # pop out the current states present in queue and append all next possible outcomes for each
        for elem in range(elem_count):
            
            curr_elem = draw_queue.popleft()
            a, b, c, prob = curr_elem[0], curr_elem[1], curr_elem[2], curr_elem[3]
            if(a >= 2):
                draw_queue.append([a-2, b  , c  , prob * draw_same_prob(a, a + b + c)])
            if(b >= 2):
                draw_queue.append([a  , b-2, c  , prob * draw_same_prob(b, a + b + c)])
            if(c >= 2):
                draw_queue.append([a  , b  , c-2, prob * draw_same_prob(c, a + b + c)])
            if(a >= 1 and b >= 1):
                draw_queue.append([a-1, b-1, c  , prob * draw_diff_prob(a, b, a + b + c)])
            if(b >= 1 and c >= 1):
                draw_queue.append([a  , b-1, c-1, prob * draw_diff_prob(b, c, a + b + c)])
            if(a >= 1 and c >= 1):
                draw_queue.append([a-1, b  , c-1, prob * draw_diff_prob(a, c, a + b + c)])
            
        draw_count += 1
    
    # take only same color outcomes for 3rd draw and add all probabilities
    elem_count = len(draw_queue)
    draw_same_color_prob = 0
    for elem in range(elem_count):
        
        curr_elem = draw_queue.popleft()
        a, b, c, prob = curr_elem[0], curr_elem[1], curr_elem[2], curr_elem[3]
        if(a >= 2):
            draw_same_color_prob += prob * draw_same_prob(a, a + b + c)
        if(b >= 2):
            draw_same_color_prob += prob * draw_same_prob(b, a + b + c)
        if(c >= 2):
            draw_same_color_prob += prob * draw_same_prob(c, a + b + c)
    
    return draw_same_color_prob

print(calcProbability(1, 1, 1))
print(calcProbability(2, 2, 2))
print(calcProbability(10, 0, 0))
print(calcProbability(15, 15, 15))
print(calcProbability(50, 100, 1000))
    
    
    
    
    