class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        next_task = []
        res = []
        
        
        sorted_tasks = [(enqueue, process, idx) for idx,(enqueue, process) in enumerate(tasks)]
        
        sorted_tasks.sort()
        
        curr_time = 0
        task_index = 0
        
        while task_index < len(tasks) or next_task:
            if not next_task and curr_time < sorted_tasks[task_index][0]:
                curr_time = sorted_tasks[task_index][0]
            while task_index < len(tasks) and curr_time >= sorted_tasks[task_index][0]:
                _, process_time, index = sorted_tasks[task_index]
                heapq.heappush(next_task, (process_time, index))
                task_index += 1
            process_time, index_res = heapq.heappop(next_task)
            
            curr_time += process_time
            
            res.append(index_res)
            
        return res