# Maintainer: Bill Sideris <bill88t@bredos.org>

pkgname=bredos-sysreport
pkgver=1.0.0
pkgrel=1
pkgdesc='BredOS System information reporter'
arch=(any)
url=https://github.com/BredOS/sys-report
license=('GPL3')

depends=(python)

source=('sys-report')
sha256sums=('445db49e238db579c15d35907d8c24d1a8406b160b6510d63ad586eb1fcfae2e')

package() {
    mkdir -p "${pkgdir}/usr/bin"
    install -Dm755 "${srcdir}/sys-report" "${pkgdir}/usr/bin/"
}
