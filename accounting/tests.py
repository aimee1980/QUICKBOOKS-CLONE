from django.test import TestCase
import openai

class OpenAITestCase(TestCase):
    def test_openai_api_connection(self):
        """Test connection to OpenAI API"""
        openai.api_key = "sk-proj-..."  # Replace with your actual key

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "What is 2 + 2?"}
                ]
            )
            content = response['choices'][0]['message']['content']
            print("✅ GPT Response:", content)
        except Exception as e:
            print("❌ ERROR from OpenAI:", e)
            self.fail(f"OpenAI API call failed: {e}")
