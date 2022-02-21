package dao

import (
	"database/sql"
	"douban/model"
)

func InsertLongPost(longpost model.Longpost)error{
	sqlstr:="insert into longpost(film_id,txt,username,post_time,score,title,likes,dislikes,comment_num)values(?,?,?,?,?,?,?,?,?)"
	_,err:=Db.Exec(sqlstr,longpost.FilmId,longpost.Txt,longpost.Username,longpost.PostTime,longpost.Score,longpost.Title,longpost.Likes,longpost.Dislikes,longpost.CommentNum)
	if err!=nil{
		return err
	}
	return nil
}

func UpdateLongPost(longpost model.Longpost)error{
	sqlstr:="update longpost set txt=?,update_time=?,score=?,title=? where post_id=?"
	_,err:=Db.Exec(sqlstr,longpost.Txt,longpost.UpdateTime,longpost.Score,longpost.Title,longpost.PostId)
	if err!=nil{
		return err
	}
	return nil
}

func DeleteLongPostById(post_id	int)error{
	sqlstr:="delete from longpost where post_id=?"
	_,err:=Db.Exec(sqlstr,post_id)
	if err!=nil{
		return err
	}
	return nil
}

func SelectLongPostByFilmId(filmId int)([]model.Longpost,int,error){
	var ps []model.Longpost
	var num=0

	rows,errr:=Db.Query("select *from longpost where film_id=?",filmId)
	if errr!=nil{
		return ps,0,errr
	}
	defer rows.Close()
	for rows.Next() {
		var p model.Longpost
		errrr := rows.Scan(&p.PostId,&p.FilmId,&p.Txt,&p.Username,&p.PostTime,&p.UpdateTime,&p.Score,&p.Title,&p.Likes,&p.Dislikes,&p.CommentNum)
		if errrr != nil {
			return ps,0,errrr
		}
		ps=append(ps,p)
		num++
	}
	return ps,num,nil
}

func SelectLongPostLikesByPostId(postId int)(int ,error){
	var likesnum int
	err:=Db.QueryRow("select likes from longpost where post_id=?",postId).Scan(&likesnum)
	if err!=nil{
		return 0,err
	}
	return likesnum,nil
}

func SelectLongPostDisLikesByPostId(postId int)(int ,error){
	var dislikesnum int
	err:=Db.QueryRow("select dislikes from longpost where post_id=?",postId).Scan(&dislikesnum)
	if err!=nil{
		return 0,err
	}
	return dislikesnum,nil
}

func SelectLongPostCommentNumByPostId(postId int)(int,error){
	var commentnum int
	err:=Db.QueryRow("select comment_num from longpost where post_id=?",postId).Scan(&commentnum)
	if err!=nil{
		return 0,err
	}
	return commentnum,nil
}

func UpdateLongPostLikeByPostId(postId int)error{
	likenum,err:=SelectLongPostLikesByPostId(postId)
	if err==nil||err==sql.ErrNoRows{
		_,errr:=Db.Exec("update longpost set likes=?",likenum+1)
		if errr!=nil{
			return err
		}
		return nil
	}
	return err
}

func UpdateLongPostDislikeByPostId(postId int)error{
	dislikenum,err:=SelectLongPostDisLikesByPostId(postId)
	if err==nil||err==sql.ErrNoRows{
		_,errr:=Db.Exec("update longpost set dislikes=?",dislikenum-1)
		if errr!=nil{
			return err
		}
		return nil
	}
	return err
}

func UpdateCommentNumByPostId(postId int)error{
	commentnum,err:=SelectLongPostCommentNumByPostId(postId)
	if err==nil||err==sql.ErrNoRows{
		_,errr:=Db.Exec("update longpost set comment_num=? where postId=?",commentnum+1,postId)
		if errr!=nil{
			return err
		}
		return nil
	}
	return err
}

func SelectLongPostByUsername(username string)([]model.Longpost,int,error){
	var ps []model.Longpost
	var num=0

	rows,errr:=Db.Query("select *from longpost where username=?",username)
	if errr!=nil{
		return ps,0,errr
	}
	defer rows.Close()
	for rows.Next() {
		var p model.Longpost
		errrr := rows.Scan(&p.PostId,&p.FilmId,&p.Txt,&p.Username,&p.PostTime,&p.UpdateTime,&p.Score,&p.Title,&p.Likes,&p.Dislikes,&p.CommentNum)
		if errrr != nil {
			return ps,0,errrr
		}
		ps=append(ps,p)
		num++
	}
	return ps,num,nil
}
