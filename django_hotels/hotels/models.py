from django.db import models

# Create your models here.


class Hotel(models.Model):
    """Declaration of the Hotel object."""

    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    rating = models.IntegerField()
    is_open = models.BooleanField(default=True)

    def __repr__(self):
        return f'<Hotel: { self.name } | location - { self.location }>'

    def __str__(self):
        return f'{ self.name }'


class Room(models.Model):
    ROOM_CHOICES = [
        ('twin', 'Twin'),
        ('double', 'Double'),
        ('queen', 'Queen'),
        ('deluxe', 'Deluxe Suite'),
        ('family', 'Family Suite'),
        ('pent', 'Penthouse')
    ]
    size = models.CharField(choices=ROOM_CHOICES, max_length=10, default='twin')
    room_num = models.CharField(max_length=5)
    floor = models.IntegerField()
    vacancy = models.BooleanField(default=True)
    smoking = models.BooleanField(default=False)
    hotel = models.ForeignKey(Hotel, related_name='rooms')

    def __repr__(self):
        return f'<Room: hotel - { self.hotel.name } | num - { self.room_num }>'
