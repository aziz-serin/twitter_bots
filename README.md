#        Twitter Bot        

---------------------------------------------
   ### 1. What is a Twitter Bot
---------------------------------------------
<p>If you are lazy like me you can use this script to automate some things or just have fun on twitter with your own bot.</p>

---------------------------------------------
 ### 2. How to install the required libraries
---------------------------------------------
<p>You can use below command to install required libraries 
<br><br>
pip install -r ./requirements.txt</p>


---------------------------------------------
  ### 3. How to use this application
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
