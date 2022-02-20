# Design Your Own Tote Bag

Design Your Own Tote Bag is an interactive command line application that aims to give people a possibility to design a custom made tote bag out of reused material. The app iterates through a number of questions regarding fabrics and colors and, based on the user responses, a unique tote bag is created and presented to the user at the end.

The app is targeted towards people who are interested in sustainable solutions and design and use their own bag when shopping or carrying things around. 

Design Your Own Tote Bag will come in handy for those who want a unique tote bag that they have designed themselves. The inspiration comes from my daughter's small business that sews tote bags from old spinnakers, scrap furnishing fabrics and old textile belts.

A link to the live application can be found [here](https://design-your-own-tote-bag.herokuapp.com/), and a link to the repository [here](https://github.com/MarieCHessler/design-your-own-tote-bag).

![Design Your Own Tote Bag on different screen sizes](assets/images/layout_on_screens.webp)

<br>

## Table of contents
1. [UX](https://github.com/MarieCHessler/design-your-own-tote-bag#ux)
    * [User needs](https://github.com/MarieCHessler/design-your-own-tote-bag#user_goals)
    * [Owner goals]((https://github.com/MarieCHessler/design-your-own-tote-bag#owner_goals))

2. [Design](https://github.com/MarieCHessler/design-your-own-tote-bag#design)
    * [Color palette](https://github.com/MarieCHessler/design-your-own-tote-bag#color_palette)
    * [Structure](https://github.com/MarieCHessler/design-your-own-tote-bag#structure)

3. [Features](https://github.com/MarieCHessler/design-your-own-tote-bag#features)
    * 

4. [Technology used](https://github.com/MarieCHessler/design-your-own-tote-bag#technology-used)

5. [Testing](https://github.com/MarieCHessler/design-your-own-tote-bag#testing)
    * 

6. [Bugs](https://github.com/MarieCHessler/design-your-own-tote-bag#bugs)
    * 

7. [Deployment](https://github.com/MarieCHessler/design-your-own-tote-bag#deployment)
    * [Heroku](https://github.com/MarieCHessler/design-your-own-tote-bag#heroku)

8. [Credits](https://github.com/MarieCHessler/design-your-own-tote-bag#credits)
    * [Content](https://github.com/MarieCHessler/design-your-own-tote-bag#content)
    * [Special thanks to](https://github.com/MarieCHessler/design-your-own-tote-bag#special-thanks-to)

<br>

## UX

### User needs
As a user, I would like a program that:
* Is easy to understand and use.
* Has an appealing layout.
* Saves the data in a spreadsheet, so it is possible to return to previous designs.
* Shows me the result at the end of the design process.
* Explains how I can return to a previous design.

### Owner goals
As a program owner, I would like to create a tool that:
* Helps the user to create a tote bag in a unique design.
* Is easy to understand and use and has an appealing look.
* Validates the data to make sure the result is correct and easy to understand.
* Saves the data and can return the design to the user, both straight away and later.


## Design

<br>

![Design Your Own Tote Bag color palette](assets/images/colors.webp)

### Color palette
* The colors that have been used in this application were produced by using Colorama and Termcolor libraries.
    * **Blue** for information, such as the introduction and the information and instructions at the end.
    * **Cyan** for questions to the user.
    * **Green** for comments on choices and final design.
    * **White** is the standard color, which is left unchanged for user input and save messages.
    * **Red** for error messages.
* The colors are chosen to give a good contrast, yet be comfortable for the user's eyes, on a black background. 
* Blue, cyan, and green match each other well, and white is a good complement.
* Red sticks out and therefore is a good choice to have the user react to the message.

### Structure
A structure for Design Your Own Tote Bag was drafted on paper at the beginning of project process, and later improved using Lucidchart, to make it more appealing and easier to understand.

The flowchart shows the different steps and checks the program follows, based on the different choices the user makes along the way.

<br>

![Flowchart showing program structure](assets/images/flowchart.webp)


## Features
The features described below have been implemented for the user to have a pleasant experience.

**Introduction, with logo and welcome**
* When starting the program ASCII ART logo, showing the name Tote Bag Design, appears. This helps the user know that he or she is in the right place. 
* Below the logo there is a headline in bold, welcoming the user, and an introduction with a bit of information about what the company does and what the user can do in the application. With this information, the user is prepared when it is time to make the first choice.

![Logo and introduction](assets/images/intro.webp)

<br>

**Choice between new and existing design**
* The first choice the user makes is if he or she wants to create a new design or pick up one that has been created earlier. Giving the user this choice is good, since he or she may already have a design that he or she is happy with.

![Choice new design](assets/images/new_choice.webp)
![Choice existing design](assets/images/existing_choice.webp)


