import requests
import json

# Firebase Database URL (Replace with your own Firebase Realtime Database URL)
firebase_url = 'https://<your-database-name>.firebaseio.com/'

# Function to send data to Firebase Realtime Database
def send_message(user_id, message):
    message_data = {
        'user_id': user_id,
        'message': message
    }

    # Send the data to the Firebase Realtime Database
    response = requests.post(f'{firebase_url}/messages.json', data=json.dumps(message_data))
    
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Error sending message:", response.text)

# Function to fetch messages from Firebase Realtime Database
def fetch_messages():
    response = requests.get(f'{firebase_url}/messages.json')
    
    if response.status_code == 200:
        messages = response.json()  # Parse the JSON response
        print("\nRecent Messages:")
        for msg_id, msg_data in messages.items():
            print(f"User {msg_data['user_id']}: {msg_data['message']}")
    else:
        print("Error fetching messages:", response.text)

# Main function to simulate a simple chat
def chat_application():
    while True:
        print("\n--- Chat Application ---")
        choice = input("1. Send Message\n2. Fetch Messages\n3. Exit\nEnter choice: ")

        if choice == "1":
            user_id = input("Enter your user ID: ")
            message = input("Enter your message: ")
            send_message(user_id, message)

        elif choice == "2":
            fetch_messages()

        elif choice == "3":
            print("Exiting the chat application...")
            break

        else:
            print("Invalid choice. Please try again.")

# Start the chat application
if __name__ == "__main__":
    chat_application()
