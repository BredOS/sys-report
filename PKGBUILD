# Maintainer: Bill Sideris <bill88t@bredos.org>

pkgname=bredos-sysreport
pkgver=1.2.0
pkgrel=1
pkgdesc='BredOS System information reporter'
arch=(any)
url=https://github.com/BredOS/sys-report
license=('GPL3')

depends=(python)

source=('sys-report.py')
sha256sums=('c49e1848edd8c79240e0a95f9f722bfaad6ef30094899d08be8c2b1bb73e4441')

package() {
    mkdir -p "${pkgdir}/usr/bin"
    install -Dm755 "${srcdir}/sys-report.py" "${pkgdir}/usr/bin/sys-report"
}
