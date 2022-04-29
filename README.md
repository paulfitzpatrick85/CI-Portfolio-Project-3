# Hang-Man
Hang-Man is a python terminal game which runs in the Code Institue mock terminal on Heroku.
The game selects a word at random, and the user must guess the word one letter at a time or they can attempt to guess the full word in one go.

Run the finished app here - https://paulfitzpatrick85.github.io/CI-Portfolio-Project-2/

IMAGE- AM I RESPONSIVE


## How to Play
When the program is ran for the first time the user is greeted with a welcome message, asked to input their name and then asked if they would like to start a new game.

![get user name](https://user-images.githubusercontent.com/55660566/165741789-4ff03bf7-f642-4daa-a71a-37fa02646d15.png)

If the user selects yes, the game begin and the user can begin guessing the word

![yes to begin game](https://user-images.githubusercontent.com/55660566/165742382-bd34252e-25be-4a2e-8c1d-34dbe62537f5.png)

If the user selects no, they are brought back to the start to begin the game when they choose.

![no for begin game](https://user-images.githubusercontent.com/55660566/165742685-6ffed7bc-2a2d-43c4-a409-36619ba75765.png)

If anything but "y" or "n" is typed, the program will continue to inform the user "you need to type either y or n" until y or n is entered.

## Features
Once the user has selected yes to begin the game, they are told the word contains four letters and are asked to guess a letter.
The user can only either input one letter at a time, or the full correct word. 

when a correct guess is entered, a message is printed to say that 'x' is in the word and its position in the word is displayed in the format _ _ _ x.

![correct guess](https://user-images.githubusercontent.com/55660566/165837869-853b0711-9188-4706-9fcf-8e5db3bcfb87.png)

When a incorrect guess is input by the user, the user is told the lettter is not in the word and a list of the their wrong guesses is display along with the ascii art depicting the hangman, with a limb added on for each incorrect guess.
The number of guess attempts remaining is also displayed.

![wrong guess](https://user-images.githubusercontent.com/55660566/165745355-c1ebe414-fcb5-4849-9590-1c0c1fcc6d97.png)

If the guess consists of more than one letter and is not the correct word, a message is printed to tell the user to enter one letter at a time or the correct word, and that a their number of guesses has decreased as a result of the attempt.

![multi-letter guess](https://user-images.githubusercontent.com/55660566/165838183-6464e1a2-b796-4347-8833-40c78b768624.png)

When the user guesses the word correct they are asked if they would like to play again by typing "y" or "n".

![correct guess](https://user-images.githubusercontent.com/55660566/165940437-f7852821-024a-4972-8e09-143a163ea425.png)

"y" will bring them straight into another game and "n" will take them back to the beginning of the program.
 
## Testing section
- I ran my code through the pep8 checker and found no significant issues, only messages regarding blank lines containing white space, which I have left as is for the sake of readability. 






### User story testing
- The game is designed to be minimalistic in terms of the amount of prompt or questions a user needs to do get through or answer before getting to the actual game, once the user enters their figures for each macro, one button does everything, tallys up individual macro totals, works out the total calories consumed so far, and how many calories they have left if they chose to set a target. 
- Navigation links between the two pages are place in the same place, the bottom is chosen as opposed to the top like a website, in order to have the app's function take the users focus and so that aesthetically it resembles an app rather than a website.
- The layout is presented in a simple format so that on first viewing the app, the target audience should have good inkling of how to use the app. The buttons on the chart.html page intentionally use the 'slang' terms for weight loss and weight gain i.e, cutting and bulking, in order to display familiarity with the fitness 'scene' (as these a terms used by seasoned professionals within sports such as power lifting, MMA and much more).
- 
     
## Bugs found while creating and testing
 Although not necessarily a bug, one problem I encountered was if the user entered eventually enetered four correct guesses the game would not end.
 To resolve this I ------------
 To do this I created an empty list called correct_guesses to store the correct guesses and I also created a variable called sorted_word which used the sorted method on the word variable.
 I then used an if statement to check the sorted_word variable was equal to the sorted guesses, eg if the word was "bake" and the 
-
  
## Deployment

I deployed the web app through github pages through the following steps:
- I saved, commited and push my work to github using the commands 'git add .',' git commit -m "example comment"', and 'git push' respectively.
- From my project repository I then navigated to the settings tab to find the github pages section where in the source section I selected main branch from the drop down menu and selected save, a link was then created for the published site.

## credits
- The code block for the charts was taken from google charts examples and the information adapted to suit the needs of the app.
 Code taken from this webpage https://www.tutorialspoint.com/googlecharts/googlecharts_pie_basic.htm 
- The initial plan for the app was to have one chart and have it be responsive to the user input, but that proved to be beyond my current knowledge. The chart was left in with future maintenability in mind, in that as I learn more throughout the course I can return to complete the initial intention.








credits 
display position of guessed letter

if position == 0:
      print(letter, "_ _ _ _")
    if position == 1:
      print("_", letter, "_ _ _ ")
    if position == 2:
      print("_ _", letter, "_ _ ")
    if position == 3:
      print("_ _ _", letter, "_ ")
    if position == 4:
      print("_ _ _ _", letter)

      https://stackoverflow.com/questions/56324522/program-in-python-to-show-letters-guessed-in-a-hangman-game-not-working




      acsii pictures

      https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c