package model

import "time"

/*
	CREATE TABLE `comment` (
		`id` BIGINT(20) NOT NULL AUTO_INCREMENT,
		`post_id` BIGINT(20) DEFAULT '0',
		`username` VARCHAR(20) DEFAULT '',
		`txt` longtext ,
		`comment_time` longtext ,
		`iscomcom`	   VARCHAR(20) DEFAULT '',
		`comcomid` 	   VARCHAR(255),
         PRIMARY KEY(`id`)
	)ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;
*/

type Comment struct {
	Id          int
	PostId      int
	Txt         string
	Username    string
	CommentTime time.Time
	IsComCom    int//是否是评论的评论
	ComComId	int//套娃的目标
}

// OtComment 用于输出的 不知道为什么转string报错
type OtComment struct {
	Id          int
	PostId      int
	Txt         string
	Username    string
	CommentTime time.Time
	IsComCom    int//是否是评论的评论
	ComComId	int//套娃的目标
}
/*
+--------------+--------------+------+-----+---------+----------------+
| Field        | Type         | Null | Key | Default | Extra          |
+--------------+--------------+------+-----+---------+----------------+
| id           | bigint       | NO   | PRI | NULL    | auto_increment |
| post_id      | bigint       | YES  |     | 0       |                |
| username     | varchar(20)  | YES  |     |         |                |
| txt          | longtext     | YES  |     | NULL    |                |
| comment_time | longtext     | YES  |     | NULL    |                |
| iscomcom     | varchar(20)  | YES  |     |         |                |
| comcomid     | varchar(255) | YES  |     | NULL    |                |
+--------------+--------------+------+-----+---------+----------------+
 */
