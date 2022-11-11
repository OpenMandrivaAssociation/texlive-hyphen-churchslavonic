Name:		texlive-hyphen-churchslavonic
Version:	58609
Release:	1
Summary:	Church Slavonic hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-churchslavonic.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Church Slavonic in UTF-8 encoding as well as in
ASCII-based encoding for 8-bit engines.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-churchslavonic
%_texmf_language_def_d/hyphen-churchslavonic
%_texmf_language_lua_d/hyphen-churchslavonic
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/*
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/*/*

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}

mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-churchslavonic <<EOF
\%% from hyphen-churchslavonic:
churchslavonic loadhyph-cu.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-churchslavonic
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-churchslavonic <<EOF
\%% from hyphen-churchslavonic:
\addlanguage{churchslavonic}{loadhyph-cu.tex}{}{1}{1}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-churchslavonic
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-churchslavonic <<EOF
-- from hyphen-churchslavonic:
	['churchslavonic'] = {
		loader = 'loadhyph-cu.tex',
		lefthyphenmin = 1,
		righthyphenmin = 1,
		synonyms = {  },
		patterns = 'hyph-cu.pat.txt',
		hyphenation = '',
	},
EOF
