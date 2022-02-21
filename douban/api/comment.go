package api

import (
	"douban/model"
	"douban/service"
	"douban/tool"
	"fmt"
	"github.com/gin-gonic/gin"
	"time"
)
//陈年烂码

func addComment(c *gin.Context) {
	txt := c.PostForm("txt")
	postid := tool.StringTOInt(c.PostForm("postid"))
	username :=c.MustGet("username").(string)
	iscomcom := tool.StringTOInt(c.PostForm("iscomcom"))
	comid 	 :=tool.StringTOInt(c.PostForm("comcomid"))
	//入参check
	info, booll := tool.PostLengthCheck(txt)
	if booll != true {
		c.JSON(200, info)
		return
	}


	if iscomcom == 1{
		com := model.Comment{
			ComComId:    comid,
			Txt:         txt,
			Username:    username,
			IsComCom: 	 iscomcom,
			CommentTime: time.Now(),
		}
		err := service.AddComCom(com)
		if err != nil {
			fmt.Println("Add CommentCom err:",err)
			tool.RespInternalError(c)
			return
		}
		tool.RespSuccessful(c, "评论套娃")

	} else {
		com := model.Comment{
			PostId:      postid,
			Txt:         txt,
			Username:    username,
			CommentTime: time.Now(),
		}
		err := service.AddComment(com)
		if err != nil {
			fmt.Println("Add comment err",err)
			tool.RespInternalError(c)
			return
		}
		tool.RespSuccessful(c, "评论")
	}
}

func DropComment(c*gin.Context){
	id := tool.StringTOInt(c.PostForm("comment_id"))
	err :=service.DelectComment(id)
	if err!=nil{
		tool.RespInternalError(c)
		return
	}
	tool.RespSuccessful(c,"删除")
}

func modifycomment(c *gin.Context){
	id :=tool.StringTOInt(c.PostForm("comment_id"))
	ntxt :=c.PostForm("txt")

	err :=service.ModifyComment(id,ntxt)
	if err!=nil{
		tool.RespInternalError(c)
		return
	}
	tool.RespSuccessful(c,"修改")
}


func ComDetail(c *gin.Context){
	id :=tool.StringTOInt(c.PostForm("comment_id"))
	com,err:=service.GetComment(id)
	if err!=nil{
		tool.RespInternalError(c)
		return
	}
	coms,num,err:=service.GetComComment(id)
	com.CommentTime=time.Now()

	c.JSON(200,gin.H{
		"status":true,
		"info":"获取评论成功",
		"comment":com,
	})
	c.JSON(200,gin.H{
		"status":true,
		"info":"获取评论的评论成功",
		"num":num,
		"recomment":coms,
	})
}
