# Sharing documentation

## What is Tishon
Short for "Practitioner", this is a coding language created from scratch in order for programmers and non-technical teams to understand how code works behind the hood at a high level.

# Creating a Lexer
Step Through
* Lexer is what goes through the input and breaks it down into usable bits called tokens. Ex: Input('123 + 132) will be broken down to the 2 integers 123 and 132 and also the addition operator.
* Each Token will have a type and a value

# Token Class
Step Through
* Has a type and a value
* Has a repr method to show the Token object 
* if it has a value then return type and value in repr, if none then just return the type

# Token Types
* Int
* Float 
* Plus
* Minus
* Multiply
* Divide 
* Left Parent
* Right Parent 

# Lexer Class
* Pass in the text and identify it, the starting position and the current character
* Make a method that will advance through positions of the text 
* constrain the method so that position does not go over length of text

# Make tokens method
* Need to identify every possible token there is out there
* Need to assign each text a token whether its an operation a digit or a string

# Run Method
* Needs to create a Lexer, catch tokens and errors and output them
* Pinpoint where the errors are