The approach our team took for this project was to focus on the structure of the program
and add additional features from there. The send program was broken down into two parts:
	1) Receiving a comfirmation that the window had fully been ACK'ed, and starting
	   to adjust RTO, window size, and other factors to increase efficiency
		- This also checked the 1st packet sent
	2) Sending the next window and confirming each subsequent ACK individually
If the first task would fail, the program would simply try to resend the first packet with
an adjusted RTO. If the second task were to fail, then the program would know that 
something timedout and would adjust the RTO and attempt to send the entire window again.

There were several things we wanted to do with ACK's, but ended up just using a single
ACK statement that would send duplicate ACK's if there was an error. It would also send
specially marked ACK copies in order to counteract dropping packets. We wanted to make 
use of a SACK system while keeping the data of ACK'ed packets to write once the next 
needed segment was properly delivered, however we had issues storing and printing the
data without errors so we resorted to just using a normal ACK. Besides that challenge,
we faced a lot of issues getting our RTO time and window size to work in various
circumstances. We had few problems with bad data, but mostly would have issues with
timeouts caused by lossy traffic.

The way that we tested our code was using the ./run, ./netsim, and ./test features to
run through as many situations as we could think of. We would generally make a change,
test it against perfect conditions to make sure it works, then test it against the
condition we were trying to counteract, and finally give it a go at the ./test group
of tests. We found overall success, but there were many cases that were just left
to chance, and we would often get unlucky with extremely lossy situations and would
timeout. Overall I think there would be a few things I wihs we could have done
differently from the get go, but did not want to scrap all of our work for just a
possible solution. 
