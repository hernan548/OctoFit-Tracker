from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Team, Activity, Leaderboard, Workout

User = get_user_model()

class BasicModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_activity_creation(self):
        activity = Activity.objects.create(user='testuser', type='Run', duration=10)
        self.assertEqual(str(activity), 'testuser - Run')

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(team='Test Team', points=100)
        self.assertEqual(str(lb), 'Test Team: 100')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='desc')
        self.assertEqual(str(workout), 'Test Workout')
