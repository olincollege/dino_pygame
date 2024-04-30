# Home

_**Authors: Toby Mallon, Kenneth Xiong, Rewa Purohit**_

----
## Introductions
We set out to recreated the Chrome dino game on python. BUT! With one small addition. The dinosaur will be controlled not only with keyboard input, but also with computer vision input from the player. The player has to physically jump and crouch to control the dinosaur.
<video controls>
<source src="SoftDes.mp4" type="video/mp4">
</video>



## Methods
We accomplished this methods by using a few external packages. For all of our game code, we leveraged **pygame**. For the pose detection used for human input, we used Google's **MediaPipe**. Specifically, we use their pre trained pose landmarker model. Of course, we also scrapped the assets for the game off of **Google Chrome** itself.

## Installation
Installation instructions are available on the [GitHub](https://github.com/olincollege/dino_pygame).