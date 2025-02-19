-- divided and returns the first number by the second number and returns
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT BEGIN
DECLARE result FLOAT;
IF b = 0 THEN RETURN 0;
ELSE
SET RETURN a / b;
END IF;
END;
