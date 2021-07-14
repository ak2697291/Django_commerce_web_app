from django.contrib import admin
from .models import User,auction_listing,bid,comments,watchlist,bidding_winner

# Register your models here.


admin.site.register(User)
admin.site.register(auction_listing)
admin.site.register(bid)
admin.site.register(comments)
admin.site.register(watchlist)
admin.site.register(bidding_winner)