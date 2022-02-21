package main

import (
	"douban/api"
	"douban/dao"
)

func main() {
	//先连接数据库
	dao.RUNDB()
	//启动引擎
	api.RUNENGINE()
}
