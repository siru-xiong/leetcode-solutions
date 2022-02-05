# Problem Id:  406
# Problem Name:  Queue Reconstruction by Height, 根据身高重建队列
# Problem Url:  https://leetcode-cn.com/problems/queue-reconstruction-by-height/
# Problem Level:  Medium
 
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(x[0],-x[1]),reverse=True)
        for i in range(1,len(people)):
            if people[i][1] != i:
                people[0:(i+1)] = people[0:people[i][1]]+[people[i]]+people[people[i][1]:i]
        return people