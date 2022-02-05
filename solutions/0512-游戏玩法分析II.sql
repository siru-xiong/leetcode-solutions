# Problem Id:  512
# Problem Name:  Game Play Analysis II, 游戏玩法分析 II
# Problem Url:  https://leetcode-cn.com/problems/game-play-analysis-ii/
# Problem Level:  Easy
 
# Write your MySQL query statement below
select player_id, device_id
from activity
where (player_id, event_date) in 
(select player_id, min(event_date)
from activity
group by player_id)