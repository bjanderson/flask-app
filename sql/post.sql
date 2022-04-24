CREATE TABLE IF NOT EXISTS post (
    content TEXT NOT NULL,
    title TEXT NOT NULL,
    insertedAt INT NOT NULL,
    modifiedAt INT NOT NULL,
    userPk TEXT NOT NULL,
    pk TEXT NOT NULL PRIMARY KEY,
    FOREIGN KEY(userPk) REFERENCES user(pk)
);

INSERT INTO post (content, title, insertedAt, modifiedAt, userPk, pk)
VALUES ('test content', 'Test Post 1', 1650479287739, 1650479287739, 'userpk1', 'postpk1');


INSERT INTO post (content, title, insertedAt, modifiedAt, userPk, pk)
VALUES ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 'Test Post 2', 1650479287739, 1650479287739, 'userpk1', 'postpk2');
