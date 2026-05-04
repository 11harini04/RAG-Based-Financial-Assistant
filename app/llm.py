from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_financial_answer(context, query):
    prompt = f"""
    You are a financial assistant.

    Rules:
    - Answer ONLY using provided context
    - If unsure, say "I don't have enough data"
    - Be precise and structured
    - Include risks if relevant

    Context:
    {context}

    Question:
    {query}

    Output format:
    Answer:
    Risks:
    Recommendation:
    """

    try:
        response = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        error_msg = str(e)
        print(f"❌ Groq API Error: {error_msg}")
        
        if "402" in error_msg or "payment" in error_msg.lower():
            return "Error: Groq API returned 402 Payment Required. Check your account credits/plan at console.groq.com"
        elif "401" in error_msg or "invalid" in error_msg.lower():
            return "Error: Invalid Groq API key. Check your .env file and console.groq.com"
        else:
            return f"Error: Groq API failed - {error_msg}"