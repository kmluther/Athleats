# Capstone Project - Athleats

Component Tree

├── CONTRIBUTING.md
├── LICENSE.md
├── Pipfile
├── Pipfile.lock
├── README.md
├── client
│   ├── README.md
│   ├── node_modules
│   ├── package-lock.json
│   ├── package.json
│   ├── public
│   └── src
|       ├── assets
|       ├── components
|           ├── Home
|           ├── SignUpForm
|           ├── AthleteProfile
|           ├── ActivityForm
|           ├── ActivityPage
|           ├── ActivityCard
|           ├── MealCard
|           ├── MealPage
|           ├── Menu
|           ├── Navigation
|       ├── app.css
|       ├── app.js
|       ├── index.css
|       ├── index.js
└── server
    ├── app.py
    ├── config.py
    ├── migrations
    ├── models.py
    └── seed.py

## User Stories

- New athletes can create a profile. Existing athletes can login to their profile.
- Athletes can upload activities using a form.
- Activities are added to athletes profile showing calories burned and recommended macronutrients for recovery.
- Athletes can find meals that match their recommended nutrients.
- Athletes can view recipes for meals and add meals to their menu.

## Stretch User Stories

- Athletes can upload activities using a GPX file.

## Wireframe

https://www.figma.com/file/H3nSZaQMSFyy6JOpKzTnw7/Final-Project?node-id=0%3A1&t=1UYUknGWAETxvqlY-1

## ORM 

https://dbdiagram.io/d/64497ec56b319470514146ae

## Algorithms

### Macronutrient Ratio:

60/20/20 Ratio for Carbohydrates/Proteins/Fats

### Calories Burned Calculation:

Calories/kcals = activity(METs) x weight(kilograms) x duration(hours)

## Technologies

- React
- Redux
- Bootstrap
- Flask
- SQLAlchemy

### References:

- Meal Nutrition API -> https://rapidapi.com/spoonacular/api/recipe-food-nutrition/
