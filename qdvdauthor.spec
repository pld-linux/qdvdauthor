Summary:	QDVDAuthor, the GUI frontend for dvdauthor and other related tools
Name:		qdvdauthor
Version:	0.0.9
Release:	0.1
License:	GPL v2
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/qdvdauthor/%{name}-%{version}.tar.gz
# Source0-md5:	465d888ef6f29162fe9b36ff8c49791c
URL:		http://qdvdauthor.sourceforge.net/
BuildRequires:	qt-devel
BuildRequires:	sed >= 4.0
BuildRequires:	xine-lib-devel >= 1:1.0.0
Requires:	dvdauthor >= 0.6.10
Requires:	mjpegtools >= 1.6.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QDVDAuthor is a gui frontend for using dvdauthor and dvd-slideshow 
scripts to easily build DVD menus and assemble the DVD VOB files. 

%prep
%setup -q

%build
%{__sed} -i 's,Categories.*,Categories=Qt;AudioVideo;AudioVideoEditing;,' qdvdauthor.desktop

export QTDIR=%{_prefix}
./configure \
	--build-qplayer \
	--build-qslideshow \
	--with-xine-support \
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
%lang(de) %{_datadir}/%{name}/qdvdauthor_de.qm
%lang(es) %{_datadir}/%{name}/qdvdauthor_es.qm
%lang(pl) %{_datadir}/%{name}/qdvdauthor_pl.qm
%lang(de) %{_datadir}/%{name}/qplayer_de.qm
%lang(es) %{_datadir}/%{name}/qplayer_es.qm
%lang(de) %{_datadir}/%{name}/qslideshow_de.qm
%lang(es) %{_datadir}/%{name}/qslideshow_es.qm
%{_desktopdir}/qdvdauthor.desktop
%{_pixmapsdir}/qdvdauthor.png
