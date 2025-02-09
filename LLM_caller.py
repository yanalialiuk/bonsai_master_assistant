from openai import OpenAI

class APICaller:
    def __init__(self, api_key, endpoint):
        self.client = OpenAI(
            api_key=api_key, 
            base_url=endpoint,
        )

    def call_llm(self, system_prompt, user_prompt, max_tokens=8000, temperature=0.5):
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=max_tokens, 
                temperature=temperature,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Ошибка вызова API: {e}")
            return None

