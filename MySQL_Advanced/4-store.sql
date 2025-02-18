-- Updates each row with a trigger
CREATE TRIGGER decrease
AFTER
INSERT ON orders FOR EACH ROW BEGIN
UPDATE items
SET quantity = quantity - NEW.item
WHERE name = NEW.item_name;
END;
