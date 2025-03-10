#list comprehnesion
# square=[]
# for i in range(1,11):
#     square.append(i**2)
# print(square)   #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
##using list comprehension
# square2=[i**2 for i in range(1,11)]
# print(square2) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#addition example   #without list comprehension
# list_add=[]
# for i in range(1,11):
#     list_add.append(i+2)
# print(list_add)  #[3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# #using list comprehension
# addlist2=[i+2 for i in range(1,11)]  #adding 2 for every element.
# print(addlist2)  #[3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#print second character of every word taken in list.
# second_char=["Pramod","Mahesh","Swami","sonu","arun"]
# second_char1=[]
# for i in second_char:
# #    second_char1.append(i[1])  #r,a,w,o,r
#     second_char1.append(i[-1])   #d,h,i,u,n  # printend last letter only
# print(second_char1)   #['r', 'a', 'w', 'o', 'r']

#using list comprehension
# char_add=[i[-1] for i in second_char]
# print(char_add)  #['r', 'a', 'w', 'o', 'r']
