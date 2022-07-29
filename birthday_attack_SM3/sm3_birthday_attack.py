from gmssl import sm3,func
import random
import string


#生成随机字符串的hash值
def getRandomStr(n):
       for i in range(2**n):
              plain=''.join(random.sample(string.ascii_letters + string.digits, n))
              result = bytes(plain,encoding='utf-8')
              list_random.append(sm3.sm3_hash(func.bytes_to_list(result))[:int(n/2)])


def birthday_attack(n):
       num = 0
       for i in range(2**(n-1)):
              plain=''.join(random.sample(string.ascii_letters + string.digits, (n-1)))
              result = bytes(plain,encoding='utf-8')
              result = sm3.sm3_hash(func.bytes_to_list(result))[:int((n-1)/2)]
              num += 1
              if result in list_random: #与之前生成的随机字符串的hash值进行比较
                     print("攻击成功")
                     return(plain)
              if num > (2**(n-1)): #没有找到碰撞
                     break
       print("攻击失败")


if __name__ == '__main__':
       n=16
       list_random=[]
       getRandomStr(n-1)
       plain=birthday_attack(n)
       print('plain:',plain)
