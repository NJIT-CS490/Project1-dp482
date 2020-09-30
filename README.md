This is one way of using the Twitter API to collect the tweets.

To get the correct result, you must follow along with the steps.

1. Create a Twitter developer account using your edu email to get approved right away.
2. Get your API and other secrets keys from the Twitter developer dashboard. (Make sure the secrets keys are safe and not accessible by anyone)
3. In your AWS Cloud 9 terminal, install tweepy and flask. (Sudo pip install x is the preferred method)
4. Create a directory to store your python and other files.
5. Make two subdirectories in the current directory from step 4. (Templates and Static).
6. CD to the main directory from step four and create a python file.
7. CD the directory to static and add a css file.
8. CD the directory to templates and add an env and html file.
9. In your main directory add .gitignore file and save the env file in the ignore file to hide the secret keys.
10. Before running your python file, you must source the env file from the templates directory to avoid the error.
11. For to run the python file, use the python command, and click on the preview running application to see the output.

Technical Issues

1. One of the main issues that I was facing was the fetched tweets were not fully printing. The tweets were getting cut, and it was printing only some contents and end it with three dots.  For the solution, I used an online source.
2. The other issue was personal email sign up for the twitter developer. I signed up at night, but until the next morning, the account was not ready to be used. For this issue, I decided to follow what the professor said and used my .edu email and got instant approval.

Current Issue

1. The current issue that I still have is to manually source the env file before running the python file.  I have acknowledged this issue from day one, but I did not pay attention to it because I was using the second option. The best possible solution is to ask the group members for help, and if that does not work, I should talk to the TA's.


Part- 2 (Spoonacular API for the Recipes and other information)

Follow the steps to get the correct results.

1. Create a Spoonacular recipe and food API account using your email. 
2. Get your API key and save it in the env file. (Make sure to put the env file in the .gitignore to keep your keys safe)
3. Set up a Heroku account for the end but to make it easier it's better to do it now.
4. Use Spoonacular API in your python file to collect information based on the category. ( Example - Search for Serving size, Search for the recipe, Search for Prep time)
5. Create an HTML and CSS file for the layout of the collected information.
6. After getting all the information in part 2 combine the code from part 2 to the original code.
7. Use git branch, git commit, git merge to combine the code.
8. Update the CSS and HTML files according to the required layout.
9. SIDE note - ( Spoonacular recipe and food API has only 150 requests/response limit)
10. Download npm install -g Heroku and login to it using the terminal in AWS cloud9.
11. To make the result viewable to anyone use the Heroku method to generate a link.
12. Use the terminal from AWS cloud9 to push all the files to Heroku.
13. You must add your secret keys to Heroku on the Heroku website for the link to work.

Technical Issue


1 - I had an issue with the Spoonacualr account. I reached my limit and waited almost a day because it said that the user gets 150 requests/responses per day, and that didn't happen. The best solution was to create a second account and update my secret key.

2 - I had an issue pushing my files. I asked my group member for help, and I was told to do a git pull and then, push the files. 



