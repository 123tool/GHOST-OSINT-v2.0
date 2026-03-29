#!/usr/bin/python
# -*- coding: utf-8 -*-
# CREATOR : SPY-E & 123Tool
# VERSION : 2.0 (Premium Edition)

import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from concurrent.futures import ThreadPoolExecutor

# Color Palette
R = '\033[1;31m'  # Red
G = '\033[1;32m'  # Green
Y = '\033[1;33m'  # Yellow
B = '\033[1;34m'  # Blue
C = '\033[1;36m'  # Cyan
W = '\033[1;37m'  # White
Reset = '\033[0m'

class GhostOSINT:
    def __init__(self):
        self.session = requests.Session()
        self.brand = "SPY-E & 123Tool"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def banner(self):
        self.clear()
        print(f"""{R}
              RECOGNIZED BY {self.brand}
               
                    ,           ,
                   / \         / \\
                  /   \       /   \\
                 /     \_____/     \\
                /  {W}I N F O {R}  \ {W}G A T H {R}  \\
               /      \     /      \\
              (        )   (        )
               \      /     \      /
                \    /       \    /
                 \  /  {W}N A G A {R}  \  /
                  \/ {W}M E R A H {R} \/
                  
        {W}=========================================
        {C}   GHOST-OSINT v2.0 | BRAND: {G}{self.brand}
        {W}========================================={Reset}""")

    def track_ip(self):
        self.banner()
        ip = input(f"{W} [?] Masukkan IP Target: {G}")
        print(f"{Y} [*] Sedang mengambil data...{Reset}")
        try:
            res = self.session.get(f"http://ipwho.is/{ip}", timeout=10).json()
            if not res.get("success"):
                print(f"{R} [!] Error: {res.get('message')}"); return

            print(f"\n{C}─── [ DATA IP ADDRESS ] ───{Reset}")
            print(f"{W} Negara      : {G}{res.get('country')} {res.get('flag', {}).get('emoji', '')}")
            print(f"{W} Kota        : {G}{res.get('city')}")
            print(f"{W} ISP         : {G}{res.get('connection', {}).get('isp')}")
            print(f"{W} Koordinat   : {G}{res.get('latitude')}, {res.get('longitude')}")
            print(f"{W} Maps        : {Y}https://www.google.com/maps?q={res.get('latitude')},{res.get('longitude')}")
        except Exception as e:
            print(f"{R} [!] Koneksi Gagal: {e}")

    def track_phone(self):
        self.banner()
        num = input(f"{W} [?] No Telepon (cth: +62812...): {G}")
        try:
            parsed = phonenumbers.parse(num, None)
            if not phonenumbers.is_valid_number(parsed):
                print(f"{R} [!] Nomor tidak valid!"); return

            print(f"\n{C}─── [ DATA TELEPON ] ───{Reset}")
            print(f"{W} Lokasi      : {G}{geocoder.description_for_number(parsed, 'id')}")
            print(f"{W} Provider    : {G}{carrier.name_for_number(parsed, 'en')}")
            print(f"{W} Zona Waktu  : {G}{', '.join(timezone.time_zones_for_number(parsed))}")
            print(f"{W} Format Int  : {G}{phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
        except Exception as e:
            print(f"{R} [!] Error: {e}")

    def _scan_user(self, site, user):
        url = site['url'].format(user)
        try:
            r = self.session.get(url, timeout=5, headers=self.headers)
            if r.status_code == 200:
                print(f"{W}[{G}FOUND{W}] {site['name']:<12}: {G}{url}")
        except: pass

    def track_username(self):
        self.banner()
        user = input(f"{W} [?] Masukkan Username: {G}")
        sites = [
            {"url": "https://www.instagram.com/{}", "name": "Instagram"},
            {"url": "https://www.github.com/{}", "name": "GitHub"},
            {"url": "https://www.facebook.com/{}", "name": "Facebook"},
            {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
            {"url": "https://twitter.com/{}", "name": "Twitter"},
            {"url": "https://t.me/{}", "name": "Telegram"},
            {"url": "https://www.youtube.com/@{}", "name": "YouTube"},
        ]
        print(f"\n{Y} [*] Memulai Bruteforce Scan (Multithread)...{Reset}\n")
        with ThreadPoolExecutor(max_workers=10) as executor:
            for site in sites:
                executor.submit(self._scan_user, site, user)

    def menu(self):
        while True:
            self.banner()
            print(f"{W}[ 1 ] Pelacak IP")
            print(f"{W}[ 2 ] Pelacak No. HP")
            print(f"{W}[ 3 ] Pelacak Username (Fast)")
            print(f"{W}[ 0 ] Keluar")
            
            cmd = input(f"\n{W}SPY-E@{G}Terminal:~# {W}")
            if cmd == '1': self.track_ip()
            elif cmd == '2': self.track_phone()
            elif cmd == '3': self.track_username()
            elif cmd == '0': print(f"{R}Shutting down..."); break
            else: continue
            input(f"\n{Y}[ Tekan Enter Untuk Kembali ]")

if __name__ == "__main__":
    app = GhostOSINT()
    try: app.menu()
    except KeyboardInterrupt: exit()
