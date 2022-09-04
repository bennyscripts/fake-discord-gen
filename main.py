import string, random, base64

if __name__ == "__main__":
    random_string = lambda length: ''.join(random.choice(string.ascii_letters) for _ in range(length))
    generate_token = lambda: base64.b64encode(str(random.randint(100000000000000000, 999999999999999999)).encode()).decode() + "." + random_string(5) + "." + random_string(38)

    amount = int(input("Amount to generate: "))
    accounts = [generate_token() for _ in range(amount)]

    if input("Save to file? (y/n): ") == "y":
        with open("accounts.txt", "w") as f:
            f.write("\n".join(accounts))