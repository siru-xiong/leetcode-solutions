-- Problem Id:  534
-- Problem Name:  Game Play Analysis III, 游戏玩法分析 III
-- Problem Url:  https://leetcode-cn.com/problems/game-play-analysis-iii/
-- Problem Level:  Medium
-- Language:  MySQL
 
# Write your MySQL query statement below
select 
    player_id, 
    event_date, 
    sum(games_played)over(partition by player_id order by event_date) games_played_so_far 
from Activity