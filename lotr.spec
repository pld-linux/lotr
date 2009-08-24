#
# NOTE: This is only game engine! If you want to play lotr you need to obtain
the Original Interplays Lord of the Rings game data.
#
Summary:	Linux engine for Interplays Lord of the Rings
Summary(pl.UTF-8):	Linukoswy silnik dla gry Władca Pierścieni stworzonej przez Interplays
Name:		lotr
Version:	0.6.4
Release:	1
License:	LGPL v2.1+
Group:		Applications/Games
Source0:	http://download.wonderland.cz/%{name}-%{version}.tgz
# Source0-md5:	642dcb09bc92dbcb3272850e2210645b
Patch0:		%{name}-ldflags.patch
URL:		http://www.wonderland.cz/lotr/
BuildRequires:	SDL_mixer-devel
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Lord of the Rings game engine which plays famous Interplays game
The Lord of the Rings, by many regarded as the best Middle-Earth game
ever. It is an old-fashioned RPG game which keeps close to the plot of
Fellowship of the Ring but have many good side-quests.

%description -l pl.UTF-8
Silnik Władcy Pierścieni, który pozwala grać w znaną grę Władca
Pierści stworzoną przez Interplays, uznaną przez wielu za
najlepszą grę o Śródziemiu. Jest to gra RPG w starym stylu, która
trzyma się blisko fabuły Drużyny Pierścienia, posiada jednak wiele
pobocznych zadań.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	PREFIX="%{_prefix}" \
	CC="%{__cc}" \
	LD="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/lotr}

install lotr $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{*.txt,README,TODO}
%attr(755,root,root) %{_bindir}/lotr
%dir %{_datadir}/games/lotr
