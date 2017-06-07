# Logistic 回归
> 一种非线性回归，多用于二分类变量分类，也用于多分类变量。

---

## 二分类 Logistic 回归
### 理论
如果直接估计样本所属类别的概率，会存在以下2个问题：
1. 	$p\\in \\left[ 0,1 \\right]$，而样本的线性函数的值域一般为$\\left( -\\infty ,+\\infty  \\right)$；
2.	概率$p$在0和1附近不够敏感。


考虑$p$的函数$Q=f\\left( p \\right)$，如果令$\\frac{dQ}{dp}=\\frac{1}{p\\left( 1-p \\right)}$，则可解决上面的两点不足。取$Q$为如下Logit变换即可满足上述条件：

{% raw %}
\\[
Q=\\ln \\frac{p}{1-p}
\\]
{% endraw %}


其逆变换为：
{% raw %}
\\[
p=\\frac{{{e}^{Q}}}{1+{{e}^{Q}}}=\\frac{1}{1+{{e}^{-Q}}}
\\]
{% endraw %}

这可样就把非线性回归问题转化为线性回归问题了，比如：
{% raw %}
\\[
\\ln \\frac{p}{1-p}=Q={{\\theta }_{0}}+{{\\theta }_{1}}{{x}_{1}}+{{\\theta }_{2}}{{x}_{2}}+\\cdots +{{\\theta }_{n}}{{x}_{n}}
\\]
{% endraw %}

这样按照线性回归方法求解了，得到估计值$\\hat{Q}$之后，再通过逆Logit变换即可得到$p$的估计值了。至于判定系数和显著性水平等指统计指标也可以一并得出。

或者用样本直接估计概率$p$：
{% raw %}
\\[
p=\\frac{{{e}^{Q}}}{1+{{e}^{Q}}}=\\frac{{{e}^{{{\\theta }_{0}}+{{\\theta }_{1}}{{x}_{1}}+{{\\theta }_{2}}{{x}_{2}}+\\cdots +{{\\theta }_{n}}{{x}_{n}}}}}{1+{{e}^{{{\\theta }_{0}}+{{\\theta }_{1}}{{x}_{1}}+{{\\theta }_{2}}{{x}_{2}}+\\cdots +{{\\theta }_{n}}{{x}_{n}}}}}
\\]
{% endraw %}

此式用于构造似然函数。

### 例：样本为已分组数据
所谓已分组数据，指每个样本对应一个概率值，所有样本对应的概率值之和等于1。例如，现有如下样本量为$m$，指标数量为$n$的样本：
{% raw %}
\\[
\\left( \\begin{matrix}
 1 & {{x}_{11}} & {{x}_{12}} & \\cdots  & {{x}_{1n}} & {{p}_{1}}  \\\\
 1 & {{x}_{21}} & {{x}_{22}} & \\cdots  & {{x}_{2n}} & {{p}_{2}}  \\\\
 \\vdots  & \\vdots  & \\vdots  & \\ddots  & \\vdots  & \\vdots   \\\\
 1 & {{x}_{m1}} & {{x}_{m2}} & \\cdots  & {{x}_{mn}} & {{p}_{m}}  \\\\
\\end{matrix} \\right)
\\]
{% endraw %}

其中，$m\\ge n$，{% raw %}
\$\$
\\sum\\limits_{i=1}^{m}{{{p}_{i}}}=1
\$\$
{% endraw %}
，为方便起见添加了第1列。则可以用其构造$n+1$元方程组：
{% raw %}
\\[
\\left\\{ 1{{\\theta }_{0}}+{{x}_{i1}}{{\\theta }_{1}}+{{x}_{i2}}{{\\theta }_{2}}+\\cdots +{{x}_{in}}{{\\theta }_{n}}=\\ln \\frac{{{p}_{i}}}{1-{{p}_{i}}} \\right.={{Q}_{i}},\\quad i=1,2,\\cdots ,m
\\]
{% endraw %}

记
{% raw %}
\$\$
\\mathbf{\\theta }={{\\left( {{\\theta }_{0}},{{\\theta }_{1}},{{\\theta }_{2}},\\cdots ,{{\\theta }_{n}} \\right)}^{T}}
\$\$
{% endraw %}
，则将上式写成矩阵的形式为：
{% raw %}
\$\$
\\mathbf{X\\theta }=\\mathbf{Q}
\$\$
{% endraw %}

其中$\\mathbf{X}$包含第1列中的1。记$\\mathbf{X}$的广义逆矩阵为{% raw %}
\$\$
{{\\mathbf{X}}^{\\dagger }}:={{\\left( {{\\mathbf{X}}^{T}}\\mathbf{X} \\right)}^{-1}}{{\\mathbf{X}}^{^{T}}}
\$\$
{% endraw %}
上面的方程的最小二乘解为：
{% raw %}
\\[
\\mathbf{\\hat{\\theta }}={{\\mathbf{X}}^{\\dagger }}\\mathbf{p}={{\\left( {{\\mathbf{X}}^{T}}\\mathbf{X} \\right)}^{-1}}{{\\mathbf{X}}^{^{T}}}\\mathbf{p}
\\]
{% endraw %}

### 例：样本为未分组变量
例如，现有如下样本量为$m$，指标数量为$n$的样本：
{% raw %}
\\[
\\left( \\begin{matrix}
 1 & {{x}_{11}} & {{x}_{12}} & \\cdots  & {{x}_{1n}} & {{y}_{1}}  \\\\
 1 & {{x}_{21}} & {{x}_{22}} & \\cdots  & {{x}_{2n}} & {{y}_{2}}  \\\\
 \\vdots  & \\vdots  & \\vdots  & \\ddots  & \\vdots  & \\vdots   \\\\
 1 & {{x}_{m1}} & {{x}_{m2}} & \\cdots  & {{x}_{mn}} & {{y}_{m}}  \\\\
\\end{matrix} \\right)
\\]
{% endraw %}

其中，$m\\ge n${% raw %}，
\$\$
{{y}_{i}}\\in \\left\\{ 0,1 \\right\\}
\$\$
{% endraw %}
。对于此种情况，一般使用极大似然方法求解。
记样本{% raw %}
\$\$
{{\\mathbf{x}}_{i}}=\\left( 1,{{x}_{i1}},{{x}_{i2}},\\cdots ,{{x}_{in}} \\right)
\$\$
{% endraw %}
，构造似然函数{% raw %}
\$\$
\\operatorname{L}\\left( \\mathbf{\\theta } \\right)=\\prod\\limits_{i=1}^{m}{\\frac{{{e}^{\\mathbf{\\theta }{{\\mathbf{x}}_{i}}}}}{1+{{e}^{\\mathbf{\\theta }{{\\mathbf{x}}_{i}}}}}}
\$\$
{% endraw %}
，两边取对数得到：
{% raw %}
\\[
\\mathbf{L}:=\\ln \\left[ \\operatorname{L}\\left( \\mathbf{\\theta } \\right) \\right]=\\ln \\left[ \\prod\\limits_{i=1}^{m}{\\frac{{{e}^{\\mathbf{\\theta }{{\\mathbf{x}}_{i}}}}}{1+{{e}^{\\mathbf{\\theta }{{\\mathbf{x}}_{i}}}}}} \\right]=\\sum\\limits_{i=1}^{m}{\\ln \\left( \\frac{{{e}^{\\mathbf{\\theta }{{\\mathbf{x}}_{i}}}}}{1+{{e}^{\\mathbf{\\theta }{{\\mathbf{x}}_{i}}}}} \\right)}=\\sum\\limits_{i=1}^{m}{\\mathbf{\\theta }{{\\mathbf{x}}_{i}}-\\ln \\left( 1+{{e}^{\\mathbf{\\theta }{{\\mathbf{x}}_{i}}}} \\right)}
\\]
{% endraw %}

一般使用随机剃度下降法来计算{% raw %}
\$\$
\mathbf{\\theta }\]，这时\[\\mathbf{L}
\$\$
{% endraw %}
一般不取所有的样本，而是随机取一部分样本，记为{% raw %}
\$\$
{{\\mathbf{L}}^{*}}
\$\$
{% endraw %}
 ，特别的，每次只随机取一个样本来计算梯度。修正公式如下：
 {% raw %}
 \\[
 {{\\mathbf{\\theta }}^{\\left( k+1 \\right)}}={{\\mathbf{\\theta }}^{\\left( k \\right)}}+\\lambda {{\\nabla }_{\\mathbf{\\theta }}}\\left( {{\\mathbf{L}}^{*}} \\right)
 \\]
 {% endraw %}

其中$\\lambda $为步长，可理解为学习速率，{% raw %}
\$\$
{{\\nabla }_{\\mathbf{\\theta }}}
\$\$
{% endraw %}
是对似然函数{% raw %}
\$\$
{{\\mathbf{L}}^{*}}
\$\$
{% endraw %}
关于向量{% raw %}
\$\$
\mathbf{\\theta }
\$\$
{% endraw %}
的梯度算子。

----

{% raw %}
\\[
\\left( \\begin{matrix}   1 & {{x}_{11}} & {{x}_{12}} & \\cdots  & {{x}_{1n}} & {{y}_{1}}  \\\\   1 & {{x}_{21}} & {{x}_{22}} & \\cdots  & {{x}_{2n}} & {{y}_{2}}  \\\\   \\vdots  & \\vdots  & \\vdots  & \\ddots  & \\vdots  & \\vdots   \\\\   1 & {{x}_{m1}} & {{x}_{m2}} & \\cdots  & {{x}_{mn}} & {{y}_{m}}  \\\\ \\end{matrix} \right)
\\]
{% endraw %}

{% raw %}
\\[
\\left( \\begin{matrix}
 1 & {{x}_{11}} & {{x}_{12}} & \\cdots  & {{x}_{1n}} & {{y}_{1}}  \\\\
 1 & {{x}_{21}} & {{x}_{22}} & \\cdots  & {{x}_{2n}} & {{y}_{2}}  \\\\
 \\vdots  & \\vdots  & \\vdots  & \\ddots  & \\vdots  & \\vdots   \\\\
 1 & {{x}_{m1}} & {{x}_{m2}} & \\cdots  & {{x}_{mn}} & {{y}_{m}}  \\\\
\\end{matrix} \\right)
\\]
{% endraw %}
