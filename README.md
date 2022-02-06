# LeetCode-CN-Submissions-Crawler

## 概述

该工具用于爬取你在LeetCode-CN，即[力扣](https://leetcode-cn.com/)上所有的提交记录。

## 使用

下载[本仓库](https://github.com/siru-xiong/leetcode-solutions)下的[main](https://github.com/siru-xiong/leetcode-solutions/blob/main/main)和[config.json](https://github.com/siru-xiong/leetcode-solutions/blob/main/config.json)到本地，并放置在同一目录下。

修改`config.json`文件为以下格式
```
{
    "username": "your_username",
    "password": "your_passcode",
    "outputDir": "your_dir",
    "time": 1000
}
```
- `username`和`password`为你在LeetCode-CN的账号和密码
- `outputDir`为输出目录，爬取的提交记录将存储在该目录
- `time`为时间，程序将只爬取最近`time`天的提交记录

然后，运行`./main`，静静等待即可。

为了防止频繁请求造成连接断开，程序会不定时休眠20秒，保证稳定性。因网络原因导致的失败将会自动重试一次。

## 结果

对于同一题目的每种语言，将只爬取最近的提交。对每一次提交，将使用`序号-中文名称.后缀`的格式命名。

文件的抬头包括题目序号，题目中英文名称，题目链接，题目难度和提交语言。

样例结果见[本仓库](https://github.com/siru-xiong/leetcode-solutions)下的[solutions](https://github.com/siru-xiong/leetcode-solutions/tree/main/solutions)文件夹。
