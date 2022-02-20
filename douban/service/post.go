package service

import (
	"database/sql"
	"douban/dao"
	"douban/model"
)

func AddPost(post model.Post)(error){
	err :=dao.InsertPost(post)
	if err!=nil{
		return err
	}
	return nil
}

func Modifypost(id int,txt,title string)(error){
	//先check 有没有
	booll,err:=dao.SelectById(id)
	if booll==false{
		return err
	}

	err2 :=dao.UpdatePost(id,title,txt)
	if err2!=nil{
		return err
	}
	return nil
}

func AllPosts()([]model.OtPost,int,error){
	post,num,err:=dao.GetAllPost()
	if err==nil||err==sql.ErrNoRows{
		return post,num,nil
	}
	return post,num,err
}

func PostOneGet(id int)(model.OtPost,error){
	post,err :=dao.OnePostGet(id)
	if err!=nil{
		return post,err
	}
	return post,nil
}