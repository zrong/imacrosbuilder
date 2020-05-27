用于将结构化表格转换成 [iMacros](https://imacros.net/) 的宏

imacros 用于 http://www.hbwhrd.org/index.aspx 网站的税务研发加计扣除。

使用说明：

1. 登录 http://www.hbwhrd.org/index.aspx 系统，并打开提交页面，生成
2. 按照下面的 CSV 格式创建 CSV，保存为 `Q1.csv/Q2.csv/Q3.csv` ，每个季度一个 CSV 文件；
3. 运行 convert.py 生成 `Q1.macro/Q2.macro/Q3.macro` ；
4. iMacros 免费版限制 50 行宏，因此需要手动分割文件，修改 convert.py 即可。


``` CSV
NUM,xingming:TEXT,shenfenzheng:TEXT,xingbie:SELECT,nianling:TEXT,xueli:SELECT,zhuanye:TEXT,cszy:TEXT,zhicheng:TEXT,bumen:TEXT,cdgz:TEXT
1,张三,422201200003030033,男,20,本科,软件工程,软件测试,产品经理,产品组,负责人
```