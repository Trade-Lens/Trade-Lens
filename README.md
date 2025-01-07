# TradeLens

Link github: https://github.com/Trade-Lens/Trade-Lens

## Despre aplicatie

> [!NOTE]
>   - TradeLens este o aplicatie de analiza de stocuri care are ca main feature `predictie de crestere a pietei` calculata cu ajutorul `inteligentei artificiale`.
>   - Utilizatorul isi poate forma un portofoliu unde poate urmari si vinde actiunile detinute.
>   - Pentru a cumpara noi actiuni, se foloseste functia de cautare pus la dispozitie de noi. Pe aceasta pagina, utilizatorul poate urmari evolutia unei companii 
    pe diferite perioade de timp sub forma unui grafic. Sub acest grafic se gaseste o scurta descriere a companiei si date care pot interesa un potential cumparator.

> [!IMPORTANT]
> Pe pagina de search se gasesc informatii despre potentialul de crestere generate de **modelele de inteligenta artificiala** cu scopul de a ajuta utilizatorul sa ia anumite decizii, precum: `cumparare cand exista potential de crestere`, `pastrarea actiunilor in perioade de crestere` si `vanzare in momentul considerat optim`.

## Tehnologii folosite:
    - Python
    - CSS

## Cum să instalați pachetele necesare.

```bash
pip install -r requirements.txt
```

>[!CAUTION]
> Este posibil sa aveti probleme la instalarea pachetelor din diverse motive. In acest caz instalati manual urmatoarele pachete:
> - streamlit
> - finnhub-python
> - streamlit-echarts
> - yfinance
> - python-dotenv
> - numpy
> - pandas
> - scikit-learn
> 
> In cazul in care am omis cateva pachete va trebui sa le instalati in functie de erorile primite.

### Rulare aplicatie:
```bash
cd src/
streamlit run app.py
```
>[!CAUTION]
> APLICATIA NU VA PUTEA GENERA PREDICTIILE MODELELOR DE IA, DEOARECE LIPSESC MODELELE DIN ARHIVA (sunt prea mari 1.8 gb)

>[!IMPORTANT]
> In demoul prezentat fizic aplicatia va functiona normal, deoarece avem toate fisierele local.

## Contributii individuale:

    1) Abahnencei Alin Andrei
        - Implementat baza de date pentru portofoliu
        - Implementat pagina de profil cu optiune de schimbare a datelor utilizatorului.
        - Adaugat feature pentru afisarea datei de inscriere a utilizatorului
        - Adaugat optiune de vanzare a unui numar fix de actiuni.

    2) Avramoniu Calin Stefan
        - Implementat feature de register si login
        - Implementat yfinance pentru optiunea de search
        - Implementat api finnhub pentru stiri despre global market si insider sentiment
        - Adaugat algoritm de predictie

## Dificultati intampinate:
    - SQL, deoarece niciunul dintre noi nu a mai folosit pana acum acest tip de baze de date
    - Obisnuirea cu biblioteca Streamlit
    - Folosirea unui algoritm de machine learning
    - Dupa ce am dat push la modelele de ia nu am mai putut da git pull si commit decat de pe un calculator care avea fisierele.

## Rezolvare:
    - Problemele enumerate mai sus au fost depasite prin parcurgerea documentatiilor puse la dispozitie pentru tehnologiile folosite, 
    prin urmarirea unor tutoriale si prin ajutorul limitat al LLM-urilor.

