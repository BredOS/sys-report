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
sha256sums=('797877da7fce2dcd21d2d8f94bcaf4a79ab81f54a9f9603acbd994f3ddb912e8')

package() {
    mkdir -p "${pkgdir}/usr/bin"
    install -Dm755 "${srcdir}/sys-report.py" "${pkgdir}/usr/bin/sys-report"
}
