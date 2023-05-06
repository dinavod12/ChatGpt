import openai
import config

openai.api_key = config.DevelopmentConfig.OPENAI_KEY

def generateprompt(prompt):
    
    message = []
    message.append({"role": "system", "content": "You are a helpful assistant."})
    
    question = {}
    
    question['role'] = 'user'
    question['content'] = prompt
    
    message.append(question)
    
    response = openai.ChatCompletion.create( model="gpt-3.5-turbo",messages=message)
    try:
        answer = response['choices'][0]['message']['content'].replace('\n',"<br>")
    except:
        answer = "Oops"
    return answer