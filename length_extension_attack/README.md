<<<<<<< Updated upstream
**A 项目代码说明**：

  SM3.py：SM3算法

  SM3_attack.py: 对SM3算法进行长度扩展攻击，根据原始字串m，扩展字串e，实现：对扩展字串e补1和0进行消息填充；计算新消息M的长度，M=m||10...||len(m)||e;利用hash(m)与e||10...||len(M)
继续迭代压缩，计算出攻击结果

  test.py : 输入原始字串m，扩展字串e，得到新消息M，计算正确的hash即SM3(M)，然后调用长度扩展攻击程序，计算攻击得到的hash，输出两个hash值，比较是否相等

**B 运行指导：**

  运行test，观察输出的两个hash值

**C 代码过程截图：**

![image](https://github.com/Dumdiii/SM3/blob/master/length_extension_attack/result.png)

**D 贡献说明：**

完成人：李美琳 独自完成
>>>>>>> Stashed changes
