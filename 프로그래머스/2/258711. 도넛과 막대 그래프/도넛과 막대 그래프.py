def solution(edges):
    answer = [0,0,0,0]
    node_dict=dict()
    for src,dst in edges:
        if not node_dict.get(src):
            node_dict[src]=[0,0]
        if not node_dict.get(dst):
            node_dict[dst]=[0,0]
        
        node_dict[src][0]+=1
        node_dict[dst][1]+=1
    for node,cnt in node_dict.items():
        out_count=cnt[0]
        in_count=cnt[1]
        if in_count==0 and out_count>=2:
            answer[0]=node # gen_node
        elif out_count==0 and in_count>0:
            answer[2]+=1  # stick graph
        elif out_count>=2 and in_count>=2:
            answer[3]+=1  # 8 graph
        
    answer[1]= node_dict[answer[0]][0]-answer[2]-answer[3] # else doughnut graph
    
    return answer
