package model

type Act struct {
	Id  		int`json:"id"`
	ActorId		int`json:"actor_id"`
	FilmId		int`json:"film_id"`
	Role		string`json:"role"`
}

/*
CREATE TABLE act (
    act_id int NOT NULL AUTO_INCREMENT,
    actor_id int NOT NULL,
    role varchar(50) NOT NULL,
    film_id int NOT NULL,
    CONSTRAINT act_pk PRIMARY KEY (act_id)
);
*/