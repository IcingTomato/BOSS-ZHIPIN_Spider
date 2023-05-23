# BOSS-ZHIPIN_Spider
BOSS直聘爬虫和数据清洗及分析（2023.05.23时可用）

采用的pyppeteer框架，对boss直聘上具体感兴趣城市招聘信息，进行抓取，保存在 `xlsx/csv` 中。

<img src="./img/QG1.png" width="500" height="400">

# 使用方法

```python
python -m pip install -r requirement.txt
```

建议使用 `conda` 虚拟环境，不影响别的，真心好用

`jobs.py` 就是爬取数据并清洗

`analyze.py` 就是分析并生成词云或统计图

# 文件目录

```
/
├── data/
├── fonts/
├── img/
├── mask/
├── analyze.py
└── jobs.py
```
