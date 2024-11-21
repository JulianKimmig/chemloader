from unittest import TestCase
from rdkit.Chem import Mol


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

    def test_LogPNadinUlrich(self):
        from chemloader.datasets.pysical.logp import LogPNadinUlrich

        loader = LogPNadinUlrich()
        i = 0
        for mol, prop in loader.iterate_with_property("logP_exp", return_list=True):
            i += 1
            self.assertIsInstance(prop, list)
            for entry in prop:
                self.assertIsInstance(entry, float)

        self.assertEqual(i, loader.expected_mol)

    def test_merged_dl(self):
        from chemloader.datasets.pysical.logp import LogPNadinUlrich
        from chemloader.datasets.pysical.mp import BradleyDoublePlusGoodMP
        from chemloader.dataloader import MergedDataLoader

        loader = MergedDataLoader([LogPNadinUlrich(), BradleyDoublePlusGoodMP()])

        self.assertEqual(
            len(loader),
            LogPNadinUlrich.expected_mol + BradleyDoublePlusGoodMP.expected_mol,
        )

        i = 0
        for mol in loader:
            self.assertIsInstance(mol, Mol)
            i += 1
        self.assertEqual(i, len(loader))
