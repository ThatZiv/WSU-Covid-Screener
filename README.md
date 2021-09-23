# WSU-Covid-Screener
Automate filling the covid screener @ wsu
i do not support the actual usage of this program, it's just for educational purposes...
if you have covid symptoms please don't use this program.

# Setup
1. install the dependencies 
```sh
python3 -m pip install bs4 requests
```
2. fill out the required information for logging in
  * open the `login.txt` and enter your accessid in the first line, password in the second line, and phone number in the third line. Save the file after
  * Template (contents of `login.txt` [do not include the '<' or '>']):
```yaml
<accessid>
<password>
<phone number>
```
3. Run the program
```sh
python3 main.py
```
4. **optional** automate cron task - edit cronjob:
```sh
crontab -e
``` 

```yaml
0 0 * * * /usr/bin/python3 /home/user/WSU-Covid-Screener/main.py
```
