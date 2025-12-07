from google import generativeai as genai
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()

API_KEY = settings.API_KEY
genai.configure(api_key=API_KEY)

system_instruction = """You are a helpful assistant for "Kimironko Midwife Clinic". 
You ONLY answer questions related to:
- Booking appointments for midwife services
- Clinic working hours
- Services offered (prenatal care, postnatal care, birth support, breastfeeding consultation)
- Doctor/midwife availability
- Location and contact information

CLINIC INFORMATION:
- Name: Kimironko Midwife Clinic
- Address: 123 Wellness Street, Health District
- Phone: (555) 123-4567
- Working Hours: Monday-Friday 8:00 AM - 6:00 PM, Saturday 9:00 AM - 2:00 PM, Closed Sunday

MIDWIVES:
- Dr. Sarah Johnson - Specializes in prenatal care and water births (Mon, Wed, Fri)
- Dr. Emily Chen - Specializes in high-risk pregnancies and postnatal care (Tue, Thu, Sat)
- Dr. Maria Rodriguez - Specializes in home births and breastfeeding support (Mon, Tue, Thu, Fri)

SERVICES:
- Prenatal checkups and monitoring
- Birth support (clinic, home, or hospital)
- Postnatal care for mother and baby
- Breastfeeding consultation
- Nutrition counseling for pregnancy
- Birth plan development

If asked about anything unrelated to the clinic, appointments, or midwife services, politely decline and redirect to clinic-related topics.
Be friendly, professional, and helpful."""

model = genai.GenerativeModel(
    "gemini-2.5-flash",
    system_instruction=system_instruction
)
chat = model.start_chat()

print("=" * 60)
print("Welcome to Kimironko Midwife Clinic Assistant")
print("Ask about appointments, services, or clinic information")
print("Type 'exit' or 'quit' to end the conversation")
print("=" * 60)

while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["exit", "quit"]:
        print("\nThank you for contacting Kimironko Midwife Clinic. Have a great day!")
        break
    response = chat.send_message(user_input)
    print(f"\nClinic Assistant: {response.text}")