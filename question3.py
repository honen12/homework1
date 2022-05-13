import json
Questions={}## empty dictionary for question from file json
result=0##variable for result
count=1##number of question

with open('quiz.json','r') as quiz_math:
    Questions  =json.load(quiz_math)##load question and answer
name=input('please inter your name:') #name    
Id=input('please inter id :')#id
print('welcome {} ({})in maths quiz ,good luck'.format(name,Id))
for q in Questions.keys():
     print('Q',count,end=')')
     print(q)#print question
     answer=input(' your answer is : ')
     while not answer.isdigit():#for processing entering letter
          print('error,you must enter number try agian in next question, try agin')
          answer=input(' your answer is : ')
         
     if answer==Questions[q] :
          print('correct')
          result+=5
     else :
          print('wrong')
     
     count+=1    
print(name,'your result is  {}%'.format(result))
     
if result>=80:
     print('excellent')
elif 70<result<80:
     print('very good')
elif 60<result<=70:
     print(' good')
else:
     print('sorry, you are not pass this quiz')#store result in separate file
result_data={name:{'id':Id,'result':result}}
with open('result.json','w') as result:
     json.dump(result_data,result)
     result.close()
