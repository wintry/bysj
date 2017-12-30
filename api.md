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

添加测试人员 带token  
user/add_user  
post  
{
	"username":"yjg",
	"pwd":"bbb",
	"phone":"18777777777"
}  
{
    "status": "succeed"
}


添加缺陷管理员 带token  
user/add_user_two  
post  
{
	"username":"yjg1",
	"pwd":"bbb",
	"phone":"18777777777"
}  
{
    "status": "succeed"
}  

添加产品 带token  
product/add_product  
post  
{
	"name":"sony ps4"
}  
{
    "status": "succeed"
}  


修改产品和产品节点  带token 
/product/edit_product  
post 
{
	"name":"sony ps4 pro"
	"product_id":1
}  
{
    "status": "succeed"
}   


添加产品节点 带token  
/product/add_line  
post  
{
	"name":"sony ps4 slim"
	"product_id":1   产品的id
}  
{
    "status": "succeed"
}  

删除产品和节点 带token  
/product/del_product
post  
{
	
	"product_id":1
}  
{
	
	"product_id":1
}  

根据产品id获得节点 带token  
/product/get_line  
post  
{
	
	"product_id":1
}  

{
    "product": [
        {
            "name": "ps4",
            "fid": 1,
            "id": 2
        },
        {
            "name": "ps4 slim",
            "fid": 1,
            "id": 3
        },
        {
            "name": "ps4 pro",
            "fid": 1,
            "id": 4
        }
    ],
    "msg_code": "001"
}

