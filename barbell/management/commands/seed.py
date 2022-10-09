from django.core.management.base import BaseCommand, CommandError
from barbell.models import User

class Command(BaseCommand):
    def __init__(self):
        super().__init__()
    
