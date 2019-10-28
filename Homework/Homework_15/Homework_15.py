def get_1():
    import requests
    res = requests.request("GET","https://httpbin.org/bytes/10")
    return res.status_code,res.content

def get_2():
    import requests
    a = "1"
    res = requests.request("GET","https://httpbin.org/cookies/set", data = a)
    return res.status_code, res.content

def get_3():
    import requests
    res = requests.request("GET","https://httpbin.org/image/svg")
    return res.status_code, res.content

def get_4():
    import requests
    res = requests.request("GET","https://httpbin.org/redirect/10")
    return res.status_code, res.content

def get_5():
    import requests
    a = {}
    a["File"] = "[10,20,30,40]"
    res = requests.request("GET", "https://httpbin.org/anything", data=a)
    return res.status_code, res.content

def post_1():
    import requests
    res = requests.request("POST","https://httpbin.org/status/302")
    return res.status_code, res.content

def post_2():
    import requests
    a = {}
    a["Learning Languge"] = "Python"
    res = requests.request("POST","https://httpbin.com/anything",data = a)
    return res.status_code, res.content

def post_3():
    import requests
    res = requests.request("POST","https://httpbin.com/redirect-to/302/303")
    return res.status_code, res.content

def post_4():
    import requests
    res = requests.request("POST","https://httpbin.com/delay/3")
    return res.status_code, res.content


def post_5():
    import requests
    res = requests.request("POST","https://httpbin.com/response-headers")
    return res.status_code, res.content


def delete_1():
    import requests
    res = requests.request("DELETE","https://httpbin.com/status/200")
    return res.status_code, res.content


def delete_2():
    import requests
    res = requests.request("DELETE","https://httpbin.com/delay/6")
    return res.status_code, res.content

def delete_3():
    import requests
    res = requests.request("DELETE","https://httpbin.com/redirect-to/302/304")
    return res.status_code, res.content


def delete_4():
    import requests
    res = requests.request("DELETE","https://httpbin.com/anything/101")
    return res.status_code, res.content

def delete_5():
    import requests
    res = requests.request("DELETE","https://httpbin.com/delete")
    return res.status_code, res.content

def put_1():
    import requests
    res = requests.request("PUT","https://httpbin.com/put")
    return res.status_code, res.content

def put_2():
    import requests
    res = requests.request("PUT","https://httpbin.com/status/404")
    return res.status_code, res.content

def put_3():
    import requests
    res = requests.request("PUT","https://httpbin.com/delay/7")
    return res.status_code, res.content

def put_4():
    import requests
    res = requests.request("PUT","https://httpbin.com/redirect-to/302/306")
    return res.status_code, res.content

def put_5():
    import requests
    a = {}
    a["surname"] = "Gasparyan"
    res = requests.request("PUT","https://httpbin.com/anything",data = a)
    return res.status_code, res.content