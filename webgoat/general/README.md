# HTTP Basics
We can see a form where when we enter our name, we get it inverted by the server.
After we get two questions:
* Was the HTTP command a POST or a GET
* What is the magic number
It was a POST request, we can check it with burp for example, and for the magic number, we just have to intercept the data with burp to get the magic_number query parameter value.

# HTTP Proxies
Similar to the previous one, but now we have to alter the request, changing the method:
* Changing the Method from POST to GET
* Changing the changeMe from the body and insert it in the URL as query string parameter, being the value "Requests are tampered easily" (we have to replace spaces with `+` or `%20` as we desire.
* Add a header `x-request-intercepted:true`

# Developer Tools
Here, we have to use the chrome/firefox... console to send this function `webgoat.customjs.phoneHome()` and pass the value we receive, being careful of disabling burp intercept mode first.

In the next one, we have to use the developer mode in our browser instead of BURP to read the HTTP request being made and entering that value.

# CIA Triad
Quiz:
* 1 -> 3
* 2 -> 1
* 3 -> 4
* 4 -> 2
