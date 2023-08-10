def outer():
    data=0
    # 자신을 감싸고 있는 함수의 데이터를 수정하는 함수. 
    def inner():
        nonlocal data
        data+=1
        print(data) 
    
    return inner
closure=outer()
closure()
