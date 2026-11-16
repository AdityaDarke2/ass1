#!/bin/bash

somecommand=""
echo "Hello!" 
whoami 
echo

echo "Today's date: "
date

echo

echo "Internet Connectivity: "
ping -c 2 google.com
echo
echo -n "Enter a command whose information you'd like to see: " 
read somecommand

echo 
whatis $somecommand
