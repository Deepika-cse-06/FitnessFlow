import os
import django
from django.core.files import File
from pathlib import Path

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitness_project.settings')
django.setup()

from django.contrib.auth.models import User
from core.models import Trainer

def create_trainer(username, first_name, last_name, email, specialties, experience, bio, is_available=True):
    # Create user account for trainer
    user, created = User.objects.get_or_create(
        username=username,
        defaults={
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'is_staff': True
        }
    )
    
    if created:
        user.set_password('trainer123')  # Set a default password
        user.save()
    
    # Create or update trainer profile
    trainer, created = Trainer.objects.get_or_create(
        user=user,
        defaults={
            'specialties': specialties,
            'experience_years': experience,
            'bio': bio,
            'is_available': is_available
        }
    )
    
    return trainer

# Add sample trainers
trainers_data = [
    {
        'username': 'john.smith',
        'first_name': 'John',
        'last_name': 'Smith',
        'email': 'john.smith@fitnesshub.com',
        'specialties': 'Strength Training, Powerlifting, Nutrition',
        'experience': 8,
        'bio': 'Certified strength coach with 8 years of experience. Specializes in powerlifting and strength training. Helped numerous clients achieve their strength goals and improve their overall fitness.'
    },
    {
        'username': 'sarah.johnson',
        'first_name': 'Sarah',
        'last_name': 'Johnson',
        'email': 'sarah.johnson@fitnesshub.com',
        'specialties': 'Yoga, Pilates, Flexibility Training',
        'experience': 6,
        'bio': 'Certified yoga instructor and flexibility specialist. Passionate about helping clients improve their mobility, posture, and mind-body connection through yoga and pilates.'
    },
    {
        'username': 'mike.davis',
        'first_name': 'Mike',
        'last_name': 'Davis',
        'email': 'mike.davis@fitnesshub.com',
        'specialties': 'HIIT, CrossFit, Functional Training',
        'experience': 5,
        'bio': 'CrossFit Level 2 trainer specializing in high-intensity workouts and functional fitness. Focuses on helping clients build strength, endurance, and overall athletic performance.'
    },
    {
        'username': 'emily.wilson',
        'first_name': 'Emily',
        'last_name': 'Wilson',
        'email': 'emily.wilson@fitnesshub.com',
        'specialties': 'Weight Loss, Nutrition Coaching, Personal Training',
        'experience': 7,
        'bio': 'Certified personal trainer and nutrition coach. Expert in designing personalized weight loss programs and helping clients develop healthy, sustainable eating habits.'
    },
    {
        'username': 'david.brown',
        'first_name': 'David',
        'last_name': 'Brown',
        'email': 'david.brown@fitnesshub.com',
        'specialties': 'Sports Conditioning, Athletic Training, Injury Prevention',
        'experience': 10,
        'bio': 'Former professional athlete turned trainer with expertise in sports-specific training and injury prevention. Helps athletes of all levels improve their performance and reach their full potential.'
    }
]

def main():
    print("Adding trainers...")
    for trainer_data in trainers_data:
        trainer = create_trainer(**trainer_data)
        print(f"Added trainer: {trainer.user.get_full_name()}")
    print("Finished adding trainers!")

if __name__ == '__main__':
    main() 