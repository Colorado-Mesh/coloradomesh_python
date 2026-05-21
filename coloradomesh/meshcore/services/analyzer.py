from corescope import CoreScopeClient, models

COLORADO_MESH_CORESCOPE_URL = "https://analyzer.meshcore.coloradomesh.org"


def _build_colorado_mesh_analyzer_client() -> CoreScopeClient:
    return CoreScopeClient(
        base_url=COLORADO_MESH_CORESCOPE_URL,
        verbose=False,
    )


def get_stats() -> models.Stats | None:
    return _build_colorado_mesh_analyzer_client().get_stats()


def get_node_health_reports() -> list[models.BulkNodeHealthEntry] | None:
    return _build_colorado_mesh_analyzer_client().get_node_health_reports()


def get_node_health(node_public_key: str) -> models.NodeHealthSummary | None:
    return _build_colorado_mesh_analyzer_client().get_node_health(public_key=node_public_key)


def get_node(node_public_key: str) -> models.NodeSummary | None:
    return _build_colorado_mesh_analyzer_client().get_node(public_key=node_public_key)


def get_observers() -> list[models.Observer] | None:
    return _build_colorado_mesh_analyzer_client().get_observers()


def get_channels() -> list[models.Channel] | None:
    return _build_colorado_mesh_analyzer_client().get_channels()


def get_packets() -> models.PacketsSummary | None:
    return _build_colorado_mesh_analyzer_client().get_packets()


def get_node_neighbors(node_public_key: str) -> models.NeighborsSummary | None:
    return _build_colorado_mesh_analyzer_client().get_node_neighbors(public_key=node_public_key)


def get_channel_messages(channel_name: str) -> models.ChannelMessagesSummary | None:
    return _build_colorado_mesh_analyzer_client().get_channel_messages(channel_name=channel_name)
