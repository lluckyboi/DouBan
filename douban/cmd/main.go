package main

import (
	"douban/api"
	"douban/dao"
)

func main() {
	//r := gin.Default()
	//// 部署前端静态网站
	//r.Use(static.Serve("/", static.LocalFile("/source", false)))
	//先连接数据库
	dao.RUNDB()
	//启动引擎
	api.RUNENGINE()
}