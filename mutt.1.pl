.\" -*-nroff-*-
.\"
.\"
.\"     Copyright (C) 1996-2000 Michael R. Elkins <me@cs.hmc.edu>
.\"
.\"     This program is free software; you can redistribute it and/or modify
.\"     it under the terms of the GNU General Public License as published by
.\"     the Free Software Foundation; either version 2 of the License, or
.\"     (at your option) any later version.
.\"
.\"     This program is distributed in the hope that it will be useful,
.\"     but WITHOUT ANY WARRANTY; without even the implied warranty of
.\"     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
.\"     GNU General Public License for more details.
.\"
.\"     You should have received a copy of the GNU General Public License
.\"     along with this program; if not, write to the Free Software
.\"     Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111, USA.
.\"
.\"     {PTM/TW/0.1/30-06-1999/"agent pocztowy u¿ytkownika"}
.\"     Translation (c) 1999 Tomasz Wendlandt <juggler@cp.pl>.
.\" transl.updated: PTM/WK/2000-VI
.TH mutt 1 "luty 2000" Unix "podrêcznik u¿ytkownika"
.SH NAZWA
mutt - agent pocztowy u¿ytkownika (MUA)
.SH SK£ADNIA
.TP 6
.B mutt
.RB [ -hnpRvxyzZ ]
.RB [-a
.IR plik ]
.RB [ -b
.IR adres ]
.RB [ -c
.IR adres ]
.br
.RB [ -e
.IR polecenie ]
.RB [-f
.IR skrzynka ]
.RB [ -F
.IR muttrc ]
.RB [ -H
.IR szkic ]
.br
.RB [ -i
.IR za³±cznik ]
.RB [ -m
.IR typ ]
.RB [ -s
.IR temat ]
.SH OPIS
.PP
Mutt jest ma³ym, lecz bardzo silnym programem tekstowym, przeznaczonym do
czytania poczty elektronicznej pod systemem operacyjnym unix, posiada takie
funkcje jak kolorowy terminal, MIME i w±tkowanie.
.SH OPCJE
.TP
.BI -a " plik"
Za³±cza plik do twojej wiadomo¶ci u¿ywaj±c MIME.
.TP
.BI -b " adres"
Okre¶la odbiorcê ¶lepej kopii wiadomo¶ci (BCC).
.TP
.BI -c " adres"
Okre¶la odbiorcê kopii wiadomo¶ci (CC).
.TP
.BI -e " polecenie"
Okre¶la polecenie konfiguracyjne, które ma byæ wykonane po inicjalizacji.
.TP
.BI -f " skrzynka"
Okre¶la, któr± skrzynkê pocztow± wczytaæ.
.TP
.BI -F " muttrc"
Okre¶la plik inicjalizacji, który ma byæ u¿yty zamiast ~/.muttrc
.TP
.BI "-h"
Wy¶wietla pomoc.
.TP
.BI -H " szkic"
Okre¶la plik ze szkicem zawieraj±cy nag³ówek i tre¶æ wiadomo¶ci,
które bêd± u¿yte do wys³ania wiadomo¶ci.
.TP
.BI -i " za³±cznik"
Okre¶la plik do w³±czenia w tre¶æ wiadomo¶ci.
.TP
.BI -m " typ"
Okre¶la domy¶lny typ skrzynki pocztowej.
.TP
.B -n
Sprawia, i¿ Mutt pomija ogólnosystemowy plik konfiguracyjny.
.TP
.B -p
Ponownie otwiera zarzucony list.
.TP
.B -R
Otwiera skrzynkê w trybie tylko do odczytu.
.TP
.BI -s " temat"
Okre¶la temat wiadomo¶ci.
.TP
.B -v
Wy¶wietla wersjê Mutt'a i wkompilowane parametry.
.TP
.B -x
Symuluje tryb tworzenia wiadomo¶ci mailx.
.TP
.BI -y
Uruchamia Mutt'a z list± wszystkich skrzynek pocztowych okre¶lonych
poleceniem \fBmailboxes\fP.
.TP
.B -z
Kiedy jest u¿ywane z \fB-f\fP, powoduje i¿ Mutt nie uruchamia siê je¿eli
w skrzynce nie ma ¿adnych wiadomo¶ci.
.TP
.B -Z
Powoduje, i¿ Mutt otwiera pierwsz± zawieraj±c± now± wiadomo¶æ skrzynkê
spo¶ród okre¶lonych przez polecenie \fBmailboxes\fP.
.SH ¦RODOWISKO
.TP
.B EDITOR
Edytor wywo³ywany podczas komponowania wiadomo¶ci.
.TP
.B HOME
Pe³na ¶cie¿ka do katalogu domowego u¿ytkownika.
.TP
.B MAIL
Pe³na ¶cie¿ka do katalogu buforowania skrzynki u¿ytkownika.
.TP
.B MAILCAPS
¦cie¿ka przeszukiwania dla plików mailcap.
.TP
.B MM_NOASK
Je¿eli ta zmienna jest ustawiona, to mailcap s± zawsze u¿ywane uprzedniego
pytania.
.TP
.B PGPPATH
Katalog, w którym znajduje siê pêk kluczy PGP (keyring) u¿ytkownika.
.TP
.B TMPDIR
Katalog, w którym tworzone s± pliki tymczasowe.
.TP
.B REPLYTO
Standardowy adres, na który maj± byæ odsy³ane odpowiedzi na wys³an± przez
u¿ytkownika pocztê.
.TP
.B VISUAL
Edytor wywo³ywany kiedy we wbudowanym edytorze podane jest polecenie ~v.
.SH PLIKI
.IP "~/.muttrc"
Plik konfiguracyjny u¿ytkownika.
.IP "/etc/Muttrc"
Ogólnosystemowy plik konfiguracyjny.
.IP "/tmp/muttXXXXXX"
Pliki tymczasowe tworzone przez Mutt'a.
.IP "~/.mailcap"
Definicja u¿ytkownika do obs³ugi nietekstowych typów MIME.
.IP "/etc/mailcap"
Definicja systemu do obs³ugi nietekstowych typów MIME.
.IP "~/.mime.types"
Osobiste mapowanie u¿ytkownika pomiêdzy typem MIME i rozszerzeniami pliku.
.IP "/etc/mime.types"
Mapowanie systemowe pomiêdzy typem MIME i rozszerzeniami pliku.
.IP "/usr/local/bin/mutt_dotlock"
Uprzywilejowany program do dotlockingu.
.SH B£ÊDY
Zawieszenie/wznawianie pracy podczas edytowania pliku za pomoc± edytora
zewnêtrznego nie dzia³a pod SunOS 4.x, je¿eli u¿ywasz bibliotek curses
w /usr/5lib. Jednak¿e \fIdzia³a\fP to z bibliotekami S-Lang.
.PP
Zmiana wielko¶ci ekranu podczas korzystania z zewnêtrznego pagera powoduje,
i¿ Mutt fiksuje na niektórych systemach.
.PP
Zawieszenie/wznawianie nie dzia³a pod Ultrix.
.PP
Linia help dla menu nie jest uaktualniana, je¿eli zmienisz powi±zania dla
jednej z pokazanych w niej funkcji podczas pracy z Muttem.
.SH BRAK GWARANCJI
Niniejszy program rozpowszechniany jest z nadziej±, i¿ bêdzie on u¿yteczny
\-\- jednak BEZ JAKIEJKOLWIEK GWARANCJI, nawet domy¶lnej gwarancji
PRZYDATNO¦CI HANDLOWEJ albo PRZYDATNO¦CI DO OKRE¦LONYCH ZASTOSOWAÑ.
W celu uzyskania bli¿szych informacji - Powszechna Licencja Publiczna GNU.
.SH ZOBACZ TAK¯E
.BR muttrc (5),
.BR curses (3),
.BR mutt_dotlock (1),
.BR ncurses (3),
.BR sendmail (1),
.BR smail (1),
.BR mailcap (5)
.PP
Strona domowa Mutt'a: http://www.mutt.org/
.PP
Powszechna Licencja Publiczna GNU (The GNU General Public License).
.SH AUTOR
Michael Elkins i inni. Skorzystaj z <mutt-dev@mutt.org> by skontaktowaæ
siê z twórcami.
