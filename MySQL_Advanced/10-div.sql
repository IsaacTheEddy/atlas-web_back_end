-- divided and returns the first numbe
CREATE FUNCTION SafeDiv (a INT, b INT) RETURNS DECIMAL(10, 2) -- Choose appropriate precision and scale
DETERMINISTIC -- Important: Add DETERMINISTIC or READS SQL DATA
BEGIN IF b = 0 THEN RETURN 0;
ELSE RETURN a / b;
-- Or CAST(a AS DECIMAL(10,2)) / b for more control
END IF;
END
