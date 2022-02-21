package api

import (
	"douban/model"
	"douban/service"
	"douban/tool"
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
	"strings"
)

//cookie鉴权中间件
func auth(jq *gin.Context){
	value,err :=jq.Cookie("douban_login")
	//错误处理
	if err!=nil{
		tool.RespErrorWithDate(jq,"请登陆后进行操作")
		jq.Abort()
	}else{
		//获取的cookie写入上下文
		jq.Set("douban_login",value)
		//挂起来执行剩下进程
		jq.Next()
	}
}

//jwt鉴权
func authHandler(c *gin.Context) {
	// 用户发送用户名和密码过来
	var user model.UserInfo
	err := c.ShouldBind(&user)
	if err != nil {
		c.JSON(http.StatusOK, gin.H{
			"status": 2001,
			"ino":  "无效的参数",
		})
		return
	}
	// 校验用户名和密码是否正确
	n,err:=service.IsPasswordCorrectAndUsernameExist(user.Username,user.Password)
	if err!=nil{
		fmt.Println("check password err: ", err)
		tool.RespInternalError(c)
		return
	}
	if n==1 {
		// 生成Token
		tokenString, _ := model.GenToken(user.Username)
		c.JSON(http.StatusOK, gin.H{
			"status": 2000,
			"info":  "success",
			"data": gin.H{"token": tokenString},
		})
		return
	}
	c.JSON(http.StatusOK, gin.H{
		"status": 2002,
		"info":  "鉴权失败",
	})
	return
}

func JWTAuthMiddleware() func(c *gin.Context) {
	return func(c *gin.Context) {
		// 客户端携带Token有三种方式 1.放在请求头 2.放在请求体 3.放在URI
		// 这里假设Token放在Header的Authorization中，并使用Bearer开头
		// 这里的具体实现方式要依据你的实际业务情况决定
		authHeader := c.Request.Header.Get("Authorization")
		if authHeader == "" {
			c.JSON(http.StatusOK, gin.H{
				"code": 2003,
				"msg":  "请求头中auth为空",
			})
			c.Abort()
			return
		}
		// 按空格分割
		parts := strings.SplitN(authHeader, " ", 2)
		if !(len(parts) == 2 && parts[0] == "Bearer") {
			c.JSON(http.StatusOK, gin.H{
				"code": 2004,
				"msg":  "请求头中auth格式有误",
			})
			c.Abort()
			return
		}
		// parts[1]是获取到的tokenString，我们使用之前定义好的解析JWT的函数来解析它
		mc, err := model.ParseToken(parts[1])
		if err != nil {
			c.JSON(http.StatusOK, gin.H{
				"code": 2005,
				"info":  "无效的Token",
			})
			c.Abort()
			return
		}
		// 将当前请求的username信息保存到请求的上下文c上
		c.Set("username", mc.Username)
		c.Next() // 后续的处理函数可以用过c.Get("username")来获取当前请求的用户信息
	}
}