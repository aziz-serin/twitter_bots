#        Twitter Bot        

---------------------------------------------
   Contents:
---------------------------------------------
1. What is a Twitter Bot?
2. How to install pip3
3. How to install the required libraries
4. How to use this application

---------------------------------------------
   ### 1. What is a Twitter Bot
---------------------------------------------
<p>Twitter bot is an application where you can use Twitters API to engage with other users, post tweets,
scrape Twitters data and many more. When it is considered that 15% of twitter users are actually bots, it does not hurt to build
one for yourself. You can experiment with the provided scripts in this repo and edit and/or use them however you like.</p>

---------------------------------------------
 ###  2. How to install pip3
---------------------------------------------
<p>This application uses some non-standard python 3.8 packages which need to be installed using pip3.
In the instance where you're unsure if your device has pip3 installed, please continue following this section.
Alternatively, if your device does have pip3 installed but simply lacks the required libraries, please install them by refering to "3. How to install the required libraries".</p>

<pre>You can check to see if pip3 is installed on your device via:
Windows:            py -m pip --version
Unix/macOS:         python -m pip --version
Linux:              pip3 --version</pre>

<pre>If pip3 is not found, then please install it by referring to the respective link:

For Windows and Unix/macOS:     https://pip.pypa.io/en/stable/installing/
For Linux Package Manager:      https://packaging.python.org/guides/installing-using-linux-tools/</pre>


---------------------------------------------
 ### 3. How to install the required libraries
---------------------------------------------
<p>For your convenience, we have provided a requirement.txt file which details the necessary libraries and their versions.
In you terminal within the root directory of the application (the one with main.py), please enter the following to install the required libraries: 
<br><br>
pip install -r ./requirements.txt</p>


---------------------------------------------
  ### 4. How to use this application
---------------------------------------------
<p>There are three main files within this repo, them being;
<br><br>
<b>src/bot.py</b> <br>
<b>src/stream.py</b> <br>
<b>main.py</b>
<br><br>
<b>bot.py</b> <br> File is a test file where you can try different methods which are provided with Twitters API. To learn more, 
check the source code, or continue reading.
<br><br>
<b>stream.py</b> <br> Is more like a bot where you can automate some tasks, first method finds the tweets you are mentioned in,
likes them, follows their authors and replies to the tweet with a desired text. Second method does the first performs the
same two actions, and then instead of replying to the tweet, sends a direct message to the author of the tweet.
<br><br>
<b>main.py</b> <br> Is a simple terminal gui where you can do two things; first, you can get methods of bot.py file and see what you can do with them. Second
is an example and/or a template for a bot which can be hosted in a local machine or a cloud. The second option creates a list of topics, then
selects one of them randomly and fetches the latest tweets which are posted on that topic in a specified amount, likes the tweets and follows its author,
replies to the tweet and dm's to the author.

</p>

<p>To do the things which are explained in the above sections, you need a pair of keys to interact with the Twitter API.
To get those keys, you need to apply for a Twitter developer account. The following link will take you to that page.

https://developer.twitter.com/en/apply-for-access 
<br><br></p>


<p>© Aziz Serin 2021 </p>
