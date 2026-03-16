import os
from typing import List, Tuple
from PIL import Image, ImageFilter, ImageDraw
from ..models.session_data import SessionData
from ..utils.config import Config


class HeatmapRenderer:
    """Telemetri koordinatlarını ısı haritası görseliyle işler."""

    def __init__(self, config: Config) -> None:
        self.config = config

    def render(self, session_data: SessionData, output_path: str = "") -> Image.Image:
        """Pipeline: veri -> nokta çizimi -> blur -> birleştirme -> kaydet."""
        if not output_path:
            output_path = self.config.output_path

        coordinates = session_data.get_all_coordinates()
        base = self._create_base_image()
        base = self._draw_points(base, coordinates)
        base = self._apply_blur(base)

        if self.config.background_path and os.path.exists(self.config.background_path):
            result = self.overlay_on_background(base, self.config.background_path)
        else:
            result = base

        out_dir = os.path.dirname(output_path)
        if out_dir:
            os.makedirs(out_dir, exist_ok=True)
        result.save(output_path)
        return result

    def _create_base_image(self) -> Image.Image:
        """Siyah, transparan temel canvas oluşturur."""
        return Image.new("RGBA", (self.config.map_width, self.config.map_height), (0, 0, 0, 0))

    def _draw_points(self, image: Image.Image, coordinates: List[Tuple[float, float]]) -> Image.Image:
        """Her koordinata yarı saydam kırmızı nokta çizer."""
        draw = ImageDraw.Draw(image)
        r = self.config.point_radius
        for x, y in coordinates:
            xi, yi = int(x), int(y)
            draw.ellipse([xi - r, yi - r, xi + r, yi + r], fill=(255, 30, 30, 80))
        return image

    def _apply_blur(self, image: Image.Image) -> Image.Image:
        """Gaussian blur uygulayarak ısı haritası efekti yaratır."""
        return image.filter(ImageFilter.GaussianBlur(radius=self.config.blur_radius))

    def overlay_on_background(self, heatmap: Image.Image, bg_path: str) -> Image.Image:
        """Isı haritasını arka plan görseli üzerine yapıştırır."""
        bg = Image.open(bg_path).convert("RGBA")
        bg = bg.resize((self.config.map_width, self.config.map_height))
        bg.paste(heatmap, (0, 0), mask=heatmap)
        return bg

    def __repr__(self) -> str:
        return f"HeatmapRenderer(config={self.config!r})"
