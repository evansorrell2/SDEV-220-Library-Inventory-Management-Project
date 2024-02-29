from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError

class Item(models.Model):
    title = models.CharField(max_length=200, help_text="Enter the title of the item")
    description = models.TextField(help_text="Enter the description of the item", default="No description available.")  # Set a default at the base class level
    class Meta:
        abstract = True

class Book(Item):
    author = models.CharField(max_length=100, help_text="Enter the author's name")
    publisher = models.CharField(max_length=100, help_text="Enter the publisher's name")
    book_type = models.CharField(max_length=100, help_text="Enter the book category (e.g., Fiction, Non-Fiction, Science, etc.)", default="General")

    def __str__(self):
        return self.title
class Video(Item):
    director = models.CharField(max_length=100, help_text="Enter the director's name")
    release_year = models.IntegerField()
    video_type = models.CharField(max_length=100, help_text="Enter the video category (e.g., Movie, Documentary, Series, etc.)", default="General")

    def clean(self):
        if self.release_year < 1900 or self.release_year > timezone.now().year:
            raise ValidationError("Release year must be between 1900 and the current year.")
    def __str__(self):
        return self.title

class Game(Item):
    platform = models.CharField(max_length=100, help_text="Enter the platform of the game(e.g., PC, PS4, etc.)")
    genre = models.CharField(max_length=100, help_text="Enter the genre of the game") 
    game_type = models.CharField(max_length=100, help_text="Enter the game category (e.g., Action, Sports, etc.)", default="General")

    def __str__(self):
        return self.title
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, blank=True, null=True, help_text="Enter phone number")
    address = models.TextField(blank=True, null=True, help_text="Enter address")

    def __str__(self):
        return self.user.username

class BorrowRecord(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    borrower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='borrowed_items')
    borrow_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(null=True, blank=True)

    def days_until_return(self):
        if not self.return_date:
            return 'Return date not set'
        now = timezone.now()
        if self.return_date > now:
            return (self.return_date - now).days
        return 'Past due'

    def __str__(self):
        item_title = self.item.title if self.item else 'Item deleted'
        return f'{item_title} borrowed by {self.borrower.user.username} on {self.borrow_date.strftime("%Y-%m-%d")}'
