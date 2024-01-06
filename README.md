# Darba sludinājumu filtrs
## Projekta uzdevums

Tīmekļa vietnē *www.cv.lv* ir nepieciešams automātiski atlasīt darba sludinājumus pēc lietotāja noteiktiem kritērijiem. Uzzināt par jaunākajiem darba piedāvājumiem un izgūt informāciju, kas saistīta ar konkrēto sludinājumu.

## Izmantotās Python bibliotēkas

1. Selenium

    Bibliotēka tiek izmantota, lai mijiedarbotos ar pārlūkprogrammu un veiktu automatizētus testus tajā.

2. Openpyxl

    Bibliotēka tiek izmantota, lai mijiedarbotos ar Excel datni.

3. Time

    Bibliotēka tiek izmantota, lai ieturētu laika intervālus starp dažādām funkciju izpildēm.

## Programmatūras imzmantošanas metodes

Pirms programmatūras palaišanas datnē **main.py** ir iespēja pielāgot filtrus atbilstošai meklēšanai.

Palaižot programmatūru, tiek nolasīti lietotāja uzstādītie filtri jeb kritēriji, tie automātiski tiek izmantoti tīmekļa vietnē, lai atrastu vēlamos rezultātus. Katram darba sludinājumam tiek iziets cauri nolasot meklēto informāciju.

Kad darba sludinājumi ir veiksmīgi tikuši nolasīti, tie tiek saglabāti Excel datnē, kur tos var brīvi apskatīt.