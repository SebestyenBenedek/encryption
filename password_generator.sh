#!/bin/bash

readonly DEFAULTLENGTH=8

# Function to return a random character from a string
get_random_char() {
    char_set=$1
    echo ${char_set:$(( RANDOM % ${#char_set} )):1}
}

generate_password() {
    local length=$1

    lowercase="abcdefghijklmnopqrstuvwxyz"
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers="0123456789"
    special_chars="!@#$%^&*()-=_+[]{}|;:'\",.<>/?"
    all_chars="${lowercase}${uppercase}${numbers}${special_chars}"

    password=""

    password+=$(get_random_char "$lowercase")
    password+=$(get_random_char "$uppercase")
    password+=$(get_random_char "$numbers")
    password+=$(get_random_char "$special_chars")

    # Fill the remaining length with random characters
    for ((i=${#password}; i<($length); i++)); do
        password+=${all_chars:$(( RANDOM % ${#all_chars} )):1}
    done

    # Shuffle the password for a random order
    password="$(echo "$password" | fold -w1 | shuf | tr -d '\n')"

    echo "Generated password: $password"
    echo "If you want a different length password than 8 character type the script: "$0" <number>"
    echo "But it must be minimum 4 character long!"
}

    specificLength=$1

    # Check if there is an argument, if doesn't it should return a eight character long password,
    # if there is, it should return an argument long password, if that argument minimum 4 character long
    if [ -z "$1" ]; then
    	generate_password "$DEFAULTLENGTH"
    elif [[ "$1" =~ ^[0-9]+$ ]] && [ "$1" -ge 4 ]; then
	generate_password "$specificLength"
    else
	echo "Error: Invalid argument. If provided, the length must be a positive integer of 4 or greater."
	exit 1
    fi
