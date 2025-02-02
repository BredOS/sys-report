# Maintainer: Bill Sideris <bill88t@bredos.org>

pkgname=bredos-sysreport
pkgver=1.1.0
pkgrel=1
pkgdesc='BredOS System information reporter'
arch=(any)
url=https://github.com/BredOS/sys-report
license=('GPL3')

depends=(python)

source=('sys-report.py')
sha256sums=('2ed326e92bd90c412fcdf2e272014cac0cdc4deb278e439afe18fbdc79aac52b')

package() {
    mkdir -p "${pkgdir}/usr/bin"
    install -Dm755 "${srcdir}/sys-report.py" "${pkgdir}/usr/bin/sys-report"
}
