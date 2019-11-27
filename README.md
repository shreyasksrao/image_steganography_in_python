# image_steganography_in_python
This python code hides the data(text) inside the image with encoding it using caesar cipher method.

Graphical User Interface is created with the standard python library Tkinter.

* User need to enter the text inside the "Enter the data to be encrypted" entry widget.
* Mandatory to enter the name of the PNG file inside which use want to hide the message.
* To save the encrypted file "Check the check box" and give some name for the output file with "PNG" extension.
* Regarding the cipher technique select 1 for Encryption level for single level ciphering technique(Caesar cipher is not an   effective mode for encoding your data because the attacker can easily brute-force the string) ,enter the key for the cipher.
* To retrieve the same string, the reciever should use the same key to decrypt the original text from cipher text. 
* click "Encode" button , after that click the "Encrypt/Decrypt" button. data will be encrypted in the image mentioned.
* To decrypt the data from the image, load the image by placing its name in the corresponding widget and then enter the correct ciphering details then click the Encrypt/Decrypt button to display the string at the bottom.
* It is possible to see the image by clicking the "Show image button", also it is possible to see the image in gray scale.
* Customise the background color according to user like.
