package service

import (
	"database/sql"
	"douban/dao"
	"douban/model"
)

// 0密码错误 1密码正确 2用户不存在
func IsPasswordCorrectAndUsernameExist(username, password string) (int, error) {
	user, err := dao.SelectUserByUsername(username)
	if err != nil {
		if err == sql.ErrNoRows {
			return 2, nil
		}
		return 0, err
	}
	if user.Password != password {
		return 0, nil
	}
	return 1, nil
}

func IsUsernameRepeat(username string)(bool,error){
	user,err :=dao.SelectUsernameByUsername(username)
	if err != nil {
		if err == sql.ErrNoRows {
			return true, nil
		}
		return false, err
	}

	if user.Username!=username{
		return true,nil
	}
		return false,nil
}

func NewUser(user model.User) error {
	err := dao.NewUser(user)
	return err
}

func NewPassword(username,newpassword string)(bool,error){
	err :=dao.Newpassword(username,newpassword)
	if err!=nil{
		return  false,err
	}
	return true,nil
}

func IsPasswordQuesOk(username,ans1,ans2 string)(bool ,error,string){
	user,err :=dao.SelectQuesAndPasswordByUsername(username)
	if err != nil {
		if err == sql.ErrNoRows {
			return false, nil ,""
		}
		return false, err ,""
	}
	if ans1==user.Ans1&&ans2==user.Ans2{
		return true,nil,user.Password
	}
		return false,nil,""
}

func GetQuesByUsername(username string)(string,string,error){
	ques1,ques2,err:=dao.SelectQuesByUsename(username)
	if err!=nil{
		return "", "", err
	}
	return ques1,ques2,nil
}

func GetUsernameById(id int)(string,bool,error){
	username,err:=dao.SelectUsernameById(id)
	if err!=nil{
		if err==sql.ErrNoRows{
			return "",false,nil
		}
		return "",false,err
	}
	return username,true,nil
}

func GetUserWatchedByUsername(username string)([]int,int,error){
	ids,num,err:= dao.SelectFilmIdUserWatchedByUsername(username)
	if err==nil||err==sql.ErrNoRows{
		return ids,num,nil
	}
	return ids,num,err
}

func GetUserWantByUsername(username string)([]int,int,error){
	ids,num,err:= dao.SelectFilmIdUserWantByUsername(username)
	if err==nil||err==sql.ErrNoRows{
		return ids,num,nil
	}
	return ids,num,err
}

func AddIntroduction(username ,introduction string)error{
	return dao.UpdateIntroduction(username,introduction)
}

func UpdatePortrait(portrait ,username string)error{
	return dao.UpdatePortrait(portrait,username)
}

func GetUserIPIPByUsername(username string)(model.User,error){
	return dao.SelectUserByUsername(username)
}