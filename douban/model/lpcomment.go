package model

type LPComment struct {
	Id          int`json:"id"`
	LPostId      int`json:"lpost_id"`
	Txt         string`json:"txt"`
	Username    string`json:"username"`
	CommentTime string`json:"comment_time"`
}

/*
CREATE TABLE lpcomment(
    lpcomment_id int NOT NULL AUTO_INCREMENT,
    post_id int NOT NULL,
    txt longtext NOT NULL,
    username varchar(20) NOT NULL,
    comment_time int NOT NULL,
    CONSTRAINT lpcomment_id PRIMARY KEY (lpcomment_id)
);
*/