
import os                          # Dostęp do operacji systemowych (czyszczenie ekranu itp.)
import re                          # Biblioteka do obsługi wyrażeń regularnych
import sys                         # Dostęp do zmiennych systemowych i interpreterowych
import argparse                    # Obsługa argumentów z linii komend
import subprocess                  # Uruchamianie poleceń systemowych (np. pip)
import json                        # Serializacja i deserializacja danych JSON
from pathlib import Path           # Praca ze ścieżkami i plikami w stylu obiektowym

REQUIRED_PACKAGES = ["PyPDF2", "rich"]  # Lista wymaganych bibliotek do działania programu

def check_and_install_packages():      # Funkcja sprawdzająca i instalująca brakujące paczki
    for pkg in REQUIRED_PACKAGES:
        try:
            __import__(pkg)           # Próba zaimportowania paczki
        except ImportError:
            print(f"📦 Instalowanie brakującej biblioteki: {pkg}")  # Info dla użytkownika
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])  # Instalacja

check_and_install_packages()          # Wywołanie sprawdzania i instalacji paczek

import PyPDF2                         # Import po instalacji – czytanie PDF
import ipaddress                      # Obsługa adresów IP (walidacja, typy)
from rich.console import Console      # Konsola z kolorami i stylami (biblioteka rich)
from rich.progress import track       # Pasek postępu podczas przetwarzania PDF

console = Console()                   # Tworzenie instancji konsoli rich
VERSION = "1.3.2"                     # Wersja aplikacji

class Colors:                         # Klasa zdefiniowana dla kolorów ANSI
    BrightRed = "\033[1;91m"
    BrightGreen = "\033[1;92m"
    BrightYellow = "\033[1;93m"
    BrightWhite = "\033[1;97m"
    Cyan = "\033[1;96m"
    Magenta = "\033[1;95m"
    Coral = "\033[38;5;209m"
    Reset = "\033[0m"

def clear_screen():                   # Czyści ekran terminala w zależności od systemu
    os.system("cls" if os.name == "nt" else "clear")

def banner(mode="main"):             # Wyświetla baner ASCII z logo i informacjami
    clear_screen()
    ascii_logo = f"""{Colors.BrightGreen}
   _______    ____     __               __               
  /  _/ _ \\  / __/_ __/ /________ _____/ /____  ____ 
 _/ // ___/ / _/ \\ \\ / __/ __/ _ `/ __/ __/ _ \\/ __/
/___/_/    /___//_\\_\\\\__/_/  \\_,_/\\__/\\__/\\___/_/
{Colors.Reset}{Colors.BrightYellow}
⚡ "Because every PDF has something to hide."
{Colors.Reset}
"""
    version_str = f"{Colors.Coral}IP Extractor v{VERSION} • © 2025 by Łukasz Wójcik{Colors.Reset}"
    print(ascii_logo)
    print(version_str)

    if mode == "info":               # Tryb informacyjny – dodatkowe info o programie
        print(f"""{Colors.Magenta}
🔍 Open-source'owe narzędzie CLI do ekstrakcji adresów IPv4 z PDF do TXT, CSV lub JSON.
Idealne do analizy dokumentów, logów i raportów dla SOC, OSINT, czy DEVOPS.
{Colors.BrightWhite}
🐙 GitHub   : https://github.com/lukaszwojcikdev/ip-extractor.git
📍 Linkedin : https://linkedin.com/h/lukasz-michal-wojcik
🌍 Dev.to   : https://dev.to/lukaszwojcikdev
🌐 Website  : https://lukaszwojcik.eu{Colors.Reset}""")
    elif mode == "help":            # Tryb pomocy – instrukcja użytkowania
        print(f"""
{Colors.Magenta}Open-source'owe narzędzie CLI do ekstrakcji adresów IPv4 z PDF do TXT, CSV lub JSON.{Colors.Reset}

{Colors.Cyan}> Usage   :{Colors.Reset} python ip_extractor.py [-e FILE.PDF] [-c] [-j] [-i] [-v] [-h]
{Colors.Cyan}> Example :{Colors.Reset} python ip_extractor.py -e plik.pdf -c -j

{Colors.Cyan}> Flags:{Colors.Reset}
  --extract, -e       Podaj ścieżkę do pliku PDF w celu ekstrakcji adresów IP
  --csv,     -c       Eksport wyników do pliku CSV 
  --json,    -j       Eksport wyników do pliku JSON 
  --info,    -i       Informacje o programie i autorze
  --version, -v       Wyświetl wersję narzędzia
  --help,    -h       Wyświetl ekran pomocy
""")

def is_valid_ip(ip):                # Sprawdza czy IP ma poprawny format IPv4
    try:
        return len(ip.split('.')) == 4 and all(0 <= int(p) <= 255 for p in ip.split('.'))
    except:
        return False

def is_public_ip(ip):              # Sprawdza czy IP jest publiczne (nie prywatne)
    try:
        return not ipaddress.ip_address(ip).is_private
    except:
        return False

def extract_ips_from_pdf(pdf_path, to_csv=False, to_json=False):  # Główna funkcja ekstrakcji IP
    console.print(f"\n[bold yellow]🔄 Przetwarzanie  : [cyan]{pdf_path.name}[/cyan][/bold yellow]")

    if not pdf_path.exists() or pdf_path.suffix.lower() != '.pdf':  # Sprawdzenie poprawności pliku
        console.print(f"[bold red]❌ Błąd: Podaj poprawny plik PDF: {pdf_path}[/bold red]")
        sys.exit(1)

    with open(pdf_path, 'rb') as pdf_file:        # Otwiera PDF w trybie binarnym
        reader = PyPDF2.PdfReader(pdf_file)       # Tworzy obiekt czytnika PDF
        ips = set()                               # Zbiór unikalnych IP

        for page in track(reader.pages, description="📄 Przeszukiwanie stron"):  # Pętla po stronach
            text = page.extract_text()            # Pobiera tekst ze strony PDF
            if not text: continue                 # Pomija puste strony
            found = re.findall(                   # Szuka IP za pomocą regexa
                r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}'
                r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b', text
            )
            valid = [ip for ip in found if is_valid_ip(ip) and is_public_ip(ip)]  # Walidacja IP
            ips.update(valid)                    # Dodaje znalezione IP do zbioru

    if not ips:                                   # Jeśli nie znaleziono IP
        console.print("[bold red]🔍 Nie znaleziono publicznych adresów IP.[/bold red]")
        return

    sorted_ips = sorted(ips, key=lambda ip: list(map(int, ip.split('.'))))  # Sortowanie IP

    out_txt = pdf_path.with_stem(pdf_path.stem + "_ips").with_suffix(".txt")  # Plik .txt wynikowy
    with open(out_txt, 'w') as f:
        f.write('\n'.join(sorted_ips))             # Zapis IP do pliku tekstowego
    console.print(f"[bold green]💾 Zapisano do    : [cyan]{out_txt}[/cyan][/bold green]")

    if to_csv:                                     # Jeśli flagi zawierają CSV
        import csv
        out_csv = pdf_path.with_stem(pdf_path.stem + "_ips").with_suffix(".csv")
        with open(out_csv, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['IPv4 Address'])
            for ip in sorted_ips:
                writer.writerow([ip])              # Zapis IP do pliku CSV
        console.print(f"[bold green]💾 Zapisano do    : [cyan]{out_csv}[/cyan][/bold green]")

    if to_json:                                    # Jeśli flagi zawierają JSON
        out_json = pdf_path.with_stem(pdf_path.stem + "_ips").with_suffix(".json")
        with open(out_json, 'w') as f:
            json.dump({"ips": sorted_ips}, f, indent=4)  # Zapis IP do pliku JSON
        console.print(f"[bold green]💾 Zapisano do    : [cyan]{out_json}[/cyan][/bold green]")

    console.print(f"[bold green]🌐 Znaleziono     : [red]{len(sorted_ips)}[/red] unikalnych adresów IP![/bold green]")
    
def main():                                       # Główna funkcja – obsługuje argumenty z linii komend
    parser = argparse.ArgumentParser(add_help=False)  # Tworzy parser argumentów bez domyślnego -h
    parser.add_argument('--extract', '-e', type=str)  # Ścieżka do pliku PDF do analizy
    parser.add_argument('--csv', '-c', action='store_true')   # Flaga eksportu wyników do CSV
    parser.add_argument('--json', '-j', action='store_true')  # Flaga eksportu wyników do JSON
    parser.add_argument('--info', '-i', action='store_true')  # Informacje o programie i autorze
    parser.add_argument('--version', '-v', action='store_true')  # Wyświetlenie wersji programu
    parser.add_argument('--help', '-h', action='store_true')  # Wyświetlenie ekranu pomocy

    args = parser.parse_args()                  # Parsowanie przekazanych argumentów

    if args.help:                               # Jeśli podano -h/--help
        banner("help")                          # Wyświetla ekran pomocy
    elif args.info:                             # Jeśli podano -i/--info
        banner("info")                          # Wyświetla informacje o programie i autorze
    elif args.version:                          # Jeśli podano -v/--version
        console.print(f"[bold cyan]📌 Wersja IP Extractor: v{VERSION}[/bold cyan]")  # Pokazuje wersję
    elif args.extract:                          # Jeśli podano -e/--extract z nazwą pliku
        banner()                                # Wyświetla baner główny
        extract_ips_from_pdf(Path(args.extract), to_csv=args.csv, to_json=args.json)  # Wywołuje ekstrakcję
    else:                                       # Jeśli brak argumentów lub nieznane flagi
        banner("help")                          # Wyświetla pomoc domyślnie

if __name__ == "__main__":                      # Punkt wejścia do programu
    main()                                       # Uruchamia funkcję main()
