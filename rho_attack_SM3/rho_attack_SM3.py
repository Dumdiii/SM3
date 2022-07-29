from gmssl import sm3,func
import random
import string


#生成随机字符串的hash值
def getRandomStr(n):
       for i in range(2**n):
              plain=''.join(random.sample(string.ascii_letters + string.digits, n))
              result = bytes(plain,encoding='utf-8')
              list_random.append(sm3.sm3_hash(func.bytes_to_list(result))[:int(n/2)])


def rho_attack(n):
       
       
       str_random=''.join(random.sample(string.ascii_letters + string.digits, (n-1)))
       plain = bytes(plain,encoding='utf-8')
       h1 = sm3.sm3_hash(func.bytes_to_list(plain))[:int((n-1)/2)]
       h2 = sm3.sm3_hash(h1)[:int((n-1)/2)]
       while True:
              h1 = sm3.sm3_hash(h1)[:int((n-1)/2)]
              h2 = sm3.sm3_hash(sm3.sm3_hash(h2)[:int((n-1)/2)])[:int((n-1)/2)]
              if h1 == h2:
                     print("攻击成功")
                     break
              
if __name__ == '__main__':
       n=16
       rho_attack(n)
       
