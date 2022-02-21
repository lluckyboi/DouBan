package api

import (
	"douban/model"
	"douban/service"
	"douban/tool"
	"fmt"
	"github.com/gin-gonic/gin"
	"time"
)

func addlongpost(c *gin.Context){
	username:=c.MustGet("username").(string)
	filmId:=tool.StringTOInt(c.PostForm("film_id"))
	txt:=c.PostForm("txt")
	score:=tool.StringToFloat2_1(c.PostForm("score"))
	dislikes:=tool.StringTOInt(c.PostForm("dislikes"))
	likes:=tool.StringTOInt(c.PostForm("likes"))
	title:=c.PostForm("title")
	commentNum:=tool.StringTOInt(c.PostForm("comment_num"))

	longpost:=model.Longpost{
		FilmId:     filmId,
		Txt:        txt,
		Username:   username,
		PostTime:   time.Now().String(),
		Score:      score,
		Likes:      likes,
		Dislikes:   dislikes,
		CommentNum: commentNum,
		Title:      title,
	}

	err:=service.AddLongPost(longpost)
	if err!=nil{
		fmt.Println("add long post err: ", err)
		tool.RespInternalError(c)
		return
	}

	nerr:=service.NewScore(score,filmId)
	if nerr!=nil{
		fmt.Println("update score and commentNum err: ", nerr)
		tool.RespInternalError(c)
		return
	}

	tool.RespSuccessful(c,"添加影评")
}

func updatelongpost(c *gin.Context){
	txt:=c.PostForm("txt")
	score:=tool.StringToFloat2_1(c.PostForm("score"))
	title:=c.PostForm("title")
	postId:=tool.StringTOInt(c.PostForm("post_id"))

	longpost:=model.Longpost{
		PostId:		postId,
		Txt:        txt,
		UpdateTime:   time.Now().String(),
		Score:      score,
		Title:      title,
	}
	err:=service.UpdateLongPost(longpost)
	if err!=nil{
		fmt.Println("update long post err: ", err)
		tool.RespInternalError(c)
		return
	}
	tool.RespSuccessful(c,"更新影评")
}

func deletelongppost(c *gin.Context){
	postId:= tool.StringTOInt(c.PostForm("post_id"))
	err:=service.DeleteLongPost(postId)
	if err!=nil{
		fmt.Println("delete long post err: ", err)
		tool.RespInternalError(c)
		return
	}
	tool.RespSuccessful(c,"删除影评")
}

func getlongpostbyfilmid(c *gin.Context){
	filmId:=tool.StringTOInt(c.PostForm("film_id"))

	longposts,num,err:=service.GetLongPostByFilmId(filmId)
	if err != nil {
		fmt.Println("get long post err: ", err)
		tool.RespInternalError(c)
		return
	}

	c.JSON(200, gin.H{
		"status": 	   true,
		"info":   "搜索成功",
		"num":		   num,
		"data": longposts[1:num+1],
	})
}

func likelongpost(c *gin.Context){
	postId:=tool.StringTOInt(c.PostForm("post_id"))
	err:=service.LikeLongPost(postId)
	if err!=nil{
		fmt.Println("update like long post err: ", err)
		tool.RespInternalError(c)
		return
	}
	tool.RespSuccessful(c,"点赞")
}

func dislikelongpost(c *gin.Context){
	postId:=tool.StringTOInt(c.PostForm("post_id"))
	err:=service.DislikeLongPost(postId)
	if err!=nil{
		fmt.Println("update dislike long post err: ", err)
		tool.RespInternalError(c)
		return
	}
	tool.RespSuccessful(c,"反对")
}

func getlongpostbyusername(c *gin.Context){
	username:=c.MustGet("username").(string)
	longposts,num,err:=service.GetLongPostByUsername(username)
	if err!=nil{
		fmt.Println("get long post err: ", err)
		tool.RespInternalError(c)
		return
	}
	c.JSON(200,gin.H{
		"status":true,
		"num":num,
		"data":longposts,
	})
}