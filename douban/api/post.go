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

func addPost(c *gin.Context){
	username :=c.MustGet("username").(string)
	txt := c.PostForm("txt")
	title:=c.PostForm("title")

	//check
	info,booll:=tool.LengthCheck(username)
	if booll!=true{
		c.JSON(200,gin.H{
			"status":false,
			"info":info,
		})
		return
	}
	info1,bool1:=tool.PostLengthCheck(txt)
	if bool1!=true{
		c.JSON(200,gin.H{
			"status":false,
			"info":info1,
		})
		return
	}

	//每次发表需要的基本信息
	post :=model.Post{
		Txt:        txt,
		Username:   username,
		Title: 		title,
		PostTime:   time.Now().String(),
		UpdateTime: time.Now().String(),
	}
	//c.String(200,"%s",post.Txt) 测试点
	err :=service.AddPost(post)
	if err!=nil {
		fmt.Println("append err: ", err)
		tool.RespInternalError(c)
		return
	}
	tool.RespSuccessful(c,"发表")
}

func modifypost(c *gin.Context){
	//读id
	id :=tool.StringTOInt(c.PostForm("post_id"))
	ntxt :=c.PostForm("txt")
	ntitle:=c.PostForm("title")

	err :=service.Modifypost(id,ntitle,ntxt)
	if err!=nil{
		tool.RespInternalError(c)
		return
	}
	tool.RespSuccessful(c,"修改")
}

func lookpost(c *gin.Context){
	post,num,err :=service.AllPosts()
	if err!=nil{
		fmt.Println("get post: ", err)
		tool.RespInternalError(c)
		return
	}
	c.JSON(200,gin.H{
		"status":true,
		"info":"获取post成功",
		"num":num,
		"data":post,
	})
}

func postDetail(c *gin.Context){

	id:=tool.StringTOInt(c.PostForm("post_id"))
	//先取post
	post,err :=service.PostOneGet(id)
	if err!=nil{
		fmt.Println("get post detail err: ", err)
		tool.RespInternalError(c)
		return
	}

	//评论
	coms,num,err :=service.GetCommentOfPost(id)
	if err!=nil{
		tool.RespInternalError(c)
		return
	}
	c.JSON(200,gin.H{
		"status":true,
		"info":"获取成功",
		"commentnum":num,
		"comments":coms,
		"post":post,
	})
}