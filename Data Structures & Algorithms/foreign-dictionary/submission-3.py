class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # make a graph
        graph = {}

        for w in words:
            for c in w:
                graph[c] = []

        # populare the graph 
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            minlen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""
            for j in range(minlen):
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    break
        visit = {}
        res = []
        # DFS
        def dfs(n):

            if n in visit:
                return visit[n]

            visit[n] = True
            for nei in graph[n]:
                if dfs(nei):
                    return True
            
            visit[n] = False
            res.append(n)
            return False

        # call DFS for each node in graph

        for node in graph:
            if dfs(node):
                return ""

        # return result 
        res.reverse()
        return "".join(res)
        