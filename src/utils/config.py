from dataclasses import dataclass


@dataclass
class Config:
    """Heatmap renderer konfigürasyon sınıfı."""
    map_width: int = 1024
    map_height: int = 1024
    blur_radius: int = 15
    point_radius: int = 8
    background_path: str = ""
    output_path: str = "output/heatmap.png"
    color_map: str = "hot"

    def __repr__(self) -> str:
        return (f"Config(size={self.map_width}x{self.map_height}, "
                f"blur={self.blur_radius}, output='{self.output_path}')")
