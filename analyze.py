import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.font_manager import FontProperties
import re
from PIL import Image
import numpy as np
import random

# 配置字体路径
font_path = './fonts/仓耳今楷03-W04.ttf'  # 替换为实际的字体文件路径
plt.rcParams['font.family'] = fm.FontProperties(fname=font_path).get_name()
font_prop = fm.FontProperties(fname=font_path)

# 读取Excel文件
df = pd.read_excel('./data/clean_全国.xlsx')
# df = pd.read_csv('./data/clean.csv')

# 使用一个形状蒙版
mask = np.array(Image.open('./mask/中国.jpeg'))  # 你的蒙版图片路径

# 生成词云
df['技能要求'] = df['技能要求'].str.replace(' ', '')
df['技能要求'] = df['技能要求'].str.replace('-', '')
wordcloud = WordCloud(width=800, height=600, background_color='white', mask=mask, collocations=False, font_path=font_path).generate(' '.join(df['技能要求'].explode()))
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('技能要求-词云', fontproperties=font_prop)
plt.axis('off')
plt.show()

# 生成词云
df['福利'] = df['福利'].fillna('无')
wordcloud = WordCloud(width=800, height=600, background_color='white', mask=mask, font_path=font_path).generate(' '.join(df['福利'].explode()))
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('福利待遇-词云', fontproperties=font_prop)
plt.axis('off')
plt.show()

# 生成词云
df['地区'] = df['地区'].str.replace('·', '')
wordcloud = WordCloud(width=800, height=600, background_color='white', mask=mask, font_path=font_path).generate(' '.join(df['地区'].explode()))
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.title('地区-词云', fontproperties=font_prop)
plt.axis('off')
plt.show()

# 生成饼图
plt.figure(figsize=(8, 8))
plt.title('学历要求百分比图', fontproperties=font_prop)
df['学历要求'].value_counts().plot(kind='pie', autopct='%1.1f%%', textprops={'fontproperties': font_prop}, shadow=True)  # 指定字体属性和添加阴影效果
plt.ylabel('')  # 去除y轴标签
plt.axis('equal')  # 设置饼图为圆形
plt.show()

salary_data = df['薪酬']
# Extract and process the salary data
converted_data = []
for salary in salary_data:
    if '·' in salary:  # Handle "z-aK·b薪" format
        parts = salary.split('·')
        salary_range = parts[0]
        multiplier = int(parts[1].replace('薪', ''))
        salary_parts = salary_range.split('-')
        min_salary = int(salary_parts[0]) * 1000 * multiplier
        converted_salary = min_salary
    elif '元/时' in salary:  # Handle "c-d元/时" format
        salary_range = salary.replace('元/时', '')
        salary_parts = salary_range.split('-')
        min_salary = int(salary_parts[0]) * 8 * 20
        converted_salary = min_salary
    elif '元/天' in salary:  # Handle "h-i元/天" format
        salary_range = salary.replace('元/天', '')
        salary_parts = salary_range.split('-')
        min_salary = int(salary_parts[0]) * 20
        converted_salary = min_salary
    elif '元/月' in salary:  # Handle "e-f元/月" format
        salary_range = salary.replace('元/月', '')
        salary_parts = salary_range.split('-')
        min_salary = int(salary_parts[0])
        converted_salary = min_salary
    else:  # Handle "x-yK" format
        salary_parts = salary.split('-')
        min_salary = float(salary_parts[0]) * 1000
        converted_salary = min_salary
    converted_data.append(converted_salary)
# Create a DataFrame
df = pd.DataFrame({'薪酬': converted_data})
# Generate the histogram
plt.figure(figsize=(8, 6))
plt.hist(df['薪酬'], bins=30, range=(100, 30000), color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('薪酬', fontproperties=font_prop)  # Specify the font for the x-axis label
plt.ylabel('频数', fontproperties=font_prop)  # Specify the font for the y-axis label
plt.title('薪酬分布直方图', fontproperties=font_prop)  # Specify the font for the title
plt.xticks(rotation=45, fontproperties=font_prop)  # Specify the font for the x-axis tick labels
plt.show()