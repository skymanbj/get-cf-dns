# 一、主要功能：获得Cloudflare账户下所有DNS记录，并且整理成Markdown格式。
# 二、使用方法
## 1.下载两个.py文件（cf_dns.py，cf_dns_form.py）到你的电脑桌面。用txt编辑cf_dns.py，将你的Cloudflare API KEY和email补充到下面引号中。
  - API_KEY = ""  # 您的 Cloudflare API 密钥
  - EMAIL = ""      # 您的 Cloudflare 账户邮箱
## 2.获取dns：打开我的电脑，切换到桌面，输入框输入cmd,回车。输入python cf_dns.py（或者py cf_dns.py）,回车。如果不能运行，需要安装pathon，并且设置PATH。
## 3.整理成Markdown格式：等待程序生成cloudflare_dns_records.csv，输入pathon cf_dns_form.py cloudflare_dns_records.csv 1.txt,回车。运行后，在桌面打开1.txt查看。
