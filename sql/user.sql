-- SELECT name FROM sqlite_master
-- WHERE type='table' AND name='user';

CREATE TABLE IF NOT EXISTS user (
    email TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    pk TEXT NOT NULL PRIMARY KEY
);

INSERT INTO user (email, name, pk)
VALUES ('user_1@email.tld', 'username 1', 'userpk1');

INSERT INTO user (email, name, pk)
VALUES ('user_2@email.tld', 'username 2', 'userpk2');

INSERT INTO user (email, name, pk)
VALUES ('user_3@email.tld', 'username 3', 'userpk3');

-- UPDATE user
-- SET email='user_one@email.tld', name='username One'
-- WHERE pk == 'userpk1';

-- SELECT * FROM user;

-- SELECT email, name, pk
-- FROM user
-- WHERE pk == 'userpk1'
-- ORDER BY name DESC;

-- DELETE FROM user
-- WHERE pk == 'userpk1';

-- DROP TABLE IF EXISTS user;
