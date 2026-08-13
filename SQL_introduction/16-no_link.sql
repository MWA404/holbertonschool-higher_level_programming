-- lists score and name from second_table, excluding NULL names, ordered by score descending
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
