#!/bin/sh

import random

first_name = input("what is the babies first name? ")
last_name = input ("What is the babies last name? ")



input_names = input("Enter middle names you like separated by a comma: ")

lst = input_names.split(",")

print("Your babies full name is " + first_name + " " + random.choice(lst) + " " + last_name)
