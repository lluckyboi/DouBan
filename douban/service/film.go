package service

import (
	"douban/dao"
	"douban/model"
)

func GetFilmByFilmId(FilmId int)(model.Film,error){
	return dao.SelectFilmByFilmId(FilmId)
}

func AddFilm(film model.Film)(error){
	return dao.InsertFim(film)
}

func DeletFilm(FilmId int)error{
	return dao.DeleteFilmById(FilmId)
}

func Searchfilm(txt,aim string)([]model.Film,int,error){
	return dao.SearchByName(txt,aim)
}

// NewScore 更新平均分和评论人数
func NewScore(score	float32,filmid int)error{
	return dao.UpdateScore(score,filmid)
}

func SuperSearch(sfilm model.Film)([]model.Film,int,error){
	return dao.SuperSearch(sfilm)
}

//排行榜
func GetFilmList()([]model.Film,int,error){
	return dao.GetFilmList()
}