# Staff Appraisals

This programme allows staff to undertake a quick questionnaire on their work life and salary requirements or desires. The programme is beneficial for both the employee and the employer as answers automatically update to a google spreadsheet. 


[Hers is a live version of the questionnaire](https://staff-appraisals.herokuapp.com/) 



## The programme

The programme collects answers to a number of questions which have been collected from the google spreadsheet.  The user is given prompts on how they should enter their answer. 
Their name should be entered. The user is then shown a number of statements which they must state on a scale of 1-5 from least to most agreement. The user then moves to be asked their current salary which must be a 5 digit numerical format. This is followed by a question on how much the user would like for their pay to increase in percentage. 

The google spreadsheet is then updated accordingly with these details (as well as their users desired annual salary based on their percentage input).

## Existing features 

The programme automatically collects the answers from the spreadsheet; this makes programme maintenance much more simple for future use. If managers wish to alter the questions slightly, they are able to do so directly on the spreadsheet.

The programme collects the users name at the beginning of the questionnaire. Their name is then used later within a message to the user to create a personal touch. 

All inputs given by the user are then checked through validation functions. The validation criteria is dependent on the question type. 

When an error occurs, the programmes reveal an error-specified message to the user to explain what is wrong with their input. 

## Future Features 

If the user inputs "yes" to the question "I believe my current pay matches my value of work" they are not offered the oppertunity to ask for a pay raise. 

Create a loop function search for all questions within the spreadsheet. This means that managers can keep adding / removing questions to the questionnaire. 

Use classes

Allow users to review data before submitting the questionnaire. They could also be offered a the option to restart / edit answers if they require before submitting their form. 

## Testing 
I have manually tested the programme. I have passed the code thorugh the PEP8 and now reveals no errors. 
The validation cost has been thoroughly tested by manually inputting incorrect/ invalid answers to retreive error messaging.
 
## Bugs 
One major bug that arose came after opting to return answers as tuples for the quesitions requiring a value of 1-5. Answers were not updating to the spreadsheet properly and the validation didn't work correctly as users could enter numbers bigger than 5 with no issue. 
To solve this, I used the len method and picked out which item within the tuple to verify against. 

## Remaining Bugs 
No known bugs remain 

## Validator Testing
The programme was run through PEP8 with no errors showing. 

## Deployment 
The programme was created within Gitpod. The code was then transfered to Heroku where the app was created. Buildpacks of Python and NodeJS were added. The app was then linked to the Gitpod repository and deployed. 

## Credits 
Code institue for the template within Gitpod. 