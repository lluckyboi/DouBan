package tool
func StringTOInt(number string)int{
	len:= len(number)
	var trannum int=0
	for i:=0;i<len;i++{
		trannum=trannum*10+int(number[i]-'0')
	}
	return trannum
}
func StringToFloat2_1(number string)float32{
	var trannum float32
	trannum=float32(number[0]-'0') +0.1*float32(number[2]-'0')
	return trannum
}