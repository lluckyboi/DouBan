package service

import (
	"database/sql"
	"douban/dao"
	"douban/model"
)

func AddLongPost(longpost model.Longpost)error{
	return dao.InsertLongPost(longpost)
}

func UpdateLongPost(longpost model.Longpost)error{
	return dao.UpdateLongPost(longpost)
}

func DeleteLongPost(postId int)error{
	return dao.DeleteLongPostById(postId)
}

func GetLongPostByFilmId(filmid int)([]model.Longpost,int,error){
	longposts,num,err:=dao.SelectLongPostByFilmId(filmid)
	if err!=nil{
		if err==sql.ErrNoRows{
			return longposts,num,nil
		}
		return longposts,num,err
	}
	return longposts,num,nil
}

func LikeLongPost(postId int)error{
	return dao.UpdateLongPostLikeByPostId(postId)
}

func DislikeLongPost(postId int)error{
	return dao.UpdateLongPostDislikeByPostId(postId)
}

func GetLongPostByUsername(username string)([]model.Longpost,int,error){
	longposts,num,err:=dao.SelectLongPostByUsername(username)
	if err!=nil{
		if err==sql.ErrNoRows{
			return longposts,num,nil
		}
		return longposts,num,err
	}
	return longposts,num,nil
}