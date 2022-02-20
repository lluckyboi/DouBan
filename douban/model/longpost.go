package model

type Longpost struct {
	PostId 			int`json:"post_id"`
	FilmId			int`json:"film_id"`
	Txt				string`json:"txt"`
	Username		string`json:"username"`
	PostTime		string`json:"post_time"`
	UpdateTime		string`json:"update_time"`
	Score			float32`json:"score"`
	Likes			int`json:"likes"`
	Dislikes		int`json:"dislikes"`
	CommentNum		int`json:"comment_num"`
	Title			string`json:"title"`
}

/*
CREATE TABLE longpost (
    post_id int NOT NULL AUTO_INCREMENT,
    film_id int NOT NULL,
    txt longtext NOT NULL,
    username varchar(20) NOT NULL,
    post_time longtext NOT NULL,
    update_time longtext NOT NULL,
    score float(2,1) NOT NULL,
    title varchar(100) NOT NULL,
    likes int NOT NULL,
    dislikes int NOT NULL,
    comment_num int NOT NULL,
    CONSTRAINT post_id PRIMARY KEY (post_id)
);
*/