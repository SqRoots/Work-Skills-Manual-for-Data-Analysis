# Logistic 回归
> 一种非线性回归，多用于二分类变量分类，也用于多分类变量。

---

## 二分类 Logistic 回归
### 理论
如果直接估计样本所属类别的概率，会存在以下2个问题：
1. 	{% raw %}$p \in \left[ {0,1} \right]${% endraw %}，而样本的线性函数的值域一般为 {% raw %}$\left( { - \infty , + \infty } \right)${% endraw %}；
2.	概率$p$在 0 和 1 附近不够敏感。


考虑$p$的函数 {% raw %}$Q = f\left( p \right)${% endraw %}，如果令 {% raw %}$\frac{{dQ}}{{dp}} = \frac{1}{{p\left( {1 - p} \right)}}${% endraw %}，则可解决上面的两点不足。取$Q$为如下Logit变换即可满足上述条件：

{% raw %}
$$Q = \ln \frac{p}{{1 - p}}$$
{% endraw %}

其逆变换为：
{% raw %}
$$p = \frac{{{e^Q}}}{{1 + {e^Q}}} = \frac{1}{{1 + {e^{ - Q}}}}$$
{% endraw %}

这可样就把非线性回归问题转化为线性回归问题了，比如：
{% raw %}
$$\ln \frac{p}{{1 - p}} = Q = {\theta _0} + {\theta _1}{x_1} + {\theta _2}{x_2} +  \cdots  + {\theta _n}{x_n}$$
{% endraw %}

这样按照线性回归方法求解了，得到估计值$\hat Q$之后，再通过逆Logit变换即可得到$p$的估计值了。至于判定系数和显著性水平等指统计指标也可以一并得出。

或者用样本直接估计概率$p$：
{% raw %}
$$p = \frac{{{e^Q}}}{{1 + {e^Q}}} = \frac{{{e^{{\theta _0} + {\theta _1}{x_1} + {\theta _2}{x_2} +  \cdots  + {\theta _n}{x_n}}}}}{{1 + {e^{{\theta _0} + {\theta _1}{x_1} + {\theta _2}{x_2} +  \cdots  + {\theta _n}{x_n}}}}}$$
{% endraw %}

此式用于构造似然函数。
### 例：样本为已分组数据
所谓已分组数据，指每个样本对应一个概率值，所有样本对应的概率值之和等于1。例如，现有如下样本量为$m$，指标数量为$n$的样本：
{% raw %}
$$\left( {\begin{array}{*{20}{c}}
1&{{x_{11}}}&{{x_{12}}}& \cdots &{{x_{1n}}}& {{p_1}}\\
1&{{x_{21}}}&{{x_{22}}}& \cdots &{{x_{2n}}}& {{p_2}}\\
 \vdots & \vdots & \vdots & \ddots & \vdots &  \vdots \\
1&{{x_{m1}}}&{{x_{m2}}}& \cdots &{{x_{mn}}}& {{p_m}}
\end{array}} \right)$$
{% endraw %}

其中，$m\ge n$， {% raw %}$\sum\limits_{i=1}^{m}{{{p}_{i}}}=1${% endraw %}，为方便起见添加了第1列。则可以用其构造$n+1$元方程组：
{% raw %}
$$\left\{ {1{\theta _0} + {x_{i1}}{\theta _1} + {x_{i2}}{\theta _2} +  \cdots  + {x_{in}}{\theta _n} = \ln \frac{{{p_i}}}{{1 - {p_i}}}} \right. = {Q_i},\quad i = 1,2, \cdots ,m$$
{% endraw %}

记
{% raw %}${\bf{\theta }} = {\left( {{\theta _0},{\theta _1},{\theta _2}, \cdots ,{\theta _n}} \right)^T}${% endraw %}
，则将上式写成矩阵的形式为：
{% raw %}
$${\bf{X\theta }} = {\bf{Q}}$$
{% endraw %}

其中$\mathbf\{X\}$包含第1列中的1。记$\mathbf\{X\}$的广义逆矩阵为
{% raw %}
${{\bf{X}}^ + }: = {\left( {{{\bf{X}}^T}{\bf{X}}} \right)^{ - 1}}{{\bf{X}}^{^T}}$
{% endraw %}

上面的方程的最小二乘解为：
{% raw %}
$${\bf{\hat \theta }} = {{\bf{X}}^ + }{\bf{p}} = {\left( {{{\bf{X}}^T}{\bf{X}}} \right)^{ - 1}}{{\bf{X}}^{^T}}{\bf{p}}$$
{% endraw %}

### 例：样本为未分组变量
例如，现有如下样本量为$m$，指标数量为$n$的样本：
{% raw %}
$$\left( {\begin{array}{*{20}{c}}
1&{{x_{11}}}&{{x_{12}}}& \cdots &{{x_{1n}}}& {{y_1}}\\
1&{{x_{21}}}&{{x_{22}}}& \cdots &{{x_{2n}}}& {{y_2}}\\
 \vdots & \vdots & \vdots & \ddots & \vdots&  \vdots \\
1&{{x_{m1}}}&{{x_{m2}}}& \cdots &{{x_{mn}}}& {{y_m}}
\end{array}} \right)$$
{% endraw %}

其中，$m\ge n$， {% raw %}${y_i} \in \left\{ {0,1} \right\}${% endraw %}
。对于此种情况，一般使用极大似然方法求解。
记样本 {% raw %}${{\bf{x}}_i} = \left( {1,{x_{i1}},{x_{i2}}, \cdots ,{x_{in}}} \right)${% endraw %}，构造似然函数
{% raw %}${\mathop{\rm L}\nolimits} \left( {\bf{\theta }} \right) = \prod\limits_{i = 1}^m {\frac{{{e^{{\bf{\theta }}{{\bf{x}}_i}}}}}{{1 + {e^{{\bf{\theta }}{{\bf{x}}_i}}}}}} ${% endraw %}

，两边取对数得到：
{% raw %}
$${\bf{L}}: = \ln \left[ {{\mathop{\rm L}\nolimits} \left( {\bf{\theta }} \right)} \right] = \ln \left[ {\prod\limits_{i = 1}^m {\frac{{{e^{{\bf{\theta }}{{\bf{x}}_i}}}}}{{1 + {e^{{\bf{\theta }}{{\bf{x}}_i}}}}}} } \right] = \sum\limits_{i = 1}^m {\ln \left( {\frac{{{e^{{\bf{\theta }}{{\bf{x}}_i}}}}}{{1 + {e^{{\bf{\theta }}{{\bf{x}}_i}}}}}} \right)}  = \sum\limits_{i = 1}^m {{\bf{\theta }}{{\bf{x}}_i} - \ln \left( {1 + {e^{{\bf{\theta }}{{\bf{x}}_i}}}} \right)} $$
{% endraw %}

一般使用随机剃度下降法来计算 {% raw %}${\bf{\theta }}${% endraw %}
一般不取所有的样本，而是随机取一部分样本，记为 {% raw %}${{\bf{L}}^*}${% endraw %}，特别的，每次只随机取一个样本来计算梯度。修正公式如下：
 {% raw %}
$${{\bf{\theta }}^{\left( {k + 1} \right)}} = {{\bf{\theta }}^{\left( k \right)}} + \lambda {\nabla _{\bf{\theta }}}\left( {{{\bf{L}}^*}} \right)$$
 {% endraw %}

其中$\lambda $为步长，可理解为学习速率，{% raw %}${\nabla _{\bf{\theta }}}${% endraw %}是对似然函数${{\bf{L}}^*}$关于向量${\bf{\theta }}$的梯度算子。
