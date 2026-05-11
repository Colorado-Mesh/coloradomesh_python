# Colorado Mesh Python Library

A utility package for Colorado Mesh-related projects

### Data

Snapshots of known Meshtastic and MeshCore nodes are taken every hour or so (via GitHub Actions) from various online sources and [cached in this repository](https://github.com/Colorado-Mesh/coloradomesh_python/tree/master/data). These snapshots are what is used by this library as the data source for Meshtastic and MeshCore node. This cache is to reduce the load on the external data sources (and to speed up response times) when dealing with "live" data.
