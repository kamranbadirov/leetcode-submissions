class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        par = [i for i in range(n)]

        def find(n):
            if par[n] != n:
                par[n] = find(par[n])
            return par[n]



        def union(n1,n2):
            p1,p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            par[p1] = p2
            return True


        for a,b in edges:
            if not union(a,b):
                return False
        return True
        
        