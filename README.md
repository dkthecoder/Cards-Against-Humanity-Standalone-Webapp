# Cards Against Humanity, Standalone Flask-Based Web-App:
Cards Against Humanity (abbreviated as CAH) is a fun, creative commons-licensed card game in which players complete "fill-in-the-blank" statements yusing words or phrases rich are typically, offensive, risqué or politically incorrect.

I aim to take this fun and enriching cardgame and convert it into a python based web-app which utilises Python, SQL, CSS and HTML, and demonstrates my skills and foresight in devops, project management, HCI and containerisation.

This repository is also part of the deliverables for the QA devops project 2. and thus, will aim to split the application across 4, deployable "Docker" containers from a script.

## Contents:
* [The App](#The-App)
* [Known Issues](#Known-Issues)
* [Future Work](#Future-Work)


# The App:  
Upon navigating to the app the user is presented with the homepage:  

![home]()  
The nav bar provides links which allow users to add a question, view questions and take the quiz. To add a question, the user simply fills in the name of the question on the form:  

![add question]()  
The user is then redirected to a page which allows them to add up to four options for the question. The view questions page displays a list of the questions which have been added so far, which are hyperlinked to allow the user to view, update and delete the associated options:  

![view questions]()  
Users can also update and delete questions, the app is set up so that deleting a question also removes the associated options.  


## Known Issues:
* Delete functionality is faulty


## Future Work:
* Custom error pages.
* Design for mobile display (for mobile web-app deployment)
* User accounts to retain custom accounts.
