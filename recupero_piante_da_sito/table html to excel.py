from bs4 import BeautifulSoup
import pandas as pd

# Sostituisci 'html_content' con il codice HTML della tabella
html_content = """
<table id="tablepress-2" class="tablepress tablepress-id-2">
<tbody class="row-hover">
<tr class="row-2 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=303" target="_parent">'Type 2'</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">unknown</td><td class="column-7">unknown</td><td class="column-8">stem width 2 inches</td><td class="column-9">fast</td><td class="column-10">South America</td><td class="column-11">unknown</td>
</tr>
<tr class="row-3 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=332" target="_parent">Aciotis acuminifolia</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Melastomataceae</td><td class="column-7">Aciotis</td><td class="column-8">Stem width 3 inches</td><td class="column-9">Moderate</td><td class="column-10">South America</td><td class="column-11">Lesser Antilles to Brazil, Bolivia</td>
</tr>
<tr class="row-4 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=339" target="_parent">Acmella repens</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Asteraceae</td><td class="column-7">Acmella</td><td class="column-8">Stem width 2 inches</td><td class="column-9">Moderate</td><td class="column-10">North America, South America</td><td class="column-11">Southern USA to Paraguay</td>
</tr>
<tr class="row-5 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=158" target="_parent">Alternanthera aquatica</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Floating</td><td class="column-6">Amaranthaceae</td><td class="column-7">Alternanthera</td><td class="column-8">Stem width: 12-14cm (5-6</td><td class="column-9">Fast</td><td class="column-10">Central/South America</td><td class="column-11">Brazil, Bolivia, Paraguay</td>
</tr>
<tr class="row-6 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=208" target="_parent">Alternanthera reineckii 'lilacina'</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Amaranthaceae</td><td class="column-7">Alternanthera</td><td class="column-8">Stem width: 5-15cm (2-6 in)</td><td class="column-9">Medium</td><td class="column-10">South America</td><td class="column-11">South America</td>
</tr>
<tr class="row-7 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=58" target="_parent">Alternanthera reineckii 'rosaefolia'</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Amaranthaceae</td><td class="column-7">Alternanthera</td><td class="column-8">Individual stem width: 10-15cm (4-6in)</td><td class="column-9">Medium</td><td class="column-10">Central/South America</td><td class="column-11">Argentina, Paraguay, Brazil</td>
</tr>
<tr class="row-8 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=337" target="_parent">Ammannia capitellata</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Lythraceae</td><td class="column-7">Ammannia</td><td class="column-8">Stem width 3 inches</td><td class="column-9">Fast</td><td class="column-10">Africa, Asia</td><td class="column-11">Madagascar</td>
</tr>
<tr class="row-9 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=135" target="_parent">Ammannia crassicaulis</a></td><td class="column-2">Difficult</td><td class="column-3">High</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Lythraceae</td><td class="column-7">Ammannia</td><td class="column-8">Stem width: 8-12cm (3-5</td><td class="column-9">Fast</td><td class="column-10">Africa</td><td class="column-11">West Africa</td>
</tr>
<tr class="row-10 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=118" target="_parent">Ammannia gracilis</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Lythraceae</td><td class="column-7">Ammannia</td><td class="column-8">Stem width: 12-20cm (5-8</td><td class="column-9">Fast</td><td class="column-10">Africa</td><td class="column-11">West Africa</td>
</tr>
<tr class="row-11 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=231" target="_parent">Ammannia latifolia</a></td><td class="column-2">Difficult</td><td class="column-3">Medium High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Lythraceae</td><td class="column-7">Ammannia</td><td class="column-8">5 inch stem width</td><td class="column-9">Slow</td><td class="column-10">North America</td><td class="column-11">United States</td>
</tr>
<tr class="row-12 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=104" target="_parent">Ammannia pedicellata</a></td><td class="column-2">Difficult</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Lythraceae</td><td class="column-7">Ammannia</td><td class="column-8">Individual stem width: 3-20cm (1-8in)</td><td class="column-9">Medium</td><td class="column-10">Africa</td><td class="column-11">West Africa</td>
</tr>
<tr class="row-13 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=97" target="_parent">Ammannia praetermissa</a></td><td class="column-2">Very Difficult</td><td class="column-3">Very High</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Lythraceae</td><td class="column-7">Ammannia</td><td class="column-8">Stem width: 3-5cm (1-2in)</td><td class="column-9">Medium</td><td class="column-10">Africa</td><td class="column-11">West Africa</td>
</tr>
<tr class="row-14 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=119" target="_parent">Anubias barteri var. barteri</a></td><td class="column-2">Very Easy</td><td class="column-3">Low</td><td class="column-4">Epiphyte</td><td class="column-5">Rhizome</td><td class="column-6">Araceae</td><td class="column-7">Anubias</td><td class="column-8">Height: 25-45cm (10-18 in)</td><td class="column-9">Slow</td><td class="column-10">Africa</td><td class="column-11">Southeast Nigeria, Cameroon, Equatorial Guinea</td>
</tr>
<tr class="row-15 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=24" target="_parent">Anubias barteri var. nana</a></td><td class="column-2">Very Easy</td><td class="column-3">Low</td><td class="column-4">Epiphyte</td><td class="column-5">Rhizome</td><td class="column-6">Araceae</td><td class="column-7">Anubias</td><td class="column-8">2-6 inches (5-15 cm) tall</td><td class="column-9">Slow</td><td class="column-10">Africa</td><td class="column-11">Cameroon</td>
</tr>
<tr class="row-16 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=163" target="_parent">Anubias barteri var. nana 'Marble'</a></td><td class="column-2">Very Easy</td><td class="column-3">Low</td><td class="column-4">Epiphyte</td><td class="column-5">Rhizome</td><td class="column-6">Araceae</td><td class="column-7">Anubias</td><td class="column-8">Height: 2-4" (5-12cm)</td><td class="column-9">Slow</td><td class="column-10">Cultivar</td><td class="column-11">Cultivar</td>
</tr>
<tr class="row-17 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=52" target="_parent">Anubias barteri var. nana 'Petite'</a></td><td class="column-2">Very Easy</td><td class="column-3">Low</td><td class="column-4">Epiphyte</td><td class="column-5">Rhizome</td><td class="column-6">Araceae</td><td class="column-7">Anubias</td><td class="column-8">3-5cm (1-2in) tall</td><td class="column-9">Slow</td><td class="column-10">Cultivar</td><td class="column-11">Cultivar</td>
</tr>
<tr class="row-18 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=227" target="_parent">Anubias gracilis</a></td><td class="column-2">Easy</td><td class="column-3">Medium Low</td><td class="column-4">Epiphyte</td><td class="column-5">Rhizome</td><td class="column-6">Araceae</td><td class="column-7">Anubias</td><td class="column-8">18 inches tall</td><td class="column-9">Slow</td><td class="column-10">Africa</td><td class="column-11">Western Africa</td>
</tr>
<tr class="row-19 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=215" target="_parent">Aponogeton boivinianus</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Bulb</td><td class="column-6">Aponagetonaceae</td><td class="column-7">Aponogeton</td><td class="column-8">Height: 30-60cm+ (12-24 in+)</td><td class="column-9">Fast</td><td class="column-10">Africa</td><td class="column-11">Madagascar</td>
</tr>
<tr class="row-20 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=87" target="_parent">Aponogeton crispus</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Bulb</td><td class="column-6">Aponagetonaceae</td><td class="column-7">Aponogeton</td><td class="column-8">Height: 25-50cm (10-20in)</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">Sri Lanka</td>
</tr>
<tr class="row-21 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=213" target="_parent">Aponogeton madagascariensis</a></td><td class="column-2">Difficult</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Bulb</td><td class="column-6">Aponagetonaceae</td><td class="column-7">Aponogeton</td><td class="column-8">Height: 30-60cm+ (12-24 in+)</td><td class="column-9">Fast</td><td class="column-10">Africa</td><td class="column-11">Madagascar</td>
</tr>
<tr class="row-22 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=145" target="_parent">Azolla caroliniana</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Floating</td><td class="column-6">Azollaceae</td><td class="column-7">Azolla</td><td class="column-8">Plant size: 0.5cm (0.25</td><td class="column-9">Very fast</td><td class="column-10">Cosmopolitan</td><td class="column-11">Cosmopolitan</td>
</tr>
<tr class="row-23 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=110" target="_parent">Bacopa australis</a></td><td class="column-2">Very Easy</td><td class="column-3">Low</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Plantaganaceae</td><td class="column-7">Bacopa</td><td class="column-8">Individual stem width:<span style="mso-spacerun:yes">Â <br />
  </span>2-4cm (1-2in)</td><td class="column-9">Fast</td><td class="column-10">Central/South America</td><td class="column-11">Brazil</td>
</tr>
<tr class="row-24 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=124" target="_parent">Bacopa caroliniana</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Plantaganaceae</td><td class="column-7">Bacopa</td><td class="column-8">Stem width: 3-6cm (1-2in)</td><td class="column-9">Moderate</td><td class="column-10">North America</td><td class="column-11">U.S.A.</td>
</tr>
<tr class="row-25 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=348" target="_parent">Bacopa innominata</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Plantaganaceae</td><td class="column-7">Bacopa</td><td class="column-8">Stem width 2 inches</td><td class="column-9">Fast</td><td class="column-10">North America, South America</td><td class="column-11">Virginia, USA to Northern SA</td>
</tr>
<tr class="row-26 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=274" target="_parent">Bacopa lanigera</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Plantaganaceae</td><td class="column-7">Bacopa</td><td class="column-8">stem width 2 inches (5cm)</td><td class="column-9">Moderate</td><td class="column-10">South America</td><td class="column-11">Brazil</td>
</tr>
<tr class="row-27 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=306" target="_parent">Bacopa madagascariensis</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Plantaganaceae</td><td class="column-7">Bacopa</td><td class="column-8">Stem width: 4-5 cm (1.5-2 in)</td><td class="column-9">Moderate</td><td class="column-10">Africa</td><td class="column-11">Madagascar</td>
</tr>
<tr class="row-28 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=55" target="_parent">Bacopa monnieri</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Plantaganaceae</td><td class="column-7">Bacopa</td><td class="column-8">Individual stem width: 3cm (1in)</td><td class="column-9">Medium</td><td class="column-10">Cosmopolitan</td><td class="column-11">Pantropical and Subtropics</td>
</tr>
<tr class="row-29 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=321" target="_parent">Bacopa salzmannii</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Plantaganaceae</td><td class="column-7">Bacopa</td><td class="column-8">Stem width 2 inches</td><td class="column-9">Fast</td><td class="column-10">South America</td><td class="column-11">Southern Mexico to Paraguay</td>
</tr>
<tr class="row-30 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=333" target="_parent">Bacopa serpyllifolia</a></td><td class="column-2">Moderate</td><td class="column-3">Medium High</td><td class="column-4">Foreground</td><td class="column-5">Stem</td><td class="column-6">Plantaganaceae</td><td class="column-7">Bacopa</td><td class="column-8">Stem width 1 inch</td><td class="column-9">Fast</td><td class="column-10">South America</td><td class="column-11">Brazil, Guyana, Venezuela</td>
</tr>
<tr class="row-31 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=205" target="_parent">Bacopa sp. 'Colorata'</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Plantaganaceae</td><td class="column-7">Bacopa</td><td class="column-8">Stem width: 3-4cm (1-1.5 in)</td><td class="column-9">Medium</td><td class="column-10">Unknown</td><td class="column-11">Unknown</td>
</tr>
<tr class="row-32 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=151" target="_parent">Barclaya longifolia</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Red</td><td class="column-5">Bulb</td><td class="column-6">Nymphaeaceae</td><td class="column-7">Barclaya</td><td class="column-8">Height: 30-80cm (12-32</td><td class="column-9">Medium</td><td class="column-10">Asia</td><td class="column-11">Southeast Asia</td>
</tr>
<tr class="row-33 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=277" target="_parent">Blyxa alternifolia</a></td><td class="column-2">Difficult</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Hydrocharitaceae</td><td class="column-7">Blyxa</td><td class="column-8">stem width 2 inches</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">Asia</td>
</tr>
<tr class="row-34 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=219" target="_parent">Blyxa aubertii</a></td><td class="column-2">Moderate</td><td class="column-3">Medium High</td><td class="column-4">Not Specific</td><td class="column-5">Rosette</td><td class="column-6">Hydrocharitaceae</td><td class="column-7">Blyxa</td><td class="column-8">16 inches</td><td class="column-9">Fast</td><td class="column-10">Old World tropics</td><td class="column-11">Asia, Africa, Australia</td>
</tr>
<tr class="row-35 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=123" target="_parent">Blyxa japonica</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Foreground</td><td class="column-5">Stem</td><td class="column-6">Hydrocharitaceae</td><td class="column-7">Blyxa</td><td class="column-8">Height: 7-15cm (3-6in)</td><td class="column-9">Medium</td><td class="column-10">Asia</td><td class="column-11">Tropical Asia</td>
</tr>
<tr class="row-36 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=260" target="_parent">Bolbitis heudelotii</a></td><td class="column-2">Easy</td><td class="column-3">Low</td><td class="column-4">Epiphyte</td><td class="column-5">Rhizome</td><td class="column-6">Dryopteridaceae</td><td class="column-7">Bolbitis</td><td class="column-8">18 inches tall</td><td class="column-9">Moderate</td><td class="column-10">Africa</td><td class="column-11">Widespread in Africa</td>
</tr>
<tr class="row-37 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=60" target="_parent">Cabomba caroliniana</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Cabombaceae</td><td class="column-7">Cabomba</td><td class="column-8">Stem Width: 5-12cm (2-5.5in)</td><td class="column-9">Very Fast</td><td class="column-10">Americas</td><td class="column-11">North and South America</td>
</tr>
<tr class="row-38 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=346" target="_parent">Cabomba caroliniana 'Silver-Green'</a></td><td class="column-2">Moderate</td><td class="column-3">Medium High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Cabombaceae</td><td class="column-7">Cabomba</td><td class="column-8">Stem width 2 inches</td><td class="column-9">Fast</td><td class="column-10">Cultivar</td><td class="column-11">Cultivar</td>
</tr>
<tr class="row-39 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=107" target="_parent">Cabomba furcata</a></td><td class="column-2">Difficult</td><td class="column-3">High</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Cabombaceae</td><td class="column-7">Cabomba</td><td class="column-8">Stem width: 5-8cm (2-3in)</td><td class="column-9">Fast</td><td class="column-10">Central/South America</td><td class="column-11">Central and South America</td>
</tr>
<tr class="row-40 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=200" target="_parent">Cabomba palaeformis</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Cabombaceae</td><td class="column-7">Cabomba</td><td class="column-8">Stem width: 5-9 cm (2-3 in)</td><td class="column-9">Fast</td><td class="column-10">Central/South America</td><td class="column-11">Central America</td>
</tr>
<tr class="row-41 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=309" target="_parent">Callitriche terrestris</a></td><td class="column-2">Moderate</td><td class="column-3">Medium High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Plantaganaceae</td><td class="column-7">Callitriche</td><td class="column-8">Stem width 1 inch</td><td class="column-9">Fast</td><td class="column-10">North America</td><td class="column-11">Northeastern North America</td>
</tr>
<tr class="row-42 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=34" target="_parent">Cardamine lyrata</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Brassicaceae</td><td class="column-7">Cardamine</td><td class="column-8">Individual stem width: 2-4cm (0.5-1.5in)</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">Japan</td>
</tr>
<tr class="row-43 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=83" target="_parent">Ceratophyllum demersum</a></td><td class="column-2">Very Easy</td><td class="column-3">Low</td><td class="column-4">Not Specific</td><td class="column-5">Floating</td><td class="column-6">Ceratophyllaceae</td><td class="column-7">Ceratophyllum</td><td class="column-8">Individual stem width: 3-5cm (1-2in)</td><td class="column-9">Very Fast</td><td class="column-10">Cosmopolitan</td><td class="column-11">Cosmopolitan</td>
</tr>
<tr class="row-44 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=138" target="_parent">Ceratopteris pteridoides</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Floating</td><td class="column-6">Parkeriaceae</td><td class="column-7">Ceratopteris</td><td class="column-8">Width: 10-30cm (5-12</td><td class="column-9">Very fast</td><td class="column-10">Tropics</td><td class="column-11">Tropics</td>
</tr>
<tr class="row-45 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=311" target="_parent">Clinopodium brownei</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Lamiaceae</td><td class="column-7">Clinopodium</td><td class="column-8">Stem width 2 inches</td><td class="column-9">Fast</td><td class="column-10">North America, South America</td><td class="column-11">Southern USA to South America</td>
</tr>
<tr class="row-46 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=269" target="_parent">Crinum calamistratum</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Rosette</td><td class="column-6">Amaryllidaceae</td><td class="column-7">Crinum</td><td class="column-8">36 inches+ (91cm)</td><td class="column-9">Moderate</td><td class="column-10">Africa</td><td class="column-11">Western Cameroon</td>
</tr>
<tr class="row-47 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=46" target="_parent">Cryptocoryne beckettii 'petchii'</a></td><td class="column-2">Easy</td><td class="column-3">Low</td><td class="column-4">Red</td><td class="column-5">Rosette</td><td class="column-6">Araceae</td><td class="column-7">Cryptocoryne</td><td class="column-8">10-15cm (4-6in) in height</td><td class="column-9">Slow</td><td class="column-10">Asia</td><td class="column-11">Sri Lanka</td>
</tr>
<tr class="row-48 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=96" target="_parent">Cryptocoryne cordata var. cordata 'blassii'</a></td><td class="column-2">Easy</td><td class="column-3">Low</td><td class="column-4">Red</td><td class="column-5">Rosette</td><td class="column-6">Araceae</td><td class="column-7">Cryptocoryne</td><td class="column-8">Height: 7-20cm (3-8in)</td><td class="column-9">Slow</td><td class="column-10">Asia</td><td class="column-11">Malaysia, Thailand</td>
</tr>
<tr class="row-49 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=27" target="_parent">Cryptocoryne crispatula var. balansae</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Rosette</td><td class="column-6">Araceae</td><td class="column-7">Cryptocoryne</td><td class="column-8">Height: 60-90 cm (24-36in)</td><td class="column-9">Medium</td><td class="column-10">Asia</td><td class="column-11">Thailand</td>
</tr>
<tr class="row-50 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=171" target="_parent">Cryptocoryne parva</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Foreground</td><td class="column-5">Rosette</td><td class="column-6">Araceae</td><td class="column-7">Cryptocoryne</td><td class="column-8">Height: 5-10cm (2-4</td><td class="column-9">Slow</td><td class="column-10">Asia</td><td class="column-11">Sri Lanka</td>
</tr>
<tr class="row-51 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=155" target="_parent">Cryptocoryne pontederiifolia</a></td><td class="column-2">Easy</td><td class="column-3">Low</td><td class="column-4">Not Specific</td><td class="column-5">Rosette</td><td class="column-6">Araceae</td><td class="column-7">Cryptocoryne</td><td class="column-8">Height: 5-12</td><td class="column-9">Slow</td><td class="column-10">Asia</td><td class="column-11">Sumatra</td>
</tr>
<tr class="row-52 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=54" target="_parent">Cryptocoryne undulata</a></td><td class="column-2">Easy</td><td class="column-3">Low</td><td class="column-4">Not Specific</td><td class="column-5">Rosette</td><td class="column-6">Araceae</td><td class="column-7">Cryptocoryne</td><td class="column-8">Height: 10-15 cm (4-6in)</td><td class="column-9">Slow</td><td class="column-10">Asia</td><td class="column-11">Sri Lanka</td>
</tr>
<tr class="row-53 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=190" target="_parent">Cryptocoryne wendtii 'Green Gecko'</a></td><td class="column-2">Very Easy</td><td class="column-3">Low</td><td class="column-4">Not Specific</td><td class="column-5">Rosette</td><td class="column-6">Araceae</td><td class="column-7">Cryptocoryne</td><td class="column-8">Height: 10-15cm (4-6 in)</td><td class="column-9">Slow</td><td class="column-10">Cultivar</td><td class="column-11">Cultivar</td>
</tr>
<tr class="row-54 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=168" target="_parent">Cryptocoryne wendtii 'Mi Oya'</a></td><td class="column-2">Very Easy</td><td class="column-3">Low</td><td class="column-4">Red</td><td class="column-5">Rosette</td><td class="column-6">Araceae</td><td class="column-7">Cryptocoryne</td><td class="column-8">Height: 25-35cm (10-14</td><td class="column-9">Slow</td><td class="column-10">Asia</td><td class="column-11">Sri Lanka</td>
</tr>
<tr class="row-55 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=71" target="_parent">Cryptocoryne wendtii 'Red'</a></td><td class="column-2">Very Easy</td><td class="column-3">Low</td><td class="column-4">Red</td><td class="column-5">Rosette</td><td class="column-6">Araceae</td><td class="column-7">Cryptocoryne</td><td class="column-8">Height: 12-50cm<span style="mso-spacerun:yes">Â <br />
  </span>(5-20in)</td><td class="column-9">Medium</td><td class="column-10">Asia</td><td class="column-11">Sri Lanka</td>
</tr>
<tr class="row-56 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=196" target="_parent">Cryptocoryne x willisii 'lucens'</a></td><td class="column-2">Easy</td><td class="column-3">Low</td><td class="column-4">Not Specific</td><td class="column-5">Rosette</td><td class="column-6">Araceae</td><td class="column-7">Cryptocoryne</td><td class="column-8">Height: 10-20cm (4-8 in)</td><td class="column-9">Slow</td><td class="column-10">Southeast Asia</td><td class="column-11">Sri Lanka</td>
</tr>
<tr class="row-57 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=304" target="_parent">Cuphea anagalloidea</a></td><td class="column-2">Difficult</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Lythraceae</td><td class="column-7">Cuphea</td><td class="column-8">stem width 3/4 inch</td><td class="column-9">Moderate</td><td class="column-10">South America</td><td class="column-11">Eastern Brazil</td>
</tr>
<tr class="row-58 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=136" target="_parent">Cyperus helferi</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Rosette</td><td class="column-6">Cyperaceae</td><td class="column-7">Cyperus</td><td class="column-8">Height: 20-50cm (8-20in)</td><td class="column-9">Slow</td><td class="column-10">Asia</td><td class="column-11">Thailand</td>
</tr>
<tr class="row-59 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=41" target="_parent">Didiplis diandra</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Lythraceae</td><td class="column-7">Didiplis</td><td class="column-8">Individual stem width: 2-4cm (1-1.5in)</td><td class="column-9">Fast</td><td class="column-10">North America</td><td class="column-11">United States</td>
</tr>
<tr class="row-60 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=325" target="_parent">Diodia virginiana</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Rubiaceae</td><td class="column-7">Diodia</td><td class="column-8">Stem width 2.5 inches</td><td class="column-9">Moderate</td><td class="column-10">North America</td><td class="column-11">United States: Connecticut to Texas</td>
</tr>
<tr class="row-61 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=249" target="_parent">Diodia cf. kuntzei</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Rubiaceae</td><td class="column-7">Diodia</td><td class="column-8">stem width 6 inches</td><td class="column-9">Moderate</td><td class="column-10">South America</td><td class="column-11">Pantanal region, Brazil</td>
</tr>
<tr class="row-62 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=25" target="_parent">Echinodorus berteroi</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Rosette</td><td class="column-6">Alismataceae</td><td class="column-7">Echinodorus</td><td class="column-8">Up to 28 inches tall</td><td class="column-9">Medium</td><td class="column-10">Americas</td><td class="column-11">North and South America</td>
</tr>
<tr class="row-63 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=201" target="_parent">Echinodorus cordifolius</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Rosette</td><td class="column-6">Alismataceae</td><td class="column-7">Echinodorus</td><td class="column-8">Height: 30-50cm+ (12-20 in+)</td><td class="column-9">Medium</td><td class="column-10">Americas</td><td class="column-11">North and South America</td>
</tr>
<tr class="row-64 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=79" target="_parent">Echinodorus major</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Rosette</td><td class="column-6">Alismataceae</td><td class="column-7">Echinodorus</td><td class="column-8">Height: 30-60cm (12-24in)</td><td class="column-9">Medium</td><td class="column-10">Central/South America</td><td class="column-11">Eastern Brazil</td>
</tr>
<tr class="row-65 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=40" target="_parent">Echinodorus parviflorus 'Tropica'</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Rosette</td><td class="column-6">Alismataceae</td><td class="column-7">Echinodorus</td><td class="column-8">5-15cm (2-6in)</td><td class="column-9">Medium</td><td class="column-10">Cultivar</td><td class="column-11">Cultivar</td>
</tr>
<tr class="row-66 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=106" target="_parent">Echinodorus uruguayensis</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Rosette</td><td class="column-6">Alismataceae</td><td class="column-7">Echinodorus</td><td class="column-8">Height: 30-60cm+ (12-24in+)</td><td class="column-9">Medium</td><td class="column-10">Central/South America</td><td class="column-11">Parts of Brazil, Uruguay, Chile and Argentina</td>
</tr>
<tr class="row-67 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=170" target="_parent">Echinodorus 'Kleiner Bar'</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Red</td><td class="column-5">Rosette</td><td class="column-6">Alismataceae</td><td class="column-7">Echinodorus</td><td class="column-8">Height: 15-40cm (6-16")</td><td class="column-9">Medium</td><td class="column-10">Cultivar</td><td class="column-11">Cultivar</td>
</tr>
<tr class="row-68 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=308" target="_parent">Echinodorus 'Ozelot'</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Red</td><td class="column-5">Rosette</td><td class="column-6">Alismataceae</td><td class="column-7">Echinodorus</td><td class="column-8">height: 18 inches+</td><td class="column-9">Moderate</td><td class="column-10">Cultivar</td><td class="column-11">Cultivar</td>
</tr>
<tr class="row-69 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=191" target="_parent">Echinodorus 'Rubin'</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Red</td><td class="column-5">Rosette</td><td class="column-6">Alismataceae</td><td class="column-7">Echinodorus</td><td class="column-8">Height: 45-75cm+ (18-30 in+)</td><td class="column-9">Medium</td><td class="column-10">Cultivar</td><td class="column-11">Cultivar</td>
</tr>
<tr class="row-70 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=105" target="_parent">Echinodorus x barthii</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Red</td><td class="column-5">Rosette</td><td class="column-6">Alismataceae</td><td class="column-7">Echinodorus</td><td class="column-8">Height: 25-50cm (10-20in)</td><td class="column-9">Medium</td><td class="column-10">Cultivar</td><td class="column-11">Cultivar</td>
</tr>
<tr class="row-71 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=92" target="_parent">Egeria densa</a></td><td class="column-2">Very Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Hydrocharitaceae</td><td class="column-7">Egeria</td><td class="column-8">Individual stem width: 3-7 cm (1-2.5 in)</td><td class="column-9">Very fast</td><td class="column-10">Central/South America</td><td class="column-11">Brazil, Argentina, Uruguay; introduced to other continents</td>
</tr>
<tr class="row-72 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=126" target="_parent">Egeria najas</a></td><td class="column-2">Very Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Hydrocharitaceae</td><td class="column-7">Egeria</td><td class="column-8">Stem width: 3-5cm (1-2</td><td class="column-9">Very fast</td><td class="column-10">Central/South America</td><td class="column-11">Paraguay</td>
</tr>
<tr class="row-73 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=95" target="_parent">Eichhornia diversifolia</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Pontederiaceae</td><td class="column-7">Eichhornia</td><td class="column-8">Stem width: 8-15cm (3-6in)</td><td class="column-9">Medium</td><td class="column-10">Central/South America</td><td class="column-11">Antilles, Guyana, Venezuela, Brazil</td>
</tr>
<tr class="row-74 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=202" target="_parent">Elatine triandra</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Foreground</td><td class="column-5">Stem</td><td class="column-6">Elatinaceae</td><td class="column-7">Elatine</td><td class="column-8">Stem width: 1-2 cm (0.5-1 in)</td><td class="column-9">Fast</td><td class="column-10">Cosmopolitan</td><td class="column-11">Cosmopolitan (not South America)</td>
</tr>
<tr class="row-75 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=154" target="_parent">Eleocharis acicularis</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Foreground</td><td class="column-5">Rosette</td><td class="column-6">Cyperaceae</td><td class="column-7">Eleocharis</td><td class="column-8">Height: 10-15cm (4-6 in)</td><td class="column-9">Medium</td><td class="column-10">Cosmopolitan</td><td class="column-11">Cosmopolitan</td>
</tr>
<tr class="row-76 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=161" target="_parent">Eleocharis fluctuans</a></td><td class="column-2">Difficult</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Cyperaceae</td><td class="column-7">Eleocharis</td><td class="column-8">Stem width: 6-9cm (2-3</td><td class="column-9">Fast</td><td class="column-10">Central/South America</td><td class="column-11">Brazil, Venezuela</td>
</tr>
<tr class="row-77 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=120" target="_parent">Eriocaulon cinereum</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Foreground</td><td class="column-5">Rosette</td><td class="column-6">Eriocaulaceae</td><td class="column-7">Eriocaulon</td><td class="column-8">Height: 3-8cm (1-3</td><td class="column-9">Slow</td><td class="column-10">Asia</td><td class="column-11">East Asia</td>
</tr>
<tr class="row-78 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=84" target="_parent">Eriocaulon setaceum</a></td><td class="column-2">Difficult</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Eriocaulaceae</td><td class="column-7">Eriocaulon</td><td class="column-8">Individual stem width: 6-16cm (3-6in)</td><td class="column-9">Medium</td><td class="column-10">Australasia</td><td class="column-11">Australasia</td>
</tr>
<tr class="row-79 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=143" target="_parent">Eriocaulon sp. 'Mato Grosso'</a></td><td class="column-2">Very Difficult</td><td class="column-3">High</td><td class="column-4">Foreground</td><td class="column-5">Rosette</td><td class="column-6">Eriocaulaceae</td><td class="column-7">Eriocaulon</td><td class="column-8">Height: 10cm (4</td><td class="column-9">Slow</td><td class="column-10">Central/South America</td><td class="column-11">Mato Grosso, Brazil</td>
</tr>
<tr class="row-80 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=144" target="_parent">Eriocaulon sp. from Goias</a></td><td class="column-2">Difficult</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Rosette</td><td class="column-6">Eriocaulaceae</td><td class="column-7">Eriocaulon</td><td class="column-8">Height: 20cm (8</td><td class="column-9">Slow</td><td class="column-10">Central/South America</td><td class="column-11">Goias, Brazil</td>
</tr>
<tr class="row-81 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=57" target="_parent">Glossostigma elatinoides</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Foreground</td><td class="column-5">Stem</td><td class="column-6">Phrymaceae</td><td class="column-7">Glossostigma</td><td class="column-8">2-3 cm (1-1.5in)</td><td class="column-9">Fast</td><td class="column-10">Australasia</td><td class="column-11">Australia</td>
</tr>
<tr class="row-82 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=344" target="_parent">Gymnocoronis spilanthoides</a></td><td class="column-2">Easy</td><td class="column-3">Low</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Asteraceae</td><td class="column-7">Gymnocoronis</td><td class="column-8">Stem width 6 inches</td><td class="column-9">Fast</td><td class="column-10">South America</td><td class="column-11">Southern South America</td>
</tr>
<tr class="row-83 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=156" target="_parent">Helanthium bolivianum 'Angustifolius'</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Rosette</td><td class="column-6">Alismataceae</td><td class="column-7">Helanthium</td><td class="column-8">Height: 12-18 inches (30-40 cm)</td><td class="column-9">Fast</td><td class="column-10">Central/South America</td><td class="column-11">Brazil</td>
</tr>
<tr class="row-84 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=216" target="_parent">Helanthium tenellum</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Foreground</td><td class="column-5">Rosette</td><td class="column-6">Alismataceae</td><td class="column-7">Helanthium</td><td class="column-8">2-3 inches (5-8cm)</td><td class="column-9">Fast</td><td class="column-10">North, Central, and South America</td><td class="column-11">Locations of specific aquarium varieties are unknown</td>
</tr>
<tr class="row-85 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=51" target="_parent">Hemianthus callitrichoides</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Foreground</td><td class="column-5">Stem</td><td class="column-6">Linderniaceae</td><td class="column-7">Hemianthus</td><td class="column-8">Individual stem width: 0.5cm (0.25in)</td><td class="column-9">Medium</td><td class="column-10">Central/South America</td><td class="column-11">Greater Antilles (Cuba, Hispaniola, Jamaica, Puerto Rico),<br />
  Bahamas</td>
</tr>
<tr class="row-86 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=33" target="_parent">Hemianthus glomeratus</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Linderniaceae</td><td class="column-7">Hemianthus</td><td class="column-8">Individual stem width: 0.5-1cm (.25-.5in)</td><td class="column-9">Fast</td><td class="column-10">North America</td><td class="column-11">Florida</td>
</tr>
<tr class="row-87 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=67" target="_parent">Heteranthera zosterifolia</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Pontederiaceae</td><td class="column-7">Heteranthera</td><td class="column-8">Individual stem width: 5-12cm (2-5in)</td><td class="column-9">Fast</td><td class="column-10">Central/South America</td><td class="column-11">Brazil</td>
</tr>
<tr class="row-88 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=42" target="_parent">Hottonia palustris</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Primulaceae</td><td class="column-7">Hottonia</td><td class="column-8">Individual stem width: 2-5cm (1-2in)</td><td class="column-9">Fast</td><td class="column-10">Europe</td><td class="column-11">Europe</td>
</tr>
<tr class="row-89 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=316" target="_parent">Hydrilla verticillata</a></td><td class="column-2">Very Easy</td><td class="column-3">Low</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Hydrocharitaceae</td><td class="column-7">Hydrilla</td><td class="column-8">stem width two inches</td><td class="column-9">Very fast</td><td class="column-10">Cosmopolitan</td><td class="column-11">Cosmopolitan</td>
</tr>
<tr class="row-90 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=146" target="_parent">Hydrocotyle leucocephala</a></td><td class="column-2">Very Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Araliaceae</td><td class="column-7">Hydrocotyle</td><td class="column-8">Stem width: 6-10cm (2-4</td><td class="column-9">Fast</td><td class="column-10">Central/South America</td><td class="column-11">South America</td>
</tr>
<tr class="row-91 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=142" target="_parent">Hydrocotyle sibthorpioides</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Araliaceae</td><td class="column-7">Hydrocotyle</td><td class="column-8">Leaf width:<span style="mso-spacerun:yes">Â  </span>0.5-2cm<br />
  (.25-.75in)</td><td class="column-9">Medium</td><td class="column-10">Asia</td><td class="column-11">Southeastern Asia</td>
</tr>
<tr class="row-92 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=53" target="_parent">Hydrocotyle verticillata</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Foreground</td><td class="column-5">Rhizome</td><td class="column-6">Araliaceae</td><td class="column-7">Hydrocotyle</td><td class="column-8">3-7 cm (1-3in)</td><td class="column-9">Medium</td><td class="column-10">Americas</td><td class="column-11">North and South America</td>
</tr>
<tr class="row-93 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=222" target="_parent">Hydrotriche hottoniiflora</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Plantaganaceae</td><td class="column-7">Hydrotriche</td><td class="column-8">4 inches</td><td class="column-9">Fast</td><td class="column-10">Africa</td><td class="column-11">Madagascar</td>
</tr>
<tr class="row-94 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=137" target="_parent">Hygrophila balsamica</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Acanthaceae</td><td class="column-7">Hygrophila</td><td class="column-8">Stem width: 5-20cm (2-8 in)</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">Sri Lanka, India</td>
</tr>
<tr class="row-95 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=139" target="_parent">Hygrophila corymbosa 'angustifolia'</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Acanthaceae</td><td class="column-7">Hygrophila</td><td class="column-8">Stem width: 15-25cm (6-10</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">Southeast Asia</td>
</tr>
<tr class="row-96 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=226" target="_parent">Hygrophila corymbosa 'Siamensis'</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Acanthaceae</td><td class="column-7">Hygrophila</td><td class="column-8">stem width 6 inches (15cm)</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">Thailand</td>
</tr>
<tr class="row-97 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=238" target="_parent">Hygrophila corymbosa 'Stricta'</a></td><td class="column-2">Easy</td><td class="column-3">Medium Low</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Acanthaceae</td><td class="column-7">Hygrophila</td><td class="column-8">stem width 6 inches (15cm)</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">Southeast Asia</td>
</tr>
<tr class="row-98 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=62" target="_parent">Hygrophila difformis</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Acanthaceae</td><td class="column-7">Hygrophila</td><td class="column-8">Individual stem width: 5-30cm (2-12 inches)</td><td class="column-9">Very fast</td><td class="column-10">Asia</td><td class="column-11">Burma, India, Thailand, parts of Malaysia</td>
</tr>
<tr class="row-99 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=341" target="_parent">Hygrophila lancea</a></td><td class="column-2">Moderate</td><td class="column-3">Medium High</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Acanthaceae</td><td class="column-7">Hygrophila</td><td class="column-8">Stem width 3 inches</td><td class="column-9">Moderate</td><td class="column-10">Asia</td><td class="column-11">Sarawak</td>
</tr>
<tr class="row-100 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=331" target="_parent">Hygrophila odora</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Acanthaceae</td><td class="column-7">Hygrophila</td><td class="column-8">Stem width 7 inches</td><td class="column-9">Moderate</td><td class="column-10">Africa</td><td class="column-11">Guinea, elsewhere?</td>
</tr>
<tr class="row-101 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=75" target="_parent">Hygrophila polysperma</a></td><td class="column-2">Very Easy</td><td class="column-3">Low</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Acanthaceae</td><td class="column-7">Hygrophila</td><td class="column-8">Individual stem width: 8-15cm (3-6in)</td><td class="column-9">Very fast</td><td class="column-10">Asia</td><td class="column-11">India, Bhutan</td>
</tr>
<tr class="row-102 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=147" target="_parent">Hygrophila polysperma 'Ceylon'</a></td><td class="column-2">Very Easy</td><td class="column-3">Medium</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Acanthaceae</td><td class="column-7">Hygrophila</td><td class="column-8">Stem width: 10-15cm (4-6in)</td><td class="column-9">Very fast</td><td class="column-10">Asia</td><td class="column-11">Sri Lanka</td>
</tr>
<tr class="row-103 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=35" target="_parent">Hygrophila polysperma 'Sunset'</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Acanthaceae</td><td class="column-7">Hygrophila</td><td class="column-8">Stem width: 6-10 cm (2-4 in)</td><td class="column-9">Fast</td><td class="column-10">Cultivar</td><td class="column-11">Cultivar</td>
</tr>
<tr class="row-104 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=254" target="_parent">Hygrophila sp. 'Araguaia'</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Foreground</td><td class="column-5">Stem</td><td class="column-6">Acanthaceae</td><td class="column-7">Hygrophila</td><td class="column-8">stem width 3 inches</td><td class="column-9">Moderate</td><td class="column-10">South America</td><td class="column-11">Araguia river</td>
</tr>
<tr class="row-105 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=244" target="_parent">Hygrophila sp. 'Bold'</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Acanthaceae</td><td class="column-7">Hygrophila</td><td class="column-8">stem width 4 inches</td><td class="column-9">Fast</td><td class="column-10">Asia?</td><td class="column-11">Unknown</td>
</tr>
<tr class="row-106 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=134" target="_parent">Hygrophila sp. 'Red'</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Acanthaceae</td><td class="column-7">Hygrophila</td><td class="column-8">Stem width:<span style="mso-spacerun:yes">Â  </span>5-20cm<br />
  (2-8in)</td><td class="column-9">Slow</td><td class="column-10">Asia</td><td class="column-11">Southeastern Asia</td>
</tr>
<tr class="row-107 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=245" target="_parent">Hygrophila sp. 'Tiger'</a></td><td class="column-2">Very Easy</td><td class="column-3">Low</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Acanthaceae</td><td class="column-7">Hygrophila</td><td class="column-8">Stem width 6 inches</td><td class="column-9">Very Fast</td><td class="column-10">Unknown</td><td class="column-11">Unknown</td>
</tr>
<tr class="row-108 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=150" target="_parent">Hyptis lorentziana</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Lamiaceae</td><td class="column-7">Hyptis</td><td class="column-8">Stem width: 10-12cm (4-5 inches)</td><td class="column-9">Fast</td><td class="column-10">South America</td><td class="column-11">Widespread in South America</td>
</tr>
<tr class="row-109 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=157" target="_parent">Juncus repens</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Juncaceae</td><td class="column-7">Juncus</td><td class="column-8">Stem width: 5-7cm (2-3 in)</td><td class="column-9">Fast</td><td class="column-10">North America</td><td class="column-11">United States, Cuba</td>
</tr>
<tr class="row-110 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=102" target="_parent">Lagarosiphon madagascariensis</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Hydrocharitaceae</td><td class="column-7">Lagarosiphon</td><td class="column-8">Stem width: 2-4cm (1-1.5in)</td><td class="column-9">Fast</td><td class="column-10">Africa</td><td class="column-11">Madagascar</td>
</tr>
<tr class="row-111 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=127" target="_parent">Lagarosiphon major</a></td><td class="column-2">Very Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Hydrocharitaceae</td><td class="column-7">Lagarosiphon</td><td class="column-8">Stem width: 3-5cm (1-2</td><td class="column-9">Fast</td><td class="column-10">Africa</td><td class="column-11">South Africa, Zimbabwe</td>
</tr>
<tr class="row-112 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=131" target="_parent">Lemna minor</a></td><td class="column-2">Very Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Floating</td><td class="column-6">Lemnaceae</td><td class="column-7">Lemna</td><td class="column-8">0.25cm+ (0.1</td><td class="column-9">Very fast</td><td class="column-10">Cosmopolitan</td><td class="column-11">Worldwide, except East Asia and Australia</td>
</tr>
<tr class="row-113 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=125" target="_parent">Lilaeopsis brasiliensis</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Foreground</td><td class="column-5">Rhizome</td><td class="column-6">Apiaceae</td><td class="column-7">Lilaeopsis</td><td class="column-8">Height: 3-6cm (1-2</td><td class="column-9">Medium</td><td class="column-10">Central/South America</td><td class="column-11">Brazil</td>
</tr>
<tr class="row-114 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=61" target="_parent">Limnobium laevigatum</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Floating</td><td class="column-6">Hydrocharitaceae</td><td class="column-7">Limnobium</td><td class="column-8">Width: 1-8cm (.5-3in)</td><td class="column-9">Very Fast</td><td class="column-10">Americas</td><td class="column-11">Central and South America</td>
</tr>
<tr class="row-115 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=98" target="_parent">Limnophila aromatica</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Plantaganaceae</td><td class="column-7">Limnophila</td><td class="column-8">Stem width: 5-8cm (2-3in)</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">Southeast Asia</td>
</tr>
<tr class="row-116 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=221" target="_parent">Limnophila repens</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Plantaganaceae</td><td class="column-7">Limnophila</td><td class="column-8">3 inches</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">India and Sri Lanka to the Philippines and Australia</td>
</tr>
<tr class="row-117 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=36" target="_parent">Limnophila sessiliflora</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Plantaganaceae</td><td class="column-7">Limnophila</td><td class="column-8">Individual stem width: 4-7cm (1.5-3in)</td><td class="column-9">Very fast</td><td class="column-10">Asia</td><td class="column-11">Southeast Asia</td>
</tr>
<tr class="row-118 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=323" target="_parent">Limnophila sp. 'Broad'</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Plantaganaceae</td><td class="column-7">Limnophila</td><td class="column-8">Stem width 3 inches</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">Unknown</td>
</tr>
<tr class="row-119 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=43" target="_parent">Limnophila sp. 'Gigantea'</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Plantaganaceae</td><td class="column-7">Limnophila</td><td class="column-8">Individual stem width: 8-12cm (3-5in)</td><td class="column-9">Very fast</td><td class="column-10">Asia</td><td class="column-11">Southeast Asia</td>
</tr>
<tr class="row-120 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=327" target="_parent">Limnophila sp. 'Guinea Broad-Leaf'</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Foreground</td><td class="column-5">Stem</td><td class="column-6">Plantaganaceae</td><td class="column-7">Limnophila</td><td class="column-8">Stem width 1.5 inches</td><td class="column-9">Fast</td><td class="column-10">Africa</td><td class="column-11">Guinea, elsewhere?</td>
</tr>
<tr class="row-121 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=335" target="_parent">Limnophila sp. 'Sulawesi'</a></td><td class="column-2">Moderate</td><td class="column-3">Medium High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Plantaganaceae</td><td class="column-7">Limnophila</td><td class="column-8">Stem width 5 inches</td><td class="column-9">Moderate</td><td class="column-10">Asia</td><td class="column-11">Sulawesi, elsewhere?</td>
</tr>
<tr class="row-122 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=250" target="_parent">Lindernia dubia</a></td><td class="column-2">Moderate</td><td class="column-3">Medium High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Linderniaceae</td><td class="column-7">Lindernia</td><td class="column-8">stem width 3 inches</td><td class="column-9">Moderate</td><td class="column-10">North America, Caribbean, Central America, South America</td><td class="column-11">Widespread in New World</td>
</tr>
<tr class="row-123 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=340" target="_parent">Lindernia grandiflora</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Linderniaceae</td><td class="column-7">Lindernia</td><td class="column-8">Stem width 1 inch</td><td class="column-9">Moderate</td><td class="column-10">North America</td><td class="column-11">Florida (endemic)</td>
</tr>
<tr class="row-124 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=322" target="_parent">Lindernia rotundifolia 'Variegated'</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Linderniaceae</td><td class="column-7">Lindernia</td><td class="column-8">Stem width 1 inch</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">cultivar</td>
</tr>
<tr class="row-125 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=228" target="_parent">Lindernia sp. 'India'</a></td><td class="column-2">Moderate</td><td class="column-3">Medium High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Linderniaceae</td><td class="column-7">Lindernia</td><td class="column-8">1/2 inch stem width</td><td class="column-9">Slow</td><td class="column-10">Asia</td><td class="column-11">India</td>
</tr>
<tr class="row-126 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=108" target="_parent">Lobelia cardinalis</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Lobeliaceae</td><td class="column-7">Lobelia</td><td class="column-8">Stem width: 7-15cm (3-6in)</td><td class="column-9">Medium</td><td class="column-10">North America</td><td class="column-11">Temperate and Subtropical North America</td>
</tr>
<tr class="row-127 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=152" target="_parent">Lobelia cardinalis 'Small Form'</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Foreground</td><td class="column-5">Stem</td><td class="column-6">Lobeliaceae</td><td class="column-7">Lobelia</td><td class="column-8">Stem width:<span style="mso-spacerun:yes">Â  </span>3-7cm (1-3</td><td class="column-9">Medium</td><td class="column-10">Cultivar</td><td class="column-11">Cultivar</td>
</tr>
<tr class="row-128 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=91" target="_parent">Ludwigia arcuata</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Onagraceae</td><td class="column-7">Ludwigia</td><td class="column-8">Individual stem width: 3-5cm (1-2in)</td><td class="column-9">Fast</td><td class="column-10">North America</td><td class="column-11">Southeastern United States</td>
</tr>
<tr class="row-129 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=141" target="_parent">Ludwigia brevipes</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Onagraceae</td><td class="column-7">Ludwigia</td><td class="column-8">Stem width: 4-6cm (1.5-2.5in)</td><td class="column-9">Fast</td><td class="column-10">North America</td><td class="column-11">southeastern United States</td>
</tr>
<tr class="row-130 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=56" target="_parent">Ludwigia glandulosa</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Onagraceae</td><td class="column-7">Ludwigia</td><td class="column-8">Individual stem width: 5-12cm (2-5in)</td><td class="column-9">Medium</td><td class="column-10">North America</td><td class="column-11">Southeastern United States</td>
</tr>
<tr class="row-131 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=195" target="_parent">Ludwigia inclinata</a></td><td class="column-2">Difficult</td><td class="column-3">High</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Onagraceae</td><td class="column-7">Ludwigia</td><td class="column-8">Individual stem width: 3-5cm (1-2in)</td><td class="column-9">Fast</td><td class="column-10">Central/South America</td><td class="column-11">South America</td>
</tr>
<tr class="row-132 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=286" target="_parent">Ludwigia inclinata var verticillata 'Araguaia'</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Onagraceae</td><td class="column-7">Ludwigia</td><td class="column-8">stem width 4 inches (10cm)</td><td class="column-9">Fast</td><td class="column-10">South America</td><td class="column-11">Rio Araguaia, Brazil</td>
</tr>
<tr class="row-133 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=81" target="_parent">Ludwigia inclinata var. verticillata 'Cuba'</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Onagraceae</td><td class="column-7">Ludwigia</td><td class="column-8">Individual stem width: 10-15cm (4-6in)</td><td class="column-9">Fast</td><td class="column-10">Central/South America</td><td class="column-11">Cuba</td>
</tr>
<tr class="row-134 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=69" target="_parent">Ludwigia inclinata var. verticillata 'Pantanal'</a></td><td class="column-2">Difficult</td><td class="column-3">High</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Onagraceae</td><td class="column-7">Ludwigia</td><td class="column-8">Individual stem width: 5-10cm (2-4in)</td><td class="column-9">Fast</td><td class="column-10">Central/South America</td><td class="column-11">Brazil</td>
</tr>
<tr class="row-135 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=94" target="_parent">Ludwigia ovalis</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Onagraceae</td><td class="column-7">Ludwigia</td><td class="column-8">Stem width: 3-6cm (1-2in)</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">East Asia; specifically widespread in Japan and Taiwan</td>
</tr>
<tr class="row-136 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=121" target="_parent">Ludwigia palustris</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Onagraceae</td><td class="column-7">Ludwigia</td><td class="column-8">Stem width: 4-7cm (1.5-3in)</td><td class="column-9">Fast</td><td class="column-10">Cosmopolitan</td><td class="column-11">Americas, North Africa, Europe, Asia</td>
</tr>
<tr class="row-137 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=26" target="_parent">Ludwigia repens</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Onagraceae</td><td class="column-7">Ludwigia</td><td class="column-8">Individual stem width: 5-8 cm(2-3in)</td><td class="column-9">Fast</td><td class="column-10">North America</td><td class="column-11">Southern North America</td>
</tr>
<tr class="row-138 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=319" target="_parent">Ludwigia repens x L. arcuata</a></td><td class="column-2">Easy</td><td class="column-3">Low</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Onagraceae</td><td class="column-7">Ludwigia</td><td class="column-8">stem width 2 inches</td><td class="column-9">Fast</td><td class="column-10">North America</td><td class="column-11">Florida</td>
</tr>
<tr class="row-139 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=112" target="_parent">Ludwigia sedoides</a></td><td class="column-2">Easy</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Floating</td><td class="column-6">Onagraceae</td><td class="column-7">Ludwigia</td><td class="column-8">Diameter: 10-15cm (4-6in)</td><td class="column-9">Fast</td><td class="column-10">Central/South America</td><td class="column-11">South America</td>
</tr>
<tr class="row-140 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=162" target="_parent">Ludwigia senegalensis</a></td><td class="column-2">Difficult</td><td class="column-3">High</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Onagraceae</td><td class="column-7">Ludwigia</td><td class="column-8">Stem width: 5-8cm (2-3</td><td class="column-9">Medium</td><td class="column-10">Africa</td><td class="column-11">Western and Central Africa</td>
</tr>
<tr class="row-141 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=338" target="_parent">Ludwigia sphaerocarpa</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Foreground</td><td class="column-5">Stem</td><td class="column-6">Onagraceae</td><td class="column-7">Ludwigia</td><td class="column-8">Stem width - five inches</td><td class="column-9">Moderate</td><td class="column-10">North America</td><td class="column-11">USA - Massachusetts to Texas</td>
</tr>
<tr class="row-142 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=218" target="_parent">Ludwigia sp. 'Rubin'</a></td><td class="column-2">Easy</td><td class="column-3">Low to Very High</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Onagraceae</td><td class="column-7">Ludwigia</td><td class="column-8">4 inches</td><td class="column-9">Fast</td><td class="column-10">Unknown</td><td class="column-11">Unknown</td>
</tr>
<tr class="row-143 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=334" target="_parent">Ludwigia x lacustris</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Onagraceae</td><td class="column-7">Ludwigia</td><td class="column-8">Stem width 2 inches</td><td class="column-9">Fast</td><td class="column-10">North America</td><td class="column-11">Scattered locations from Rhode Island to Georgia</td>
</tr>
<tr class="row-144 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=111" target="_parent">Lysimachia nummularia 'Aurea'</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Primulaceae</td><td class="column-7">Lysimachia</td><td class="column-8">Stem width: 3cm (1in)</td><td class="column-9">Medium</td><td class="column-10">Cultivar</td><td class="column-11">Cultivar</td>
</tr>
<tr class="row-145 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=313" target="_parent">Marsilea spp.</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Foreground</td><td class="column-5">Moss / Fern</td><td class="column-6">Marsileaceae</td><td class="column-7">Marsilea</td><td class="column-8">1/8-1-2 inch leaf width, 1/4-1 inch tall submersed growth</td><td class="column-9">Moderate</td><td class="column-10">Cosmopolitan</td><td class="column-11">Cosmopolitan</td>
</tr>
<tr class="row-146 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=255" target="_parent">Mayaca fluviatilis</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Mayacaceae</td><td class="column-7">Mayaca</td><td class="column-8">stem width 1 inch</td><td class="column-9">Fast</td><td class="column-10">North, Central and South America</td><td class="column-11">Widespread</td>
</tr>
<tr class="row-147 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=185" target="_parent">Micranthemum umbrosum</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Linderniaceae</td><td class="column-7">Micranthemum</td><td class="column-8">Stem width: 1-2cm (0.5-1in)</td><td class="column-9">Fast</td><td class="column-10">North America</td><td class="column-11">United States</td>
</tr>
<tr class="row-148 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=37" target="_parent">Microsorum pteropus</a></td><td class="column-2">Very Easy</td><td class="column-3">Low</td><td class="column-4">Epiphyte</td><td class="column-5">Moss / Fern</td><td class="column-6">Polypodiaceae</td><td class="column-7">Microsorum</td><td class="column-8">Height: 15-30cm (6-12in)</td><td class="column-9">Medium</td><td class="column-10">Asia</td><td class="column-11">Southeast Asia</td>
</tr>
<tr class="row-149 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=232" target="_parent">Microsorum pteropus 'Philippine'</a></td><td class="column-2">Easy</td><td class="column-3">Low</td><td class="column-4">Epiphyte</td><td class="column-5">Rhizome</td><td class="column-6">Polypodiaceae</td><td class="column-7">Microsorum</td><td class="column-8">16 inches (40cm)</td><td class="column-9">Medium</td><td class="column-10">Southeast Asia</td><td class="column-11">Philippines</td>
</tr>
<tr class="row-150 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=310" target="_parent">Microsorum pteropus 'Trident'</a></td><td class="column-2">Very Easy</td><td class="column-3">Low</td><td class="column-4">Epiphyte</td><td class="column-5">Moss / Fern</td><td class="column-6">Polypodiaceae</td><td class="column-7">Microsorum</td><td class="column-8">Leaf width 4 inches</td><td class="column-9">Moderate</td><td class="column-10">Asia</td><td class="column-11">Sarawak</td>
</tr>
<tr class="row-151 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=241" target="_parent">Microsorum pteropus 'Tropica'</a></td><td class="column-2">Very Easy</td><td class="column-3">Low</td><td class="column-4">Epiphyte</td><td class="column-5">Rhizome</td><td class="column-6">Polypodiaceae</td><td class="column-7">Microsorum</td><td class="column-8">18 inches tall</td><td class="column-9">Moderate</td><td class="column-10">Cultivar</td><td class="column-11">Cultivar</td>
</tr>
<tr class="row-152 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=194" target="_parent">Microsorum pteropus 'Windelov'</a></td><td class="column-2">Very Easy</td><td class="column-3">Low</td><td class="column-4">Epiphyte</td><td class="column-5">Moss / Fern</td><td class="column-6">Polypodiaceae</td><td class="column-7">Microsorum</td><td class="column-8">Height: 10-20 cm (4-8 in)</td><td class="column-9">Slow</td><td class="column-10">Cultivar</td><td class="column-11">Cultivar</td>
</tr>
<tr class="row-153 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=153" target="_parent">Monosolenium tenerum</a></td><td class="column-2">Easy</td><td class="column-3">Low</td><td class="column-4">Epiphyte</td><td class="column-5">Moss / Fern</td><td class="column-6">Monoseleniaceae</td><td class="column-7">Monosolenium</td><td class="column-8">Size: Infinite</td><td class="column-9">Medium</td><td class="column-10">Asia</td><td class="column-11">Asia</td>
</tr>
<tr class="row-154 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=301" target="_parent">Murdannia keisak</a></td><td class="column-2">Moderate</td><td class="column-3">Medium High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Commelinaceae</td><td class="column-7">Murdannia</td><td class="column-8">stem width 4 inches</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">widespread in Asia, introduced elsewhere</td>
</tr>
<tr class="row-155 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=336" target="_parent">Murdannia sp. 'Red'</a></td><td class="column-2">Moderate</td><td class="column-3">Medium High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Commelinaceae</td><td class="column-7">Murdannia</td><td class="column-8">Stem width 4 inches</td><td class="column-9">Moderate</td><td class="column-10">Asia?</td><td class="column-11">Unknown</td>
</tr>
<tr class="row-156 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=176" target="_parent">Myriophyllum aquaticum</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Haloragaceae</td><td class="column-7">Myriophyllum</td><td class="column-8">Stem width: 5-10cm (2-4")</td><td class="column-9">Very fast</td><td class="column-10">Central/South America</td><td class="column-11">South America</td>
</tr>
<tr class="row-157 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=48" target="_parent">Myriophyllum mattogrossense</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Haloragaceae</td><td class="column-7">Myriophyllum</td><td class="column-8">Individual stem width: 5-8cm (2-3in)</td><td class="column-9">Very fast</td><td class="column-10">South America</td><td class="column-11">Bolivia, Ecuador, Brazil, Peru</td>
</tr>
<tr class="row-158 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=130" target="_parent">Myriophyllum propinquum</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Haloragaceae</td><td class="column-7">Myriophyllum</td><td class="column-8">Stem width: 5-7cm (2-3</td><td class="column-9">Fast</td><td class="column-10">Central/South America</td><td class="column-11">South America</td>
</tr>
<tr class="row-159 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=114" target="_parent">Myriophyllum tuberculatum</a></td><td class="column-2">Difficult</td><td class="column-3">High</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Haloragaceae</td><td class="column-7">Myriophyllum</td><td class="column-8">Stem width: 5-10cm (2-4in)</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">India, Pakistan, Indonesia</td>
</tr>
<tr class="row-160 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=47" target="_parent">Nymphaea lotus 'Red'</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Red</td><td class="column-5">Bulb</td><td class="column-6">Nymphaeaceae</td><td class="column-7">Nymphaea</td><td class="column-8">Height: 20-80cm (8-32in)</td><td class="column-9">Medium</td><td class="column-10">Africa</td><td class="column-11">West Africa</td>
</tr>
<tr class="row-161 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=109" target="_parent">Nymphaea micrantha</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Red</td><td class="column-5">Bulb</td><td class="column-6">Nymphaeaceae</td><td class="column-7">Nymphaea</td><td class="column-8">Height: 20-80cm (8-32in)</td><td class="column-9">Medium</td><td class="column-10">Africa</td><td class="column-11">West Africa</td>
</tr>
<tr class="row-162 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=247" target="_parent">Oldenlandia salzmannii</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Rubiaceae</td><td class="column-7">Oldenlandia</td><td class="column-8">Stem width 2 inches</td><td class="column-9">Fast</td><td class="column-10">South America</td><td class="column-11">Brazil</td>
</tr>
<tr class="row-163 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=242" target="_parent">Penthorum sedoides</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Penthoraceae</td><td class="column-7">Penthorum</td><td class="column-8">stem width 4 inches</td><td class="column-9">Slow</td><td class="column-10">North America</td><td class="column-11">Eastern United States</td>
</tr>
<tr class="row-164 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=240" target="_parent">Persicaria hydropiperoides</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Polygonaceae</td><td class="column-7">Persicaria</td><td class="column-8">Stem width 5 inches</td><td class="column-9">Fast</td><td class="column-10">North and South America</td><td class="column-11">North and South America</td>
</tr>
<tr class="row-165 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=278" target="_parent">Persicaria praetermissa</a></td><td class="column-2">Moderate</td><td class="column-3">Medium High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Polygonaceae</td><td class="column-7">Persicaria</td><td class="column-8">Stem width 4 inches</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">China, India, Sri Lanka, Australia, Taiwan, Japan, Philippines</td>
</tr>
<tr class="row-166 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=252" target="_parent">Persicaria sp. 'acre'</a></td><td class="column-2">Moderate</td><td class="column-3">Medium High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Polygonaceae</td><td class="column-7">Persicaria</td><td class="column-8">stem width 4 inches</td><td class="column-9">Fast</td><td class="column-10">unknown</td><td class="column-11">Unknown</td>
</tr>
<tr class="row-167 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=239" target="_parent">Persicaria sp. 'Kawagoeanum'</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Polygonaceae</td><td class="column-7">Persicaria</td><td class="column-8">stem width 6 inches (15cm)</td><td class="column-9">Fast</td><td class="column-10">unknown</td><td class="column-11">unknown</td>
</tr>
<tr class="row-168 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=330" target="_parent">Persicaria sp. 'Porto Velho'</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Polygonaceae</td><td class="column-7">Persicaria</td><td class="column-8">Stem width 4 inches</td><td class="column-9">Fast</td><td class="column-10">South America</td><td class="column-11">Brazil</td>
</tr>
<tr class="row-169 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=243" target="_parent">Persicaria sp. 'Sao Paulo'</a></td><td class="column-2">Moderate</td><td class="column-3">Medium High</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Polygonaceae</td><td class="column-7">Persicaria</td><td class="column-8">Stem width 5 inches</td><td class="column-9">Fast</td><td class="column-10">South America</td><td class="column-11">Sao Paulo region, Brazil</td>
</tr>
<tr class="row-170 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=45" target="_parent">Phyllanthus fluitans</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Floating</td><td class="column-6">Phyllanthaceae</td><td class="column-7">Phyllanthus</td><td class="column-8">2cm (1in)</td><td class="column-9">Very fast</td><td class="column-10">Central/South America</td><td class="column-11">Amazon Basin</td>
</tr>
<tr class="row-171 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=272" target="_parent">Pogostemon erectus</a></td><td class="column-2">Moderate</td><td class="column-3">Medium High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Lamiaceae</td><td class="column-7">Pogostemon</td><td class="column-8">Stem width: 5-6cm (2-2.5in)</td><td class="column-9">Moderate</td><td class="column-10">Asia</td><td class="column-11">Southwestern India</td>
</tr>
<tr class="row-172 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=187" target="_parent">Pogostemon helferi</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Foreground</td><td class="column-5">Stem</td><td class="column-6">Lamiaceae</td><td class="column-7">Pogostemon</td><td class="column-8">Stem width: 2-5cm (1-2 in)</td><td class="column-9">Medium</td><td class="column-10">Asia</td><td class="column-11">Thailand</td>
</tr>
<tr class="row-173 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=93" target="_parent">Pogostemon stellatus</a></td><td class="column-2">Difficult</td><td class="column-3">High</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Lamiaceae</td><td class="column-7">Pogostemon</td><td class="column-8">Individual stem width: 6-14cm (2-6in)</td><td class="column-9">Fast</td><td class="column-10">Australasia</td><td class="column-11">Australasia</td>
</tr>
<tr class="row-174 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=80" target="_parent">Pogostemon stellatus 'Broad Leaf'</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Lamiaceae</td><td class="column-7">Pogostemon</td><td class="column-8">Individual stem width: 8-20cm (3-8in)</td><td class="column-9">Medium</td><td class="column-10">Australasia</td><td class="column-11">Papua New Guinea</td>
</tr>
<tr class="row-175 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=246" target="_parent">Pogostemon yatabeanus</a></td><td class="column-2">Moderate</td><td class="column-3">Medium High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Lamiaceae</td><td class="column-7">Pogostemon</td><td class="column-8">Stem width 6 inches</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">Japan, China, South Korea</td>
</tr>
<tr class="row-176 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=305" target="_parent">Potamogeton crispus</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Potamogetonaceae</td><td class="column-7">Potamogeton</td><td class="column-8">stem width 2 inches</td><td class="column-9">Fast</td><td class="column-10">North America</td><td class="column-11">Central US</td>
</tr>
<tr class="row-177 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=230" target="_parent">Potamogeton dentatus</a></td><td class="column-2">Moderate</td><td class="column-3">Medium High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Potamogetonaceae</td><td class="column-7">Potamogeton</td><td class="column-8">4 inch stem width</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">Japan, Korea</td>
</tr>
<tr class="row-178 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=89" target="_parent">Potamogeton gayi</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Potamogetonaceae</td><td class="column-7">Potamogeton</td><td class="column-8">Individual stem width: 10-20cm (4-8in)</td><td class="column-9">Fast</td><td class="column-10">Central/South America</td><td class="column-11">South America</td>
</tr>
<tr class="row-179 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=44" target="_parent">Potamogeton perfoliatus</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Potamogetonaceae</td><td class="column-7">Potamogeton</td><td class="column-8">Individual stem width: 4-5cm (1.5-2in)</td><td class="column-9">Very fast</td><td class="column-10">Cosmopolitan</td><td class="column-11">Cosmopolitan</td>
</tr>
<tr class="row-180 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=197" target="_parent">Proserpinaca palustris from Cuba</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Haloragaceae</td><td class="column-7">Proserpinaca</td><td class="column-8">Stem width: 3-5cm (1-2 in)</td><td class="column-9">Medium</td><td class="column-10">Americas</td><td class="column-11">Americas</td>
</tr>
<tr class="row-181 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=148" target="_parent">Ranunculus inundatus</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Foreground</td><td class="column-5">Rhizome</td><td class="column-6">Ranunculaceae</td><td class="column-7">Ranunculus</td><td class="column-8">Height: 5-15cm (2-6in)</td><td class="column-9">Medium</td><td class="column-10">Australasia</td><td class="column-11">Southeastern Australia</td>
</tr>
<tr class="row-182 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=342" target="_parent">Riccardia chamedryfolia</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Epiphyte</td><td class="column-5">Unknown</td><td class="column-6">Aneuraceae</td><td class="column-7">Riccardia</td><td class="column-8">small</td><td class="column-9">Slow</td><td class="column-10">Cosmopolitan</td><td class="column-11">Cosmopolitan</td>
</tr>
<tr class="row-183 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=99" target="_parent">Riccia fluitans</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Epiphyte</td><td class="column-5">Floating</td><td class="column-6">Ricciaceae</td><td class="column-7">Riccia</td><td class="column-8">Infinite</td><td class="column-9">Fast</td><td class="column-10">Cosmopolitan</td><td class="column-11">Cosmopolitan</td>
</tr>
<tr class="row-184 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=50" target="_parent">Riccia sp. 'Dwarf'</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Epiphyte</td><td class="column-5">Floating</td><td class="column-6">Ricciaceae</td><td class="column-7">Riccia</td><td class="column-8">1cm (0.5</td><td class="column-9">Fast</td><td class="column-10">Tropics</td><td class="column-11">Unknown</td>
</tr>
<tr class="row-185 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=324" target="_parent">Ricciocarpus natans</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Floating</td><td class="column-6">Ricciaceae</td><td class="column-7">Ricciocarpus</td><td class="column-8">1/4 inch</td><td class="column-9">Moderate</td><td class="column-10">Cosmopolitan</td><td class="column-11">Cosmopolitan</td>
</tr>
<tr class="row-186 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=317" target="_parent">Rotala indica</a></td><td class="column-2">Moderate</td><td class="column-3">Medium High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Lythraceae</td><td class="column-7">Rotala</td><td class="column-8">Stem width 1/2 inch</td><td class="column-9">Moderate</td><td class="column-10">Asia</td><td class="column-11">Iran to Japan, common in Southeast Asia, naturalized elsewhere</td>
</tr>
<tr class="row-187 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=68" target="_parent">Rotala macrandra</a></td><td class="column-2">Difficult</td><td class="column-3">High</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Lythraceae</td><td class="column-7">Rotala</td><td class="column-8">Individual stem width: 2-7cm (1-3in)</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">India</td>
</tr>
<tr class="row-188 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=193" target="_parent">Rotala macrandra 'Green Narrow Leaf'</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Lythraceae</td><td class="column-7">Rotala</td><td class="column-8">Stem width: 2-3 cm (1 in)</td><td class="column-9">Fast</td><td class="column-10">Cultivar</td><td class="column-11">Cultivar</td>
</tr>
<tr class="row-189 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=164" target="_parent">Rotala macrandra 'Green'</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Lythraceae</td><td class="column-7">Rotala</td><td class="column-8">Stem width: 1.5--2.5cm (1-2 in)</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">India</td>
</tr>
<tr class="row-190 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=326" target="_parent">Rotala macrandra 'Mini Type 2'</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Lythraceae</td><td class="column-7">Rotala</td><td class="column-8">Stem width 1/2 inch</td><td class="column-9">Moderate</td><td class="column-10">Asia</td><td class="column-11">Cultivar?</td>
</tr>
<tr class="row-191 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=115" target="_parent">Rotala macrandra 'Narrow Leaf'</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Lythraceae</td><td class="column-7">Rotala</td><td class="column-8">Stem width: 4-6cm (1.5-2.5</td><td class="column-9">Fast</td><td class="column-10">Cultivar</td><td class="column-11">Cultivar</td>
</tr>
<tr class="row-192 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=116" target="_parent">Rotala macrandra 'Variegated'</a></td><td class="column-2">Difficult</td><td class="column-3">High</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Lythraceae</td><td class="column-7">Rotala</td><td class="column-8">Individual stem width: 2-7cm (1-3in)</td><td class="column-9">Fast</td><td class="column-10">Cultivar</td><td class="column-11">Cultivar</td>
</tr>
<tr class="row-193 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=203" target="_parent">Rotala mexicana 'Araguaia'</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Lythraceae</td><td class="column-7">Rotala</td><td class="column-8">Stem width: 2-4 cm (1-1.5 in)</td><td class="column-9">Fast</td><td class="column-10">Central/South America, Africa, Asia, Australia</td><td class="column-11">Worldwide in warm areas</td>
</tr>
<tr class="row-194 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=209" target="_parent">Rotala mexicana 'Goias'</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Foreground</td><td class="column-5">Stem</td><td class="column-6">Lythraceae</td><td class="column-7">Rotala</td><td class="column-8">Stem width: 1-3cm (0.5-1 in)</td><td class="column-9">Fast</td><td class="column-10">South America</td><td class="column-11">Goias</td>
</tr>
<tr class="row-195 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=192" target="_parent">Rotala ramosior</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Lythraceae</td><td class="column-7">Rotala</td><td class="column-8">Stem width: 2.5 inches</td><td class="column-9">Medium</td><td class="column-10">Americas</td><td class="column-11">North and South America</td>
</tr>
<tr class="row-196 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=39" target="_parent">Rotala rotundifolia</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Lythraceae</td><td class="column-7">Rotala</td><td class="column-8">Individual stem width: 1.5-2cm (0.75-1in)</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">Southeast Asia</td>
</tr>
<tr class="row-197 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=76" target="_parent">Rotala wallichii</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Lythraceae</td><td class="column-7">Rotala</td><td class="column-8">Individual stem width: 2-5cm (1-2in)</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">Southeast Asia</td>
</tr>
<tr class="row-198 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=224" target="_parent">Rotala sp. 'Colorata'</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Lythraceae</td><td class="column-7">Rotala</td><td class="column-8">1.5 inches stem width</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">Unknown</td>
</tr>
<tr class="row-199 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=103" target="_parent">Rotala sp. 'Green'</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Lythraceae</td><td class="column-7">Rotala</td><td class="column-8">Individual stem width: 3 cm ( 1in)</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">Unknown</td>
</tr>
<tr class="row-200 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=169" target="_parent">Rotala sp. 'Nanjenshan'</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Lythraceae</td><td class="column-7">Rotala</td><td class="column-8">Stem width:<span style="mso-spacerun:yes">Â  </span>2-5cm (1-2<br />
  in)</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">Taiwan</td>
</tr>
<tr class="row-201 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=347" target="_parent">Rotala sp. 'Sunset'</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Lythraceae</td><td class="column-7">Rotala</td><td class="column-8">stem width 2 inches</td><td class="column-9">Moderate</td><td class="column-10">unknown</td><td class="column-11">unknown</td>
</tr>
<tr class="row-202 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=132" target="_parent">Rotala sp. 'Vietnam'</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Red</td><td class="column-5">Stem</td><td class="column-6">Lythraceae</td><td class="column-7">Rotala</td><td class="column-8">Stem width: 4-8cm (1.5-3in)</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">Vietnam</td>
</tr>
<tr class="row-203 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=77" target="_parent">Sagittaria subulata</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Foreground</td><td class="column-5">Rosette</td><td class="column-6">Alismataceae</td><td class="column-7">Sagittaria</td><td class="column-8">Height: 5-15cm (4-6in)</td><td class="column-9">Fast</td><td class="column-10">North America</td><td class="column-11">Eastern United States</td>
</tr>
<tr class="row-204 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=49" target="_parent">Salvinia minima</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Floating</td><td class="column-6">Salviniaceae</td><td class="column-7">Salvinia</td><td class="column-8">1cm (0.5</td><td class="column-9">Very fast</td><td class="column-10">Central/South America</td><td class="column-11">South America</td>
</tr>
<tr class="row-205 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=113" target="_parent">Salvinia natans</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Floating</td><td class="column-6">Salviniaceae</td><td class="column-7">Salvinia</td><td class="column-8">Leaf size: 3cm (1")</td><td class="column-9">Fast</td><td class="column-10">Cosmopolitan</td><td class="column-11">Cosmopolitan</td>
</tr>
<tr class="row-206 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=159" target="_parent">Salvinia oblongifolia</a></td><td class="column-2">Easy</td><td class="column-3">Medium</td><td class="column-4">Not Specific</td><td class="column-5">Floating</td><td class="column-6">Salviniaceae</td><td class="column-7">Salvinia</td><td class="column-8">Leaf size: 2.5-4.5cm (1-2</td><td class="column-9">Fast</td><td class="column-10">Central/South America</td><td class="column-11">Eastern Brazil</td>
</tr>
<tr class="row-207 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=100" target="_parent">Saururus cernuus</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Saururaceae</td><td class="column-7">Saururus</td><td class="column-8">Individual stem width: 5-15cm (2-6</td><td class="column-9">Slow</td><td class="column-10">North America</td><td class="column-11">Southeastern U.S.A.</td>
</tr>
<tr class="row-208 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=220" target="_parent">Saururus chinensis</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Saururaceae</td><td class="column-7">Saururus</td><td class="column-8">Individual stem width: 10-15cm (4-6in)</td><td class="column-9">Moderate</td><td class="column-10">Asia</td><td class="column-11">China</td>
</tr>
<tr class="row-209 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=282" target="_parent">Sphaerocaryum malaccense</a></td><td class="column-2">Moderate</td><td class="column-3">Medium High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Poaceae</td><td class="column-7">Sphaerocaryum</td><td class="column-8">stem width 1-1.5 inches</td><td class="column-9">Moderate</td><td class="column-10">Asia</td><td class="column-11">India to Philippines, south to Vietnam</td>
</tr>
<tr class="row-210 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=307" target="_parent">Staurogyne stolonifera</a></td><td class="column-2">Moderate</td><td class="column-3">Medium High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Acanthaceae</td><td class="column-7">Staurogyne</td><td class="column-8">Stem width 4 inches</td><td class="column-9">Fast</td><td class="column-10">South America</td><td class="column-11">Brazil, Guyana, French Guyana, Suriname</td>
</tr>
<tr class="row-211 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=329" target="_parent">Staurogyne sp. 'Bihar'</a></td><td class="column-2">Moderate</td><td class="column-3">Medium High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Acanthaceae</td><td class="column-7">Staurogyne</td><td class="column-8">Stem with 6 inches</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">India</td>
</tr>
<tr class="row-212 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=302" target="_parent">Staurogyne sp. 'Low Grow'</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Foreground</td><td class="column-5">Stem</td><td class="column-6">Acanthaceae</td><td class="column-7">Staurogyne</td><td class="column-8">stem width 4 inches</td><td class="column-9">Moderate</td><td class="column-10">South America</td><td class="column-11">Brazil</td>
</tr>
<tr class="row-213 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=253" target="_parent">Staurogyne sp. 'Porto Velho'</a></td><td class="column-2">Moderate</td><td class="column-3">Medium High</td><td class="column-4">Foreground</td><td class="column-5">Stem</td><td class="column-6">Acanthaceae</td><td class="column-7">Staurogyne</td><td class="column-8">stem width 2 inches</td><td class="column-9">Moderate</td><td class="column-10">South America</td><td class="column-11">Brazil</td>
</tr>
<tr class="row-214 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=128" target="_parent">Syngonanthus sp. 'Belem'</a></td><td class="column-2">Difficult</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Eriocaulaceae</td><td class="column-7">Syngonanthus</td><td class="column-8">Stem width: 5-6cm (2-2.5in)</td><td class="column-9">Medium</td><td class="column-10">Central/South America</td><td class="column-11">Brazil</td>
</tr>
<tr class="row-215 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=129" target="_parent">Syngonanthus sp. 'Manaus'</a></td><td class="column-2">Difficult</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Eriocaulaceae</td><td class="column-7">Syngonanthus</td><td class="column-8">Stem width: 4-5cm (1.5-2</td><td class="column-9">Medium</td><td class="column-10">Central/South America</td><td class="column-11">Brazil</td>
</tr>
<tr class="row-216 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=212" target="_parent">Taxiphyllum alternans</a></td><td class="column-2">Easy</td><td class="column-3">Low</td><td class="column-4">Epiphyte</td><td class="column-5">Moss / Fern</td><td class="column-6">Hypnaceae</td><td class="column-7">Taxiphyllum</td><td class="column-8">Infinite</td><td class="column-9">Slow</td><td class="column-10">Unknown</td><td class="column-11">Unknown</td>
</tr>
<tr class="row-217 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=101" target="_parent">Taxiphyllum barbieri</a></td><td class="column-2">Very Easy</td><td class="column-3">Low</td><td class="column-4">Epiphyte</td><td class="column-5">Moss / Fern</td><td class="column-6">Hypnaceae</td><td class="column-7">Taxiphyllum</td><td class="column-8">Infinite</td><td class="column-9">Slow</td><td class="column-10">Asia</td><td class="column-11">Southeast Asia</td>
</tr>
<tr class="row-218 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=88" target="_parent">Tonina fluviatilis</a></td><td class="column-2">Difficult</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Eriocaulaceae</td><td class="column-7">Tonina</td><td class="column-8">Individual stem width: 2-3cm (1-1.5in)</td><td class="column-9">Medium</td><td class="column-10">Central/South America, West Indies, Mexico</td><td class="column-11">South America, ranging north into Central America</td>
</tr>
<tr class="row-219 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=268" target="_parent">Utricularia gibba</a></td><td class="column-2">Very Easy</td><td class="column-3">Low to Very High</td><td class="column-4">Not Specific</td><td class="column-5">Unknown</td><td class="column-6">Lentibulariaceae</td><td class="column-7">Utricularia</td><td class="column-8">very small</td><td class="column-9">Fast</td><td class="column-10">Cosmopolitan</td><td class="column-11">Cosmopolitan</td>
</tr>
<tr class="row-220 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=343" target="_parent">Utricularia graminifolia</a></td><td class="column-2">Moderate</td><td class="column-3">Medium</td><td class="column-4">Foreground</td><td class="column-5">Rhizome</td><td class="column-6">Lentibulariaceae</td><td class="column-7">Utricularia</td><td class="column-8">Leaf lenth 1 inch</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">India to China</td>
</tr>
<tr class="row-221 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=198" target="_parent">Vesicularia ferriei</a></td><td class="column-2">Easy</td><td class="column-3">Low</td><td class="column-4">Epiphyte</td><td class="column-5">Moss / Fern</td><td class="column-6">Hypnaceae</td><td class="column-7">Vesicularia</td><td class="column-8">Infinite</td><td class="column-9">Slow</td><td class="column-10">Unknown</td><td class="column-11">Unknown</td>
</tr>
<tr class="row-222 even">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=160" target="_parent">Vesicularia montagnei</a></td><td class="column-2">Easy</td><td class="column-3">Low</td><td class="column-4">Epiphyte</td><td class="column-5">Moss / Fern</td><td class="column-6">Hypnaceae</td><td class="column-7">Vesicularia</td><td class="column-8">Infinite</td><td class="column-9">Slow</td><td class="column-10">Unknown</td><td class="column-11">Unknown</td>
</tr>
<tr class="row-223 odd">
	<td class="column-1"><a href="http://www.aquaticplantcentral.com/forumapc/plantfinder/details.php?id=258" target="_parent">Poaceae sp. 'Purple Bamboo'</a></td><td class="column-2">Moderate</td><td class="column-3">High</td><td class="column-4">Not Specific</td><td class="column-5">Stem</td><td class="column-6">Poaceae</td><td class="column-7">Unknown</td><td class="column-8">stem width 2-3 inches (5-8cm)</td><td class="column-9">Fast</td><td class="column-10">Asia</td><td class="column-11">Unknown</td>
</tr>
</tbody>
</table>
"""

# Parsing del contenuto HTML
soup = BeautifulSoup(html_content, "html.parser")

# Trova la tabella
table = soup.find("table")

# Controlla se la tabella è stata trovata
if table:
    # Inizializzazione della lista per memorizzare i dati
    table_data = []
    # Ciclo per estrarre i dati da ogni riga della tabella
    for row in table.find_all("tr"):
        # Inizializzazione della lista per memorizzare i dati di una riga
        row_data = []

        # Ciclo per estrarre i dati da ogni cella della riga
        for cell in row.find_all("td"):
            # Estrazione del testo
            text = cell.text.strip()

            # Se la cella contiene un link, estrai solo il testo del link
            if cell.find("a"):
                text = cell.find("a").text.strip()

            # Aggiunta del testo alla lista
            row_data.append(text)

        # Aggiunta dei dati della riga alla lista principale
        table_data.append(row_data)

    # Check if table data is not empty (avoid empty DataFrame creation)
    # print(table_data)
    if len(table_data) > 0:
        # Extract column names from the first row (assuming your table has headers)
        columns = table_data[0]
        print(table_data)
        # Create the DataFrame using the extracted data and column names
        plant_data = pd.DataFrame(table_data[1:], columns=columns)  # Skip header row
    else:
        print("No data found in the table.")

    # Stampa del DataFrame (opzionale)
    print(plant_data.to_string())
    print("salvataggio")
    # Salvataggio del DataFrame su file Excel (opzionale)
    plant_data.to_excel("data_piante.xlsx", index=False)


else:
    print("Errore: la tabella non è stata trovata.")
