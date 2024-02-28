# def add(a,b):
#     return a+b
# # sum=add(2,2)
# # print(sum)


# myList=[]
# sum=0
# num=int(input('How many numbers'))
# for i in range (1,num+1):
#     toadd=int(input(f'Enter number {i}:'))
#     myList.append(toadd)
#     sum=add(sum,toadd)
# print(f'Sum of elements in {myList} is: {sum}')

# def mul_table(num=5,upto=10):
#     for i in range(upto+1):
#         print(f'{num} X {i} = {num*i}')

# mul_table(6)

'''
def display(name='H adolf'):
    print(f"Hello {name} !!")

name=input('Enter your name:')
display(name)
'''
import datetime as dt

'''
def sum_of_numbers(*nums):
    return sum(nums)
start_time=dt.datetime.now()
sumtotal=sum_of_numbers(1,2,3,4,5)
end_time=dt.datetime.now()
print(f'Sum={sumtotal}')
print(f'Execition time: {end_time-start_time}')
'''

# def addition (**numbers):
#     return numbers['default']
    
# print(addition(first=1, second=2, default=0))

def generate_q(**ques):
    return ques

def check_ans(ansList,ans,points):
    pass

def add_question():
    global question_count
    question=input('Question: ')
    options=[]
    for i in range(1,5):
        options.append(input(f'Option {i}: '))
    correct_ans=input('Correct Ans: ')
    if(correct_ans in options):
        pass
    else:
        print('Option doesnot exist !')
        exit() 
    question_count+=1
    q_var='q'+str(question_count)
    qn=generate_q(ques=question,option=options)
    question_db[q_var]=qn
    ans_db[q_var]=correct_ans

def ask_question():
    while True:
        global ans_count, score
        if ans_count==question_count:
            print('Out of Questions ! Come back Later..')
            print('-'*100)
            exit()
        ask_var='q'+str(ans_count+1)
        print(question_db[ask_var]['ques'])
        print("Options ::",end=' s')
        print(question_db[ask_var]['option'])
        ans=input('Your Ans: ')
        if ans_db[ask_var]==ans:
            score+=10
            print(f'Corrrect Ans !! Score={score} !!')
            print('-'*100)
            ans_count+=1
        else:
            print('Incorrect Ans !! Game over !!')
            print(f'Your score: {score}')
            print('-'*100)
            exit()


question_db={}
ans_db={}
question_count=0
ans_count=0
score=0
while True:
    print('-'*100)
    print('Let\'s Play')
    print('-'*100)
    print('1. Add Question')
    print('2. Play quiz')
    print('*. Exit')
    print('-'*100)
    try:
        value=int(input('Enter Choice: '))
    except:
        print('Input Error')
        break
    match value:
        case 1:
            key=input('Authorization key !!: ')
            if key=='1234':
                while True:
                    add_question()
                    another=input('Another question [y/n]?! ')
                    if another=='n' or another=='N':
                        break
                    else:
                        print('-'*100)
            else:
                print('Error! You cannot add question')
                print('-'*100)
                exit()
        case 2:
            ask_question()
        case _:
            exit()

    

