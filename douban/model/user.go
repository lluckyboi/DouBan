package model

type User struct {
	Id       int
	Username 		string
	Password 		string
	Ques1 	 		string//密保1
	Ans1 	 		string//答案1
	Ques2	 		string//密保2
	Ans2	 		string//答案2
	Introduction	string
	PictureUrl		string
}

type UserInfo struct {
	Username	string`json:"username"`
	Password 	string`json:"password"`
}


type OtUserInfo struct {
	Username		string`json:"username"`
	PictureUrl		string`json:"picture_url"`
	Introduction 	string`json:"introduction"`
}
/*
CREATE TABLE `user` (
		`id` BIGINT(20) NOT NULL AUTO_INCREMENT,
		`username` VARCHAR(20) NOT NULL,
		`password` VARCHAR(20) NOT NULL,
		`ans1` VARCHAR(50) NOT NULL,
		`ans2` VARCHAR(50) NOT NULL,
		`ques1` VARCHAR(50) NOT NULL,
		`ques2` VARCHAR(50) NOT NULL,
		`introduction` VARCHAR(1000) default "还没有简介哦",
		`picture_url`  VARCHAR(1000) DEFAULT "https://img2.baidu.com/it/u=3644629312,823020752&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500",
         PRIMARY KEY(`id`)
	)ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;
*/
