# 贝塞尔曲线和 B-样条曲线

[详解样条曲线（上）（包含贝塞尔曲线）-CSDN 博客](https://blog.csdn.net/deepsprings/article/details/107828889)
[样条曲线(下)之插值问题(贝塞尔曲线、B 样条和一般样条曲线插值)\_b 样条插值-CSDN 博客](https://blog.csdn.net/deepsprings/article/details/107881698)
[贝塞尔曲线与 B 样条 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/369753167)

---

## 以我的理解推导 B-样条曲线

## 参考资料

### B 样条（上）

先介绍几个概念，容易混淆的概念：
![](pic/Pasted%20image%2020240402163819.png)
![](https://img-blog.csdnimg.cn/20200806001326759.png)
![](pic/Pasted%20image%2020240402163956.png)
我们的目标是得到控制点对应的权重
![](pic/Pasted%20image%2020240402164125.png)
![](https://img-blog.csdnimg.cn/20200806001338484.png)
![](pic/Pasted%20image%2020240402164612.png)
![](https://img-blog.csdnimg.cn/20200806001352787.png)
k=1 时候：
![](https://img-blog.csdnimg.cn/2020080600143221.png)
利用递推式求解 k=2、3、4。。。。。。
![](https://img-blog.csdnimg.cn/20200806001447169.png)
![](pic/Pasted%20image%2020240402165202.png)

### B 样条（下）

前篇中在尝试各种节点列表时，得到了很多结果，但对结果总结分析较少，以下是一些**非常重要的**小总结和补充：
![](pic/Pasted%20image%2020240402172346.png)
![](pic/Pasted%20image%2020240402172554.png)
![](pic/Pasted%20image%2020240402172703.png)

#### 三次 clamped B-样条

![](pic/Pasted%20image%2020240402193745.png)
![](https://img-blog.csdnimg.cn/20200808162750593.png)
![](pic/Pasted%20image%2020240402193834.png)
![](pic/Pasted%20image%2020240402193911.png)

#### B 样条插值方程的获取与求解
