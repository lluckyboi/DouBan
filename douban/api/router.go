package api

import (
	"github.com/gin-contrib/cors"
	"github.com/gin-contrib/static"
	"github.com/gin-gonic/gin"
)

func RUNENGINE() {
	r := gin.Default()

	//cors解决跨域问题
	config := cors.DefaultConfig()
	config.AllowAllOrigins = true //允许所有域名
	config.AllowMethods = []string{"GET", "POST", "OPTIONS" ,"PUT" ,"DELETE"}//允许请求的方法
	config.AllowHeaders = []string{"tus-resumable", "upload-length", "upload-metadata", "cache-control", "x-requested-with", "*"}//允许的Header
	r.Use(cors.New(config))

	// 部署前端静态网站
	r.Use(static.Serve("/", static.LocalFile("./source", false)))

	//获取token接口
	r.POST("/auth", authHandler)
	//测试
	r.GET("/home", JWTAuthMiddleware(), homeHandler)

	//登录 login放包内 不大写
	r.POST("/login",login)
	//注册 同样
	r.POST("/newuser",newuser)
	//获取密保问题
	r.POST("/getques",getques)
	//获取用户信息ById
	r.POST("/getusername",getusername)
	//找回密码
	r.POST("/findpassword",findpassword)

	//设置路由组 同url前缀放一组
	userGroup :=r.Group("/user")
	{
		userGroup.PUT("/newpassword",JWTAuthMiddleware(),newpassword)//修改密码
		userGroup.GET("/getwatched",JWTAuthMiddleware(),getwatched)
		userGroup.GET("/getwant",JWTAuthMiddleware(),getwant)
		userGroup.PUT("/updateintroduction",JWTAuthMiddleware(),updateintroduction)
		userGroup.PUT("/updateportrait",JWTAuthMiddleware(),updateportrait)
		userGroup.GET("/getuserinfo",JWTAuthMiddleware(),getuserinfo)
		userGroup.POST("/getusername",getusername)
	}

	filmGroup :=r.Group("/film")
	{
		filmGroup.POST("/getfilm",getfilm)
		filmGroup.PUT("/addfilm",addfilm)
		filmGroup.DELETE("deletefilm",deletefilm)
		filmGroup.POST("/searchfilm",searchfilm)
		filmGroup.POST("/supersearch",supersearch)
		filmGroup.GET("/filmlist",getfilmlist)
	}

	shortpostGroup:=r.Group("/shortpost")
	{
		shortpostGroup.PUT("/addshortpost",JWTAuthMiddleware(),addshrotpost)
		shortpostGroup.PUT("/updateshortpost",JWTAuthMiddleware(),updateshortpost)
		shortpostGroup.PUT("/likeshrotpost",JWTAuthMiddleware(),likeshortpost)
		shortpostGroup.GET("getshortpostsofuser",JWTAuthMiddleware(),getshortpostbyusername)
		shortpostGroup.POST("/getshortpostbyfilmid",getshortpostbyfilmid)
		shortpostGroup.DELETE("/deleteshortpost",JWTAuthMiddleware(),deleteshortpost)
	}

	longpostGroup:=r.Group("/longpost")
	{
		longpostGroup.POST("/getlongpostbyfilmid",getlongpostbyfilmid)
		longpostGroup.PUT("/addlongpost",JWTAuthMiddleware(),addlongpost)
		longpostGroup.DELETE("/deletelongpost",deletelongppost)
		longpostGroup.PUT("/likelongpost",JWTAuthMiddleware(),likelongpost)
		longpostGroup.PUT("/dislikelongpost",JWTAuthMiddleware(),dislikelongpost)
		longpostGroup.PUT("/updateloongpost",JWTAuthMiddleware(),updatelongpost)
	}

	lpcommentGroup:=r.Group("/lpcomment")
	{
		lpcommentGroup.PUT("/addlpcomment",JWTAuthMiddleware(),addlpcomment)
		lpcommentGroup.POST("/getlpcomment",getlpcomment)
		lpcommentGroup.DELETE("/deletelpcomment",deletelpcomment)
	}

	actorGroup:=r.Group("/actor")
	{
		actorGroup.PUT("/addactor",addactor)
		actorGroup.POST("/searchactor",getactordetail)
		actorGroup.DELETE("/deleteactor",deleteactor)
		actorGroup.POST("/getactorsbyfilmid",getactorbyfilmid)
		actorGroup.POST("/getfilmids",getfilmids)
	}

	actGroup:=r.Group("/act")
	{
		actGroup.PUT("/addact",addact)
	}

	//讨论区留言相关路由组
	postGroup :=r.Group("/post")
	{
		postGroup.POST("/addpost",JWTAuthMiddleware(),addPost)//发留言
		postGroup.POST("/modifypost",JWTAuthMiddleware(),modifypost)//修改留言 给出相应ID就可以修改
		postGroup.GET("/lookpost",lookpost)//看留言
		postGroup.GET("/postdetail",postDetail) //查看一条留言详细信息和其下属评论
	}

	//讨论区评论路由组
	commentGroup :=r.Group("/comment")
	{
		commentGroup.POST("/addcomment",JWTAuthMiddleware(),addComment)  //发评论
		commentGroup.POST("/modifycomment",JWTAuthMiddleware(),modifycomment)//改评论
		commentGroup.DELETE("/dropcomment",JWTAuthMiddleware(),DropComment) //删评论
		commentGroup.GET("/commentdetail",ComDetail)//查看评论和对它的回复
	}

	//剧照
	filmpictureGroup:=r.Group("/filmpicture")
	{
		filmpictureGroup.PUT("/addfilmpicture",addfilmpicture)
		filmpictureGroup.POST("/getfilmpictures",getfilmpictures)
	}

	r.Run(":9920")
}