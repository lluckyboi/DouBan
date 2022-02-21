package dao
import (
	"database/sql"
	_ "github.com/go-sql-driver/mysql"
	"log"
)

// Db 全局变量
var Db *sql.DB

func RUNDB() {
	//启用数据库
	db, err := sql.Open("mysql", "douban:Tkx2636kYDFkp3c2@/douban")
	if err != nil {
		log.Fatal(err)
	}
	Db=db
}
