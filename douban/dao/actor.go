package dao

import "douban/model"

func InsertActor(actor model.Actor)error{
	sqlstr:="insert into actor (name,mainrole,sex,introduction,picture_url)values(?,?,?,?,?)"
	_,err:=Db.Exec(sqlstr,actor.Name,actor.MainRole,actor.Sex,actor.Introduction,actor.PictureUrl)
	if err!=nil{
		return err
	}
	return nil
}

func DeleteActorById(actorId int)error{
	sqlstr:="delete from actor where actor_id=?"
	_,err:=Db.Exec(sqlstr,actorId)
	if err!=nil{
		return err
	}
	return nil
}

func SelectActorById(actorId int)(model.Actor,error){
	var actor model.Actor
	err:=Db.QueryRow("select *from actor where actor_id=?",actorId).Scan(&actor.ActorId,&actor.Name,&actor.MainRole,&actor.Sex,&actor.Introduction,&actor.PictureUrl)
	if err!=nil{
		return actor,err
	}
	return actor,nil
}

func SelectActorsByFilmId(filmId int)([]model.ActorRole,int,error){
	var actors []model.ActorRole
	var num=0
	rows, err := Db.Query("SELECT actor_id,role FROM act WHERE film_id =?",filmId)
	if err != nil {
		return nil,num, err
	}
	defer rows.Close()
	for rows.Next() {
		var actorr model.ActorRole
		err = rows.Scan(&actorr.ActorId,&actorr.Role)
		if err != nil {
			return nil,num, err
		}
		//actor,errr:=SelectActorById(actorr.ActorId)
		//if errr!=nil{
		//	return nil,num,err
		//}
		//actorr.PictureUrl=actor.PictureUrl
		actors = append(actors, actorr)
		num++
	}
	return actors,num, nil
}

func SelectFilmIdByActorId(actorId int)([]int,int,error){
	var filmids []int
	var num=0
	rows, err := Db.Query("SELECT film_id FROM act WHERE actor_id = ?",actorId)
	if err != nil {
		return nil,num, err
	}
	defer rows.Close()
	for rows.Next() {
		var filmid int
		err = rows.Scan(&filmid)
		if err != nil {
			return nil,num, err
		}
		filmids = append(filmids, filmid)
		num++
	}
	return filmids,num, nil
}