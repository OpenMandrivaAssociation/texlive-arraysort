%global tl_name arraysort
%global tl_revision 31576

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Sort arrays (or portions of them)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/arraysort
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arraysort.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arraysort.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/arraysort.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a mechanism for sorting arrays (or portions of
them); the arrays should have been created using the arrayjobx package.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/arraysort
%dir %{_datadir}/texmf-dist/source/latex/arraysort
%dir %{_datadir}/texmf-dist/tex/latex/arraysort
%doc %{_datadir}/texmf-dist/doc/latex/arraysort/Makefile
%doc %{_datadir}/texmf-dist/doc/latex/arraysort/README
%doc %{_datadir}/texmf-dist/doc/latex/arraysort/arraysort.pdf
%doc %{_datadir}/texmf-dist/source/latex/arraysort/arraysort.dtx
%doc %{_datadir}/texmf-dist/source/latex/arraysort/arraysort.ins
%{_datadir}/texmf-dist/tex/latex/arraysort/arraysort.sty
