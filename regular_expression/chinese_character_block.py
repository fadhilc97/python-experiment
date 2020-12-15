import re

text = "麦克风测试"
detect_chinese_chars = re.search("[\u4e00-\u9fff]", text)
replace_chinese_chars = re.sub("[\u4e00-\u9fff]", "1", text)
print(detect_chinese_chars)
print(replace_chinese_chars)