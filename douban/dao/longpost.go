package dao

import (
	"database/sql"
	"douban/model"
)

func InsertLongPost(longpost model.Longpost)error{
	sqlstr:="insert into longpost(film_id,txt,username,post_time,score,title,likes,dislikes,comment_num)values(?,?,?,?,?,?,?,?,?)"
	_,err:=Db.Exec(sqlstr,longpost.FilmId,longpost.Txt,longpost.UpdateTime,longpost.PostTime,longpost.PostId,longpost.Title,longpost.Likes,longpost.Dislikes,longpost.CommentNum)
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
	var p =make([]model.Longpost,10000)
	var i=1

	rows,errr:=Db.Query("select *from longpost where film_id=?",filmId)
	if errr!=nil{
		return p,0,errr
	}
	defer rows.Close()
	for rows.Next() {
		errrr := rows.Scan(&p[i].PostId,&p[i].FilmId,&p[i].Txt,&p[i].Username,&p[i].PostTime,&p[i].UpdateTime,&p[i].Score,&p[i].Title,&p[i].Likes,&p[i].Dislikes,&p[i].CommentNum)
		if errrr != nil {
			return p,0,errrr
		}
		i++
	}
	return p,i-1,nil
}

func SelectLongPostLikesByPostId(postId int)(int ,error){
	var likesnum int
	err:=Db.QueryRow("select likes from longpost where post_id=?",postId).Scan(&likesnum)
	if err!=nil{
		return 0,err
	}
	return likesnum,nil
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
	likenum,err:=SelectLongPostLikesByPostId(postId)
	if err==nil||err==sql.ErrNoRows{
		if likenum==0{likenum++}
		_,errr:=Db.Exec("update longpost set likes=?",likenum-1)
		if errr!=nil{
			return err
		}
		return nil
	}
	return err
}

func UpdateCommentNumByPostId(postId int)error{
	commentnum,err:=SelectShortPostLikesByPostId(postId)
	if err==nil||err==sql.ErrNoRows{
		_,errr:=Db.Exec("update longpost set commment_num=?",commentnum+1)
		if errr!=nil{
			return err
		}
		return nil
	}
	return err
}