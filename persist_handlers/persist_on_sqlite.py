"""Persist the data on sqlite database"""
import sqlite3
import json

from .base import PersistSpeedTestResult


class PersistOnSqlite(PersistSpeedTestResult):
    """Persist the data on sqlite database"""
    def __init__(self, db_file: str = "./results/speed_test.db"):
        self.db_file = db_file
        self._create_table_if_not_exists()

    def persist(self, data: str):
        data_dict = json.loads(data)
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        self._insert_data(c, data_dict)
        conn.commit()
        conn.close()

    def _create_table_if_not_exists(self):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS speed_test (
                download REAL,
                upload REAL,
                ping REAL,
                server_url TEXT,
                server_lat TEXT,
                server_lon TEXT,
                server_name TEXT,
                server_country TEXT,
                server_cc TEXT,
                server_sponsor TEXT,
                server_id TEXT,
                server_host TEXT,
                server_d REAL,
                server_latency REAL,
                timestamp TEXT,
                bytes_sent INTEGER,
                bytes_received INTEGER,
                share TEXT,
                client_ip TEXT,
                client_lat TEXT,
                client_lon TEXT,
                client_isp TEXT,
                client_isprating TEXT,
                client_rating TEXT,
                client_ispdlavg TEXT,
                client_ispulavg TEXT,
                client_loggedin TEXT,
                client_country TEXT
            )''')
        conn.commit()
        conn.close()

    def _insert_data(self, cursor, data_dict):
        server = data_dict['server']
        client = data_dict['client']

        sql_query = """
            INSERT INTO speed_test (
                download, upload, ping, server_url, server_lat, server_lon, 
                server_name, server_country, server_cc, server_sponsor, server_id, server_host, server_d, 
                server_latency, timestamp, bytes_sent, bytes_received, share, client_ip, client_lat, 
                client_lon, client_isp, client_isprating, client_rating, client_ispdlavg, client_ispulavg, 
                client_loggedin, client_country) 
                VALUES (:download, :upload, :ping, :server_url, :server_lat, :server_lon, 
                :server_name, :server_country, :server_cc, :server_sponsor, :server_id, :server_host, :server_d, 
                :server_latency, :timestamp, :bytes_sent, :bytes_received, 
                :share, :client_ip, :client_lat, :client_lon, :client_isp, 
                :client_isprating, :client_rating, :client_ispdlavg, :client_ispulavg, 
                :client_loggedin, :client_country)
        """

        cursor.execute(sql_query, {
            'download': data_dict['download'],
            'upload': data_dict['upload'],
            'ping': data_dict['ping'],
            'server_url': server['url'],
            'server_lat': server['lat'],
            'server_lon': server['lon'],
            'server_name': server['name'],
            'server_country': server['country'],
            'server_cc': server['cc'],
            'server_sponsor': server['sponsor'],
            'server_id': server['id'],
            'server_host': server['host'],
            'server_d': server['d'],
            'server_latency': server['latency'],
            'timestamp': data_dict['timestamp'],
            'bytes_sent': data_dict['bytes_sent'],
            'bytes_received': data_dict['bytes_received'],
            'share': data_dict['share'],
            'client_ip': client['ip'],
            'client_lat': client['lat'],
            'client_lon': client['lon'],
            'client_isp': client['isp'],
            'client_isprating': client['isprating'],
            'client_rating': client['rating'],
            'client_ispdlavg': client['ispdlavg'],
            'client_ispulavg': client['ispulavg'],
            'client_loggedin': client['loggedin'],
            'client_country': client['country']
        })
