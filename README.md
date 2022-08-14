Update 1:
A 2-part project. The first part of the project is to allow communication between someone who can speak and someone who is deaf. While learning ASL or using a 
translator is always preferable for personal or professional connections, there are instances where this is not a feasible solution. And yes while many deaf people are espectially
astute at being able to read lips, in a stream or call camera quality can severely affect this ability. As such the first part of the code will take audio input and then from there
convert it to a series of either images and/or short signes clips to communicate this in signs. In the event a name or number is detected, the program will opt to instead sign a 
series of letters spelling out the name or number in ASL.

The second part is far simpler, on the end of the deaf person, they can sign to their hearts content and their program will use object detection to attempt to accurately guage what
the sign is and send a text message next to it to notify the non deaf communicator. An option to have it verbally say what the sign is rather than in text form is planned for later.
As it stands right now the code should be functioning, all there is thats left to do is fully assemble and gather the images/mp4 clips as needed to represent the signs. This can be
gathered from any reputable asl dictionary

Update 2:
After much trial and error with object detection, I finally managed to find a system that works. Utilizing the YOLO system for training a model I was able to test andd train a model successfully to recognize the difference between Autobot and Decepticon symbols. With this done on a smaller scale with only 2 classes, I will have to find somewhere where I can train the model with far more classes and a large amount of data for an effective dataset
