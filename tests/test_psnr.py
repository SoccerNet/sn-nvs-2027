import importlib.util
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('psnr', ROOT / 'evaluation/psnr.py')
psnr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(psnr)


class PSNRTests(unittest.TestCase):
    def test_known_pixel_difference_and_scene_matching(self):
        with TemporaryDirectory() as folder:
            base = Path(folder)
            gt = base / 'ref' / 'scene-1-challenge' / 'renders'
            pred = base / 'res' / 'scene-1-challenge' / 'renders'
            gt.mkdir(parents=True)
            pred.mkdir(parents=True)
            Image.new('RGB', (2, 2), (0, 0, 0)).save(gt / '00000.png')
            Image.new('RGB', (2, 2), (255, 255, 255)).save(pred / '00000.png')
            self.assertAlmostEqual(psnr.psnr_pair(gt / '00000.png', pred / '00000.png', (2, 2)), 0)
            self.assertAlmostEqual(psnr.evaluate(base / 'ref', base / 'res', (2, 2))['scene-1-challenge'], 0)
            (pred / '00000.png').unlink()
            with self.assertRaises(ValueError):
                psnr.evaluate(base / 'ref', base / 'res', (2, 2))
