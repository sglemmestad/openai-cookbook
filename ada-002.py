import openai
openai.api_key = "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"

prompt = "Say this is a test"

response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=5)

print(response)