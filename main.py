import string
import random
import faker
import base64

class Account:
    def __init__(self, username, email, token):
        self.username = username
        self.email = email
        self.token = token

def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_token():
    user_id = random.randint(100000000000000000, 999999999999999999)
    encoded_user_id = base64.b64encode(str(user_id).encode()).decode()
    return encoded_user_id + "." + random_string(5) + "." + random_string(38)

def generate_account():
    username = "BenGen_" + random_string(8)
    email = username + random.choice(["@gmail.com", "@yahoo.com", "@hotmail.com"])
    token = generate_token()
    return Account(username, email, token)

def main():
    amount = int(input("Amount to generate: "))
    accounts = []
    for _ in range(amount):
        accounts.append(generate_account())

    save_to_file = input("Save to file? (y/n): ")
    if save_to_file == "y":
        with open("accounts.txt", "w") as f:
            for account in accounts:
                f.write(f"{account.token}\n")

if __name__ == "__main__":
    main()