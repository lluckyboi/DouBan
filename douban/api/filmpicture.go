package api

import (
	"douban/service"
	"douban/tool"
	"fmt"
	"github.com/gin-gonic/gin"
)

//添加剧照
func addfilmpicture(c *gin.Context){
	filmId:=tool.StringTOInt(c.PostForm("film_id"))
	url:=c.PostForm("url")
	err:=service.AddFilmPicture(filmId,url)
	if err!=nil{
		fmt.Println("add film picture err: ", err)
		tool.RespInternalError(c)
		return
	}
	tool.RespSuccessful(c,"添加剧照")
}

//获取剧照
func getfilmpictures(c *gin.Context){
	filmId:=tool.StringTOInt(c.PostForm("film_id"))
	filmpictures,num,err:=service.GetFilmPicture(filmId)
	if err!=nil{
		fmt.Println("get film pictures err: ", err)
		tool.RespInternalError(c)
		return
	}
	c.JSON(200,gin.H{
		"status":true,
		"info":"获取剧照成功",
		"num":num,
		"data":filmpictures,
	})
}