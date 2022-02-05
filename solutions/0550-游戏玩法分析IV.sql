# Problem Id:  550
# Problem Name:  Game Play Analysis IV, 游戏玩法分析 IV
# Problem Url:  https://leetcode-cn.com/problems/game-play-analysis-iv/
# Problem Level:  Medium
 
# Write your MySQL query statement below
SELECT
	ROUND(COUNT(DISTINCT player_id)/(SELECT COUNT(distinct player_id) FROM Activity), 
	2) AS fraction
FROM
    Activity
WHERE
	(player_id,event_date)
	IN
	(SELECT 
        player_id,
        Date(min(event_date)+1)
	FROM Activity
	GROUP BY player_id);