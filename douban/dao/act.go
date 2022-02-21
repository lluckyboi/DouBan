package dao

import "douban/model"

func InsertAct(act model.Act)error{
	sqlstr:="insert into act(actor_id,role,film_id)values(?,?,?)"
	_,err:=Db.Exec(sqlstr,act.ActorId,act.Role,act.FilmId)
	return err
}
