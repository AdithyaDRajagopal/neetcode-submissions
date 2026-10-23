class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_waiting = 0
        total_time = 0
        for arrival, time in customers:
            if arrival > total_time:
                total_time = arrival + time
            else:
                total_time += time
            
            waiting = total_time - arrival
            total_waiting += waiting
        
        return total_waiting/len(customers)
