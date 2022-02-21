package dao

import (
	"database/sql"
	"douban/model"
)

func InsertShortPost(shortpost model.ShortPost)error{
	sqltsr:="insert into shortpost(film_id,txt,username,post_time,score,want,watched,likes,tags)values(?,?,?,?,?,?,?,?,?)"
	_,err:=Db.Exec(sqltsr,&shortpost.FilmId,&shortpost.Txt,&shortpost.Username,&shortpost.PostTime,&shortpost.Score,&shortpost.Want,&shortpost.Watched,&shortpost.Likes,&shortpost.Tags)
	if err!=nil{
		return err
	}
	return nil
}

func DeleteShortPostById(postId int)error{
	sqlstr:="delete from shortpost where post_id=?"
	_,err:=Db.Exec(sqlstr,postId)
	if err!=nil{
		return err
	}
	return nil
}

func UpdateShortPost(shortpost model.ShortPost)error{
	sqlstr:="update shortpost set txt=?,update_time=?,score=?,want=?,watched=?,tags=? where post_id=?"
	_,err:=Db.Exec(sqlstr,shortpost.Txt,shortpost.UpdateTime,shortpost.Score,shortpost.Want,shortpost.Watched,shortpost.Tags,shortpost.Id)
	if err!=nil{
		return err
	}
	return nil
}

func SelectShortPsotByFilmId(filmId int)([]model.OtShortPost,int,error){
	var p =make([]model.OtShortPost,10000)
	var i=1

	rows,errr:=Db.Query("select *from shortpost where film_id=?",filmId)
	if errr!=nil{
		return p,0,errr
	}
	defer rows.Close()
	for rows.Next() {
		errrr := rows.Scan(&p[i].Id,&p[i].FilmId,&p[i].Txt,&p[i].Username,&p[i].PostTime,&p[i].UpdateTime,&p[i].Score,&p[i].Want,&p[i].Watched,&p[i].Likes,&p[i].Tags)
		if errrr != nil {
			return p,0,errrr
		}
		i++
	}
	return p,i-1,nil
}

func SelectShortPostByUsername(username string)([]model.OtShortPost,int,error){
	var p =make([]model.OtShortPost,10000)
	var i=1

	rows,errr:=Db.Query("select *from shortpost where username=?",username)
	if errr!=nil{
		return p,0,errr
	}
	defer rows.Close()
	for rows.Next() {
		errrr := rows.Scan(&p[i].Id,&p[i].FilmId,&p[i].Txt,&p[i].Username,&p[i].PostTime,&p[i].UpdateTime,&p[i].Score,&p[i].Want,&p[i].Watched,&p[i].Likes,&p[i].Tags)
		if errrr != nil {
			return p,0,errrr
		}
		i++
	}
	return p,i-1,nil
}

// SelectShortPostLikesByPostId 获取点赞数
func SelectShortPostLikesByPostId(postId int)(int,error){
	var likesnum int
	err:=Db.QueryRow("select likes from shortpost where post_id=?",postId).Scan(&likesnum)
	if err!=nil{
		return 0,err
	}
	return likesnum,nil
}

func UpdateShortPostLikeById(post_id int)error{
	likenum,err:=SelectShortPostLikesByPostId(post_id)
	if err==nil||err==sql.ErrNoRows{
		_,errr:=Db.Exec("update shortpost set likes=?",likenum+1)
		if errr!=nil{
			return err
		}
		return nil
	}
	return err
}
