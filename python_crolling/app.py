

# 파일 = open('a.txt', 'w')
# 파일.write('hello')
# 파일.close()

# 파일 = open('a.txt', 'a')
# 파일.write('\n반가워')
# 파일.close()


# 파일 = open('a.txt', 'r')
# print(파일.read())
# 파일.close()

# f = open('data.csv', 'w')
# f.write('김,이,박')
# f.write('\n김,이,박')
# f.close()


# 리스트 = ['삼성전자', '카카오', '네이버', '신풍제약']

리스트 = open('a.txt', 'w')
리스트.write('\n삼성전자')
리스트.write('\n카카오')
리스트.write('\n네이버')
리스트.write('\n신풍제약')
리스트.close()

리스트트 = ['삼성전자', '카카오', '네이버', '신풍제약']
반복문 = open('b.txt', 'w')
for i in 리스트트:
    반복문.write(f'\n{i}')

print(반복문)
반복문.close()