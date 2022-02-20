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

func SelectLPCommentByPostId(postId int) ([]model.LPComment, error) {
	var comments []model.LPComment

	rows, err := Db.Query("SELECT id, post_id, txt, username, comment_time FROM comment WHERE post_id = ?", postId)
	if err != nil {
		return nil, err
	}
	defer rows.Close()
	for rows.Next() {
		var comment model.LPComment
		err = rows.Scan(&comment.Id, &comment.LPostId, &comment.Txt, &comment.Username, &comment.CommentTime)
		if err != nil {
			return nil, err
		}
		comments = append(comments, comment)
	}
	return comments, nil
}

func DeleteLPCommentById(lpcommentId int)error{
	sqlstr:="delete from lpcomment where comment_id=?"
	_,err:=Db.Exec(sqlstr,lpcommentId)
	return err
}