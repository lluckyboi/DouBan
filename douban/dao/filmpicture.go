package dao

func InsertFimPicture(filmId int,url string)error{
	sqlstr:="insert into filmpicture(film_id,url)values(?,?)"
	_,err:=Db.Exec(sqlstr,filmId,url)
	if err!=nil{
		return err
	}
	return nil
}

func SelectFilmPicturesByFilmId(filmId int)([]string,int,error){
	var filmpictures []string
	var num=0
	rows,errr:=Db.Query("select url from filmpicture where film_id=?",filmId)
	if errr!=nil{
		return nil,num,errr
	}
	defer rows.Close()
	for rows.Next() {
		var filmpicture string
		errrr := rows.Scan(&filmpicture)
		if errrr != nil {
			return nil,num,errrr
		}
		filmpictures=append(filmpictures,filmpicture)
		num++
	}
	return filmpictures,num,nil
}