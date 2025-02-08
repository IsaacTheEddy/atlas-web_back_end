-- Creates table users
-- id - in not null and auto increments pk
--email - not null unique key
-- name
CREATE TABLE IF NOT EXISTS users (
    id int NOT NULL AUTO_INCREMENT,
    email varchar(255) NOT NULL,
    name varchar(255),
    PRIMARY KEY(id),
    UNIQUE(email)
)
