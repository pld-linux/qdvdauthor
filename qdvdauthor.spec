
Summary:	QDVDAuthor, the GUI frontend for dvdauthor and other related tools
Summary(pl.UTF-8):	QDVDAuthor - graficzny interfejs do programu dvdauthor i powiązanych narzędzi
Name:		qdvdauthor
Version:	1.5.0
Release:	2
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/qdvdauthor/%{name}-%{version}-2.tar.gz
# Source0-md5:	1d1f29825fe0ae49faac8a0269c5c550
URL:		http://qdvdauthor.sourceforge.net/
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRequires:	qt-linguist
BuildRequires:	sed >= 4.0
BuildRequires:	xine-lib-devel >= 1:1.0.0
Requires:	dvd-slideshow >= 0.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QDVDAuthor is a GUI frontend for using dvdauthor and dvd-slideshow
scripts to easily build DVD menus and assemble the DVD VOB files.

%description -l pl.UTF-8
QDVDAuthor to graficzny interfejs użytkownika do używania skryptów
dvdauthor i dvd-slideshow do łatwego tworzenia menu DVD i składania
plików DVD VOB.

%prep
%setup -q

%build
%{__sed} -i 's,Categories.*,Categories=Qt;AudioVideo;AudioVideoEditing;,' qdvdauthor.desktop
%{__sed} -i 's,x23,043,g' qdvdauthor/{qdvdauthor.pro,qplayer/qplayer.pro}

./configure \
	--build-qplayer \
	--build-qslideshow \
	--with-mplayer-support \
	--with-xine-support \
	--qt-dir=%{_prefix} \
	--with-qt-lib=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/qdvdauthor,%{_desktopdir},%{_pixmapsdir}}

install bin/qdvdauthor $RPM_BUILD_ROOT%{_bindir}
install bin/qplayer $RPM_BUILD_ROOT%{_bindir}
install bin/qslideshow $RPM_BUILD_ROOT%{_bindir}
install qdvdauthor/i18n/*.qm $RPM_BUILD_ROOT%{_datadir}/qdvdauthor
install qdvdauthor.desktop $RPM_BUILD_ROOT%{_desktopdir}
install qdvdauthor.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/qdvdauthor
%lang(ca) %{_datadir}/%{name}/qdvdauthor_ca.qm
%lang(de) %{_datadir}/%{name}/qdvdauthor_de.qm
%lang(eo) %{_datadir}/%{name}/qdvdauthor_eo.qm
%lang(es) %{_datadir}/%{name}/qdvdauthor_es.qm
%lang(fr) %{_datadir}/%{name}/qdvdauthor_fr.qm
%lang(it) %{_datadir}/%{name}/qdvdauthor_it.qm
%lang(pl) %{_datadir}/%{name}/qdvdauthor_pl.qm
%lang(ca) %{_datadir}/%{name}/qplayer_ca.qm
%lang(de) %{_datadir}/%{name}/qplayer_de.qm
%lang(es) %{_datadir}/%{name}/qplayer_es.qm
%lang(fr) %{_datadir}/%{name}/qplayer_fr.qm
%lang(ca) %{_datadir}/%{name}/qslideshow_ca.qm
%lang(de) %{_datadir}/%{name}/qslideshow_de.qm
%lang(es) %{_datadir}/%{name}/qslideshow_es.qm
%lang(fr) %{_datadir}/%{name}/qslideshow_fr.qm
%lang(it) %{_datadir}/%{name}/qslideshow_it.qm
%lang(ca) %{_datadir}/%{name}/qrender_ca.qm
%lang(de) %{_datadir}/%{name}/qrender_de.qm
%lang(es) %{_datadir}/%{name}/qrender_es.qm
%{_desktopdir}/qdvdauthor.desktop
%{_pixmapsdir}/qdvdauthor.png
