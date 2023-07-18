# Author: Kathleen Gundran
# Course: CS 361
# Program Description: Animal Crossing Villagers will be able to be randomly selected,
#                      if you enter the Villager's name their characteristics will be shown,
#                      and you can randomly filter the Villagers by their personality traits.

# https://api.nookipedia.com/doc
# import modules and API key

import requests
from requests import Session
import api_key
import json
import random

# url = 'https://api.nookipedia.com/villagers'
# headers = {'X-API-KEY': api_key.API_KEY, 'Accept-Version': '1.0.0'}
# response_API = requests.get(url, headers=headers)
# data = response_API.text
# json_object = json.dumps(data)

# with open("villager.json", "w") as outfile:
#     outfile.write(json_object)


# class to access API
class Villagers:
    """ Gets the information from the villagers """
    def __init__(self, token):
        self._apiurl = 'https://api.nookipedia.com/villagers'
        self._headers = headers = {'X-API-KEY': api_key.API_KEY, 'Accept-Version': '1.0.0'}
        self._session = Session()
        self._session.headers.update(headers=headers)
        self._response_api = requests.get(self._apiurl, headers=headers)
        self._data = self._response_api.json()              # array containing dictionaries

    def villager_info(self, villager_name):
        """
        When option **(1) Search Villager by Name** is selected,
        user enters a name, and characteristics of the villager is printed.
        """
        villager_characteristics = {}
        count = 0
        for object in self._data:                           # object variable is a villager dictionary
            if villager_name in object["name"]:             # checks to see if villager_name is in dictionary in "name"
                villager_data_dict = self._data[count]
                villager_characteristics["Name"] = villager_name
                villager_characteristics["Gender"] = villager_data_dict["gender"]
                villager_characteristics["Species"] = villager_data_dict["species"]
                villager_characteristics["Personality"] = villager_data_dict["personality"]
                birthmonth = str(villager_data_dict["birthday_month"])
                birthday = str(villager_data_dict["birthday_day"])
                villager_characteristics["Birthday"] = birthmonth + birthday
                villager_characteristics["Zodiac Sign"] = villager_data_dict["sign"]
                villager_characteristics["Quote"] = villager_data_dict["quote"]
                villager_characteristics["Catch Phrase"] = villager_data_dict["phrase"]
                return villager_characteristics
            count += 1
        return "Villager not found!"

    def random_villager(self):
        """
        When option **(2) Generate Random Villager** is selected,
        a random villager name will be printed.
        """
        villagers_num = len(self._data)
        villagers_last_index = villagers_num - 1
        random_index = random.randint(0, villagers_last_index - 1)
        return self._data[random_index]["name"]

    def filter_villager(self, personality_type):
        """
        When option **(3) Filter by Personality Type** is selected,
        user enters a personality type, and a list of villager names will
        be printed based off the personality entered.
        """
        villagers_filtered = []
        count = 0
        for object in self._data:
            if personality_type in object["personality"]:
                villagers_filtered.append(self._data[count]["name"])
            count += 1

        if len(villagers_filtered) == 0:
            villagers_filtered = "Villagers not found with this personality type."
        return villagers_filtered

    def continue_option(self):
        """
        After an option is selected, program will ask to be rerun or exited
        """
        print()
        print("Would you like to try again?")
        user_input_cont = input("Enter (1) for YES or (0) for NO: ")
        return user_input_cont



def main():
    """ Main function to run the program """

    villagers = Villagers(api_key.API_KEY)                  # creates a Villager Class to access JSON API info

    menu_options = ('1',  '2', '3', '4')

    while True:
        print("ANIMAL CROSSING RESIDENT SERVICE INFO")
        print("** Welcome to the Animal Crossing Resident Service Info by gundrank from island Venus **")
        print("** Seems like Isabelle and Tom Nook are on vacation right now, so please use this tool to find information about all the villagers! **")
        print()
        print("** MENU:")
        print("(1) Search Villager by Name")
        print("(2) Generate Random Villager")
        print("(3) Filter by Personality Type")
        print("(4) Exit")
        print()

        user_input = input("** Enter an option: ")

        if user_input in menu_options:

            if user_input == "1":
                print()
                print("** YOU'VE SELECTED:")
                print("(1) Search Villager by Name")
                user_input_1 = input("Enter Name: ")
                print(villagers.villager_info(user_input_1))            # accesses the villager_info method

                # decides if user want's to continue or not
                user_input_cont = villagers.continue_option()           # 1 to continue, 2 to exit
                if user_input_cont == "0":
                    break
                print()

            elif user_input == "2":
                print()
                print("** YOU'VE SELECTED:")
                print("(2) Generate Random Villager")
                print("Randomly Generated Villager:")
                print(villagers.random_villager())

                # decides if user want's to continue or not
                user_input_cont = villagers.continue_option()           # 1 to continue, 2 to exit
                if user_input_cont == "0":
                    break
                print()

            elif user_input == "3":
                print()
                print("** YOU'VE SELECTED:")
                print("(3) Filter by Personality Type")
                user_input_3 = input("Enter Personality Type: ")
                print(villagers.filter_villager(user_input_3))          # accesses the filter_villager method

                # decides if user want's to continue or not
                user_input_cont = villagers.continue_option()           # 1 to continue, 2 to exit
                if user_input_cont == "0":
                    break
                print()

            elif user_input == "4":
                print()
                print("** YOU'VE SELECTED:")
                print("(4) Exit")
                print("Goodbye!")
                break

        else:
            print()
            print("Sorry! That option is not available :(")
            print()


if __name__ == "__main__":
    main()
