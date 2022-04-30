# fillect
<img src="https://img.shields.io/badge/needs-imrpovement-purple?style=flat-square"/>
basically tweets archillects photos randomly

‎
‎<br>
‎
‎
### how 2 do it urself 
<img src="https://img.shields.io/badge/termux-only-grey?style=flat-square"/>

• copy and paste this command <br>
> this will clone , install the required module & create **config.py**
```
git clone https://github.com/ayamkv/fillect
pip install -r requirements.txt
echo $'apikey = "#yourapikey"\napikey_secret = "#yourapikeysecret"\ntoken = "#yourtoken"\ntoken_secret = "#yourtokensecret"' >> config.py

```

• fill in your api key in **config.py**

> this is what it looks like inside **config.py**
```
apikey = "#yourapikey"
apikey_secret = '#yourapikeysecret'
token = '#yourtoken'
token_secret = '#yourtokensecret'
```
• then run 
```
python main.py
```

