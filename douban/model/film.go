package model

type Film struct {
	Id				int			`json:"id"`
	Name			string		`json:"name"`
	Directer		string		`json:"directer"`
	Screenwriter	string		`json:"screenwriter"`
	Type 			string		`json:"type"`
	Location		string		`json:"location"`
	Language		string		`json:"language"`
	Introduction	string		`json:"introduction"`
	ReleaseTime		string		`json:"release_time"`
	Length			string		`json:"length"`
	OtherName		string		`json:"other_name"`
	IMDb			string		`json:"imdb"`
	Score			float32		`json:"score"`
	PostNum			int			`json:"post_num"`
	PosterUrl		string		`json:"poster_url"`
	Tag				string		`json:"tag"`//查询输出用
}


/*
CREATE TABLE film (
    film_id int NOT NULL AUTO_INCREMENT,
    name varchar(20) NOT NULL,
    directer varchar(20) NOT NULL,
    screenwriter varchar(20) NOT NULL,
    type varchar(20) NOT NULL,
    location varchar(20) NOT NULL,
    language varchar(20) NOT NULL,
    introduction varchar(20) NOT NULL,
    release_time varchar(100) NOT NULL,
    length varchar(100) NOT NULL,
    othername varchar(100) NOT NULL,
    IMDb varchar(20) NOT NULL,
    score float(2,1) NOT NULL,
    post_num int NOT NULL,
	poster_url text NOT NULL,
	mainrole text NOT NULL,
    CONSTRAINT film_id PRIMARY KEY (film_id)
);
*/