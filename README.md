# Darba sludinājumu filtrs
## Projekta uzdevums

Tīmekļa vietnē *www.cv.lv* ir nepieciešams automātiski atlasīt darba sludinājumus pēc lietotāja noteiktiem filtriem jeb kritērijiem. Kritēriji, kas ir obligāti jāaizpilda ir darba atrašanās vieta(s), amata kategorija un atslēgvārdi. Papildus, lai meklēšana būtu izvērstāka, ir iespēja aizpildīt šādus kritērijus: minimālā darba alga un darba veids, virs darba veida komentāros ir dotas alternatīvas. Bez minētajiem filtriem, ir iespēja izvēlēties veidu, starp dotajām alternatīvām, kā sakārtot pārlūkprogrammā parādītos rezultātus.

Tīmekļa vietnē ir nepieciešams izgūt informāciju, kas saistīta ar konkrēto sludinājumu, tas programmatūras lietotājam dod iespēju uzzināt par aktuālajiem darba piedāvājumiem.

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

    Bibliotēka tiek izmantota, lai mijiedarbotos - lasīt lapas saturu, noklikšķināt uz pogām un aizpildīt formas elementus - ar pārlūkprogrammu un veiktu automatizētus testus pārlūkprogrammā.

2. Openpyxl

    Bibliotēka tiek izmantota, lai mijiedarbotos - nolasīt informāciju un rakstīt datus Excel datnē - ar Excel datni.

3. Time

    Bibliotēka tiek izmantota, lai ieturētu laika intervālus starp dažādām funkciju izpildēm. Tā palīdz novērst potenciālus konfliktus, piemēram, elementu neielādēšanās pārlūkprogrammā, vienlaikus funkcijā pieprasot konkrēto elementu. Kā arī šī bibliotēka palīdz izprast koda efektivitāti un saprast, kuras funkcijas prasa ilgāku gaidīšanu.

## Programmatūras izmantošanas metodes

Pirms programmatūras palaišanas datnē **main.py**, lietotājam ir nepieciešams pielāgot meklēšanas filtrus jeb kritērijus (pamata un papildus filtrus), lai notiktu atbilstošu darba sludinājumu meklēšana.

Palaižot programmatūru, tiek nolasīti lietotāja uzstādītie filtri. Tie automātiski tiek izmantoti tīmekļa vietnē, lai atrastu vēlamos rezultātus. Katram darba sludinājumam tiek iziets cauri, nolasot lietotāja meklēto informāciju.

Kad darba sludinājumi ir veiksmīgi tikuši nolasīti, saistītā informācija tiek saglabāta Excel datnē **result.xlsx**, kur tā ir brīvi apskatāma. Informācija datnē saglabājas tik ilgi, kamēr programma nav tikusi atkārtoti veiksmīgi izpildīta.