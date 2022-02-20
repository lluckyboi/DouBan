package main

import (
	"douban/api"
	"douban/dao"
)

func main() {
	//先连接数据库
	dao.RUNDB()
	// 部署前端静态网站
	r.Use(static.Serve("/", static.LocalFile("./static", false)))
	//启动引擎
	api.RUNENGINE()
}
