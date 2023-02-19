## 商城自动化测试脚本
### 自动化框架
pytest + request + yaml +allure

### 测试项目
本自动化脚本基于[新蜂商城](https://github.com/newbee-ltd/newbee-mall-api-go) 接口，
你可以按照项目的搭建方法本地搭建测试项目，或者直接使用公司项目的接口

### 分支说明
每个分支对应不同的实战内容，建议切换不同的分支以对应教程内容

分支名     | 自动化内容说明 |教程地址
-------- | ----- | -----
master | 最新项目代码|
single_interface  | 无需登陆的独立
auth_interface | 需要登陆的独立接口
order_process | 下单业务流程
mysql_assert | mysql断言使用
public | 项目公共部分封装
data_driven | 数据驱动封装
add_interface |增量用例添加

### 参考项目
[pytestDemo
Public](https://github.com/wintests/pytestDemo)
