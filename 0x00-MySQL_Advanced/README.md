# 0x00. MySQL advanced

## Tasks
### 0. We are all unique!
- Write a SQL script that creates a table users following these requirements:
	* With these attributes:
		- id, integer, never null, auto increment and primary key
		- email, string (255 characters), never null and unique
		- name, string (255 characters)
	* If the table already exists, your script should not fail
	* Your script can be executed on any database

### 1. In and not out

### 2. Best band ever!
- Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

### 3. Old school band
- Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

### 4. Buy buy buy
- Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

### 5. Email validation to sent
- Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

### 6. Add bonus
- Write a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

### 7. Average score
- Write a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal

### 8. Optimize simple search
- Write a SQL script that creates an index idx_name_first on the table names and the first letter of name.

### 9. Optimize search and score
- Write a SQL script that creates an index idx_name_first_score on the table names and the first letter of name and the score.

### 10. Safe divide
- Write a SQL script that creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

### 11. No table for a meeting
- Write a SQL script that creates a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month.

### 12. Average weighted score
- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.

### 13. Average weighted score for all!
- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
