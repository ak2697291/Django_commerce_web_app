from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.db.models import Max
import datetime


from .models import User,auction_listing,bid,comments,watchlist,bidding_winner


def index(request):
    active_listing = auction_listing.objects.filter(status = 1)

    return render(request, "auctions/index.html",{
        "listings":active_listing
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create_listing(request):
    return render(request,"auctions/create_listing.html")

def create_listing_send(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        starting_bid  = request.POST["starting_bid"]
        category  = request.POST["category"]
        image_url = request.POST["image_url"]
        user = request.POST["username"]
        
        listing = auction_listing(title = title,description = description,starting_bid = starting_bid,category=category,image_url=image_url,date = datetime.datetime.now(),user=user,status = 1)
        listing.save()
        return HttpResponseRedirect(reverse("create_listing"))
        

def categories(request):
    filtered_listing = auction_listing.objects.filter(status=1) 
    categories = filtered_listing.values_list('category')
    ctgries = []
    for category in categories:
        ctgries.append(category[0])
    return render(request,"auctions/categories.html",{
        "categories": ctgries
    })

def category_list(request):
    if request.method == "POST":
        category = request.POST["category"]
        items = auction_listing.objects.filter(category = category, status=1)
        return render(request,"auctions/category_list.html",{
            "items": items,
            "category_name" : request.POST["category"].upper()
        })


def watchlist_show(request):
    list = []

    items = watchlist.objects.filter(user = request.user.username)
    print(items)
    for item in items:
        
        list.append(auction_listing.objects.filter(title = item.title,status = 1)[0])
       
    return render(request, "auctions/watchlist.html",{
        "list": list
    })



def listing_page(request):
    if request.method == "POST":
        title = request.POST["listing"]
        listing  = auction_listing.objects.filter(title = title)
        comment = comments.objects.filter(title = title)
        bid_values = bid.objects.filter(title= title) 
        check_watchlist = watchlist.objects.filter(title = title,user = request.user.username)
        current_user = request.user.username
        parent_user = listing[0].user 
        if check_watchlist:
            watchlist_item = check_watchlist[0]
            
        else:
            watchlist_item = None
        
        if comment:
            comments_data = comment
        else:
            comments_data = None
        if bid_values:
            max_bid = bid_values.aggregate(Max('bids'))
            current_bid = list(max_bid.values())[0]
        else:
            current_bid = listing[0].starting_bid
        
        if parent_user == current_user:
            authority = 1
        else:
            authority = 0
        
        if listing[0].status:
            close =0
        else:
            close = 1
        return render(request,"auctions/listing_page.html",{
            "listing" : listing[0], 
            "check_watchlist":watchlist_item,
            "comments_data": comments_data,
            "current_bid": current_bid,
            "authority": authority,
            "close":close
        })
def watchlist_add(request):
    if request.method == "POST":
        title = request.POST["add"]
        item  = auction_listing.objects.filter(title = title,status=1)
        watchlist1 = watchlist(item = item[0],title = title,user = request.user.username)
        watchlist1.save()
        current_user = request.user.username
        parent_user = item[0].user 
        comment = comments.objects.filter(title = title)
        bid_values = bid.objects.filter(title= title)
        if comment:
            comments_data = comment
        else:
            comments_data = None
        if bid_values:
            max_bid = bid_values.aggregate(Max('bids'))
            current_bid = list(max_bid.values())[0]
        else:
            current_bid = item[0].starting_bid 
        if parent_user == current_user:
            authority = 1
        else:
            authority = 0
        return render(request,"auctions/listing_page.html",{
            "listing" : item[0],
            "check_watchlist": watchlist1,
            "comments_data": comments_data,
            "current_bid": current_bid,
            "authority": authority
            })


def watchlist_remove(request):
    if request.method == "POST":
        title = request.POST["remove"]
        
        item  = auction_listing.objects.filter(title = title,status=1)
        watchlist.objects.filter(title = title,user = request.user.username).delete()
        comment = comments.objects.filter(title = title)
        bid_values = bid.objects.filter(title= title)
        current_user = request.user.username
        parent_user = item[0].user 

        if comment:
            comments_data = comment
        else:
            comments_data = None
        if bid_values:
            max_bid = bid_values.aggregate(Max('bids'))
            current_bid = list(max_bid.values())[0]
        else:
            current_bid = item[0].starting_bid 
        
        if parent_user == current_user:
            authority = 1
        else:
            authority = 0
        return render(request,"auctions/listing_page.html",{
            "listing" : item[0],
            "check_watchlist": None,
            "comments_data": comments_data,
            "current_bid": current_bid,
            "authority": authority
        })


def add_comments(request):
    if request.method == "POST":
        title = request.POST["title"]
        data = request.POST["comment_data"]
        comment1 = comments(user = request.user.username,data= data,title = title, date = datetime.datetime.now())
        comment1.save()
        listing  = auction_listing.objects.filter(title = title,status = 1)
        comment = comments.objects.filter(title = title)
        bid_values = bid.objects.filter(title= title) 
        check_watchlist = watchlist.objects.filter(title = title,user = request.user.username)
        current_user = request.user.username
        parent_user = listing[0].user 
        if check_watchlist:
            watchlist_item = check_watchlist[0]
            
        else:
            watchlist_item = None
        
        if comment:
            comments_data = comment
        else:
            comments_data = None
        if bid_values:
            max_bid = bid_values.aggregate(Max('bids'))
            current_bid = list(max_bid.values())[0]
        else:
            current_bid = listing[0].starting_bid
        
        if parent_user == current_user:
            authority = 1
        else:
            authority = 0
        return render(request,"auctions/listing_page.html",{
            "listing" : listing[0], 
            "check_watchlist":watchlist_item,
            "comments_data": comments_data,
            "current_bid": current_bid,
            "authority": authority
        })

def add_bid(request):
    if request.method == "POST":
        title = request.POST["title"]
        bid_amount = request.POST["bid_amount"]
        item = auction_listing.objects.filter(title = title,status = 1)
        listing  = auction_listing.objects.filter(title = title)
        comment = comments.objects.filter(title = title)
        bid_values = bid.objects.filter(title= title) 
        check_watchlist = watchlist.objects.filter(title = title,user = request.user.username)
        current_user = request.user.username
        parent_user = listing[0].user 
        if check_watchlist:
            watchlist_item = check_watchlist[0]
            
        else:
            watchlist_item = None
        
        if comment:
            comments_data = comment
        else:
            comments_data = None
        if bid_values:
            max_bid = bid_values.aggregate(Max('bids'))
            current_bid = list(max_bid.values())[0]


        else:
            current_bid = listing[0].starting_bid
        
        
        if int(bid_amount) >= current_bid:
            make_bid = bid(title = title,user = request.user.username, bids = bid_amount,item = item[0])
            make_bid.save()
            current_bid = int(bid_amount)
            status = 1 
        else:
            status = 0

        if parent_user == current_user:
            authority = 1
        else:
            authority = 0
        return render(request,"auctions/listing_page.html",{
            "listing" : listing[0], 
            "check_watchlist":watchlist_item,
            "comments_data": comments_data,
            "current_bid": current_bid,
            "making_bid": 1,
            "status":status,
            "authority": authority
        })




def delete_listing(request):
    if request.method =="POST":
        title = request.POST['title']
        listing = auction_listing.objects.filter(title = title)
        bid_values = bid.objects.filter(title= title)
        watchlist.objects.filter(title = title).delete()
        if bid_values:
            max_bid = bid_values.aggregate(Max('bids'))
            current_bid = list(max_bid.values())[0]
            users = bid_values.filter(bids = current_bid)
            winner = users[0].user


        else:
            current_bid = listing[0].starting_bid
            winner = listing[0].user


        created_by = listing[0].user
        
        winner_add = bidding_winner(title = title,created_by=created_by,winner = winner,winning_bid=current_bid,date = datetime.datetime.now())
        winner_add.save()
        close_listing = auction_listing.objects.get(title = title)
        close_listing.status = 0
        close_listing.save()
        comment = comments.objects.filter(title = title)
        if comment:
            comments_data = comment
        else:
            comments_data = None
        close = 1

        return render(request,"auctions/listing_page.html",{
            "listing":listing[0],
            "winner":winner,
            "winning_bid":current_bid,
            "close":close,
            "comments_data":comments_data,
            "authority": 0
            
        })

