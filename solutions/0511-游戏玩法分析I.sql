# Problem Id:  511
# Problem Name:  Game Play Analysis I, 游戏玩法分析 I
# Problem Url:  https://leetcode-cn.com/problems/game-play-analysis-i/
# Problem Level:  Easy
 
# Write your MySQL query statement below
select player_id, min(event_date) as first_login from Activity
group by player_id