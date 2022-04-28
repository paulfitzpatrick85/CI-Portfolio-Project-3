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

## Features
Once the user has selected yes to begin the game, they are asked to guess a letter.
The user can only either input one letter at a time, or the full correct word. 
If their guess consists of more than one letter and is not the correct word, a message is print to tell the user to enter one letter at a time or the correct word.

![guess single letter only](https://user-images.githubusercontent.com/55660566/165744951-b9de6837-ea6e-4a94-b902-16d693263338.png)

When a incorrect guess is input by the user, the user is told the lettter is not in the word and a list of the their wrong guesses is display along with the ascii art depicting the hangman, with a limb added on for each incorrect guess.
The number of guess attempts remaining is also displayed.

![wrong guess](https://user-images.githubusercontent.com/55660566/165745355-c1ebe414-fcb5-4849-9590-1c0c1fcc6d97.png)
 
## Testing section
- I tested and confirmed that the app displays correctly across all screen sizes from large monitors, laptop, tablet and small smartphones (down to 325px).
The charts display perfect upon loading to any screen, but as a note, when viewing the charts in dev tools and minimising the screen down in width the charts will stay the same size until the page is refreshed.
This was thought to be a bug until the effect of the refresh was pointed out to me by my mentor.

- I tested my html on the w3c vaildator and my css on jigsaw and found all code to be ok with no errors.

![htmlValid](https://user-images.githubusercontent.com/55660566/160015555-342b6f9d-4f7d-46a5-a86d-42150f3b784f.png)

![html2Valid](https://user-images.githubusercontent.com/55660566/160015568-d423cb6b-bc46-4f45-98a1-5e38d7bb692e.png)

![cssValid](https://user-images.githubusercontent.com/55660566/160015588-748a53ce-5bfb-4a86-b607-39bc2b79261a.png)

- I tested my JavaScript on the jshint vaildator and returned no significant issues. All warnings and issues where discussed we my mentor who assured me the issues where not significant, and also my tutor was happy as long as everything worked as intended.
The warnings where as follows:
- for each instance let is used :'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
- 13 unused variables: jshint then lists all functions used, not variables.
- One undefined variable : 'google' as used in the code block for each chart, again I was assured this was not a significant issue.

![jsValidLet](https://user-images.githubusercontent.com/55660566/160015950-8382d8b9-0830-4868-8364-4331d12c51c8.png)
![jsValidUndefined](https://user-images.githubusercontent.com/55660566/160015961-ab6ee0d3-8518-4512-bbc2-111efe73f75b.png)
![jsValidFunc](https://user-images.githubusercontent.com/55660566/160016133-c9321fcf-3168-4734-92b9-2002c26caa90.png)

- I tested that the link  on each page works correctly.

- I tested the sites accessibility through lighthouse, the image below showing the results.

![lighthouse](https://user-images.githubusercontent.com/55660566/160016789-e57e3a4a-301e-4935-aefa-233779583508.png)

### User story testing
- The app is designed to be minimalistic in terms of the amount of work and clicking a user needs to do to, once the user enters their figures for each macro, one button does everything, tallys up individual macro totals, works out the total calories consumed so far, and how many calories they have left if they chose to set a target. 
- Navigation links between the two pages are place in the same place, the bottom is chosen as opposed to the top like a website, in order to have the app's function take the users focus and so that aesthetically it resembles an app rather than a website.
- The layout is presented in a simple format so that on first viewing the app, the target audience should have good inkling of how to use the app. The buttons on the chart.html page intentionally use the 'slang' terms for weight loss and weight gain i.e, cutting and bulking, in order to display familiarity with the fitness 'scene' (as these a terms used by seasoned professionals within sports such as power lifting, MMA and much more).
- 
     
## Bugs found while creating and testing
 
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