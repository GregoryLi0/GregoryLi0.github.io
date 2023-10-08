import pandas as pd

# 读取CSV文件
csv_file = 'photourls/20231006-baiyunshan.csv'  # 请替换成你的CSV文件路径
df = pd.read_csv(csv_file)

# 创建一个空列表，用于存储转换后的数据
formatted_data = []

# 遍历CSV中的每一行
for index, row in df.iterrows():
    url = row['url']  # 假设CSV文件中的URL列名为'url'
    # 假设URL的格式为：https://example.com/2021/01/01/xxxx.jpg
    title = url.split('/')[-1].split('.')[0]
    # 构建格式化后的数据
    formatted_item = f"- image: {url}\n  title: {title}\n"

    # 将格式化后的数据添加到列表中
    formatted_data.append(formatted_item)

# 将格式化后的数据保存到文件或进行其他操作
formatted_output = '\n\n'.join(formatted_data)

# 打印格式化后的数据（可选）
print(formatted_output)

# 如果需要将格式化后的数据保存到文件，可以使用以下代码
# with open('formatted_data.txt', 'w', encoding='utf-8') as f:
#     f.write(formatted_output)
