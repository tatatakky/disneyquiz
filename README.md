# DisneyQuiz LineBot
This app is LineBot for people who like Disney.</br>
I wanted to make my girlfriend happy, so I made this app.</br></br>
![LineBot sample1](https://github.com/tatatakky/DisneyQuiz/blob/master/picture/samp1.png)
</br>

### Description
You can kill time using this LineBot when you wait Disney Attraction and so on.</br></br>
![LineBot sample2](https://github.com/tatatakky/DisneyQuiz/blob/master/picture/samp2.png)
</br>

### Requirements
・LINE developers (https://developers.line.me/en/)</br>
・Python 3.6</br>
・heroku (like rental server) </br>
・Package `Flask`(web framework),`gunicorn`,`line-bot-sdk`,`numpy`</br>
・ngrok (we can access into running server in localhost from outside of LAN)
</br>

### Installation
need to install packages.
```
brew install ngrok
pip install gunicorn
pip install line_bot_sdk
pip install Flask
```
if you cannot install ngrok, you should run following command ↓
```
brew cask install ngrok
```
### Explanation important file
・main.py
```
line_bot_api = LineBotApi('**********')     #Channel access token
handler = WebhookHandler('**********')     #Channel secret
```

・Procfile
```
web: gunicorn main:app --log-file=-
```

・requirement.txt
```
Flask==0.12.2
gunicorn==19.7.1
line-bot-sdk==1.5.0
numpy==1.13.3
```
