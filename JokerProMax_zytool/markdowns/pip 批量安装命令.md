### 日期：2020-12-16

#### 要义：因为 pip 版本问题会导致生成的 requirements.txt 中有些第三方库的版本变成 @ file 路径，因此需要使用以下命令进行规避：

```shell
pip list --format=freeze > requirements.txt
```

#### 具体原因：

##### 因为在 pip 19.1 以后的版本以后 PEP404 规范，因此仅能在本地文件系统中使用并不能供别人使用