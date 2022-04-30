# Hang-Man
Hang-Man is a python terminal game which runs in the Code Institue mock terminal on Heroku.
The game selects a word at random, and the user must guess the word one letter at a time or they can attempt to guess the full word in one go.

Run the game here - https://ci-pp3-pf-hangman.herokuapp.com/

![mock terminal](https://user-images.githubusercontent.com/55660566/166123315-58d5bc57-c968-42ea-892c-40dff7c8e51d.png)

## User Storys
- As a user I want to be able to play the game easily and without having to go through any trial and error to figure it out.
- As a user I want to see where in the word my correctly guessed letter is posistioned in order to keep me interested and engaged in playing.
-As a user I want to continue on to a new game without having to re-enter my data.


## How to Play
When the program is ran for the first time the user is greeted with a welcome message, asked to input their name and then asked if they would like to start a new game.

![welcome message](https://user-images.githubusercontent.com/55660566/166121544-562c455a-8550-4b72-ba25-551e5ec5aed4.png)

If the user selects yes, the game begins and the user can begin guessing the word.

![yes to begin game](https://user-images.githubusercontent.com/55660566/165742382-bd34252e-25be-4a2e-8c1d-34dbe62537f5.png)

If the user selects no, they are brought back to the start to begin the game when they choose.

![no for begin game](https://user-images.githubusercontent.com/55660566/165742685-6ffed7bc-2a2d-43c4-a409-36619ba75765.png)

If anything but "y" or "n" is typed, the program will continue to inform the user "you need to type either y or n" until y or n is entered.

## Features
Once the user has selected yes to begin the game, they are told the word contains four letters and are asked to guess a letter.
The user can only either input one letter at a time, or the full correct word. 

When a correct guess is entered, a message is printed to say that 'x' is in the word and its position in the word is displayed in the format _ _ _ x.

![correct guess](https://user-images.githubusercontent.com/55660566/165837869-853b0711-9188-4706-9fcf-8e5db3bcfb87.png)

When a incorrect guess is input by the user, the user is told the lettter is not in the word and a list of the their wrong guesses is displayed along with the ascii art depicting the hangman, with a limb added on for each incorrect guess.
The number of guess attempts remaining is also displayed.

![wrong guess](https://user-images.githubusercontent.com/55660566/165745355-c1ebe414-fcb5-4849-9590-1c0c1fcc6d97.png)

If the guess consists of more than one letter and is not the correct word, a message is printed to tell the user to enter one letter at a time or the correct word, and that a their number of guesses has decreased as a result of the attempt.

![multi-letter guess](https://user-images.githubusercontent.com/55660566/165838183-6464e1a2-b796-4347-8833-40c78b768624.png)

When the user guesses the correct word they are asked if they would like to play again by typing "y" or "n".

![word guessed](https://user-images.githubusercontent.com/55660566/166117376-4a11092a-3741-47c4-bee8-00411a27ab22.png)

"y" will bring them straight into another game and "n" will take them back to the beginning of the program.
 
## Testing section
- I ran my code through the pep8 checker and found no significant issues, only messages regarding blank lines containing white space, which I have left as is for the sake of readability. 

![pep8](https://user-images.githubusercontent.com/55660566/166117448-53357289-06a1-4ba2-b5fb-8d3961b828d2.png)


### User story testing
- The game is designed to be minimalistic in terms of the amount of prompts or questions a user needs to do get through or answer before getting to the actual game.
- The game is launched after only two prompts: "input your name" and "would you like to play a new game?", the user is straight into the game with little to no waiting.
- Hints are displayed throughout the game: position in word of correctly guessed letter, list of previous wrong guesses and at game over the word is displayed to show the user what they missed. 
     
## Bugs found while creating and testing
 Although not necessarily a bug, one problem I encountered was if the user eventually entered four correct guesses and therefore completing the word, the game would not end.

 To resolve this I needed to compare the individual letters guessed to the individual letters in the word.
 To do this I created an empty list called correct_guesses to append the correct guesses to and I also created a variable called sorted_word which used the sorted method on the word variable.
 I then used an if statement to check the sorted_word variable was equal to the sorted guesses, eg if the word was "bake" and the guesses where in the order of for example: k,e,a,b, this if statement would be comparing if sorted word(in this case -"a","b", "e","k") is the same as the sorted guesses list ["a","b","e","k"], as opposed to checking if "a","b", "e","k" was the same as "bake" which was happen originally.

  
## Deployment
Due to the recent security issue with git hub, I added my project to my heroku profile, but for the actual deployment, I deployed the game through the terminal in gitpod.
- First I created a new app in heroku and I added a config vars with a key of PORT and value of 8000.
- I then added the build packs python and node.js.
- I then deployed the game itself through the terminal in gitpod using the following commands:
1. "heroku login -i"  to login to heroku
2. "heroku apps"  to display a list of apps in heroku profile.
3.  "heroku git:remote -a ci-pp3-pf-hangman" to set the heroku remote. 
4. 'git add . && git commit -m "Deploy to Heroku via CLI"' to Add, commit and push to github
5. git push origin main : Push to github 
6. git push heroku main  : Push to heroku

## Credits
The following code to display position of a correctly guessed letter was taken from stackover where a user was having a similar problem showing the user a hint of where in the word their correct guess is:

position = word.find(letter)

pos_list[position] = letter

print(' '.join(pos_list))

-Taken from the following webpage:
https://stackoverflow.com/questions/56324522/program-in-python-to-show-letters-guessed-in-a-hangman-game-not-working
(the above code is found a number of responses below the original posters question)


-The "images" for the hangman where copied from the following page:
https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c