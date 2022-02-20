package api

import (
	"douban/model"
	"douban/service"
	"douban/tool"
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
)

//测试
func homeHandler(c *gin.Context) {
	username := c.MustGet("username").(string)
	c.JSON(http.StatusOK, gin.H{
		"status": 2000,
		"info":  "success",
		"data": gin.H{"username": username},
	})
}
func sayhello(c *gin.Context){
	c.JSON(200,gin.H{
		"status":true,
		"info":"hello",
	})
}


func login(c *gin.Context){
	username:=c.PostForm("username")
	password:=c.PostForm("password")
	//check账号密码
	isok, err :=service.IsPasswordCorrectAndUsernameExist(username,password)

	//错误处理
	if err !=nil{
		fmt.Println("judge password correct err: ", err)
		tool.RespInternalError(c)
		return
	}
	if isok==0{
		c.JSON(200,gin.H{
			"status":false,
			"info":"密码错误",
		})
		return
	}else if isok==2{
		c.JSON(200,gin.H{
			"status":false,
			"info":"用户不存在",
		})
		return
	}

	//登录成功的反馈
	tool.RespSuccessful(c,username+"登录")

	////设置cookie
	//c.SetCookie("gin_cookie", username, 3600, "/", "", false, true)
}

func newuser(c *gin.Context){
	username:=c.PostForm("username")
	password:=c.PostForm("password")
	ques1	:=c.PostForm("ques1")
	ques2	:=c.PostForm("ques2")
	ans1	:=c.PostForm("ans1")
	ans2	:=c.PostForm("ans2")

	//length check
	infou,isoverlu:=tool.LengthCheck(username)
	if isoverlu==false{
		c.JSON(200,gin.H{
			"status":false,
			"info":"用户名"+infou,
		})
		return
	}
	infop,isoverp:=tool.LengthCheck(password)
	if isoverp==false{
		c.JSON(200,gin.H{
			"status":false,
			"info":"密码"+infop,
		})
		return
	}

	user :=model.User{
		Username :  username,
		Password :  password,
		Ques1    :  ques1,
		Ans1 	 :  ans1,
		Ques2	 : ques2,
		Ans2	 :  ans2,
	}
	isok,err:=service.IsUsernameRepeat(username)
	if err!=nil{
		fmt.Println("judge username repeat err: ", err)
		tool.RespInternalError(c)
		return
	}
	//重复了
	if isok!=true{
		c.JSON(200,gin.H{
			"status":false,
			"info":"用户名重复",
		})
		return
	}

	err =service.NewUser(user)
	if err!=nil{
		fmt.Println("register err: ", err)
		tool.RespInternalError(c)
		return
	}
	tool.RespSuccessful(c,"注册")
}

func getques(c*gin.Context){
	username:=c.PostForm("username")
	isok,err:=service.IsPasswordCorrectAndUsernameExist(username,"")
	if err!=nil{
		fmt.Println("GetQuestion err: ", err)
		tool.RespInternalError(c)
		return
	}
	//用户存在
	if isok!=2{
		que1,que2,errr:=service.GetQuesByUsername(username)
		if errr!=nil{
			fmt.Println("GetQuestion err: ", err)
			tool.RespInternalError(c)
			return
		}
		c.JSON(200,gin.H{
			"status":true,
			"info":"获取密保问题成功",
			"data":gin.H{
				"ques1":que1,
				"ques2":que2,
			},

		})
	}
}

func findpassword(c *gin.Context){
	//获取相关信息
	username:=c.PostForm("username")
	ans1:=c.PostForm("ans1")
	ans2:=c.PostForm("ans2")

	isok,err,password:=service.IsPasswordQuesOk(username,ans1,ans2)
	if err!=nil{
		fmt.Println("judge answers correct err: ", err)
		tool.RespInternalError(c)
		return
	}
	if isok==false{
		c.JSON(200,gin.H{
			"status":false,
			"info":"密保问题答案错误",
		})
		return
	}

	c.JSON(200,gin.H{
		"status":true,
		"info":"获取密码成功",
		"data":password,
	})
}

//改密码
func newpassword(c *gin.Context){
	BefPassword := c.PostForm("BefPassword")
	NewPassword := c.PostForm("NewPassword")
	username 	:= c.PostForm("username")

	info,isoverl:=tool.LengthCheck(NewPassword)
	if isoverl==false{
		c.JSON(200,gin.H{
			"status":false,
			"info":"新密码"+info,
		})
		return
	}

	isokk, errr := service.IsPasswordCorrectAndUsernameExist(username,BefPassword)
	if errr != nil {
		fmt.Println("judge password correct err: ", errr)
		tool.RespInternalError(c)
		return
	}
	if isokk==0{
		c.JSON(200,gin.H{
			"status":false,
			"info":"密码错误",
		})
		return
	}else if isokk==2{
		c.JSON(200,gin.H{
			"status":false,
			"info":"用户不存在",
		})
	}

	isok,err :=service.NewPassword(username,NewPassword)
	if err!=nil{
		fmt.Println("updata password  err: ", err)
		tool.RespInternalError(c)
		return
	}
	if isok==false {
		c.JSON(200, gin.H{
			"status":false,
			"info":"修改失败",
		})
		return
	}
	c.JSON(200,gin.H{
		"status":true,
		"info":"修改成功",
	})
}

//通过ID获取用户名
func getusername(c *gin.Context){
	userId:=tool.StringTOInt(c.PostForm("id"))
	username,booll,err:=service.GetUsernameById(userId)
	if err!=nil{
		fmt.Println("get username err: ", err)
		tool.RespInternalError(c)
		return
	}
	if booll==false{
		c.JSON(200,gin.H{
			"status":201,
			"info":"用户不存在",
		})
		return
	}
	c.JSON(200,gin.H{
		"status":200,
		"info":"获取成功",
		"data":username,
	})
}

//获取看过
func getwatched(c *gin.Context){
	username:=c.MustGet("username").(string)
	filmids,num,err:=service.GetUserWatchedByUsername(username)
	if err!=nil{
		fmt.Println("get user watched err: ", err)
		tool.RespInternalError(c)
		return
	}
	c.JSON(200,gin.H{
		"status":true,
		"info":"获取watched成功",
		"num":num,
		"data":filmids,
	})
}

//获取想看
func getwant(c *gin.Context){
	username:=c.MustGet("username").(string)
	filmids,num,err:=service.GetUserWantByUsername(username)
	if err!=nil{
		fmt.Println("get user watched err: ", err)
		tool.RespInternalError(c)
		return
	}
	c.JSON(200,gin.H{
		"status":true,
		"info":"获取watched成功",
		"num":num,
		"data":filmids,
	})
}

//个人简介
func updateintroduction(c *gin.Context){
	username:=c.MustGet("username").(string)
	introduction:=c.PostForm("introduction")

	err:=service.AddIntroduction(username,introduction)
	if err!=nil{
		fmt.Println("add introduction err: ", err)
		tool.RespInternalError(c)
		return
	}
	tool.RespSuccessful(c,"添加个人简介")
}

//添加头像
func updateportrait(c *gin.Context){
	username:=c.MustGet("username").(string)
	portrait:=c.PostForm("portrait")
	err:=service.UpdatePortrait(portrait,username)
	if err!=nil{
		fmt.Println("add portrait err: ", err)
		tool.RespInternalError(c)
		return
	}
	tool.RespSuccessful(c,"上传")
}

func getuserinfo(c *gin.Context){
	username:=c.MustGet("username").(string)
	user,err:=service.GetUserIPIPByUsername(username)
	if err!=nil{
		fmt.Println("get user info err: ", err)
		tool.RespInternalError(c)
		return
	}
	Otuser:=model.OtUserInfo{
		Username:     username,
		PictureUrl:   user.PictureUrl,
		Introduction: user.Introduction,
	}
	c.JSON(200,gin.H{
		"status":true,
		"info":"获取成功",
		"data":Otuser,
	})
}