# SM3 Rho Attack  

**A.代码说明**  
	对SM3进行前16bit的攻击，根据Rho环路攻击原理可以更快找到碰撞  
  ![](https://github.com/Dumdiii/SM3/raw/master/rho_attack_SM3/png2.png))   
  在代码实现中参考Floyd判圈法  
  ```
  x=rand()
  h1 = SM3(x)
  h2 = SM3(h1)
  while(true)
    h1=SM3(h1)
    h2=SM3(SM3(h2)) //计算两次，因为如果成环，那么两倍速一定能追上一倍速的
    if h1 == h2:
        break  
  ```
  
**B.运行指导**  
	运行若成功会返回找到的碰撞hash值  
**C.代码运行截图**  
![](https://github.com/Dumdiii/SM3/raw/master/rho_attack_SM3/png1.png))  
**D.个人贡献说明**  
 本项目由李怡然完成
