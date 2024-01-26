import pandas as pd
import langid
import re

# 读取xlsx文件
df = pd.read_excel("D:/NJU文件/社会网络分析赛题/赛题1/dev.xlsx")

# 定义一个函数来检测语言
def detect_language(text):
    if isinstance(text, str):
        return langid.classify(text)[0]
    else:
        return 'unknown'
# 定义一个函数来去掉表情符号
def remove_emojis(text):
    if isinstance(text, str):
        # 匹配表情符号和除日文和韩文外的Unicode字符
        emoji_pattern = re.compile("["
                                   u"\U0001F600-\U0001F64F"  # emoticons
                                   u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                   u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                   u"\U0001F700-\U0001F77F"  # alchemical symbols
                                   u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                                   u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                                   u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                                   u"\U0001FA00-\U0001FA6F"  # Chess Symbols
                                   u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                                   u"\U00002702-\U000027B0"  # Dingbats
                                   u"\U000024C2-\U0001F251" 
                                   u"\u3040-\u30FF"          # Japanese Hiragana and Katakana
                                   u"\u1100-\u11FF"          # Hangul Jamo
                                   u"\u3130-\u318F"          # Hangul Compatibility Jamo
                                   u"\uAC00-\uD7AF"          # Hangul Syllables
                                   "]+", flags=re.UNICODE)
        cleaned_text = emoji_pattern.sub(r'', text)
        return cleaned_text
    else:
        return ''


# 去掉表情符号
df['cleaned_description'] = df['user/description'].apply(remove_emojis)

# 在DataFrame中添加一个language列
df['language1'] = df['user/description'].apply(detect_language)
df['language2'] = df['cleaned_description'].apply(detect_language)

# 保存带有新language列的DataFrame为新的xlsx文件
df.to_excel("D:/NJU文件/社会网络分析赛题/赛题1/output_test.xlsx", index=False, engine='openpyxl')
