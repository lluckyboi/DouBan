package api

import (
	"douban/model"
	"douban/service"
	"douban/tool"
	"fmt"
	"github.com/gin-gonic/gin"
	"time"
)

func addlpcomment(ctx *gin.Context) {
	username := ctx.MustGet("username").(string)
	txt := ctx.PostForm("txt")
	lpostId:=tool.StringTOInt(ctx.PostForm("post_id"))


	lpcomment := model.LPComment{
		LPostId:     lpostId,
		Txt:         txt,
		Username:    username,
		CommentTime: time.Now().String(),
	}
	err := service.AddLPComment(lpcomment)
	if err != nil {
		fmt.Println("add lpcomment err: ", err)
		tool.RespInternalError(ctx)
		return
	}

	tool.RespSuccessful(ctx,"添加回复")
}

func getlpcomment(c *gin.Context){
	postId:=tool.StringTOInt(c.PostForm("post_id"))
	lpcomments,err:=service.GetLPComments(postId)
	if err!=nil{
		fmt.Println("get lpcommen err: ", err)
		tool.RespInternalError(c)
		return
	}
	c.JSON(200,gin.H{
		"status":true,
		"info":"获取回复成功",
		"data":lpcomments,
	})
}

func deletelpcomment(c *gin.Context){
	commentId:=tool.StringTOInt(c.PostForm("lpcomment_id"))
	err:=service.DeleteLPCommentById(commentId)
	if err!=nil{
		fmt.Println("delete lpcomment err: ", err)
		tool.RespInternalError(c)
		return
	}
	tool.RespSuccessful(c,"删除回复")
}
