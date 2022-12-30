from collections import deque

def get_average(temp_list:list,k:int = 100)->list:
        temp_q = deque(temp_q[:k]);

        sum_temp_q = sum(temp_q);
        average_temp = [sum_temp_q/k];

        for nt in temp_list[k:]: # nt is next temperature
            sum_temp_q = sum_temp_q + nt - sum_temp_q.popleft();
            temp_q.append(nt);
            average_temp.append(sum_temp_q/k);
        
        return average_temp;
