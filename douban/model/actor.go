package model

type Actor struct {
	ActorId			int`json:"actor_id"`
	Name 			string`json:"name"`
	MainRole		string`json:"mainrole"`
	Sex				string`json:"sex"`
	Introduction	string`json:"introduction"`
	PictureUrl		string`json:"picture_url"`
}

type ActorRole struct {
	ActorId 	int`json:"actor_id"`
	Role 		string`json:"role"`
	PictureUrl	string`json:"picture_url"`
}

/*
CREATE TABLE `actor` (
    `actor_id` int NOT NULL AUTO_INCREMENT,
    `name` varchar(20) NOT NULL,
    `mainrole` varchar(100) NOT NULL,
    `sex` varchar(20) NOT NULL,
    `introduction` varchar(1000) NULL,
	`picture_url` varchar(1000) NULL,
    CONSTRAINT actor_id PRIMARY KEY (actor_id)
);
*/