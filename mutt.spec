Summary:     The Mutt Mail User Agent
Summary(de): Der Mutt Mail-User-Agent 
Summary(fr): Agent courrier Mutt
Summary(pl): Program pocztowy Mutt
Summary(tr): Mutt elektronik posta programý
Name:        mutt
Version:     0.95
Release:     1i
Copyright:   GPL
Group:       Applications/Mail
Source:      ftp://riemann.iam.uni-bonn.de/pub/mutt/%{name}-%{version}i.tar.gz
Source1:     mutt.wmconfig
Source2:     Muttrc
Patch0:      http://www.rhein.de/~roland/mutt/patch-0.95.rr.compressed.1.gz
URL:         http://www.mutt.org/
Requires:    smtpdaemon, mailcap, pgp, slang >= 1.2.2-2
Buildroot:   /tmp/%{name}-%{version}-root

%description
Mutt is a small but very poweful full-screen Unix mail client.
Features include MIME support, color, POP3 support, message threading,
bindable keys, and threaded sorting mode.

%description -l de
Mutt ist ein kleiner aber leistungsfähiger Vollbild-Mail-Client für Unix mit
MIME-Unterstützung, Farbe, POP3-Unterstützung, Nachrichten-Threading,
zuweisbaren Tasten und Sortieren nach Threads.

%description -l fr
mutt est un client courrier Unix plein écran, petit mais très puissant.
Il dispose de la gestion MIME, des couleurs, de la gestion POP, des fils
de discussion, des touches liées et d'un mode de tri sur les fils.
                                                                                                              
%description -l it
Mutt è un piccolo ma potente programma per la gestione della posta in gardo
di gestire il formato MIME. E' altamente configurabile ed è ben equipaggiato
per l'utente avanzato con opzioni quali come associazioni dei tasti, macro,
gestione dei threads, ricerche ed un potente linguaggio per la selezione di
gruppi di messaggi.

%description -l pl
Mutt jest niewielkim programem pocztowym dla terminali tekstowych
posiadaj±cym du¿e mo¿liwo¶ci.  Obs³uguje MIME, POP3, cztery formaty skrzynek
pocztowych, obs³uguje kolory, w±tki i ocenê wa¿no¶ci listów (scoring). W tej
wersji dodano tak¿e obs³ugê skompresowanych folderów.

%description -l tr
Mutt, küçük ama çok güçlü bir tam-ekran Unix mektup istemcisidir. MIME desteði,
renk ve POP3 desteði içerir.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS -I/usr/include/slang" \
./configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--with-sharedir=/usr/share \
	--with-slang \
	--with-docdir=/usr/doc/%{name}-%{version} \
	--enable-pop \
	--without-domain \
	--disable-warnings \
        --enable-compressed
make mutt_LDFLAGS="-s"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig

make install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/mutt
install %{SOURCE2} $RPM_BUILD_ROOT/etc/Muttrc

gzip -9nf $RPM_BUILD_ROOT/usr/man/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc NEWS TODO contrib/*rc doc/manual.txt
%config /etc/Muttrc
/etc/X11/wmconfig/mutt
/usr/share/charsets
%attr(2755, root, mail) /usr/bin/mutt
%attr(0755, root,  man) /usr/man/man1/mutt.1.gz
%lang(de) /usr/share/locale/de/LC_MESSAGES/mutt.mo
%lang(es) /usr/share/locale/es/LC_MESSAGES/mutt.mo
%lang(fr) /usr/share/locale/fr/LC_MESSAGES/mutt.mo
%lang(it) /usr/share/locale/it/LC_MESSAGES/mutt.mo
%lang(ru) /usr/share/locale/ru/LC_MESSAGES/mutt.mo
%lang(uk) /usr/share/locale/uk/LC_MESSAGES/mutt.mo

%changelog
* Sat Dec 12 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.95i-1]
- added gzipping man pages,
- added /usr/share/locale/*/LC_MESSAGES/mutt.mo to %files,
- updated patch for compressed folders,
- fixed sysconfdir (added --sysconfdir=/etc for ./configure parameters),
- --with-sharedir changed to /usr/share,
- added using DESTDIR on "make install",
- revisited list %doc files,
- added "Requires: slang >= 1.2.2-2",
- added /usr/share/charsets to %files,
- fixed passing "-s" ld flag,
- Italian description (Fabio Coatti <cova@felix.unife.it>).

* Sat Sep 19 1998 Marcin Korzonek <mkorz@shadow.eu.org>
  [0.93.2i-1]
- added pl translation,
- added patch for compressed folders,
- rewrites system Muttrc based on ones from Roland Rosenfeld.

* Sun Sep  6 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.93.2i-1]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added using %{SOURCE#} macro in %install,
- changed base Source Url to ftp://riemann.iam.uni-bonn.de/pub/mutt/.

* Wed Jul 29 1998 Bill Nottingham <notting@redhat.com>
- fix setgid removal
- spec file comsetics

* Tue Jul 28 1998 Jeff Johnson <jbj@redhat.com>
- security fix
- turn off setgid mail.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 21 1998 Cristian Gafton <gafton@redhat.com>
- updated to 0.91.1

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- updated to mutt-0.89.1

* Thu Oct 16 1997 Otto Hammersmith <otto@redhat.com>
- Updated to mutt 0.85.
- added wmconfig entries.
- removed mime.types

* Mon Sep 1 1997 Donnie Barnes <djb@redhat.com>
- Rebuilt to insure all sources were fresh and patches were clean.

* Wed Aug 6 1997 Manoj Kasichainula <manojk@io.com>
 - Initial version for 0.81(e)
