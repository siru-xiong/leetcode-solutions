# Problem Id:  71
# Problem Name:  Simplify Path, 简化路径
# Problem Url:  https://leetcode-cn.com/problems/simplify-path/
# Problem Level:  Medium
 
class Solution:
    def simplifyPath(self, path: str) -> str:
        while len(path) != len(path.replace('//','/')):
            path = path.replace('//','/')
        if path == '/':
            return '/'
        if path[-1] == '/':
            path = path[:(-1)]
        path = path.split('/')[1:]
        path = ['/'+i for i in path]
        res = []
        for i in path:
            if i == '/.':
                pass
            elif i == '/..':
                if len(res) > 0:
                    del res[-1]
            else:
                res.append(i)
        if len(res) == 0:
            return '/'
        else:
            return ''.join(res)
        