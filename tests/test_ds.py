from unittest import TestCase


class TestDS(TestCase):
    def test_BradleyDoublePlusGoodMP(self):
        from chemloader.datasets.pysical.mp import BradleyDoublePlusGoodMP

        loader = BradleyDoublePlusGoodMP()
        i = 0
        for mol, prop in loader.iterate_with_property("mpC", return_list=True):
            i += 1
            self.assertIsInstance(prop, list)
            for entry in prop:
                self.assertIsInstance(entry, float)

        self.assertEqual(i, loader.expected_mol)
