from telethon.sync import TelegramClient, events
import asyncio

# Replace these with your own values
api_id = '26752628'
api_hash = '99ae28f73ee1d7619a9d44d216dbe3f4'

async def create_telegram_account():
    async with TelegramClient('anon', api_id, api_hash) as client:
        try:
            print("Creating a new Telegram account...")
            
            # Prompt for phone number
            phone_number = input("Enter your phone number : ")

            # Send code request and get phone_code_hash
            sent_code = await client.send_code_request(phone_number)
            phone_code_hash = sent_code.phone_code_hash

            # Wait for user to enter the verification code
            verification_code = input("Enter the verification code: ")

            # Sign up with the provided code
            await client.sign_up(
                phone_number,
                verification_code,
                first_name='YourFirstName',
                last_name='YourLastName'
            )

            print("Account created successfully!")

        except Exception as e:
            print("Error creating account:", e)

if __name__ == '__main__':
    asyncio.run(create_telegram_account())
