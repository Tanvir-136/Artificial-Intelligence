from collections import deque

tree={
    'A':['B', 'E'],
    'B':['A','C','D'],
    'C':['B','F'],
    'D':['B'],
    'E':['A'],
    'F':['C']
}

def bidirectional(tree, start, goal):
    if start == goal:
        return None, None
    
    st_vis = []
    st_q = deque([start])
    goal_vis = []
    goal_q = deque([goal])
    
    while st_q and goal_q:
        st_node = st_q.popleft()
        if st_node not in st_vis:
            st_vis.append(st_node)
            for neighbor in tree[st_node]:
                if neighbor not in st_vis:
                    st_q.append(neighbor)
                    
        # from 
        goal_node = goal_q.popleft()
        if goal_node not in goal_vis:
            goal_vis.append(goal_node)
            for neighbor in tree[goal_node]:
                goal_q.append(neighbor)
                
        if st_node in goal_vis or goal_node in st_vis:
            return st_vis,goal_vis
        
print(bidirectional(tree,'A', 'D'))