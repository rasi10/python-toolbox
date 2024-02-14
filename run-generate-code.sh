#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: sh $0 \"[parameter]\""
    exit 1
fi

source .env

PARAMETER_CONTENT="$1"

PAYLOAD=$(cat <<EOF
{
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "system",
      "content": "You are a highly experienced programming assistant with high expertise in the python programming language. Provide detailed, practical coding solutions."
    },
    {
      "role": "user",
      "content": "$PARAMETER_CONTENT"
    }
  ]
}
EOF
)

mkdir -p "generated_scripts"

curl -s https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $API_TOKEN" \
  -d "$PAYLOAD" > ./generated_scripts/raw_response.json

jq -r '.choices[0].message.content' ./generated_scripts/raw_response.json | 
sed -n '/^```python/,/^```/{/^```python\|^```/!p}' > ./generated_scripts/python_script.py

bash run-autopep8.sh

rm ./generated_scripts/raw_response.json

echo "END OF EXECUTION. SCRIPT SAVED TO ./generated_scripts/python_script.py"
