%global tl_name hyphen-churchslavonic
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Church Slavonic hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-churchslavonic
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-churchslavonic.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for Church Slavonic in UTF-8 encoding


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-churchslavonic:
churchslavonic loadhyph-cu.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-churchslavonic:
\addlanguage{churchslavonic}{loadhyph-cu.tex}{}{1}{2}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-churchslavonic:
['churchslavonic'] = {
	loader = 'loadhyph-cu.tex',
	lefthyphenmin = 1,
	righthyphenmin = 2,
	synonyms = {  },
	patterns = 'hyph-cu.pat.txt',
	hyphenation = 'hyph-cu.hyp.txt',
},
TL_HYPHEN_EOF
