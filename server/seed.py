from app import app
from models import Athlete, Activity, Meal, db
from werkzeug.security import generate_password_hash

# create a list of primary sports
with app.app_context():

    Athlete.query.delete()
    Activity.query.delete()
    Meal.query.delete()

    athletes = [
        Athlete(
            username="johndoe",
            email="johndoe@example.com",
            _password_hash=generate_password_hash("password123"),
            age=25,
            weight=165,
            primary_sport="Run"
        ),
        Athlete(
            username="janedoe",
            email="janedoe@example.com",
            _password_hash=generate_password_hash("password456"),
            age=30,
            weight=150,
            primary_sport="Bike"
        ),
        Athlete(
            username="bobsmith",
            email="bobsmith@example.com",
            _password_hash=generate_password_hash("password789"),
            age=40,
            weight=180,
            primary_sport="Run"
        ),
        # Add more athletes here
    ]

    # add athletes to database
    for athlete in athletes:
        db.session.add(athlete)

    # create a list of activity types
    activities = [
        Activity(
            athlete_id=1,
            type="Run",
            distance=5,
            time=30,
            pace=6,
            calories_burned=300
        ),
        Activity(
            athlete_id=2,
            type="Bike",
            distance=10,
            time=45,
            pace=12,
            calories_burned=400
        ),
        Activity(
            athlete_id=3,
            type="Run",
            distance=8,
            time=50,
            pace=7,
            calories_burned=450
        ),
        Activity(
            athlete_id=2,
            type="Run",
            distance=6,
            time=45,
            pace=7,
            calories_burned=400
        ),
        Activity(
            athlete_id=1,
            type="Bike",
            distance=20,
            time=70,
            pace=15,
            calories_burned=600
        ),
        Activity(
            athlete_id=3,
            type="Run",
            distance=10,
            time=80,
            pace=8,
            calories_burned=600
        ),
        # Add more activities here
    ]

    # add activities to database
    for activity in activities:
        db.session.add(activity)

    meals = [
        Meal(name='Grilled Chicken Salad', calories=400, fats=15, carbs=20, proteins=45, recipe='Grill chicken and add to mixed greens with avocado, tomatoes, and vinaigrette.'),
        Meal(name='Beef and Broccoli Stir Fry', calories=500, fats=20, carbs=40, proteins=35, recipe='Sauté beef with garlic and ginger, add broccoli, and stir fry in soy sauce.'),
        Meal(name='Roasted Vegetable Quinoa Bowl', calories=350, fats=10, carbs=50, proteins=15, recipe='Roast vegetables of your choice and mix with cooked quinoa, chickpeas, and a lemon-tahini dressing.'),
        Meal(name='Turkey Chili', calories=350, fats=10, carbs=35, proteins=30, recipe='Brown ground turkey with onions and garlic, add canned tomatoes, beans, chili powder, and simmer.'),
        Meal(name='Salmon and Sweet Potato', calories=450, fats=20, carbs=30, proteins=35, recipe='Roast salmon and sweet potato with olive oil and lemon, serve with steamed vegetables.'),
        Meal(name='Chicken and Broccoli Alfredo', calories=550, fats=25, carbs=50, proteins=30, recipe='Sauté chicken and broccoli, add cooked pasta and Alfredo sauce.'),
        Meal(name='Spinach and Feta Stuffed Chicken', calories=400, fats=15, carbs=10, proteins=50, recipe='Butterfly chicken breast, stuff with spinach and feta, bake in the oven.'),
        Meal(name='Veggie Omelette', calories=300, fats=15, carbs=10, proteins=25, recipe='Whisk eggs with vegetables of your choice, cook in a non-stick pan.'),
        Meal(name='Tuna Salad Sandwich', calories=350, fats=15, carbs=30, proteins=25, recipe='Mix canned tuna with mayonnaise and chopped celery, serve on whole grain bread with lettuce and tomato.'),
        Meal(name='Mediterranean Grain Bowl', calories=400, fats=15, carbs=50, proteins=20, recipe='Mix cooked farro with roasted vegetables, hummus, olives, and feta cheese.'),
        Meal(name='Beef and Barley Soup', calories=350, fats=10, carbs=40, proteins=25, recipe='Sauté beef with onions and garlic, add carrots, celery, barley, and beef broth, simmer.'),
        Meal(name='Chicken Tacos', calories=400, fats=15, carbs=30, proteins=35, recipe='Grill chicken and serve on corn tortillas with lettuce, tomato, and salsa.'),
        Meal(name='Pesto Pasta with Shrimp', calories=500, fats=20, carbs=50, proteins=30, recipe='Cook pasta, sauté shrimp with garlic and olive oil, mix with pesto sauce.'),
        Meal(name='Turkey Burger', calories=400, fats=15, carbs=30, proteins=35, recipe='Grill turkey burger and serve on whole wheat bun with lettuce, tomato, and avocado.'),
        Meal(name='Stuffed Peppers', calories=350, fats=10, carbs=35, proteins=25, recipe='Stuff bell peppers with ground beef, rice, and tomato sauce, bake in the oven.')
    ]
    db.session.add_all(meals)

    db.session.commit()

    print('Done!')