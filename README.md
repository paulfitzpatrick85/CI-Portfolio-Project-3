# Marco Tracker

View the finished website here - https://paulfitzpatrick85.github.io/CI-Portfolio-Project-2/

## Who is this site for?

The function of the Macro Tracker web app, is to allow a user to manually enter and keep track of their daily macronutrient (protein, carbohydrate and fat) intake, and to also calculate the calories based on the macro's entered.
While some calorie tracking app use a database of popular foods to choose from and add, these app's often lack less popular foods items such as foreign brand protein powders or foods/supplements only available in healths shops and not in the typical supermarket.

![amIResponsive](https://user-images.githubusercontent.com/55660566/159682173-45369723-3459-4d11-b484-5c038d0205f9.png)



## User stories

- As a user I want to be able to use the app for its intended purpose easily and without having to through any trail and error to figure it out.
- As a user I want to I  want input a number of grams for each macro and have the overall totals of macro, total calories and remaining calories of my target to be calculated for me without out multiple click or inputting of data.
- As a user I would like to see popular ways of breaking down of food intake in the form of charts with percentages representative of how much of each macronutrient to consume.

# Features

 ## Main Page - Welcome and Data Entry Prompt.
On loading the app, the user is greeted with a prompt welcoming them to the page and they are asked to enter the number of calories they want to set as a target to consume each day.

When the user enters a number, an alert follows to say "Great! let us help keep you within (number entered) calories!"
The number entered is then displayed in 'Calorie Target'.

 ![initialPrompt](https://user-images.githubusercontent.com/55660566/159681041-110da584-db52-463a-adcd-6be349d8f791.png)

 ![numberEnteredCorrect](https://user-images.githubusercontent.com/55660566/159681060-4fa41e35-c7cc-48c9-bfa9-0b07fac62f58.png)

 ![targetDisplayed](https://user-images.githubusercontent.com/55660566/159681072-17959e7d-94dc-42ed-a580-d4a2ebfe201d.png)
 
 If the user enters anything that is not a number in the prompt, an alert will follow that reads "Sorry! (text entered) isn't a number! Please refresh the page and try again!" The user has the choice to refresh the page or continue using the app, in which case 'Calorie Target' will diplay "Target Not Set!"

 ![NaNmessage](https://user-images.githubusercontent.com/55660566/159678510-f90d00d4-f1ba-4118-a503-8e7ba8970477.png)

![TargetNotSet1](https://user-images.githubusercontent.com/55660566/159679067-d9fc76ff-f230-4df2-8c23-287490e5582e.png)
 
 ## Inputting Macros
Once a user has entered their target calorie number and it has been displayed, they can then begin to input there required number of protein, carbs and fat using the plus or if needs be the minus buttons, which along with all other buttons on the page will enlarge when the mouse is hovering over it to show the user the anyway on the page with the same styling is a button.

![inputtingMacros](https://user-images.githubusercontent.com/55660566/159685700-92ceb996-f60d-43f6-870a-1bbca6b58fde.png)

The user is required to enter data for all fields.
If one or more fields are left at zero and the user attempts to 'Calculate Totals Calories', an alert will be displayed request the user add inputs for all fields. Once the user clicks 'ok', the input fields are reset to zero.

![alertEnterAllInputs](https://user-images.githubusercontent.com/55660566/159695081-9e1ddad1-77b4-4d81-ae22-3d12a8e83843.png)


## Calculating Totals
After all macros numbers are input, the user can navagate to the "Calculate Total Calories" button which when clicked will trigger the following functions at the one time.
- Figures from the input fields are displayed in their corresponding 'Total grams' output. And on each subsequent click, once the user has input more numbers, the input numbers will be added to the current totals for protein, carbs and fat.  
- The totals for protein, carbs and fat are calculated into calories using the formula : (protein total x 4)+(carb total x 4)+(fat total x 9) =  total calories. The result is then displayed in 'Calories Consumed'.
- The current figure for 'Calories Consumed' is subtracted from the 'Calorie Target' set by the user. The Result of which is then displayed as 'Calories Remaining'. 

![totalsCalculated](https://user-images.githubusercontent.com/55660566/159685718-34ddf491-3cc0-4478-a394-41f33cff8a66.png)

## Navagation.

The web app is made up of two pages. At the bottom of each page is a link styled to look like the other button. On the home page this link brings the user to the second page, where three charts are displayed representing popular percentages of macro intake for the different phases of bodybuilding, using the terminology known to people interested in the subject: cutting(fat loss) , maintenance(staying as you are), and bulking(building muscle mass).
Clicking on each of the three button will call a function to display a different chart.

![chartPic](https://user-images.githubusercontent.com/55660566/159893401-ae27ed84-f9f9-4a66-bf01-07c65e585ada.png)
![chartPic2](https://user-images.githubusercontent.com/55660566/159893712-638b6c0e-ac78-45ae-bfce-8a97bd7f4ec7.png)

Below the chart buttons is the "Back to App" link, which will bring the user back to the home page of the app.

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
- While testing an earlier version of the app, each input fields had below it an 'add' button. This button when clicked would add the figure in the input field to the corresponding 'total grams', then the user had to clicked 'Calculate total Calories'. A bug or rather a loop hole for potential user error is that the user could continuously click 'Calculate total Calories' and continue adding the figures in each 'Total grams' which would see the total calories increase while each of the three 'total grams' would stay the same.
I decided the best course of action was to remove the 'add' button, place the 'add protein', 'add carb' and 'add fat' function in the onclick attribute of 'Calculate total Calories'. This eliminated the issue and also results in less work to be done by the user creating a better and easier user experience. 
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