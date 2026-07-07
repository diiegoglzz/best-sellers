import pandas as pd

def top_books_by_rating(df, n=10):
    resultado = df.sort_values(['Rating'], ascending=False).drop_duplicates(subset=['Book_Title'])
    return resultado.head(n)

def top_authors(df, n=10):
    resultados = df.groupby('Author')['Book_Title'].count()
    return resultados.sort_values(ascending=False).head(n)