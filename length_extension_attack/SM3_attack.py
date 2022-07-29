import SM3
import math
def SM3_attack(message,extend):
    hm = SM3.SM3(message)
    e = bin(int(extend, 16))[2:]
    if len(e) != len(extend) * 4:
        e = '0' * (len(extend) * 4 - len(e)) + e
    ## 计算m_new的长度
    l_e = len(e)
    m = bin(int(message, 16))[2:]
    if len(m) != len(message) * 4:
        m = '0' * (len(message) * 4 - len(m)) + m
    l_m_padding = math.ceil(len(m)/512)*512
    l = l_e + l_m_padding #+ 64
    l_bin = '0' * (64 - len(bin(l)[2:])) + bin(l)[2:]
    ##extension消息填充
    e = e + '1'
    e = e + '0' * (448 - len(e) % 512) + l_bin
    e = hex(int(e, 2))[2:]
    # print("填充后的消息为:", e)
    ##消息分组
    E = SM3.Group(e)
    ##处理Hm,使其继续输入
    Hm = []
    for i in range(8):
        Hm.append(int(hm[i * 8:i * 8 + 8], 16))
    ##迭代压缩
    n = len(E)
    V = []
    V.append(Hm)
    for i in range(n):
        V.append(SM3.CF(V, E, i))
    ##最终结果hash值
    result = ''
    for x in V[n]:
        result += (hex(x)[2:])
    return result



