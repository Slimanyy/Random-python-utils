import csv
import requests

# function to log in with given credentials
def login(username, password):
    url = "https://example.com/login"
    data = {"username": username, "password": password}
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

# read CSV file with login credentials
with open("credentials.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        username = row[0]
        password = row[1]
        # try logging in with current credentials
        logged_in = False
        while not logged_in:
            logged_in = login(username, password)
        print(f"Successfully logged in with {username}.")