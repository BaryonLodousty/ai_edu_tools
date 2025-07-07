# Mój pierwszy skrypt do przetwarzania tekstu
# Data: 8 lipca 2025
# Cel: Test środowiska i pierwszy krok w projekcie

def witaj():
    """
    Funkcja powitalna - sprawdza, czy wszystko działa
    """
    print("🎉 Witaj w projekcie edukacyjnym AI!")
    print("📚 Python działa: ✅")
    print("💻 VS Code działa: ✅") 
    print("🚀 Gotowy do nauki przetwarzania tekstu!")

def test_podstawowych_funkcji():
    """
    Test podstawowych operacji na tekście
    """
    tekst_przyklad = "To jest mój pierwszy tekst do analizy. Zawiera kilka zdań."
    
    print(f"\n📝 Tekst przykładowy: {tekst_przyklad}")
    print(f"📊 Liczba znaków: {len(tekst_przyklad)}")
    print(f"📊 Liczba słów: {len(tekst_przyklad.split())}")
    print(f"📊 Liczba zdań: {tekst_przyklad.count('.')}")

if __name__ == "__main__":
    witaj()
    test_podstawowych_funkcji()
    print("\n✨ Pierwszy test zakończony pomyślnie!")
