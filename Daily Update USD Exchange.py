#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Hàm để lấy tỷ giá từ trang web
def get_usd_rate(url, selector):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        element = soup.select(selector)

        if element:
            usd_rate = element[0].text.strip()
            # Chuyển định dạng tỷ giá về số nguyên
            usd_rate = int(usd_rate.replace(',', '').replace('.', ''))
            return usd_rate
        else:http://localhost:8888/notebooks/Untitled5.ipynb?kernel_name=python3#
            return None
    else:
        return None

# URL và selector cho các ngân hàng
vietinbank_url = 'https://www.vietinbank.vn/web/home/vn/ty-gia/'
vietinbank_selector = 'td:contains("USD") + td'

vrbank_url = 'https://vrbank.com.vn/vi/ty-gia-ngoai-te/'
vrbank_selector = 'div.tbl-td:nth-child(7) > div:nth-child(3)'

lpbank_url = 'https://lpbank.com.vn/ti-gia/'
lpbank_selector = 'td:contains("USD ≥ 50") + td + td + td + td'

# Lấy tỷ giá từ các nguồn
usd_rate_vietinbank = get_usd_rate(vietinbank_url, vietinbank_selector)
usd_rate_vrbank = get_usd_rate(vrbank_url, vrbank_selector)
usd_rate_lpbank = get_usd_rate(lpbank_url, lpbank_selector)

# Kiểm tra và in tỷ giá
if usd_rate_vietinbank is not None:
    print(f'Tỷ giá USD VietinBank: {usd_rate_vietinbank}')
else:
    print('Không tìm thấy thông tin tỷ giá USD VietinBank.')

if usd_rate_vrbank is not None:
    print(f'Tỷ giá USD VRBank: {usd_rate_vrbank}')
else:
    print('Không tìm thấy thông tin tỷ giá USD VRBank.')

if usd_rate_lpbank is not None:
    print(f'Tỷ giá USD LPBank: {usd_rate_lpbank}')
else:
    print('Không tìm thấy thông tin tỷ giá USD LPBank.')

# Vẽ biểu đồ
banks = ['VietinBank', 'VRBank', 'LPBank']
usd_rates = [usd_rate_vietinbank, usd_rate_vrbank, usd_rate_lpbank]

# Điều chỉnh độ rộng cột bằng tham số width (đặt giá trị smaller để giảm độ rộng)
plt.bar(banks, usd_rates, width=0.5)
plt.xlabel('Ngân hàng')
plt.ylabel('Tỷ giá USD')

# Thêm nhãn gán giá trị lên từng cột
for i, rate in enumerate(usd_rates):
    plt.text(banks[i], rate + 100, str(rate), ha='center', va='bottom', fontsize=10)

plt.title('Tỷ giá USD từ các ngân hàng')
plt.show()


# In[ ]:




