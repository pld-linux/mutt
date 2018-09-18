#
# TODO:
# - gss/heimdal
# - finish -folder_columns.patch
#
# Conditional build:
%bcond_with	slang		# use slang library instead of ncurses
%bcond_with	nntp		# use VVV's NNTP patch
%bcond_with	folder_column	# build with folder_column patch
%bcond_with	imap_recent	# show IMAP RECENT messages as new (instead of UNSEEN)
%bcond_without	sasl		# don't use sasl
%bcond_without	home_etc	# don't use home_etc
%bcond_with	gdbm		# use GDBM instead of BerkeleyDB
%bcond_with	qdbm		# use QDBM instead of BerkeleyDB
%bcond_with	tokyocabinet	# use TokyoCabinet instead of BerkeleyDB
#
%if %{without gdbm} && %{without qdbm} && %{without tokyocabinet}
%define	with_bdb	1
%endif
Summary:	The Mutt Mail User Agent
Summary(de.UTF-8):	Der Mutt Mail-User-Agent
Summary(es.UTF-8):	Mutt, cliente de correo electrónico
Summary(fr.UTF-8):	Agent courrier Mutt
Summary(ko.UTF-8):	텍스트 기반의 MUA
Summary(pl.UTF-8):	Program pocztowy Mutt
Summary(pt_BR.UTF-8):	Mutt, cliente de correio eletrônico
Summary(ru.UTF-8):	Почтовая клиентская программа Mutt
Summary(tr.UTF-8):	Mutt elektronik posta programı
Summary(uk.UTF-8):	Поштова клієнтська програма Mutt
Name:		mutt
Version:	1.6.2
Release:	3
Epoch:		6
License:	GPL v2+
Group:		Applications/Mail
# temporarily dead? (Jun 2014)
Source0:	ftp://ftp.mutt.org/pub/mutt/%{name}-%{version}.tar.gz
# Source0-md5:	9f0f9cc35878987d7cdc7df6a1967376
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	%{name}.1.pl
Patch0:		%{name}-pl.po-update.patch
# http://mutt.org.ua/download/
Patch2:		%{name}-rr.compressed.patch
Patch3:		%{name}-bj.status-time.patch
# http://mutt.org.ua/download/
Patch4:		%{name}-vvv.quote.patch
Patch5:		%{name}-null_name.patch
Patch6:		%{name}-cd.trash_folder.patch
Patch7:		%{name}-cd.purge_message.patch
Patch8:		%{name}-cd.signatures_menu.patch
# http://www.mutt.ca/patches/ (dw.crypt-autoselectkey)
Patch9:		%{name}-crypt-autoselectkey.patch
Patch10:	%{name}-manual.patch
Patch11:	%{name}-xface.patch
Patch12:	%{name}-Muttrc_mbox_path.patch
Patch13:	%{name}-po.patch
Patch14:	%{name}-home_etc.patch
Patch15:	%{name}-Muttrc.patch
Patch16:	%{name}-muttbug-tmp.patch
Patch17:	%{name}-folder_columns.patch
Patch18:	%{name}-imap_recent.patch
Patch19:	%{name}-Muttrc.head.patch
Patch20:	%{name}-smime.rc.patch
Patch21:	%{name}-sidebar.patch
Patch22:	%{name}-imap_fast_trash.patch
Patch23:	%{name}-db.patch
# http://mutt.org.ua/download/
Patch24:	%{name}-vvv.nntp.patch
Patch25:	format-security.patch
Patch26:	%{name}-keep_to.patch
Patch27:	mutt-gpgme.patch
Patch28:	openssl.patch
URL:		http://www.mutt.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1.6
%{?with_sasl:BuildRequires:	cyrus-sasl-devel >= 2.1.0}
%{?with_bdb:BuildRequires:	db-devel >= 4.0}
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
%{?with_gdbm:BuildRequires:	gdbm-devel}
BuildRequires:	gettext-tools
BuildRequires:	gpgme-devel >= 1:1.1.1
%{?with_home_etc:BuildRequires:	home-etc-devel >= 1.0.8}
BuildRequires:	libidn-devel
BuildRequires:	libxslt-progs
BuildRequires:	lynx
%{!?with_slang:BuildRequires:	ncurses-devel >= 5.0}
BuildRequires:	openssl-devel >= 0.9.7d
%{?with_qdbm:BuildRequires:	qdbm-devel}
%{?with_slang:BuildRequires:	slang-devel}
%{?with_tokyocabinet:BuildRequires:	tokyocabinet-devel}
%{?with_home_etc:Requires:	home-etc-lib >= 1.0.8}
Requires:	iconv
Suggests:	mailcap
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_ia32	-fomit-frame-pointer

%description
Mutt is a small but very poweful full-screen Unix mail client.
Features include MIME support, color, POP3 support, message threading,
bindable keys, and threaded sorting mode.

%description -l de.UTF-8
Mutt ist ein kleiner aber leistungsfähiger Vollbild-Mail-Client für
Unix mit MIME-Unterstützung, Farbe, POP3-Unterstützung,
Nachrichten-Threading, zuweisbaren Tasten und Sortieren nach Threads.

%description -l es.UTF-8
Mutt es un pequeño, pero muy potente cliente de correo en pantalla
llena. Incluye soporte a tipos MINE, color, POP3; encadenamiento de
mensajes, teclas configurables y clasificaciones por encadenamiento.

%description -l fr.UTF-8
mutt est un client courrier Unix plein écran, petit mais très
puissant. Il dispose de la gestion MIME, des couleurs, de la gestion
POP, des fils de discussion, des touches liées et d'un mode de tri sur
les fils.

%description -l ko.UTF-8
Mutt는 작지만 매우 강력한 텍스트 기반의 메일 클라이언트이다. Mutt는 많은 설정이 가능하다. 그리고, 키바인딩, 키보드
메크로, 메일 스레딩과 같은 진보된 형태와 정규표현식 검색, 메일에서 선택된 그룹의 내용에서 강력하게 일정한 패턴을 찾아내는
것을 지원함으로써 메일의 파워 유저에게 가장 적합하다.

%description -l pl.UTF-8
Mutt jest niewielkim programem pocztowym dla terminali tekstowych,
posiadającym duże możliwości. Obsługuje MIME, POP3, cztery formaty
skrzynek pocztowych, kolory, wątki, ocenę ważności listów (scoring)
oraz skompresowane foldery.

%description -l pt_BR.UTF-8
O Mutt é um pequeno mas muito poderoso cliente de correio em tela
cheia. Inclui suporte a tipos MIME, cor, POP3, encadeamento de
mensagens, teclas configuráveis e classificação por encadeamento.

%description -l ru.UTF-8
Mutt - это небольшой, но мощный полноэкранный почтовый клиент.
Включает поддержку MIME, цвет, поддержку POP3 и IMAP, группировку
сообщений по цепочкам, переопределяемые клавиши, поддержку pgp/gpg и
сортировку сообщений в цепочках. Включает также (пока что
экспериментальную) поддержку NNTP.

%description -l tr.UTF-8
Mutt, küçük ama çok güçlü bir tam-ekran Unix mektup istemcisidir. MIME
desteği, renk ve POP3 desteği içerir.

%description -l uk.UTF-8
Mutt - це невеликий, але потужний повноекранний поштовий клієнт.
Містить підтримку MIME, колір, підтримку POP3 та IMAP, групування
повідомлень по ланцюжкам, перевизначення клавіш, підтримку pgp/gpg та
сортування повідомлень у ланцюжках. Містить також (поки що
експериментальну) підтримку NNTP.

%prep
%setup -q
%patch0 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%{?with_home_etc:%patch14 -p1}
%patch15 -p1
%patch16 -p1
# breaks display if arrow_cursor is set
%{?with_folder_column:%patch17 -p1}
%{?with_imap_recent:%patch18 -p1}
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%{?with_nntp:%patch24 -p1}
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1

# force regeneration (manual.sgml is modified by some patches)
%{__rm} doc/{manual*.html,manual.txt}

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	mutt_cv_groupwrite=yes \
	mutt_cv_worldwrite=no \
	%{!?debug:--disable-debug} %{?debug:--enable-debug} \
	--disable-warnings \
	--enable-compressed \
	--enable-external-dotlock \
	--enable-gpgme \
	--enable-hcache \
	--enable-imap \
	--enable-mailtool \
	%{?with_nntp:--enable-nntp} \
	--enable-pop \
	--enable-smtp \
	%{?with_bdb:--with-bdb=/usr} \
	%{!?with_slang:--with-curses} \
	--with-docdir=%{_docdir}/%{name} \
	%{?with_gdbm:--with-gdbm} \
	%{?with_home_etc:--with-home-etc} \
	--with-mailpath=/var/mail \
	--with-mixmaster \
	%{?with_qdbm:--with-qdbm} \
	--with-regex \
	%{?with_sasl:--with-sasl} \
	%{?with_slang:--with-slang} \
	--with-ssl \
	%{?with_tokyocabinet:--with-tokyocabinet}

%{__make} -j1 -C doc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_mandir}/pl/man1} \
	$RPM_BUILD_ROOT%{_sysconfdir}/Muttrc.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	DOTLOCK_GROUP=

%{__patch} -p2 -d $RPM_BUILD_ROOT%{_sysconfdir} < %{PATCH15}

install contrib/gpg.rc $RPM_BUILD_ROOT%{_sysconfdir}/Muttrc.d
install contrib/smime.rc $RPM_BUILD_ROOT%{_sysconfdir}/Muttrc.d
install contrib/colors.linux $RPM_BUILD_ROOT%{_sysconfdir}/Muttrc.d/colors.rc

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/pl/man1

cat <<'EOF' >$RPM_BUILD_ROOT%{_bindir}/mutt_source-muttrc.d
#!/bin/sh -e
for rc in %{_sysconfdir}/Muttrc.d/*.rc; do
	[ ! -r "$rc" ] || echo "source \"$rc\""
done
EOF

# keep manual.txt.gz, the rest is installed as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}/[!m]*

# conflict with qmail
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man5/mbox.5*
# belongs to mailcap
%{__rm} $RPM_BUILD_ROOT%{_sysconfdir}/mime.types

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc contrib/{*rc*,*cap*} ChangeLog README TODO NEWS README.SECURITY README.SSL README.xface
%dir %{_sysconfdir}/Muttrc.d
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/Muttrc
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/Muttrc.d/*.rc
%attr(755,root,root) %{_bindir}/mutt
%attr(755,root,root) %{_bindir}/mutt_source-muttrc.d
%attr(755,root,root) %{_bindir}/flea
%attr(755,root,root) %{_bindir}/muttbug
%attr(755,root,root) %{_bindir}/pgp*
%attr(755,root,root) %{_bindir}/smime_keys
%attr(2755,root,mail) %{_bindir}/mutt_dotlock

%{_docdir}/%{name}
%{_desktopdir}/mutt.desktop
%{_pixmapsdir}/mutt.png
%{_mandir}/man1/flea.1*
%{_mandir}/man1/mutt*.1*
%{_mandir}/man1/pgp*.1*
%{_mandir}/man1/smime_keys.1*
%{_mandir}/man5/mmdf.5*
%{_mandir}/man5/muttrc.5*
%lang(pl) %{_mandir}/pl/man1/*
