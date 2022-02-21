package api

import (
	"douban/model"
	"douban/service"
	"douban/tool"
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
)
//获取电影详情
func getfilm(c *gin.Context){
	SFilmId :=c.PostForm("film_id")
	FilmId	 :=tool.StringTOInt(SFilmId)
	film,err:=service.GetFilmByFilmId(FilmId)
	if err!=nil{
		fmt.Println("get film err: ", err)
		tool.RespInternalError(c)
		return
	}
	c.JSON(http.StatusOK,gin.H{
		"status":true,
		"info":"获取电影成功",
		"data":film,
	})
}

//添加电影
func addfilm(c *gin.Context){
	name :=c.PostForm("name")
	directer :=c.PostForm("directer")
	screenwriter :=c.PostForm("screenwriter")
	Type :=c.PostForm("type")
	location :=c.PostForm("location")
	language :=c.PostForm("language")
	introduction := c.PostForm("introduction")
	releaseTime :=c.PostForm("release_time")
	length :=c.PostForm("length")
	othername :=c.PostForm("othername")
	IMDb :=c.PostForm("IMDb")
	score :=tool.StringToFloat2_1(c.PostForm("score"))
	postNum :=tool.StringTOInt(c.PostForm("post_num"))
	posterUrl :=c.PostForm("poster_url")


	film:=model.Film{
		Name:         name,
		Directer:     directer,
		Screenwriter: screenwriter,
		Type:         Type,
		Location:     location,
		Language:     language 	,
		Introduction: introduction,
		ReleaseTime:  releaseTime,
		Length:       length,
		OtherName:    othername,
		IMDb:         IMDb,
		Score:        score,
		PostNum:      postNum,
		PosterUrl:    posterUrl,
	}
	err:=service.AddFilm(film)
	if err!=nil{
		fmt.Println("add film err: ", err)
		tool.RespInternalError(c)
		return
	}
	tool.RespSuccessful(c,"添加电影")
}

//删除电影
func deletefilm(c *gin.Context){
	filmId:=c.PostForm("film_id")
	FilmId :=tool.StringTOInt(filmId)
	err:=service.DeletFilm(FilmId)
	if err!=nil{
		fmt.Println("delete film err: ", err)
		tool.RespInternalError(c)
		return
	}
	tool.RespSuccessful(c,"删除电影")
}

//搜索电影
func searchfilm(c *gin.Context){
	txt:= c.PostForm("name")
	aim:= c.PostForm("aim")

	filmm,num,err:=service.Searchfilm(txt,aim)
	if err!=nil{
		fmt.Println("search film err: ", err)
		tool.RespInternalError(c)
		return
	}
	c.JSON(200,gin.H{
		"status":true,
		"info":"搜索成功",
		"num":num,
		"data":filmm[1:num+1],
	})
}

//supersearch
func supersearch(c *gin.Context){
	Type:=c.PostForm("type")
	location:=c.PostForm("location")
	releaseTime:=c.PostForm("release_time")
	tag:=c.PostForm("tag")

	sfilm:=model.Film{
		Type:         Type,
		Location:     location,
		ReleaseTime:  releaseTime,
		Tag:          tag,
	}

	films,num,err:=service.SuperSearch(sfilm)
	if err!=nil{
		fmt.Println("search err: ", err)
		tool.RespInternalError(c)
		return
	}

	c.JSON(200,gin.H{
		"status":true,
		"info":"搜索成功",
		"num":	num,
		"data": films[1:num+1],
	})
}

//排行榜
func getfilmlist(c *gin.Context){
	films,num,err:=service.GetFilmList()
	if err!=nil{
		fmt.Println("get film list err: ", err)
		tool.RespInternalError(c)
		return
	}
	c.JSON(200,gin.H{
		"status":true,
		"num":num,
		"info":"搜索成功",
		"data": films[1:num+1],
	})
}