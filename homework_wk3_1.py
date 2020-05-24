# Exercise 1
import string
alphabet = " " + string.ascii_lowercase
alphabet


# Exercise 2
positions = { alphabet[v] : v for v in range(0, len(alphabet)) }
positions


# Exercise 3
message = "hi my name is caesar"
encoded_message = ''
encoded_message = encoded_message.join([ alphabet[positions[c]+1] for c in message ])
encoded_message


# Exercise 4
def encoding(message, key):
    encoded_message = ""
    alphabet_len = len(alphabet)
    return encoded_message.join( [alphabet[ (positions[c] + key) % alphabet_len ] for c in message ] )

encoded_message = encoding("hi my name is caesar", 3)
print(encoded_message)


# Exercise 5
decoded_message = encoding(encoded_message, -3)
print(decoded_message)

