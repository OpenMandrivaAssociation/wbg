Name:           wbg
Version:        1.1.0
Release:        0
Summary:        Wallpaper application for layer-shell Wayland compositors
License:        MIT
Group:          System/GUI/Other
URL:            https://codeberg.org/dnkl/wbg
Source0:        https://codeberg.org/dnkl/wbg/archive/%version.tar.gz
# Patch 1 based of https://codeberg.org/dnkl/wbg/commit/61af8e87661b93cfefe77c083328fef962c4121d.patch
Patch1:         0001-fix-mfd-noexec-seal.patch
# Patch 4 is based of https://codeberg.org/dnkl/wbg/commit/fee19f79bb41a9f90c25b3470ec2806be7293607.patch
Patch4:         0004-impl-layer-surface-closed-event.patch
# Patch 5 is based of https://codeberg.org/dnkl/wbg/commit/670d577ad0cd45a0c7bf4a264b791a2cd86557c3.patch
Patch5:         0005-mark-surface-as-opaque.patch
BuildRequires:  c_compiler
BuildRequires:  meson >= 0.58.0
BuildRequires:  pkgconfig
BuildRequires:  python3
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
%patch1 -p1
%patch4 -p1
%patch5 -p1

%build
export CFLAGS="%{optflags}"
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/wbg
