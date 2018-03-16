Patent Download
=======
专利下载:中国专利信息下载(专利之星)

"PatentDown" (Download Chinese patent information) Download patents what you want!

由于作者Python水平限制，此项目现在已经不再提供维护，如果需要，可以使用patent-down项目（Java版本）非开源
====================

功能
=======
* 下载中国专利之星网站[patentStar](http://www.patentstar.cn/)上的专利信息
* 可指定默认的检索词,现阶段默认全局搜索,后期可能加上特定条件搜索
* 需要专利之星网站的账户,可在[patentStar](http://www.patentstar.cn/)注册(直接注册,无需其他条件).

环境
=======
* 所需依赖
	* 目前测试环境`Python 2.7.5, CentOS 7.1`
	* 需要
`re`,`cookielib`,`urllib`,`urllib2`,`optparse`,`bs4`,`sys`库(默认在`Python2.7.5`)
	* 需要`MySQLdb`库,使用`yum install MySQL-Python`安装
	* 需要MySQL数据库,默认数据库链接信息:
```
User:root
Password:root
DataBase:patent
IP:127.0.0.1
Port:3306
```


使用
======
1. 运行项目中SQL文件,在patent数据库中创建表
2. 使用`python patent2Db.py -u USERNAME -p PASSWORD -k KEYWORD`运行程序,其中`USERNAME`指patentStar网站的用户名,`KEYWORD`指patentStar网站用户名对应的密码,`KEYWORD`指定的关键词(需要使用`UTF-8`编码)

参与
======
* 任何意见与建议,欢迎联系<jliu666@hotmail.com>
* 欢迎大家参与到此项目中来

其他
======
如果认为此专利下载项目帮助到了你,欢迎`star`
