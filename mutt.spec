Summary:	The Mutt Mail User Agent
Summary(de):	Der Mutt Mail-User-Agent
Summary(fr):	Agent courrier Mutt
Summary(pl):	Program pocztowy Mutt
Summary(tr):	Mutt elektronik posta programý
Name:		mutt
Version:	1.3.18i
Release:	4
Epoch:		4
License:	GPL
Group:		Applications/Mail
Group(de):	Applikationen/Post
Group(pl):	Aplikacje/Poczta
Group(pt):	Aplicações/Correio Eletrônico
Source0:	ftp://ftp.mutt.org/pub/mutt/devel/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-forcedotlock.patch
Patch1:		%{name}-in_reply_to.patch
Patch2:		%{name}-home_etc.patch
Patch3:		%{name}-muttbug-tmp.patch
URL:		http://www.mutt.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	openssl-devel >= 0.9.6a
%{!?_without_sasl:BuildRequires:	cyrus-sasl-devel}
Requires:	iconv
Requires:	mailcap
Requires:	smtpdaemon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Mutt is a small but very poweful full-screen Unix mail client.
Features include MIME support, color, POP3 support, message threading,
bindable keys, and threaded sorting mode.

%description -l de
Mutt ist ein kleiner aber leistungsfähiger Vollbild-Mail-Client für
Unix mit MIME-Unterstützung, Farbe, POP3-Unterstützung,
Nachrichten-Threading, zuweisbaren Tasten und Sortieren nach Threads.

%description -l fr
mutt est un client courrier Unix plein écran, petit mais très
puissant. Il dispose de la gestion MIME, des couleurs, de la gestion
POP, des fils de discussion, des touches liées et d'un mode de tri sur
les fils.

%description -l pl
Mutt jest niewielkim programem pocztowym dla terminali tekstowych
posiadaj±cym du¿e mo¿liwo¶ci. Obs³uguje MIME, POP3, cztery formaty
skrzynek pocztowych, kolory, w±tki, ocenê wa¿no¶ci listów (scoring)
oraz skompresowane foldery.

%description -l tr
Mutt, küçük ama çok güçlü bir tam-ekran Unix mektup istemcisidir. MIME
desteði, renk ve POP3 desteði içerir.

%prep
%setup -q -n %{name}-%(echo %{version} | sed 's/i$//')
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
aclocal -I m4
autoheader
autoconf
automake -a -c
%configure \
	--with-curses \
	--with-regex \
	--with-homespool=Maildir \
	--with-mailpath=/var/mail \
	--enable-external-dotlock \
	--with-sharedir=%{_datadir} \
	--with-iconv \
	--with-docdir=%{_defaultdocdir}/%{name}-%{version} \
	--enable-pop \
	--enable-imap \
	--with-ssl \
	%{!?_without_sasl:--with-sasl} %{?_without_sasl:--without-sasl} \
	%{!?debug:--disable-debug} %{?debug:--enable-debug} \
	--disable-warnings \
	--enable-mailtool \
	--without-included-nls

%{__make} keymap.h
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/Mail,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Mail
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf contrib/{*rc*,*cap*} \
	ChangeLog README TODO NEWS README.SECURITY README.SSL README.UPGRADE

# conflict with qmail
rm -f $RPM_BUILD_ROOT%{_mandir}/man5/mbox.5*

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz contrib/{*rc*,*cap*} doc/manual*html doc/manual.txt
%config(noreplace,missingok) %verify(not md5 size mtime) %{_sysconfdir}/Muttrc
%attr(755,root,root) %{_bindir}/mutt
%attr(755,root,root) %{_bindir}/flea
%attr(755,root,root) %{_bindir}/muttbug
%attr(755,root,root) %{_bindir}/pgp*
%attr(2755,root,mail) %{_bindir}/mutt_dotlock

%{_applnkdir}/Network/Mail/mutt.desktop
%{_pixmapsdir}/mutt.png
%{_mandir}/man*/*
