package service

import (
	"database/sql"
	"douban/dao"
	"douban/model"
)

func AddActor(actor model.Actor)error{
	err:=dao.InsertActor(actor)
	if err!=nil{
		return err
	}
	return nil
}

func DeleteActor(actorId int)error{
	err:=dao.DeleteActorById(actorId)
	if err!=nil{
		return err
	}
	return nil
}

func SearchActor(actorId int)(model.Actor,bool,error){
	actor,err:=dao.SelectActorById(actorId)
	if err != nil {
		if err == sql.ErrNoRows {
			return actor,false,nil
		}
		return actor,false,err
	}
	return actor,true,nil
}

func GetActorsByFilmId(FilmId int)([]model.ActorRole,int,error){
	actors,num,err:=dao.SelectActorsByFilmId(FilmId)
	if err == nil ||err==sql.ErrNoRows{
		return actors,num,nil
	}
	return actors,num,err
}

func GetFilmIdsByActorId(actorId int)([]int,int,error){
	filmids,num,err:=dao.SelectFilmIdByActorId(actorId)
	if err==nil||err==sql.ErrNoRows{
		return filmids,num,nil
	}
	return filmids,num,err
}
