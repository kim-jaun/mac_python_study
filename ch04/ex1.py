s = 'usr/local/bin/python'
# dic = ‘/usr/local/bin’, filename = ‘python’
i = s.rfind("/")
print("dic =",s[:i])
print('filename =',s[i+1:])
