import SM3
import SM3_attack

message = '91623'   # 原始消息
extension = '12355' # 扩展字段
message_new = ''
hash_attack = SM3_attack.SM3_attack(message,extension)  #长度扩展攻击得到的hash值
message = SM3.Fill(message)
message_new = message + extension   #原始消息与扩展字段组成的新的消息
hash_new = SM3.SM3(message_new)     #SM3压缩新的消息得到的hash值
print('正确hash值：',hash_new)
print('攻击hash值：',hash_attack)
