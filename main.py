from openai import OpenAI
from openai import RateLimitError
from sk import my_sk

client = OpenAI(api_key=my_sk)

try:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": "Hello"}
        ]
    )

    print(response.choices[0].message.content)

except RateLimitError:
    print("API limit reached. Check your credits.")