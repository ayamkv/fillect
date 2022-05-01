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
> this will clone and install the required modules
```
git clone https://github.com/ayamkv/fillect
pip install -r requirements.txt

```

• fill in your api key in **config.py**


```
# your api keys
apikey = '#'
apikey_secret = '#'
token = '#'
token_secret = '#'

# LOOP 
loop = True
hours = 2   
# loops every ... seconds 
# ignore if loop is False
sleeptime = hours * 60 * 60

```
• then run 
```
python main.py
```

