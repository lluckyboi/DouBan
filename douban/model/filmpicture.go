package model

type FilmPicture struct {
	Id 			int`json:"id"`
	FilmId		int`json:"film_id"`
	Url 	 	string`json:"url"`
}

/*
CREATE TABLE filmpicture (
    id int NOT NULL auto_increment,
    film_id int NOT NULL,
    url     varchar(1000) NOT NULL ,
    CONSTRAINT id PRIMARY KEY (id)
);
*/