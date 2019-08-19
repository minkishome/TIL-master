def add(x,y):
    return x+y


def sub(x, y):
    return x - y
    
def mul(x,y):
    return x*y

def div(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return '0으로 나눌 수 없음'

#만약 정확하게 이 파일을 실행했을 때만, 실행되면 좋겠다.
# python calc.py

if __name__ == '__main__':
    print(add(1,2))
    print(div(1,0))