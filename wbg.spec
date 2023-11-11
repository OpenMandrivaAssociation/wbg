Name:           wbg
Version:        1.1.0
Release:        1
Summary:        Wallpaper application for layer-shell Wayland compositors
License:        MIT
Group:          System/GUI/Wayland
URL:            https://codeberg.org/dnkl/wbg
Source0:        https://codeberg.org/dnkl/wbg/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson >= 0.58.0
BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(tllist) >= 1.0.1
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)

%description
Wbg is a wallpaper setter for Wayland compositors that implement the
layer-shell protocol.

It takes a single argument, the image filename, which is displayed
scaled-to-fit on all monitors.

%prep
%setup -n %name

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/wbg
