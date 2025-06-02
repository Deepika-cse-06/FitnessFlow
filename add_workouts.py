import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitness_project.settings')
django.setup()

from core.models import WorkoutCategory, WorkoutPlan
from django.utils.text import slugify

# Create Categories
categories = [
    {
        'name': 'Cardio',
        'description': 'Cardiovascular exercises to improve heart health and endurance.',
    },
    {
        'name': 'Strength Training',
        'description': 'Resistance training exercises to build muscle and strength.',
    },
    {
        'name': 'Calisthenics',
        'description': 'Bodyweight exercises for strength, flexibility, and agility.',
    },
    {
        'name': 'Full Body',
        'description': 'Comprehensive workouts targeting all major muscle groups.',
    }
]

# Create or update categories
for cat_data in categories:
    category, created = WorkoutCategory.objects.get_or_create(
        name=cat_data['name'],
        defaults={
            'description': cat_data['description'],
            'slug': slugify(cat_data['name'])
        }
    )
    print(f"{'Created' if created else 'Updated'} category: {category.name}")

# Workout Plans
workouts = [
    {
        'title': 'Beginner Running Program',
        'description': 'A 6-week program designed for beginners to build running endurance. Includes walk-run intervals, gradually increasing running duration. Perfect for those aiming to run their first 5K.',
        'category_name': 'Cardio',
        'duration_weeks': 6,
        'difficulty_level': 'beginner'
    },
    {
        'title': 'Advanced Runner\'s Training',
        'description': 'An 8-week intensive running program for experienced runners. Includes interval training, hill runs, and speed work. Ideal for improving 10K times and preparing for half marathons.',
        'category_name': 'Cardio',
        'duration_weeks': 8,
        'difficulty_level': 'advanced'
    },
    {
        'title': 'Dumbbell Strength Fundamentals',
        'description': 'A comprehensive 4-week dumbbell program covering all major muscle groups. Learn proper form and basic strength training principles with dumbbells.',
        'category_name': 'Strength Training',
        'duration_weeks': 4,
        'difficulty_level': 'beginner'
    },
    {
        'title': 'Advanced Dumbbell Sculpting',
        'description': 'An intense 6-week dumbbell program featuring supersets, drop sets, and complex movements. Perfect for building muscle and strength with minimal equipment.',
        'category_name': 'Strength Training',
        'duration_weeks': 6,
        'difficulty_level': 'advanced'
    },
    {
        'title': 'Pull-up Progression Program',
        'description': 'A structured 8-week program to master pull-ups. Starting from dead hangs and negative pull-ups to achieving multiple clean pull-ups.',
        'category_name': 'Calisthenics',
        'duration_weeks': 8,
        'difficulty_level': 'intermediate'
    },
    {
        'title': 'Bodyweight Mastery',
        'description': 'A 6-week calisthenics program featuring pull-ups, push-ups, and advanced bodyweight movements. Develop strength, control, and body awareness.',
        'category_name': 'Calisthenics',
        'duration_weeks': 6,
        'difficulty_level': 'advanced'
    },
    {
        'title': 'Squat Challenge',
        'description': 'A 4-week program focused on squat variations and lower body strength. Progress from basic squats to advanced variations while building leg strength and stability.',
        'category_name': 'Strength Training',
        'duration_weeks': 4,
        'difficulty_level': 'intermediate'
    },
    {
        'title': 'Total Body Transformation',
        'description': 'A comprehensive 12-week full body workout program combining strength training, cardio, and flexibility work. Perfect for overall fitness improvement.',
        'category_name': 'Full Body',
        'duration_weeks': 12,
        'difficulty_level': 'intermediate'
    },
    {
        'title': 'Full Body Express',
        'description': 'An efficient 4-week program featuring 30-minute full body workouts. Ideal for busy individuals looking to maintain fitness with time-efficient workouts.',
        'category_name': 'Full Body',
        'duration_weeks': 4,
        'difficulty_level': 'beginner'
    },
    {
        'title': 'Ultimate Full Body Challenge',
        'description': 'An intense 8-week program combining strength training, HIIT, and endurance work. Features complex movements and challenging workouts for advanced fitness enthusiasts.',
        'category_name': 'Full Body',
        'duration_weeks': 8,
        'difficulty_level': 'advanced'
    }
]

# Create or update workout plans
for workout_data in workouts:
    category = WorkoutCategory.objects.get(name=workout_data['category_name'])
    workout, created = WorkoutPlan.objects.get_or_create(
        title=workout_data['title'],
        defaults={
            'description': workout_data['description'],
            'category': category,
            'duration_weeks': workout_data['duration_weeks'],
            'difficulty_level': workout_data['difficulty_level'],
            'slug': slugify(workout_data['title'])
        }
    )
    print(f"{'Created' if created else 'Updated'} workout: {workout.title}")

print("\nWorkout plans have been added successfully!") 