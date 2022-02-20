package service

import (
	"database/sql"
	"douban/dao"
)

func AddFilmPicture(filmId int,url string)error{
	return dao.InsertFimPicture(filmId,url)
}

func GetFilmPicture(filmId int)([]string,int,error){
	filmpictures,num,err:=dao.SelectFilmPicturesByFilmId(filmId)
	if err!=nil&&err!=sql.ErrNoRows{
		return filmpictures,num,err
	}
	return filmpictures,num,nil
}
