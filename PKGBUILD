# Maintainer: Bill Sideris <bill88t@bredos.org>

pkgname=bredos-sysreport
pkgver=1.2.1
pkgrel=1
pkgdesc='BredOS System information reporter'
arch=(any)
url=https://github.com/BredOS/sys-report
license=('GPL3')

depends=(python)

source=('sys-report.py')
sha256sums=('6cb6125b85baf1986724f38d2f69cc04bcb3f6a1f9db4ab6bcf43598d1f3277d')

package() {
    mkdir -p "${pkgdir}/usr/bin"
    install -Dm755 "${srcdir}/sys-report.py" "${pkgdir}/usr/bin/sys-report"
}
