from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-3.5",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);

