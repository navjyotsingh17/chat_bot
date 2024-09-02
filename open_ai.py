from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key = os.getenv("OPEN_API_KEY"))
command = """
[11:37 am, 16/8/2024] Rajveersingh Rathod: Oo mila mila
[11:37 am, 16/8/2024] Rajveersingh Rathod: Bo thoda kala talav ke pass chupa huea tha
[11:37 am, 16/8/2024] Rajveersingh Rathod: Mila
[3:13 pm, 16/8/2024] Navjyotsingh Pulaha: 😂😂 aaj aa rha hai kya gym?
[3:14 pm, 16/8/2024] Rajveersingh Rathod: Are bhai
[3:14 pm, 16/8/2024] Rajveersingh Rathod: Meko pay karna padega right
[3:14 pm, 16/8/2024] Rajveersingh Rathod: Par seen assa hae ke meko jana hae na pune😂
[3:14 pm, 16/8/2024] Rajveersingh Rathod: So 1 mhaine ka deke phayda kya ?
[3:14 pm, 16/8/2024] Rajveersingh Rathod: Iss lea nahi aa raha
[3:15 pm, 16/8/2024] Rajveersingh Rathod: Me gandhari jata hoon roz sham ko
[3:15 pm, 16/8/2024] Rajveersingh Rathod: Walk karne
[3:16 pm, 16/8/2024] Navjyotsingh Pulaha: haa woh bhi hai chal phir pune se aane ke baad he continue kar
[3:17 pm, 16/8/2024] Rajveersingh Rathod: Aa yes
[3:17 pm, 16/8/2024] Rajveersingh Rathod: Tu agar free ho to chal gnadhari
"""

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a person named navjyot, and he speaks english and hindi languages. You are from India and you are a software developer engineer. Analyze the chat history and respond like navjyot"},
        {
            "role": "user",
            "content": command
        }
    ]
)

print(completion.choices[0].message.content)