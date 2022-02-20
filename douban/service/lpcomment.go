package service

import (
	"douban/dao"
	"douban/model"
)

func AddLPComment(comment model.LPComment) error {
	return dao.InsertLPComment(comment)
}

func GetLPComments(postId int) ([]model.LPComment, error) {
	return dao.SelectLPCommentByPostId(postId)
}

func DeleteLPCommentById(lpcommentId int)error{
	return dao.DeleteLPCommentById(lpcommentId)
}