package dao

import (
	"database/sql"
	"douban/model"
	"time"
)

func InsertCommentCom(com model.Comment)(error){
	sqlstr :="insert into comment(comcomid,txt,username,iscomcom,comment_time)values(?,?,?,?,?)"
	_,err:=Db.Exec(sqlstr,com.ComComId,com.Txt,com.Username,com.IsComCom,com.CommentTime)
	if err!=nil{
		return err
	}
	return nil
}

func InsertComment(com model.Comment)(error){
	sqlstr :="insert into comment(post_id,txt,username,comment_time)values(?,?,?,?)"
	_,err:=Db.Exec(sqlstr,com.PostId,com.Txt,com.Username,com.CommentTime)
	if err!=nil{
		return err
	}
	err2:=PostCommentNumAdd(com.PostId)
	if err2!=nil{
		return err2
	}
	return nil
}

func PostCommentNumAdd(postid int)(error){
	err,num :=GetCommentNumById(postid)
	if err!=nil{
		return err
	}
	num=num+1;
	err2 :=UpdateCommentNum(num)
	if err2!=nil{
		return err2
	}
	return nil
}

func SelectComsByPostid(postid int)([]model.OtComment,int,error){
	sqlstr:="select id,txt,username from comment where post_id=?"
	rows,err :=Db.Query(sqlstr,postid)
	var coms []model.OtComment
	var num=0
	if err!=nil{
		return coms,num,err
	}

	defer rows.Close()
	// 循环读取结果集中的数据
	for rows.Next() {
		com:=model.OtComment{
			PostId: postid,
			CommentTime:time.Now(),
		}
		err := rows.Scan(&com.Id,&com.Txt,&com.Username)
		if err != nil {
			return coms,num,err
		}
		coms = append(coms, com)
		num++
	}
	return coms,num,nil
}

func DeleteCommentById(id int)(error){
	sqlstr:="delect from comment where id=?"
	_,err:=Db.Exec(sqlstr,id)
	if err!=nil{
		return err
	}
	return nil
}

func UpdateCommentById(id int,ntxt string)(error){
	sqlstr:="update comment set txt=? where id=?"
	_,err:=Db.Exec(sqlstr,ntxt,id)
	if err!=nil{
		return err
	}
	return nil
}

func SelectComComsByCId(id int)([]model.OtComment,int,error){
	sqlstr:="select id,txt,username,iscomcom from comment where comcomid=?"
	rows,err :=Db.Query(sqlstr,id)
	var coms []model.OtComment
	var num=0
	if err!=nil{
		return coms,num,err
	}

	defer rows.Close()
	// 循环读取结果集中的数据
	com:=model.OtComment{
		CommentTime:time.Now(),
	}
	for rows.Next() {

		errr := rows.Scan(&com.Id,&com.Txt,&com.Username,&com.IsComCom)
		if errr != nil {
			return coms,num,errr
		}
		coms = append(coms, com)
		num++
	}
	return coms,num,nil
}
func SelectCommentById(id int)(model.OtComment,error){
	sqlstr:="select txt,username,post_id from comment where id=?"
	var coms model.OtComment
	err:=Db.QueryRow(sqlstr,id).Scan(&coms.Txt,&coms.Username,&coms.PostId)
	if err!=nil&&err!=sql.ErrNoRows{
		return coms,err
	}
	return coms,nil

}