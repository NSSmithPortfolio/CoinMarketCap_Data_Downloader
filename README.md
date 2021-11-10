Utility to download the latest cryptocurrency prices, market cap rank, 90/60/30/7/1 day returns (%) and URL to the coin itself.  I run this daily for excel dumps of where everything was at a particular time.  I then utilize output with other utilities for further analysis of currencies with lower market caps.  In particular I dial in on coins with rising market caps ranks.  

To use:
Download zip of files or git pull repository locally

pip install dotenv, json, pandas, time libraries if you don't have installed.  To install dotenv, use line: "pip install -U python-dotenv"

Create an account on https://coinmarketcap.com/ and create an API key.  For running this utility daily, the basic free price tier will more than cover this utility

Create a text file within the directory named ".env" using an editor like Notepad++

Open the file and add the text API_KEY: 'your API key here you created earlier'

Execute, and find current output in the outputs folder

