meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "AFK": "Klavyeden uzakta",
            "GG": "Güzel oyun",
            "WP": "İyi oynuyorsun ",
            "F2P": "Parasız oynayan",
            "NT": "Eline sağlık",
            "FPS": "Saniyede oynatılan kare sayısı"
            
            }

kelime = input("Kelime girin").upper()

if kelime in meme_dict.keys():
    print(meme_dict[kelime])
    # Kelime eşleşiyorsa ne yapmalıyız?
else: 
    print('Kelime listede yok.')
