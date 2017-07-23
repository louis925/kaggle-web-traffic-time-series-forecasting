# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

import data_processing as dp

print('Reading data...', end = '')
dates, page, visit, key, predict_dates = dp.read_data()
print('done!')

n_days = len(visit[0])
print('Number of days:', n_days)
print('visit[0]', visit[0])

n_page = len(page)
print('Number of pages:', n_page)
print(page)

# nuber of page from 'spider'
tag1 = 'spider'
tag_exist = [1 if tag1 in a else 0 for a in page]
n_tag_exist = sum(tag_exist)
print("Number of page name that contain", tag1, "is", n_tag_exist, "/", n_page)
print("which is about", n_tag_exist / n_page)

# nuber of page from 'all-agents'
tag2 = 'all-agents'
tag2_exist = [1 if tag2 in a else 0 for a in page]
n_tag2_exist = sum(tag2_exist)
print("Number of page name that contain", tag2, "is", n_tag2_exist, "/", n_page)
print("which is about", n_tag2_exist / n_page)

print(tag1, "+", tag2, "=", (n_tag_exist + n_tag2_exist), "/", n_page)

# nuber of page from 'all-access'
tag3 = 'all-access'
tag3_exist = [1 if tag3 in a else 0 for a in page]
n_tag3_exist = sum(tag3_exist)
print("Number of page name that contain", tag3, "is", n_tag3_exist, "/", n_page)
print("which is about", n_tag3_exist / n_page)

# nuber of page from 'desktop'
tag4 = 'desktop'
tag4_exist = [1 if tag4 in a else 0 for a in page]
n_tag4_exist = sum(tag4_exist)
print("Number of page name that contain", tag4, "is", n_tag4_exist, "/", n_page)
print("which is about", n_tag4_exist / n_page)

# nuber of page from 'mobile-web'
tag5 = 'mobile-web'
tag5_exist = [1 if tag5 in a else 0 for a in page]
n_tag5_exist = sum(tag5_exist)
print("Number of page name that contain", tag5, "is", n_tag5_exist, "/", n_page)
print("which is about", n_tag5_exist / n_page)

print(tag3, "+", tag4,"+", tag5, "=", n_tag3_exist + n_tag4_exist + n_tag5_exist, "/", n_page)

print("The first 5 page_dates and keys:\n", key[:5])

print("The first 5 dates in data:", dates[:5])
print("The last 5 dates in data:", dates[-5:])

dp.plot_visit(0, visit, page)
dp.plot_visit(32000, visit, page)
dp.plot_visit(21120, visit, page)
dp.plot_some_visit(visit, page)
