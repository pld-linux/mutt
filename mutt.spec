Summary:	The Mutt Mail User Agent
Summary(de):	Der Mutt Mail-User-Agent 
Summary(fr):	Agent courrier Mutt
Summary(pl):	Program pocztowy Mutt
Summary(tr):	Mutt elektronik posta programý
Name:		mutt
Version:	1.0
Release:	2i
Copyright:	GPL
Group:		Applications/Mail
Group(pl):	Aplikacje/Poczta
Source0:	ftp://riemann.iam.uni-bonn.de/pub/mutt/%{name}-%{version}i.tar.gz
Source1:	mutt.desktop
Source2:	Muttrc
Patch0:		mutt-mail.patch
Patch1:		ftp://dione.ids.pl/people/siewca/patches/mutt-confdir.patch
URL:		http://www.mutt.org/
Requires:	smtpdaemon
Requires:	mailcap
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir		/etc

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

%description -l pl
Mutt jest niewielkim programem pocztowym dla terminali tekstowych
posiadaj±cym du¿e mo¿liwo¶ci. Obs³uguje MIME, POP3, cztery formaty
skrzynek pocztowych, kolory, w±tki, ocenê wa¿no¶ci listów (scoring)
oraz skompresowane foldery.

%description -l tr
Mutt, küçük ama çok güçlü bir tam-ekran Unix mektup istemcisidir. MIME desteði,
renk ve POP3 desteði içerir.

%prep
%setup -q
%patch0 -p0
%patch1 -p1 

%build
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
LDFLAGS="-s"
export CFLAGS LDFLAGS
%configure \
	--with-sharedir=%{_datadir} \
	--enable-pop \
	--enable-imap \
	--with-curses \
	--disable-warnings \
	--disable-domain \
        --enable-compressed \
	--with-docdir=%{_defaultdocdir}/%{name}-%{version}

make 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/share/applnk/Networking/Mail

make install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/usr/X11R6/share/applnk/Networking/Mail
install %{SOURCE2} $RPM_BUILD_ROOT/etc/Muttrc

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	contrib/{*rc,*cap} \
	ChangeLog README TODO NEWS README.SECURITY

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {ChangeLog,README,TODO,NEWS,README.SECURITY}.gz

%config(noreplace) %verify(not size md5 mtime) /etc/Muttrc
/usr/X11R6/share/applnk/Networking/Mail/mutt.desktop

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
