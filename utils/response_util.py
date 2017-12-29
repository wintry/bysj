

SUCCESS = ''

def success(message= None,**kw):
    return ret(SUCCESS,message,**kw)

def ret(type,message= None,**kw):
    ret = {}
    aret = {}
    ret['msg_code'] = type
    if message:
        ret['message'] = message
    if kw:
        for k, v in kw.items():
            # 判断v是否是对象
            if isinstance(v, dict):
                for kk, vv in v.items():
                    aret[kk] = vv
                ret[k] = aret
            else:
                ret[k] = v
    return ret


