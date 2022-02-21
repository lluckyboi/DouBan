package service

import (
	"douban/dao"
	"douban/model"
)

func AddAct(act model.Act)error{
	return dao.InsertAct(act)
}
