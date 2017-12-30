登陆  
user/login    
post  
{"username":"xuyh",
"pwd":"aaa"}  
{
    "user": {
        "phone": "18758290214",
        "token": "2b687fbdad52459ab48027bb10d840c0",
        "username": "xuyh",
        "id": 1,
        "lv": 1
    },
    "msg_code": "001"
}  

修改手机 带token 
user/eidt_phone  
post  
{"phone":"13777777777"}  
{
    "status": "succeed"
}  

修改密码 带token  
user/edit_pwd  
post  
{
	"pwd":"bbb",
	"new_pwd":"aaa"
}  
{
    "status": "succeed"
}
