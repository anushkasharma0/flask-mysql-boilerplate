# Dine Diary

## Project Overview
  These days, there are so many options for eating out at restaurants, whether they’re fine dining or fast casual. These restaurants can be hard to keep track of given that you visit them over longer periods of time, so having a way to organize the information would be helpful. 
  
  Our application would allow users to input their restaurant visits, including the dishes they ordered, so they can refer back to the application when recommending or revisiting a spot. It would include user information like name, email, dietary restrictions, primary locations, and a unique user id. The restaurant information that would be tracked would be the cuisine, category (casual, sit-down, fine), and the general price range. For each visit, we would track the first and last date the user visited it, the user-given rating, and the guests who went with them. Also for each visit, we’d have capabilities for the users to input the name of the dish they got, category (entree, appetizer, dessert), a description, and a review. 
  
  This app would revolutionize the way that people keep track of their favorite spots and the specific dishes they enjoyed at those spots. We’d expect a wide variety of users to be able to use the app regardless of age, dietary preferences, and other factors. 

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 




