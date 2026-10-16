class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        route = { start for start, end in paths }
        
        for start, end in paths:
            if end not in route:
                return end
