# Darba sludinājumu filtrs
## Projekta uzdevums

Tīmekļa vietnē *www.cv.lv* ir nepieciešams automātiski atlasīt darba sludinājumus pēc lietotāja noteiktiem filtriem jeb kritērijiem. Kritēriji, kas ir obligāti jāaizpilda ir darba atrašanās vieta(s), amata kategorija un atslēgvārdi. Papildus, lai meklēšana būtu paplašinātāka, ir iespēja aizpildīt šādus kritērijus: minimālā darba alga un darba veids.

Tīmekļa vietnē ir nepieciešams izgūt informāciju, kas saistīta ar konkrēto sludinājumu, tas programmatūras lietotājam dod iespēju uzzināt par jaunākajiem darba piedāvājumiem.

Informācija, kas ir jāiegūst no katra darba sludinājuma:

* Sludinājuma virsraksts;
* Uzņēmuma nosaukums;
* Atrašanās vieta (pilsēta);
* Darba alga;
* Darba vakances apraksts;
* Laiks, pirms kāda sludinājums ir ticis atjaunots vai publicēts;
* Datums, kad beidzas pieteikšanās termiņš uz vakanci;
* Saite uz sludinājumu.

## Izmantotās Python bibliotēkas

1. Selenium

    Bibliotēka tiek izmantota, lai mijiedarbotos ar pārlūkprogrammu un veiktu automatizētus testus pārlūkprogrammā.

2. Openpyxl

    Bibliotēka tiek izmantota, lai mijiedarbotos - nolasītu un rakstītu datus - ar Excel datni.

3. Time

    Bibliotēka tiek izmantota, lai ieturētu laika intervālus starp dažādām funkciju izpildēm.

## Programmatūras izmantošanas metodes

Pirms programmatūras palaišanas datnē **main.py**, lietotājam ir nepieciešams pielāgot meklēšanas filtrus jeb kritērijus, lai notiktu atbilstošu darba sludinājumu meklēšana.

Palaižot programmatūru, tiek nolasīti lietotāja uzstādītie filtri. Tie automātiski tiek izmantoti tīmekļa vietnē, lai atrastu vēlamos rezultātus. Katram darba sludinājumam tiek iziets cauri, nolasot lietotāja meklēto informāciju.

Kad darba sludinājumi ir veiksmīgi tikuši nolasīti, saistītā informācija tiek saglabāta Excel datnē **result.xlsx**, kur to var brīvi apskatīt.