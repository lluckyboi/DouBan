package api

import (
	"douban/model"
	"douban/service"
	"douban/tool"
	"fmt"
	"github.com/gin-gonic/gin"
)

func addact(c *gin.Context){
	ActorId:=tool.StringTOInt(c.PostForm("actor_id"))
	FilmId:=tool.StringTOInt(c.PostForm("film_id"))
	role:=c.PostForm("role")

	act:=model.Act{
		ActorId: ActorId,
		FilmId:  FilmId,
		Role:    role,
	}

	err:=service.AddAct(act)
	if err!=nil{
		fmt.Println("add act correct err: ", err)
		tool.RespInternalError(c)
		return
	}
	tool.RespSuccessful(c,"添加act")
}