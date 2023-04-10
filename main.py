#!/bin/sh

import random

first_name = input("what is the baby's first name? ")
last_name = input ("What is the baby's last name? ")



input_names = input("Enter middle names you like separated by a comma: ")

lst = input_names.split(",")

print("Your baby's full name is " + first_name + " " + random.choice(lst) + " " + last_name)
