package dao

import (
	"database/sql"
	"douban/model"
)

func InsertPost(post model.Post) error {
	sqlstr :="insert into post(username,txt,title,post_time,comment_num)values(?,?,?,?,?)"
	_,err:=Db.Exec(sqlstr,post.Username,post.Txt,post.Title,post.PostTime,post.CommentNum)
	if err!=nil{
		return err
	}
	return nil
}

func SelectById(id int) (bool,error){
	var txt string
	sqlstr :="select txt from post where id=?"
	err :=Db.QueryRow(sqlstr,id).Scan(&txt)
	if err!=nil&&err!=sql.ErrNoRows{
		return false,err
	}
	return true,nil
}

func UpdatePost(id int,txt,title string) error {
	sqlstr :="update post set title=?,txt=? where id=?"
	_,err :=Db.Exec(sqlstr,title,txt,id)
	if err!=nil{
		return err
	}
	return nil
}

func GetAllPost()([]model.OtPost,int,error){
	sqlstr:="select id,comment_num,username,txt,title,post_time,update_time from post"
	rows,err:=Db.Query(sqlstr)
	//post类型切片 存多个post
	var posts []model.OtPost
	var num=0
	if err != nil {
		return posts,num,err
	}
	//延迟关闭连接
	defer rows.Close()
	// 循环读取结果集中的数据
	for rows.Next() {
		post:=model.OtPost{}
		err := rows.Scan(&post.Id,&post.CommentNum,&post.Username,&post.Txt,&post.Title,&post.PostTime,&post.UpdateTime)
		if err != nil {
			return posts,num,err
		}
		posts = append(posts, post)
		num++
	}
	return posts,num,nil
}

func OnePostGet(id int)(model.OtPost,error){
	sqlstr:="select id,comment_num,username,txt,post_time,update_time from post where id=?"
	post :=model.OtPost{}
	err:=Db.QueryRow(sqlstr,id).Scan(&post.Id,&post.CommentNum,&post.Username,&post.Txt,&post.PostTime,&post.UpdateTime)
	if err!=nil{
		return post,err
	}
	return post,nil
}

func GetCommentNumById(id int) (error,int){
	var num int
	sqlstr:="select comment_num from post where id=?"
	err :=Db.QueryRow(sqlstr,id).Scan(&num)
	if err!=nil&&err!=sql.ErrNoRows{
		return err,0
	}
	return nil,num
}

func UpdateCommentNum(num int)(error){
	sqlstr:="update post set comment_num=?"
	_,err :=Db.Exec(sqlstr,num)
	if err!=nil{
		return err
	}
	return  nil
}