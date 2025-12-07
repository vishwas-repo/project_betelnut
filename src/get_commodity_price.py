import requests
import os
import csv
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the data.gov.in key
AGMARKNET_API_KEY = os.getenv("AGMARKNET_API_KEY")


def get_agmarknet_price(apmc_name, commodity):
    """
    Fetch betelnut price from AGMARKNET API for a given APMC.
    """
    url = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
    params = {
        "api-key": AGMARKNET_API_KEY,
        "format": "json",
        "limit": 10,
        "filters[commodity]": commodity,
        "filters[market]": apmc_name
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if "records" in data and data["records"]:
            for record in data["records"]:
                print(f"[AGMARKNET] {record['state']} - {record['market']} - {record['variety']} : "
                      f"Modal ₹{record['modal_price']} | Min ₹{record['min_price']} | Max ₹{record['max_price']}")
        else:
            print("No records found for this APMC in AGMARKNET.")
    else:
        print("AGMARKNET API error:", response.status_code)


def get_enam_price(apmc_name, commodity):
    """
    Fetch betelnut price from e-NAM API/dashboard.
    NOTE: Replace 'url' with the actual JSON endpoint you find via DevTools.
    """
    # Placeholder URL — inspect e-NAM dashboard network calls for actual endpoint
    url = f"https://enam.gov.in/api/marketprice?commodity={commodity}&market={apmc_name}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        try:
            data = response.json()
            # Example structure — adapt based on actual JSON
            for record in data.get("records", []):
                print(f"[e-NAM] {record['state']} - {record['market']} : "
                      f"Modal ₹{record['modal_price']} | Min ₹{record['min_price']} | Max ₹{record['max_price']}")
        except ValueError:
            print("e-NAM response is not JSON. Inspect the endpoint.")
    else:
        print("e-NAM API error:", response.status_code)


if __name__ == "__main__":

    # API_URL = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"


    # params = {
    #     "api-key": AGMARKNET_API_KEY,
    #     "format": "json",
    #     "limit": 10000  # fetch more records
    # }

    # response = requests.get(API_URL, params=params)
    # if response.status_code == 200:
    #     print("Successfully fetched market data.")
    # else:
    #     print("Error fetching market data:", response.status_code)
    # data = response.json()
    # markets = set()
    # market_list = []
    # print(len(data.get("records", [])))
    # for record in data.get("records", []):
    #     markets.add((record["state"], record["district"], record["market"]))
    #     market_list.append((record["state"], record["district"], record["market"]))
    # filename = r"D:\vishwas_code\project_betelnut\project_betelnut\config\apmc_markets.csv"
    # with open(filename, mode="w", newline="", encoding="utf-8") as file:
    #     writer = csv.writer(file)
    #     writer.writerow(["State", "District", "Market"])
    #     for state, district, market in market_list:
    #         writer.writerow([state, district, market]) 
    # markets = {record["market"] for record in data["records"]}
    # print("Valid APMC markets (sample):")
    # for m in sorted(markets):
    #     print(m)

    apmc = "Ramanagara"  # Example APMC market
    print(f"Fetching prices for {apmc} APMC...\n")
    get_agmarknet_price(apmc,"Green Chilli")
    # get_enam_price(apmc)
