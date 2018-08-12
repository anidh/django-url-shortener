# Django Based URL Shortener
A Django web based application which takes a url and shortens the given url in from of 7.0.0.1:8000/{Some_Short_Url}. When the short url is generated the user can click on the given short url or can copy anc paste that url in the new tab.

#How it works

The url shortener first takes the long url and stores it into the database and assigns it a number. The number is then fed into a base62 conversion algorithm which takes the number and converts it to base62 with base 0-9A-Za-z. The short url which is generated is also stored in the databse. For resolution of short url to the long one we use the base 62 to Decimal algo to convert it back to deciaml number and using that number we query the database to get the long URL.

#Issues

No currently known issues. Test cases needs to be formed in future release.

#Future Features

The following features are scheduled to be added in the future releases-
1)Bootsrtapping the whole website. Adding appropriate CSS and JS where neccessary in very future releases there is a provison for adding React JS.
2)Count, Copy to clipboard and open in new window features to increasing the user experience.
3)Building a REST api. The REST api then can be used on the other site to shorten the URL on the other sites where it is neccessary.
4)Building a Google Chrome extension for the website which could in a click shorten the URL of the page on which user is currently on
5)Publishing the site on the server.

#Version

Shortify- 1.0.0

#Contributor

Anidh Singh
