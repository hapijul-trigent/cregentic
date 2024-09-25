

import requests, json

# Send a POST request to the running Llama 3 model on localhost
response = requests.post('http://localhost:11434/api/generate', json={
    "model": "llama3.1:8b",
    "prompt": "What is 5 + 6?"
})

# Print the JSON response
print(response.text)
print(response.text.splitlines())
# print(json.load({response.text}))
with open('resp.json', mode='w') as f:
    f.write('[')
    lines = response.text.splitlines()
    length = len(lines)
    for line in range(len(lines)):
        if line > length-2: f.write(lines[line])
        else: f.write(lines[line]+',')
    f.write(']')