from bs4 import BeautifulSoup
import requests
import csv

def scrape_nhl():
    url = 'https://www.hockey-reference.com/leagues/NHL_2024_skaters.html'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the table with class 'stats_table'
        table = soup.find('table', {'class': 'stats_table'})
        
        if table is None:
            print("Table not found.")
            return
        
        # Extract table headers
        headers = []
        header_row = table.find('thead').find('tr')
        for th in header_row.find_all('th'):
            headers.append(th.text.strip())
        
        # Extract table rows
        players = []
        for row in table.find('tbody').find_all('tr'):
            cols = row.find_all('td')
            if len(cols) > 0:  # Ensure the row has data
                player_data = [col.text.strip() for col in cols]
                players.append(player_data)
        
        # Save to CSV file with UTF-8 encoding
        with open('nhl_player_stats.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(players)
        
        print(f"Scraped {len(players)} players.")
    else:
        print(f"Failed to fetch data: {response.status_code}")

if __name__ == "__main__":
    scrape_nhl()
