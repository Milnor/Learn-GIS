# QGIS

## Installation on Debian-based Linux Distros
```
sudo apt install gnupg software-properties-common
sudo wget -O /etc/apt/keyrings/qgis-archive-keyring.gpg https://download.qgis.org/downloads/qgis-archive-keyring.gpg
```
Add the following to `/etc/apt/sources.list.d/qgis.sources` (requires sudo)
```
Types: deb deb-src
URIs: https://qgis.org/debian
Suites: jammy # or your-distro's-codename
Architectures: amd64
Components: main
Signed-By: /etc/apt/keyrings/qgis-archive-keyring.gpg
```

```
sudo apt update
sudo apt install qgis qgis-plugin-grass
```

## Basic Usage

Type `world` into the "Coordinate" box at the bottom and hit `Enter` to get a map of the world.

Hit `Ctrl` + `Shift` + `F` to zoom out to the full extent.

"EPSG4326" in lower right is the **projection** of the map.
* many options are available

## References
* Klas Karlsson, [QGIS 3 for Absolute Beginners](https://www.youtube.com/watch?v=kCnNWyl9qSE&t=566s), Apr. 1, 2019.
* QGIS, [QGIS Installers - Linux - Debian/Ubuntu](https://www.qgis.org/en/site/forusers/alldownloads.html#debian-ubuntu)
