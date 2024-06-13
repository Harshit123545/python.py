s1="hello i m harshit"
print(s1.capitalize()) #covert first lower case character into upper case
print(s1.title()) # convert all letters in upper case


mystr="hello worldddd"
countstr=mystr.count("l")
print(countstr)
startstr=mystr.startswith("ll")
print(startstr)
endstr=mystr.endswith("dd")
print(endstr)


s1="hello;i;am;harshit"
s2=s1.split(";",2)
print(s2)
s3=s1.rsplit(";",2)
print(s3)


list1=["5","6","8","9"]
str1="".join(list1)
print(str1)
str2=" ".join(list1)
print(str2)
str3=",".join(list1)
print(str3)




set1={"5","6","8","9"}
str1="".join(set1)
print(str1)
str2=" ".join(set1)
print(str2)
str3=",".join(set1)
print(str3)




song="JINGLE Bells jingle Bells Jingle All The Way"
song.upper()
song_words=song.split()
count=0
print(song_words)