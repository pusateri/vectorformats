import os
import unittest

from VectorFormats.Formats.KML import KML


class KMLDecodeTest(unittest.TestCase):

    def read_file(self, filename):
        """
        Process a file stored in tests/data/ and return its content.
        """
        current_path = os.path.dirname(os.path.realpath(__file__))
        fixture_path = os.path.join(
            current_path,
            'data',
            filename
        )
        f = open(fixture_path)
        return f.read()

    def decode(self, filename, **kwargs):
        """
        Process a file an return features.
        """
        content = self.read_file(filename)
        kml = KML(**kwargs)
        return kml.decode(content)

    def test_decode_simple_point(self):
        features = self.decode("simple_point.kml")
        self.assertEqual(len(features), 1)
        point = features[0]
        self.assertEqual(point.properties['title'], 'Simple point')
        self.assertEqual(point.properties['description'], 'Here is a simple description.')
        self.assertEqual(point.geometry['type'], 'Point')
        self.assertEqual(point.geometry['coordinates'], [-122.0822035425683, 37.42228990140251, 0.0])

    def test_decode_simple_path(self):
        features = self.decode("simple_path.kml")
        self.assertEqual(len(features), 1)
        path = features[0]
        self.assertEqual(path.properties['title'], 'Simple path')
        self.assertEqual(path.properties['description'], 'Simple description')
        self.assertEqual(path.geometry['type'], 'LineString')
        self.assertEqual(path.geometry['coordinates'], [[-112.2550785337791, 36.07954952145647, 2357], [-112.2549277039738, 36.08117083492122, 2357], [-112.2552505069063, 36.08260761307279, 2357]])


if __name__ == '__main__':
    unittest.main()
