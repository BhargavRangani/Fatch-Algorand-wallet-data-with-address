import requests
import json
from datetime import datetime


txn_id = input("\nEnter Transaction ID: ")
#TM5TOINR2EDJPTGRRUBJSFYZATBCWNONZ4UX77L6LZQUT6KBJCKQ
headers = {"Host": "indexer.algoexplorerapi.io",
'Sec-Ch-Ua': '"(Not(A:Brand";v="8", "Chromium";v="99"',
"Accept": "application/json, text/plain, */*",
"Sec-Ch-Ua-Mobile": "?0",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
"Sec-Ch-Ua-Platform": '"Windows"',
"Origin": "https://algoexplorer.io",
"Sec-Fetch-Site": "cross-site",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Dest": "empty",
"Referer": "https://algoexplorer.io/",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "en-US,en;q=0.9"}

algo_page = requests.get("https://indexer.algoexplorerapi.io/v2/transactions/"+txn_id, headers=headers)

#print(type(algo_page))
#print(type(algo_page.text))

response_dict = json.loads(algo_page.text)
#print(type(response_dict))
#print(response_dict)
transaction_data = response_dict["transaction"]
#print(type(transaction_data))
print("==================================Transactions========================================")
print("Sender: ", transaction_data['sender'])
print("Receiver: ", transaction_data['asset-transfer-transaction']['receiver'])
print("Asset ID: ", transaction_data['asset-transfer-transaction']['asset-id'])
print("Time: ", datetime.fromtimestamp(transaction_data['round-time']))
print("Type: ", transaction_data['tx-type'])
print("Block: ", transaction_data['block-rewards-level'])
print("Amount: ", transaction_data['asset-transfer-transaction']['amount'])
print("Asset Name: ", transaction_data['asset-transfer-transaction']['asset-name'])
print("Asset Unit Name: ", transaction_data['asset-transfer-transaction']['asset-unit-name'])
print("Sender Balance: ", transaction_data['sender-balance']/1000000)
print("Receiver Balance: ", transaction_data['asset-transfer-transaction']['receiver-balance']/1000000)
print("\n======================================END============================================")


