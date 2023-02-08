import csv
import requests

#url of login page
login_url = input('Enter login url here: ')

#reading csv files containing login information
with open('file.csv', 'r') as login_file:
    login_reader = csv.reader(login_file)
    for row in login_reader:
        #csv should contain 2 columns for username and password
        username = row[0]
        password = row[1]

        #staring login attempts with current data
        session = requests.Session()
        login_data = {'username':username, 'password':password}
        response = session.post(login_url, data=login_data)

        #checking if the login was successful
        if 'Welcome' in response.text:
            print(f'Successfull login with {username} and {password}')
            break
        else :
             print(f'Unsuccessfull login with {username} and {password}')

