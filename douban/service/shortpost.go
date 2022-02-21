package service

import (
	"database/sql"
	"douban/dao"
	"douban/model"
)

func AddShortPost(shortpost model.ShortPost)error{
	return dao.InsertShortPost(shortpost)
}

func DeleteShortPostByPostId(postId int)error{
	return dao.DeleteShortPostById(postId)
}

func UpdateShortPost(shortpost model.ShortPost)error{
	return dao.UpdateShortPost(shortpost)
}

func GetShortPostByFilmId(filmId int)([]model.OtShortPost,int,error){
	shortposts,num,err:=dao.SelectShortPsotByFilmId(filmId)
	if err!=nil {
		if err==sql.ErrNoRows{
			return shortposts,num,nil
		}
		return shortposts,num,err
	}
	return shortposts,num,nil
}

func GetShortPostByUsername(username string)([]model.OtShortPost,int,error){
	shortposts,num,err:=dao.SelectShortPostByUsername(username)
	if err!=nil {
		if err==sql.ErrNoRows{
			return shortposts,num,nil
		}
		return shortposts,num,err
	}
	return shortposts,num,nil
}

func LikeShortPostById(postId int)error{
	return dao.UpdateShortPostLikeById(postId)
}

