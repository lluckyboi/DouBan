package api

import (
	"douban/model"
	"douban/service"
	"douban/tool"
	"fmt"
	"github.com/gin-gonic/gin"
	"time"
)

func addshrotpost(c *gin.Context){
	username:=c.MustGet("username").(string)
	filmId:=tool.StringTOInt(c.PostForm("film_id"))
	txt:=c.PostForm("txt")
	score:=tool.StringToFloat2_1(c.PostForm("score"))
	want:=tool.StringTOInt(c.PostForm("want"))
	watched:=tool.StringTOInt(c.PostForm("watched"))
	likes:=tool.StringTOInt(c.PostForm("likes"))
	tags:=c.PostForm("tags")



	shortpost:=model.ShortPost{
		FilmId:     filmId,
		Txt:        txt,
		Username:   username,
		PostTime:   time.Now().String(),
		Score:      score,
		Want:       want,
		Watched:    watched,
		Likes:		likes,
		Tags: 		tags,
	}
	err:=service.AddShortPost(shortpost)
	if err!=nil{
		fmt.Println("add short post err: ", err)
		tool.RespInternalError(c)
		return
	}
	nerr:=service.NewScore(score,filmId)
	if nerr!=nil{
		fmt.Println("update score and commentNum err:", nerr)
		tool.RespInternalError(c)
		return
	}

	tool.RespSuccessful(c,"添加短评")
}

func deleteshortpost(c *gin.Context){
	postId:=tool.StringTOInt(c.PostForm("post_id"))
	err:=service.DeleteShortPostByPostId(postId)
	if err!=nil{
		fmt.Println("delete short post err: ", err)
		tool.RespInternalError(c)
		return
	}

	tool.RespSuccessful(c,"删除短评")
}

func updateshortpost(c *gin.Context){
	username:=c.MustGet("username").(string)
	filmId:=tool.StringTOInt(c.PostForm("film_id"))
	txt:=c.PostForm("txt")
	score:=tool.StringToFloat2_1(c.PostForm("score"))
	want:=tool.StringTOInt(c.PostForm("want"))
	watched:=tool.StringTOInt(c.PostForm("watched"))
	likes:=tool.StringTOInt(c.PostForm("likes"))
	tags:=c.PostForm("tags")

	_,ferr:=service.GetFilmByFilmId(filmId)
	if ferr!=nil{
		fmt.Println("get film by id err: ", ferr)
		tool.RespInternalError(c)
		return
	}

	shortpost:=model.ShortPost{
		FilmId:     filmId,
		Txt:        txt,
		Username:   username,
		UpdateTime:  time.Now().String(),
		Score:      score,
		Want:       want,
		Watched:    watched,
		Likes:		likes,
		Tags: 		tags,
	}
	err:=service.UpdateShortPost(shortpost)
	if err!=nil{
		fmt.Println("update short post err: ", err)
		tool.RespInternalError(c)
		return
	}

	tool.RespSuccessful(c,"更新")
}

func getshortpostbyfilmid(c *gin.Context) {
	filmId := tool.StringTOInt(c.PostForm("film_id"))

	shortposts, num, err := service.GetShortPostByFilmId(filmId)
	if err != nil {
		fmt.Println("get short post err: ", err)
		tool.RespInternalError(c)
		return
	}

	c.JSON(200, gin.H{
		"status": 	true,
		"info":   "搜索成功",
		"num":		num,
		"data": shortposts[1:num+1],
	})
}

func getshortpostbyusername(c *gin.Context){
	username:=c.MustGet("username").(string)
	shortposts, num, err :=service.GetShortPostByUsername(username)
	if err != nil {
		fmt.Println("get short post err: ", err)
		tool.RespInternalError(c)
		return
	}

	c.JSON(200, gin.H{
		"status":  true,
		"info":   "搜索成功",
		"num":	   num,
		"data": shortposts[1:num+1],
	})
}

func likeshortpost(c *gin.Context){
	postId:=tool.StringTOInt(c.PostForm("post_id"))
	err:=service.LikeShortPostById(postId)
	if err!=nil{
		fmt.Println("update like short post err: ", err)
		tool.RespInternalError(c)
		return
	}
	tool.RespSuccessful(c,"点赞")
}