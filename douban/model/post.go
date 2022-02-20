package model

import "time"
/*
	CREATE TABLE `post` (
		`id` BIGINT(20) NOT NULL AUTO_INCREMENT,
		`comment_num` BIGINT(20) DEFAULT '0',
		`username` VARCHAR(20) NOT NULL,
		`txt` longtext NOT NULL,
		`title` varchar(100) NOT NULL,
		`post_time` longtext ,
		`update_time` longtext,
         PRIMARY KEY(`id`)
	)ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;
 */
// Post 留言结构 用js tag处理过的容器
type Post struct {
	Id         int       `json:"id"`
	CommentNum int       `json:"comment_num"`
	Txt        string    `json:"txt"`
	Title	   string	  `json:"title"`
	Username   string    `json:"username"`
	PostTime   time.Time `json:"post_time"`
	UpdateTime time.Time `json:"update_time"`
}

// OtPost string类型方便点
type OtPost struct {
	Id         int       `json:"id"`
	CommentNum string       `json:"comment_num"`
	Txt        string    `json:"txt"`
	Title	   string	  `json:"title"`
	Username   string    `json:"username"`
	PostTime   string `json:"post_time"`
	UpdateTime string `json:"update_time"`
}
/*					数据库中post 用longtext防炸
+-------------+-------------+------+-----+---------+----------------+
| Field       | Type        | Null | Key | Default | Extra          |
+-------------+-------------+------+-----+---------+----------------+
| id          | bigint      | NO   | PRI | NULL    | auto_increment |
| comment_num | bigint      | YES  |     | 0       |                |
| username    | varchar(20) | YES  |     |         |                |
| txt         | longtext    | YES  |     | NULL    |                |
| post_time   | longtext    | YES  |     | NULL    |                |
| update_time | longtext    | YES  |     | NULL    |                |
+-------------+-------------+------+-----+---------+----------------+
 */