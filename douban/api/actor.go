package api

import (
	"douban/model"
	"douban/service"
	"douban/tool"
	"fmt"
	"github.com/gin-gonic/gin"
)

func addactor(c *gin.Context){
	name:=c.PostForm("name")
	mainrole:=c.PostForm("mainrole")
	sex:=c.PostForm("sex")
	introduction:=c.PostForm("introduction")
	pictureUrl:=c.PostForm("picture_url")

	actor:=model.Actor{
		Name:         name,
		MainRole:     mainrole,
		Sex:          sex,
		Introduction: introduction,
		PictureUrl: pictureUrl,
	}

	err:=service.AddActor(actor)
	if err!=nil{
		fmt.Println("add actor err: ", err)
		tool.RespInternalError(c)
		return
	}
	tool.RespSuccessful(c,"添加演员")
}

func deleteactor(c *gin.Context){
	actorId:=tool.StringTOInt(c.PostForm("actor_id"))
	err:=service.DeleteActor(actorId)
	if err!=nil{
		fmt.Println("delete actor err: ", err)
		tool.RespInternalError(c)
		return
	}

	tool.RespSuccessful(c,"删除")
}

func getactordetail(c *gin.Context){
	actorId:=tool.StringTOInt(c.PostForm("actor_id"))
	actor,booll,err:=service.SearchActor(actorId)
	if err!=nil{
		fmt.Println("search actor err: ", err)
		tool.RespInternalError(c)
		return
	}

	if booll==false{
		c.JSON(200,gin.H{
			"status":201,
			"info":"未找到该演员",
		})
		return
	}
	c.JSON(200,gin.H{
		"status":200,
		"info":"搜索成功",
		"data":actor,
	})
}

func getactorbyfilmid(c *gin.Context){
	filmId:=tool.StringTOInt(c.PostForm("film_id"))
	actors,num,err:=service.GetActorsByFilmId(filmId)
	if err!=nil{
		fmt.Println("get actor and role err: ", err)
		tool.RespInternalError(c)
		return
	}
	c.JSON(200,gin.H{
		"status":true,
		"info":"获取演员与角色成功",
		"num":num,
		"data":actors,
	})
}

func getfilmids(c *gin.Context){
	actorId:=tool.StringTOInt(c.PostForm("actor_id"))
	filmids,num,err:=service.GetFilmIdsByActorId(actorId)
	if err!=nil{
		fmt.Println("get actor and role err: ", err)
		tool.RespInternalError(c)
		return
	}
	c.JSON(200,gin.H{
		"status":true,
		"info":"获取参演电影成功",
		"num":num,
		"data":filmids,
	})
}