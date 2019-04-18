Approach:
For our approach, we used a looping request structure that while attempting to keep-alive. The first set of our requests
are separate from our loop since they are individual requests that are different from the requests of the loop. Using these,
we log into fakebook and establish our cookies. Then from there we loop through our URI's that we get from the request, popping
each on off from our list and adding it to our visited list. Once we go through all of our frontier URI's, or get 5 secret
flags, the program stops and prints the files.

Challenges:
We had some challenges with getting the project running initially with setting cookies and formatting HTTP. Once we got those
finished, we had some challenges with 500 responses and keep-alive. We managed this through closing and re-opening the socket.

Debugging:
We initially used Wireshark and Chrome DevTools to start building our HTTP requests. Once we got a stable system, we used
internal print lines to finish off debugging.
