Name:		maxr
Version:	0.2.8
Release:	1
Summary:	A classic turn-based strategy game
Group:		Games/Other
License:	GPLv2+ and GFDL
URL:		http://www.maxr.org
Source0:	http://www.maxr.org/downloads/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	desktop-file-utils

%description
M.A.X.R. (Mechanized Assault and eXploration Reloaded) is a fanmade strategy 
game by the community of maxr.org. MAXR is OpenSource and a remake of
the old M.A.X.by Interplay from 1996 featuring network games based on TCP/IP 
(e.g. over the internet). The game can be played in a turn-based mode (with or 
without time limit), or simultaneous mode (all the players take their turns at 
the same time), and features combat in air, land, and sea. Three resources are 
present on the maps - Raw Materials, which are needed to manufacture units, 
structures and ammunition, Fuel, which power generators need to function, and 
Gold, which is used to purchase upgrades. This game is a mix of realtime and 
turnbased strategy with battle chess character.

%prep
%setup -q
# Needed because of this rpmlint warning "W: wrong-file-end-of-line-encoding"
sed -i 's/\r//' CHANGELOG
# Convert everything to UTF-8
# COPYING.README
iconv -f iso-8859-1 -t utf-8 -o COPYING.README.utf8 COPYING.README
touch -c -r COPYING.README COPYING.README.utf8
mv -f COPYING.README.utf8 COPYING.README
# ABOUT
iconv -f iso-8859-1 -t utf-8 -o ABOUT.utf8 ABOUT
touch -c -r ABOUT ABOUT.utf8
mv -f ABOUT.utf8 ABOUT

%build
%configure2_5x
%make

%install
%makeinstall_std

desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications \
	%{SOURCE1}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps

install -p -m 0644 %{SOURCE2} \
	%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

%files
%doc ABOUT CHANGELOG COPYING COPYING.README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

