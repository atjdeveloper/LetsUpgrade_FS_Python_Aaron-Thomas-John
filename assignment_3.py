str1 = "What we think we become";
count=0;
index=0;
for i in range(len(str1)):
  k = str1.find("we",index);
  index=k+1;
print(k)  
