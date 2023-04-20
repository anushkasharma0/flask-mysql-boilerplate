# Dine Diary

## Project Overview
  Dine Diary is the ultimate restaurant reviewing app that puts the power of food exploration and sharing in your hands! With Dine Diary, you can easily track and rate all the places you've dined, while also creating and sharing your own personalized restaurant reviews and content with your followers.

  You can keep a record of your favorite spots, and make notes of various different aspects of restaurants such as their service, ambiance, menu, and more. Also, you can snap mouthwatering photos of your meals, add ratings and comments, and share your culinary adventures with your friends, family, and fellow foodies.

  But Dine Diary isn't just about tracking and sharing your foodie journeys - it's also a community of passionate food lovers who connect, share tips, and inspire each other. Discover new places through the recommendations of like-minded foodies, and join discussions on the latest food trends and restaurant hotspots.

  Whether you're a casual diner or a seasoned food critic, Dine Diary is your go-to app for keeping track of your dining experiences, sharing your foodie content, and being part of a vibrant foodie community. 

## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
1. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
1. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
1. Build the images with `docker compose build`
1. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 

## Link to Project Video:




