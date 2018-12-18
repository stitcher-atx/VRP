# VRP
Using Python 3.5 and various Google Api and others to solve the Vehicle Routing Problem

So I have built VRP solver by modifying the Googles OR-tools demo they have in the developer guide. Yeah! Problem solved. That felt like cheating, and karma agreed! I lost that solution to the VRP, thanks to a windows update/reboot, so I am going recode it! Like from scratch. Mostly. I dunno. So far I am on kinda the right track. I'll probably use the OR-Tools solver, at bare minimum, or I might try Pulp or other libraries to finish out this project's framework and solver if I am feeling overly ambitious.


AS OF 12/17/18

I have 2 parts complete in this project. Geocode.py and distancematrix.py work in unison to take a csv file, pull locations out and covert them to lat/long coordinates, figure out distance from each location to each location, and return the distances into a data frame.
Check out the sweet picture below to see distancematrix.py final out put.

![distance matrix](https://i.ibb.co/vPt4n8C/distancematrix.jpg)

That's a sexy data frame. And it only takes like 30 seconds to generate... Oh, I'm not a professional coder. Aspiring, sure, so suggestions to optimize sections of code are appreciated. 


If you wanna follow along by using my code you will need to get an Api key to use Google DistanceMatrix Api and probably maps as well. 

NEXT UP

I need to set objectives and code constraints. That part about "bare minimum" or "feeling overly ambitious" applies very strongly to how I approach solving these next couple of tasks.
