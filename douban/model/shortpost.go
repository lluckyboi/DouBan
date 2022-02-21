package model

type ShortPost struct {
	Id 				int
	FilmId			int
	Txt				string
	Username		string
	PostTime		string
	UpdateTime		string
	Score			float32
	Want			int
	Watched			int
	Likes			int
	Tags 			string
}

//便于输出
type OtShortPost struct {
	Id 				int`json:"id"`
	FilmId			int`json:"film_id"`
	Txt				string`json:"txt"`
	Username		string`json:"username"`
	PostTime		string`json:"post_time"`
	UpdateTime		string`json:"update_time"`
	Score			float32`json:"score"`
	Want			int`json:"want"`
	Watched			int`json:"watched"`
	Likes			int`json:"likes"`
	Tags			string`json:"tags"`
}
/*
CREATE TABLE shortpost (
    post_id int NOT NULL AUTO_INCREMENT,
    film_id int NOT NULL,
    txt longtext NOT NULL,
    username varchar(20) NOT NULL,
    post_time text NOT NULL,
    update_time text NOT NULL,
    score float(2,1) NOT NULL,
    want bool NOT NULL,
    watched bool NOT NULL,
    likes int NOT NULL,
	tags  varchar(100) NOT NULL,
    CONSTRAINT post_id PRIMARY KEY (post_id)
);
*/

