import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.parsers.csv_parser import CSVParser
from src.generators.heatmap_renderer import HeatmapRenderer
from src.utils.config import Config


def main() -> None:
    parser = argparse.ArgumentParser(description="Player Telemetry Heatmap Generator")
    parser.add_argument("--input", required=True, help="CSV veri dosyası yolu")
    parser.add_argument("--output", default="output/heatmap.png", help="Çıktı PNG yolu")
    parser.add_argument("--map", default="", dest="background", help="Arka plan harita görseli")
    parser.add_argument("--blur_radius", type=int, default=15, help="Gaussian blur yarıçapı")
    args = parser.parse_args()

    config = Config(
        blur_radius=args.blur_radius,
        background_path=args.background,
        output_path=args.output,
    )

    session = CSVParser().parse(args.input)
    print(f"[+] {len(session)} olay yüklendi.")

    renderer = HeatmapRenderer(config)
    renderer.render(session, args.output)
    print(f"[+] Heatmap kaydedildi: {args.output}")


if __name__ == "__main__":
    main()
