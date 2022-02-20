package dao

import "douban/model"

// SelectQuesAndPasswordByUsername 通过密保找回密码模块
func SelectQuesAndPasswordByUsername(username string)(model.User,error){
	user :=model.User{}
	sqlstr :="select ans1,ans2,password from user where username=?"
	errs :=Db.QueryRow(sqlstr,username)
	//Err provides a way for wrapping packages to check for query errors without calling Scan.
	if errs.Err() != nil {
		return user, errs.Err()
	}
	//扫进user
	err := errs.Scan(&user.Ans1,&user.Ans2,&user.Password)
	if err != nil {
		return user, err
	}
	return user, nil
}

// SelectUserByUsername 信息查询
func SelectUserByUsername(username string)(model.User,error) {
	user :=model.User{}
	sqlstr := "select id,password,introduction,picture_url from user where username=?"
	//单行查询
	errs :=Db.QueryRow(sqlstr,username)

	//错误处理
	if errs.Err()!=nil{
		return user, errs.Err()
	}
	err :=errs.Scan(&user.Id,&user.Password,&user.Introduction,&user.PictureUrl)
	if err != nil {
		return user, err
	}
	return user, nil
}

// SelectUsernameByUsername 用户名查重
func SelectUsernameByUsername(username string)(model.User,error){
	user :=model.User{}
	sqlstr :="select username from user where username=?"
	errs :=Db.QueryRow(sqlstr,username)
	if errs.Err() != nil {
		return user, errs.Err()
	}
	err := errs.Scan(&user.Username)
	if err != nil {
		return user, err
	}
	return user, nil
}

// SelectQuesByUsename 得到密保问题
func SelectQuesByUsename(username string)(string,string,error){
	user :=model.User{}
	sqlstr :="select ques1,ques2 from user where username=?"
	errs :=Db.QueryRow(sqlstr,username)
	if errs.Err() != nil {
		return "","", errs.Err()
	}
	err := errs.Scan(&user.Ques1,&user.Ques2)
	if err != nil {
		return "","", err
	}
	return user.Ques1,user.Ques2,nil
}

// NewUser 注册账户
func NewUser(user model.User)(error){
	sqlstr:="insert into user(username,password,ques1,ques2,ans1,ans2)values(?,?,?,?,?,?);"
	_, errs :=Db.Exec(sqlstr,user.Username,user.Password,user.Ques1,user.Ques2,user.Ans1,user.Ans2)
	if errs!=nil{
		return errs
	}
	return nil
}

// Newpassword 修改密码
func Newpassword(username,newpassword string)(error){
	user:=model.User{}
	sqlstr :="select password from user where username=?"
	errs :=Db.QueryRow(sqlstr,username)
	if errs.Err() != nil {
		return errs.Err()
	}
	err := errs.Scan(&user.Password)
	if err != nil {
		return err
	}

	sqlstr ="UPDATE user SET password=? WHERE username =?"
	_,err=Db.Exec(sqlstr,newpassword,username)
	if err!=nil{
		return err
	}
	return nil
}

// SelectUsernameById 获取用户名
func SelectUsernameById(id int)(string,error){
	var username string
	err:=Db.QueryRow("select *from user where id=?",id).Scan(&username)
	if err!=nil{
		return "",err
	}
	return username,nil
}

func SelectFilmIdUserWatchedByUsername(username string)([]int,int,error){
	var ids []int
	var num=0
	rows, err := Db.Query("SELECT film_id FROM shortpost WHERE username = ? and watched=1", username)
	if err != nil {
		return nil,num, err
	}

	defer rows.Close()
	for rows.Next() {
		var id int
		err = rows.Scan(&id)
		if err != nil {
			return nil,num, err
		}
		ids=append(ids,id)
		num++
	}
	return ids, num,nil
}

func SelectFilmIdUserWantByUsername(username string)([]int,int,error){
	var ids []int
	var num=0
	rows, err := Db.Query("SELECT film_id FROM shortpost WHERE username = ?&& want=1", username)
	if err != nil {
		return nil,num, err
	}

	defer rows.Close()
	for rows.Next() {
		var id int
		err = rows.Scan(&id)
		if err != nil {
			return nil,num, err
		}
		ids=append(ids,id)
		num++
	}
	return ids, num,nil
}

func UpdateIntroduction(username,introduction string)error{
	sqlstr:="update user set introduction=? where username=?"
	_,err:=Db.Exec(sqlstr,introduction,username)
	return err
}

func UpdatePortrait(portrait,username string)error{
	sqlstr:="update user set picture_url=? where username=?"
	_,err:=Db.Exec(sqlstr,portrait,username)
	return err
}