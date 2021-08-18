-- creates a function SafeDiv that divides (and returns) the first by the
-- second number or returns 0 if the second number is equal to 0.


DELIMITER //
DROP FUNCTION IF EXISTS `SafeDiv`;
CREATE FUNCTION SafeDiv(
	a INTEGER,
        b INTEGER
) 
RETURNS FLOAT
DETERMINISTIC
BEGIN
    DECLARE res FLOAT;
    IF b = 0 THEN
        SET res = 0;
    ELSE
        SET res = (a * 1.0) / b;
    END IF;
	RETURN (res);
END //
DELIMITER ;