package dao

import (
	"douban/model"
)

// SelectFilmByFilmId 通过ID 搜film
func SelectFilmByFilmId(FilmId int)(model.Film,error){
	film:=model.Film{}
	sqlstr := "select name,directer,screenwriter,type,location,language,introduction,release_time,length,othername,IMDb,score,post_num,poster_url from film where film_id=?"
	//单行查询
	errs :=Db.QueryRow(sqlstr,FilmId)

	//错误处理
	if errs.Err()!=nil{
		return film, errs.Err()
	}
	err :=errs.Scan(&film.Name,&film.Directer,&film.Screenwriter,&film.Type,&film.Location,&film.Language,&film.Introduction,&film.ReleaseTime,&film.Length,&film.OtherName,&film.IMDb,&film.Score,&film.PostNum,&film.PosterUrl)
	if err != nil {
		return film, err
	}
	return film, nil
}

// InsertFim 添加film
func InsertFim(film model.Film)(error){
	if film.PosterUrl==""{
		film.PosterUrl="https://img2.baidu.com/it/u=3644629312,823020752&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500"
	}
	if film.Introduction==""{
		film.Introduction="暂时没有简介哦"
	}
	sqlstr :=" insert into film(name,directer,screenwriter,type,location,language,introduction,release_time,length,othername,IMDb,score,post_num,poster_url)values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
	_,err:=Db.Exec(sqlstr,film.Name,film.Directer,film.Screenwriter,film.Type,film.Location,film.Language,film.Introduction,film.ReleaseTime,film.Length,film.OtherName,film.IMDb,film.Score,film.PostNum,film.PosterUrl)
	if err!=nil{
		return err
	}
	return nil
}

func DeleteFilmById(film_id int) error {
	sqlstr:="delete from film where film_id=?"
	_,err:=Db.Exec(sqlstr,film_id)
	if err!=nil{
		return err
	}
	return nil
}

func SearchByName(name,aim string)([]model.Film,int,error){
	var u []model.Film=make([]model.Film,10000)
	var i=1
	var tag string
	//sqlstr:="select *from film where name like ?"

	////预处理
	//stmt, err := Db.Prepare(sqlstr)
	//if err != nil {
	//	return nil,0,err
	//}
	//defer stmt.Close()
	////

	//name="'%"+name+"%'"
	//fmt.Println(name)
	rows,errr:=Db.Query("select *from film where "+aim+" like '%"+name+"%'")
	if errr!=nil{
		return u,0,errr
	}
	defer rows.Close()
	for rows.Next() {
		errrr := rows.Scan(&u[i].Id,&u[i].Name, &u[i].Directer,&u[i].Screenwriter,&u[i].Type,&u[i].Location,&u[i].Language,&u[i].Introduction,&u[i].ReleaseTime,&u[i].Length,&u[i].OtherName,&u[i].IMDb,&u[i].Score,&u[i].PostNum,&u[i].PosterUrl,&tag)
		if errrr != nil {
			return u,0,errrr
		}
		i++
	}
	return u,i-1,nil
}

//UpdateScore 更新分数
func UpdateScore(score float32,film_id int)error{
	film,err:=SelectFilmByFilmId(film_id)
	if err!=nil{
		return err
	}

	//进行加权平均
	num:=film.PostNum+1
	oscore:=film.Score
	nscore:=float32((num-1)/num)*oscore+float32(1.00/num)*score

	sqlstr:="update film set post_num=?,score=?"
	_,errr:=Db.Exec(sqlstr,num,nscore)
	if err!=nil{
		return errr
	}
	return nil
}

func SuperSearch(sfilm model.Film)([]model.Film,int,error){
	var u =make([]model.Film,10000)
	var i=1
	var tag string
	rows,errr:=Db.Query("select film.film_id,film.name,film.directer,film.screenwriter,film.type ,film.location ,film.language ,film.introduction ,film.release_time ,film.length ,film.othername,film.IMDb,film.score,film.post_num,film.poster_url from film where exists (select *from shortpost where shortpost.tags like '%"+sfilm.Tag+ "%' and film.type like '%"+sfilm.Type+"%' and film.location like '%"+sfilm.Location+"%' and film.release_time like '%"+sfilm.ReleaseTime+"%')")
	if errr!=nil{
		return u,0,errr
	}
	defer rows.Close()
	for rows.Next() {
		errrr := rows.Scan(&u[i].Id,&u[i].Name, &u[i].Directer,&u[i].Screenwriter,&u[i].Type,&u[i].Location,&u[i].Language,&u[i].Introduction,&u[i].ReleaseTime,&u[i].Length,&u[i].OtherName,&u[i].IMDb,&u[i].Score,&u[i].PostNum,&u[i].PosterUrl,&tag)
		if errrr != nil {
			return u,0,errrr
		}
		i++
	}
	return u,i-1,nil
}

// GetFilmList 排行榜
func GetFilmList()([]model.Film,int,error){
	var u =make([]model.Film,10000)
	var i=1
	var tag string
	rows,errr:=Db.Query("select *from film order by score desc")
	if errr!=nil{
		return u,0,errr
	}
	defer rows.Close()
	for rows.Next() {
		errrr := rows.Scan(&u[i].Id,&u[i].Name, &u[i].Directer,&u[i].Screenwriter,&u[i].Type,&u[i].Location,&u[i].Language,&u[i].Introduction,&u[i].ReleaseTime,&u[i].Length,&u[i].OtherName,&u[i].IMDb,&u[i].Score,&u[i].PostNum,&u[i].PosterUrl,&tag)
		if errrr != nil {
			return u,0,errrr
		}
		i++
	}
	return u,i-1,nil
}