# get_commodity_price
This project is related to getting commodity price in India from data.gov.in
All development work should be created as a feature branch and finally merged with dev_get_commodity_price only.

Setup:
----------
Create env with python 3.10
activate the env and install requirements.txt
Get a API key from data.gov.in and keep it in a .env file parallel to get_commodity_price.py with format like AGMARKNET_API_KEY=<your_key>
They have a test key available, you can use that.
Uses the below dataset from data.gov.in
https://www.data.gov.in/resource/current-daily-price-various-commodities-various-markets-mandi

Test:
--------
Running 
python get_commodity_price.py
will give the prices related to green chilly in Ramanagara APMC
Results are not good due to API bugs and data limitations
