import csv
import time
import sys
from datetime import datetime
from typing import Dict, Set, List  # "Any" entfernt (Cleanups)

# --- KONFIGURATION ---
USER_FILE = 'users.csv'
RULE_FILE = 'sod_matrix.csv'
REPORT_FILE = 'sod_report.txt'
SIMULATE_DELAY = True  # Setze auf False für sofortige Ergebnisse

def pause(seconds: float):
    """
    Hilfsfunktion für künstliche Verzögerung (Enterprise-Feeling).
    Kann über SIMULATE_DELAY global abgeschaltet werden.
    """
    if SIMULATE_DELAY:
        time.sleep(seconds)

def load_user_data(filename: str) -> Dict[str, Set[str]]:
    """
    Lädt User-Rollen aus einer CSV-Datei.
    Rückgabe: Dictionary { 'User': {'Rolle1', 'Rolle2'} }
    """
    user_roles = {}
    try:
        with open(filename, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                user = row['User']
                role = row['Role_Technical_Name']
                
                if user not in user_roles:
                    user_roles[user] = set()
                user_roles[user].add(role)
    except FileNotFoundError:
        print(f"[ERROR] Datei '{filename}' nicht gefunden.")
    except Exception as e:
        print(f"[ERROR] Fehler beim Lesen von '{filename}': {e}")
        
    return user_roles

def load_sod_rules(filename: str) -> List[Dict[str, str]]:
    """
    Lädt die Risikomatrix (Regelwerk).
    """
    rules = []
    try:
        with open(filename, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                rules.append(row)
    except FileNotFoundError:
        print(f"[ERROR] Datei '{filename}' nicht gefunden.")
    return rules

def print_progress(iteration: int, total: int, prefix: str = '', suffix: str = '', decimals: int = 1, length: int = 50, fill: str = '█'):
    """
    Erzeugt einen Ladebalken für das Terminal.
    """
    if total == 0:
        return
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()

def run_analysis() -> None:
    """
    Führt die komplette SoD-Analyse durch:
    - CSV-Daten laden
    - Regeln anwenden
    - Ergebnisse im Terminal anzeigen
    - Report als Textdatei schreiben
    """
    print("\n========================================")
    print("   SAP GRC SIMULATOR v2.1 (Final)        ")
    print("========================================")
    print(f"[*] Initializing System... {datetime.now().strftime('%H:%M:%S')}")
    pause(0.8)

    # 1. Daten laden
    print("[*] Loading User Data Repository...", end=" ")
    users = load_user_data(USER_FILE)
    pause(0.5)
    
    # CRASH-SCHUTZ: Wenn keine User da sind, abbrechen
    if not users:
        print("\n[CRITICAL ERROR] Keine Userdaten geladen. Analyse wird abgebrochen.")
        return
    
    print(f"DONE ({len(users)} Users loaded)")

    print("[*] Loading SoD Rule Matrix...", end=" ")
    rules = load_sod_rules(RULE_FILE)
    pause(0.5)
    
    if not rules:
        print("\n[CRITICAL ERROR] Keine Regeln geladen. Analyse wird abgebrochen.")
        return

    print(f"DONE ({len(rules)} Rules loaded)")
    
    print("-" * 60)
    print("[*] Starting Risk Analysis Engine (ARA)...")
    
    findings = []
    
    # Simulation des Scan-Vorgangs
    for i, (user, roles) in enumerate(users.items()):
        pause(0.2) # Performance-Simulation via Helper-Funktion
        
        for rule in rules:
            role_a = rule['Role_A']
            role_b = rule['Role_B']
            
            if role_a in roles and role_b in roles:
                findings.append({
                    'User': user,
                    'Risk_ID': rule['Risk_ID'],
                    'Level': rule['Risk_Level'],
                    'Desc': rule['Description']
                })
        
        print_progress(i + 1, len(users), prefix='Scanning:', suffix='Complete', length=30)

    print("\n" + "-" * 60)
    
    # --- MANAGEMENT SUMMARY ---
    # Set nutzen, um eindeutige User mit Risiken zu zählen
    users_with_risks = set([f['User'] for f in findings])
    clean_users = len(users) - len(users_with_risks)
    
    if len(users) > 0:
        compliance_rate = (clean_users / len(users)) * 100
    else:
        compliance_rate = 0.0

    print("\n>>> MANAGEMENT SUMMARY <<<\n")
    print(f"Total Users Scanned:      {len(users)}")
    print(f"Users with Risks:         {len(users_with_risks)}")
    print(f"Clean Users:              {clean_users}")
    print(f"Compliance Score:         {compliance_rate:.1f}%")
    
    if compliance_rate < 100:
        print("Status:                   CRITICAL ❌")
    else:
        print("Status:                   COMPLIANT ✅")

    print("\n>>> DETAILED FINDINGS (Sorted by User & Risk) <<<")
    if findings:
        # SORTIERUNG: Erst nach User, dann nach Risk_ID für saubere Liste
        sorted_findings = sorted(findings, key=lambda x: (x['User'], x['Risk_ID']))
        
        for f in sorted_findings:
            print(f" [!] {f['User']:<15} | {f['Level']:<8} | {f['Risk_ID']} - {f['Desc']}")
            
        # Report schreiben
        try:
            with open(REPORT_FILE, 'w', encoding='utf-8') as f:
                f.write(f"REPORT GENERATED: {datetime.now()}\n")
                f.write(f"COMPLIANCE SCORE: {compliance_rate:.1f}%\n")
                f.write("-" * 40 + "\n")
                for item in sorted_findings:
                    f.write(f"USER: {item['User']} | RISK: {item['Risk_ID']} ({item['Level']})\n")
            print(f"\n[INFO] Full report exported to '{REPORT_FILE}'")
        except IOError:
            print(f"\n[ERROR] Konnte Report nicht schreiben (Zugriffsrechte?).")
    else:
        print("No risks found.")

if __name__ == "__main__":
    run_analysis()