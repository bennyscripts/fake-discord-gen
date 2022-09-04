import string, random, base64

random_string = lambda length: ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_token():
    return base64.b64encode(str(random.randint(100000000000000000, 999999999999999999)).encode()).decode() + "." + random_string(5) + "." + random_string(38)

if __name__ == "__main__":
    amount = int(input("Amount to generate: "))
    accounts = [generate_token() for _ in range(amount)]

    save_to_file = input("Save to file? (y/n): ")
    if save_to_file == "y":
        with open("accounts.txt", "w") as f:
            f.write("\n".join(accounts))