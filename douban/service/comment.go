package service

import (
	"database/sql"
	"douban/dao"
	"douban/model"
)

func AddComCom(com model.Comment)(error){
	err :=dao.InsertCommentCom(com)
	if err!=nil{
		return err
	}
	return nil
}

func AddComment(com model.Comment)(error){
	err :=dao.InsertComment(com)
	if err!=nil{
		return err
	}
	return nil
}

func GetCommentOfPost(postid int)([]model.OtComment,int,error){
	com,num,err :=dao.SelectComsByPostid(postid)
	if err==nil||err==sql.ErrNoRows{
		return com,num,nil
	}
	return com,num,err
}

func GetComComment(cid int)([]model.OtComment,int,error){
	coms,num,err :=dao.SelectComComsByCId(cid)
	if err!=nil&&err!=sql.ErrNoRows{
		return coms,num,err
	}
	return coms,num,nil
}

func GetComment(id int)(model.OtComment,error){
	com,err :=dao.SelectCommentById(id)
	if err!=nil&&err!=sql.ErrNoRows{
		return com,err
	}
	return com,nil
}
func DelectComment(id int)(error){
	err :=dao.DeleteCommentById(id)
	if err!=nil{
		return err
	}
	return nil
}

func ModifyComment(id int ,ntxt string)(error){
	err :=dao.UpdateCommentById(id,ntxt)
	if err!=nil{
		return err
	}
	return nil
}