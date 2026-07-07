import pandas as pd

def top_books_by_rating(df, n=10):
    resultado = df.sort_values(['Rating'], ascending=False).drop_duplicates(subset=['Book_Title'])
    return resultado.head(n)

def top_authors(df, n=10):
    resultados = df.groupby('Author')['Book_Title'].count()
    return resultados.sort_values(ascending=False).head(n)

def most_reviewed_books(df, n=10):
    resultado = df.sort_values('Num_Customers_Rated', ascending=False).drop_duplicates(subset=['Book_Title'])
    return resultado[['Book_Title', 'Author','Num_Customers_Rated', 'Rating']].head(n)

def books_per_year(df):
    resultado = df.groupby('Year')['Book_Title'].count()
    return resultado