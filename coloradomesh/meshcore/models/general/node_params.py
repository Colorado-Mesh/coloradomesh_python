from typing import Optional

from coloradomesh.internal import BaseModel


class NodeParams(BaseModel):
    """
    Represents the params of a MeshCore node on the Colorado Mesh network.
    """
    freq: Optional[float] = None
    cr: Optional[int] = None
    sf: Optional[int] = None
    bw: Optional[float] = None

    def to_json(self) -> dict:
        """
        Serialize this node's param to a JSON-compatible dictionary
        :return: A dictionary representation of this node's param that can be serialized to JSON.
        """
        return {
            'freq': self.freq,
            'cr': self.cr,
            'sf': self.sf,
            'bw': self.bw
        }

    def to_human_hash(self) -> str:
        """
        Generate a human-readable hash of this node.
        :return: A human-readable hash of this node.
        """
        return f"{self.freq}:{self.cr}:{self.sf}:{self.bw}"

    def to_hash(self) -> int:
        """
        Generate a hash value for this node
        :return: An integer hash value representing this node.
        """
        return hash(self.to_human_hash())
