#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-listviewer
Version  : 2.1.0
Release  : 12
URL      : https://cran.r-project.org/src/contrib/listviewer_2.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/listviewer_2.1.0.tar.gz
Summary  : 'htmlwidget' for Interactive Views of R Lists
Group    : Development/Tools
License  : Apache-2.0 MIT
BuildRequires : R-htmltools
BuildRequires : R-htmlwidgets
BuildRequires : R-reactR
BuildRequires : R-shiny
BuildRequires : buildreq-R

%description
[![npm](https://img.shields.io/npm/v/react-json-view.svg)](https://www.npmjs.com/package/react-json-view) [![npm](https://img.shields.io/npm/l/react-json-view.svg)](https://github.com/mac-s-g/react-json-view/blob/master/LISCENSE) [![Build Status](https://travis-ci.org/mac-s-g/react-json-view.svg)](https://travis-ci.org/mac-s-g/react-json-view) [![Coverage Status](https://coveralls.io/repos/github/mac-s-g/react-json-view/badge.svg?branch=master)](https://coveralls.io/github/mac-s-g/react-json-view?branch=master) [![Join the community on Spectrum](https://withspectrum.github.io/badge/badge.svg)](https://spectrum.chat/react-json-view)

%prep
%setup -q -c -n listviewer

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552888965

%install
export SOURCE_DATE_EPOCH=1552888965
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library listviewer
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library listviewer
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library listviewer
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  listviewer || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/listviewer/DESCRIPTION
/usr/lib64/R/library/listviewer/INDEX
/usr/lib64/R/library/listviewer/LICENSE
/usr/lib64/R/library/listviewer/Meta/Rd.rds
/usr/lib64/R/library/listviewer/Meta/features.rds
/usr/lib64/R/library/listviewer/Meta/hsearch.rds
/usr/lib64/R/library/listviewer/Meta/links.rds
/usr/lib64/R/library/listviewer/Meta/nsInfo.rds
/usr/lib64/R/library/listviewer/Meta/package.rds
/usr/lib64/R/library/listviewer/NAMESPACE
/usr/lib64/R/library/listviewer/NEWS.md
/usr/lib64/R/library/listviewer/R/listviewer
/usr/lib64/R/library/listviewer/R/listviewer.rdb
/usr/lib64/R/library/listviewer/R/listviewer.rdx
/usr/lib64/R/library/listviewer/examples/examples_gadget.R
/usr/lib64/R/library/listviewer/examples/examples_reactjson.R
/usr/lib64/R/library/listviewer/help/AnIndex
/usr/lib64/R/library/listviewer/help/aliases.rds
/usr/lib64/R/library/listviewer/help/listviewer.rdb
/usr/lib64/R/library/listviewer/help/listviewer.rdx
/usr/lib64/R/library/listviewer/help/paths.rds
/usr/lib64/R/library/listviewer/html/00Index.html
/usr/lib64/R/library/listviewer/html/R.css
/usr/lib64/R/library/listviewer/htmlwidgets/core-js/LICENSE
/usr/lib64/R/library/listviewer/htmlwidgets/core-js/dist/shim.min.js
/usr/lib64/R/library/listviewer/htmlwidgets/core-js/package.json
/usr/lib64/R/library/listviewer/htmlwidgets/jsonedit.js
/usr/lib64/R/library/listviewer/htmlwidgets/jsonedit.yaml
/usr/lib64/R/library/listviewer/htmlwidgets/jsoneditor/LICENSE
/usr/lib64/R/library/listviewer/htmlwidgets/jsoneditor/NOTICE
/usr/lib64/R/library/listviewer/htmlwidgets/jsoneditor/README.md
/usr/lib64/R/library/listviewer/htmlwidgets/jsoneditor/dist/img/jsoneditor-icons.png
/usr/lib64/R/library/listviewer/htmlwidgets/jsoneditor/dist/img/jsoneditor-icons.svg
/usr/lib64/R/library/listviewer/htmlwidgets/jsoneditor/dist/jsoneditor.min.css
/usr/lib64/R/library/listviewer/htmlwidgets/jsoneditor/dist/jsoneditor.min.js
/usr/lib64/R/library/listviewer/htmlwidgets/reactjson.js
/usr/lib64/R/library/listviewer/htmlwidgets/reactjson.yaml
/usr/lib64/R/library/listviewer/htmlwidgets/reactjson/LICENSE
/usr/lib64/R/library/listviewer/htmlwidgets/reactjson/README.md
/usr/lib64/R/library/listviewer/htmlwidgets/reactjson/dist/main.js
/usr/lib64/R/library/listviewer/htmlwidgets/reactjson/package.json
/usr/lib64/R/library/listviewer/rstudio/addins.dcf
