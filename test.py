import webbrowser
import time

# Исходная строка с артикулами
articles = "REPA21F3; A21-3502010; A21-3502020; A21-3502210; REPCHERY; A21-3502013; A21-3502410; A21-3502420; A21-3502027; A21-3502025; A21-3502026; A21-3502028; A21-3502027; A21-3502011; A21-3502013"

# Преобразуем в список
articles_list = [article.strip() for article in articles.split(';')]

print(f"Будет открыто {len(articles_list)} вкладок с поиском на Ozon...")

# Открываем каждый артикул в новой вкладке
for i, article in enumerate(articles_list, 1):
    # Формируем URL для поиска на Ozon
    url = f"https://www.ozon.ru/search/?text={article}"
    
    # Открываем в новой вкладке
    webbrowser.open_new_tab(url)
    
    print(f"{i}. Открыт поиск для артикула: {article}")
    
    # Небольшая задержка чтобы не перегрузить браузер
    time.sleep(0.5)

print("Все вкладки открыты!")