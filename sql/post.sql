CREATE TABLE IF NOT EXISTS post (
    content TEXT NOT NULL,
    title TEXT NOT NULL,
    insertedAt INT NOT NULL,
    modifiedAt INT NOT NULL,
    userPk TEXT NOT NULL,
    pk TEXT NOT NULL PRIMARY KEY,
    FOREIGN KEY(userPk) REFERENCES user(pk)
);
