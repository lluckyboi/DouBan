package dao

import "douban/model"

func InsertLPComment(comment model.LPComment) error {
	_, err := Db.Exec("INSERT INTO lpcomment(username, txt, comment_time, post_id) "+"values(?, ?, ?, ?);", comment.Username, comment.Txt, comment.CommentTime, comment.LPostId)
	if err!=nil{
		return err
	}

	errr:=UpdateCommentNumByPostId(comment.LPostId)
	if errr!=nil{
		return errr
	}
	return nil
}

func SelectLPCommentByPostId(postId int) ([]model.LPComment,int, error) {
	var comments []model.LPComment
	var num=0
	rows, err := Db.Query("SELECT lpcomment_id, post_id, txt, username, comment_time FROM lpcomment WHERE post_id = ?", postId)
	if err != nil {
		return nil,num,err
	}
	defer rows.Close()
	for rows.Next() {
		var comment model.LPComment
		err = rows.Scan(&comment.Id, &comment.LPostId, &comment.Txt, &comment.Username, &comment.CommentTime)
		if err != nil {
			return nil, num,err
		}
		comments = append(comments, comment)
		num++
	}
	return comments, num,nil
}

func DeleteLPCommentById(lpcommentId int)error{
	sqlstr:="delete from lpcomment where comment_id=?"
	_,err:=Db.Exec(sqlstr,lpcommentId)
	return err
}