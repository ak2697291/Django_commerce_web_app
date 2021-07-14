from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class auction_listing(models.Model):
    title = models.CharField(max_length = 64)
    description  = models.CharField(max_length=255)
    starting_bid = models.IntegerField()
    category =  models.CharField(max_length= 100)
    image_url = models.URLField()
    date = models.DateTimeField()
    user = models.CharField(max_length=65)
    status = models.IntegerField()
    def __str__(self):
        return f"{self.title , self.description , self.starting_bid, self.category , self.image_url, self.date, self.user,self.status}"


class bid(models.Model):
    item = models.ForeignKey(auction_listing,on_delete = models.CASCADE,related_name="bids")
    bids = models.IntegerField()
    title = models.CharField(max_length = 64)
    user = models.CharField(max_length=65)

    def __str__(self):
        return f"{self.item,  self.bids,self.title, self.user}"


class comments(models.Model):
    user = models.CharField(max_length=255)
    data = models.CharField(max_length= 255)
    title = models.CharField(max_length=64)
    date = models.DateTimeField()
    
    def __str__(self):
        return f"{self.user, self.data, self.title, self.date}"

class watchlist(models.Model):
    item = models.ForeignKey(auction_listing,on_delete = models.CASCADE,related_name="name")
    title = models.CharField(max_length=65)
    user = models.CharField(max_length=65)
    def __str__(self):
        return f"{self.item,self.title, self.user}"
class bidding_winner(models.Model):
    title = models.CharField(max_length=64)
    created_by = models.CharField(max_length=64)
    winner = models.CharField(max_length=64)
    winning_bid = models.IntegerField()
    date = models.DateTimeField()
    def __str__(self):
        return f"{self.title, self.created_by, self.winner, self.winning_bid, self.date}"


