#Q1

#數學及格的有: Tom, John, Mary, Jimmy, Sunny, Amy
math={'Tom','John','Mary','Jimmy','Sunny','Amy'}
print(math)

#英⽂及格的有: John, Mary , Tony , Bob , Pony, Tom , Alice
english={'John','Mary','Tony','Bob','Pony','Tom','Alice'}
print(english)

#數學及格但英⽂不及格的名單
list1=math-english
print(list1)


#數學不及格但英⽂及格的名單
list2=english-math
print(list2)

#兩科都及格的名單
total=math&english
print(total)

#全班總共有幾個同學
nums=len(math|english)
print(nums)

#Q2

#Tom 作業成績為 80, 100, 90, 95，John 作業成績為100,93,75,80
#請以dict 型別存放兩個同學的資料 key:名字，value:分數列表(list)


homework={'Tom':[80,100,90,95],'John':[100,93,75,80]}
print(homework)

#平均分數

Tom_avg=(80+100+90+95)/4
John_avg=(100+93+75+80)/4
print(Tom_avg)
print(John_avg)
