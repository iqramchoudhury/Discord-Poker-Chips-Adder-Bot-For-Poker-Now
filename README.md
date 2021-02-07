## Background
 This bot was created in response to a discord server which had a large number of users who were using the poker now discord app
 as well as a significant number of user who were not. A problem arose when we wanted to add chips to all users playing without having to repeat the command for adding chips each time for every user. The code below creates a bot which calls the command for
 adding chips to all current players using a single command.

## Example
 ![Typing command image](Images/Command.png "Typing Command")
 ![Command result image](Images/Result.png "Command Result")

## Details
 The bot works on the basis that poker now has a downloadable folder which contains all the current players names when the
 command !pcr is called. After the name of the folder has been changed the bot iterates through the current players names
 and adds the chosen number of chips to them.

 To implement this bot in your server you must change a few things in my code given to you.


