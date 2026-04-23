# [Bronze II] Adria - 26362 

[문제 링크](https://www.acmicpc.net/problem/26362) 

### 성능 요약

메모리: 32412 KB, 시간: 120 ms

### 분류

구현, 브루트포스 알고리즘

### 제출 일자

2026년 4월 23일 19:19:52

### 문제 설명

<p>Josip i Nikola su online igrali tenis. Njihov tenis je igra u kojoj igrači osvajaju gemove, a onaj koji prvi osvoji G gemova osvojio je set. Nikola i Josip su do sada odigrali N online setova.</p>

<p>Sada analiziraju odigrane setove te ih zanima odgovor na sljedeća dva pitanja:</p>

<ol>
	<li>Koliko je gemova u prvom odigranom setu osvojio Nikola?</li>
	<li>Koliko je, od N odigranih setova, osvojio Josip?</li>
</ol>

<p>Sada su odlučili zaigrati tenis i u stvarnosti. Kako Nikola nema kondicije, odlučio je u stvarnosti broj G iz online svijeta zamijeniti novim brojem G1 koji je strogo manji od G. Prvo je analizirao koliko bi osvojio setova u online igri da se i tamo osvajao set za G1 osvojenih gemova te onda odabrao onaj G1 za koji bi osvojio najviše setova. U slučaju da novi G1 nije jedinstven, Nikola će odabrati najmanji mogući. Gemovi koji bi se u online igri u setu odigrali nakon što bi Nikola osvojio G1 gemova se zanemaruju i prelazi se na novi set.</p>

<ol start="3">
	<li>Koji je novi broj G1 odabrao Nikola?</li>
</ol>

<p>Napiši program koji će za zadane ulazne podatke ispisati odgovore na zadana pitanja.</p>

### 입력 

 <p>U prvom je retku prirodan broj G (1 ≤ G ≤ 20), broj iz teksta zadatka.</p>

<p>U drugom je retku prirodan broj N (1 ≤ N ≤ 100), broj iz teksta zadatka.</p>

<p>Slijedi opis N odigranih setova oblika:</p>

<ul>
	<li>u prvom je retku prirodan broj X, broj odigranih gemova u i-tom setu</li>
	<li>u sljedećih X redaka nalazi se ili prirodan broj jedan koji označava da je Nikola osvojio i-ti odigrani gem ili broj dva koji označava da je Josip osvojio taj gem.</li>
</ul>

### 출력 

 <p>U prvi redak ispiši cijeli broj, odgovor na prvo pitanje iz zadatka.</p>

<p>U drugi redak ispiši cijeli broj, odgovor na drugo pitanje iz zadatka.</p>

<p>U treći redak ispiši prirodan broj, odgovor na treće pitanje iz zadatka.</p>

