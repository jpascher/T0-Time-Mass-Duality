import feedparser
import time
import random
import webbrowser
import re

# Konfiguration
SUBREDDITS = ["Physics", "AskPhysics", "TheoreticalPhysics", "cosmology", "AskScience"]
SEARCH_TERMS = [
    "quantum mechanics", "relativity theory", "unified field theory",
    "time-mass duality", "intrinsic time field", "emergent gravitation"
]

# Antwortvorlagen für das T0-Modell
RESPONSE_TEMPLATES = [
    "Interesting discussion! The T0 model examines this problem through the concept of time-mass duality, where time is considered absolute and mass variable. This offers an alternative explanation for {search_term}.",
    "In the T0 model, {search_term} is explained through the intrinsic time field T(x) = ℏ/max(mc², ω), which bridges quantum mechanics and relativity theory.",
    "The topic you're discussing has an interesting parallel to the T0 model, which explains {search_term} through emergent gravitation from time field gradients, without requiring curved spacetime."
]

def search_subreddit_rss(subreddit):
    """Sucht im RSS-Feed eines Subreddits nach neuen Beiträgen"""
    print(f"Durchsuche r/{subreddit}...")
    
    # RSS-Feed-URL für neue Beiträge
    url = f"https://www.reddit.com/r/{subreddit}/new/.rss"
    
    try:
        # Feed abrufen
        feed = feedparser.parse(url)
        
        if not feed.entries:
            print(f"Keine Beiträge in r/{subreddit} gefunden oder Feed nicht verfügbar.")
            return []
        
        results = []
        
        for entry in feed.entries[:10]:  # Nur die 10 neuesten Beiträge
            title = entry.title
            link = entry.link
            # Datum konvertieren
            date = entry.published if hasattr(entry, 'published') else "Unbekanntes Datum"
            # Inhalt bereinigen
            content = entry.description if hasattr(entry, 'description') else ""
            content = re.sub(r'<[^>]+>', '', content)  # HTML-Tags entfernen
            
            # Prüfen, ob einer der Suchbegriffe im Titel oder Inhalt vorkommt
            relevant_terms = []
            for term in SEARCH_TERMS:
                if term.lower() in title.lower() or term.lower() in content.lower():
                    relevant_terms.append(term)
            
            # Relevanz bestimmen
            relevance = len(relevant_terms)
            
            # Auch wenn kein Suchbegriff gefunden wurde, den Beitrag hinzufügen
            # aber mit niedrigerer Relevanz
            results.append({
                'title': title,
                'url': link,
                'date': date,
                'subreddit': subreddit,
                'search_terms': relevant_terms if relevant_terms else ["physics topics"],
                'relevance': relevance,
                'content_preview': content[:200] + "..." if len(content) > 200 else content
            })
        
        return results
    except Exception as e:
        print(f"Fehler beim Abrufen des RSS-Feeds für r/{subreddit}: {e}")
        return []

def generate_response(discussion):
    """Generiert eine Antwort basierend auf der Diskussion"""
    # Zufälligen Suchbegriff auswählen, falls verfügbar
    search_term = random.choice(discussion['search_terms']) if discussion['search_terms'] else "physics"
    
    # Zufällige Antwortvorlage auswählen
    template = random.choice(RESPONSE_TEMPLATES)
    
    # Vorlage mit dem Suchbegriff füllen
    response = template.format(search_term=search_term)
    
    # Hinzufügen eines Verweises
    response += "\n\nFor more information on the T0 model and time-mass duality, you can check the work by Johann Pascher."
    
    return response

def main():
    all_results = []
    
    print("T0-Modell Diskussions-Finder gestartet")
    print("=====================================")
    print("Suche nach relevanten Diskussionen in wissenschaftlichen Subreddits...")
    
    # Alle Subreddits durchsuchen
    for subreddit in SUBREDDITS:
        results = search_subreddit_rss(subreddit)
        all_results.extend(results)
        
        # Kurze Pause, um Rate-Limits zu vermeiden
        time.sleep(1)
    
    if not all_results:
        print("\nKeine Diskussionen gefunden. Überprüfen Sie Ihre Internetverbindung oder versuchen Sie es später erneut.")
        return
    
    # Sortieren nach Relevanz (hohe Relevanz zuerst) und dann nach Datum
    all_results.sort(key=lambda x: (-x['relevance'], x['date']), reverse=True)
    
    # Bis zu 10 der relevantesten Beiträge anzeigen
    print("\n=== Gefundene relevante Diskussionen ===")
    for i, discussion in enumerate(all_results[:10], 1):
        relevance_indicator = "*" * (discussion['relevance'] + 1) if discussion['relevance'] > 0 else ""
        print(f"{i}. r/{discussion['subreddit']} {relevance_indicator}")
        print(f"   Titel: {discussion['title']}")
        print(f"   Vorschau: {discussion['content_preview']}")
        print(f"   Relevante Begriffe: {', '.join(discussion['search_terms'])}")
        print(f"   Datum: {discussion['date']}")
        print(f"   URL: {discussion['url']}")
        print()
    
    # Auswahl einer Diskussion durch den Benutzer
    if all_results:
        choice = None
        while choice is None:
            try:
                selection = input("Wählen Sie eine Diskussion zum Ansehen (1-10) oder 'q' zum Beenden: ")
                if selection.lower() == 'q':
                    print("Programm beendet.")
                    return
                choice = int(selection) - 1
                if choice < 0 or choice >= min(10, len(all_results)):
                    print("Ungültige Auswahl. Bitte wählen Sie eine Zahl zwischen 1 und", min(10, len(all_results)))
                    choice = None
            except ValueError:
                print("Bitte geben Sie eine Zahl ein.")
        
        # Ausgewählte Diskussion
        discussion = all_results[choice]
        
        # Antwort generieren
        response = generate_response(discussion)
        
        print("\n=== Generierte Antwort ===")
        print(response)
        
        # Fragen, ob die Diskussion im Browser geöffnet werden soll
        open_browser = input("\nMöchten Sie die Diskussion im Browser öffnen? (j/n): ")
        if open_browser.lower() == 'j':
            print(f"Öffne Diskussion: {discussion['title']}")
            webbrowser.open(discussion['url'])
            print("\nKopieren Sie die generierte Antwort und fügen Sie sie manuell in den Reddit-Thread ein.")
    else:
        print("Keine relevanten Diskussionen gefunden.")

if __name__ == "__main__":
    main()