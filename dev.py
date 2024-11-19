# from moldata.datasets.medical.tox21 import Tox21 as DS

# from moldata.datasets.chemical.nmr.phosphorus import Ilm_NMR_P31 as DS
# from moldata.datasets.chemical.solubility.ESOL import ESOL as DS
# from moldata.datasets.chemical.solubility.FreeSolv import FreeSolv as DS
# from moldata.datasets.chemical.lipophilicity import Lipo1 as DS
# from moldata.datasets.chemical.pka import IUPAC_DissociationConstantsV1_0 as DS
# from moldata.datasets.chemical.pka import HybridpKaDatasetforAcidMolecules as DS
from moldata.datasets.chemical.quantumemchanics import QM9 as DS

# from moldata.datasets.pysical.logp import LogPNadinUlrich as DS
# from moldata.datasets.pysical.mp import BradleyDoublePlusGoodMP as DS
from tqdm import tqdm

if __name__ == "__main__":
    loader = DS()
    all_prop_keys = set()
    for mol in tqdm(loader, total=len(loader)):
        print(mol.GetPropsAsDict())
        all_prop_keys.update(mol.GetPropsAsDict().keys())
        break
    exit()

    propcount = {}
    for prop in all_prop_keys:
        propcount[prop] = 0
        propcount["no" + prop] = 0

    for mol in tqdm(loader, total=len(loader)):
        for prop in all_prop_keys:
            if mol.HasProp(prop):
                propcount[prop] += 1
            else:
                propcount["no" + prop] += 1

    from pprint import pprint

    for prop in all_prop_keys:
        print(
            f"{prop}: {propcount[prop]}/{propcount['no' + prop]} -> ({propcount[prop] + propcount['no' + prop]})"
        )
    for prop in all_prop_keys:
        del propcount["no" + prop]
    pprint(propcount)

    meanps = list(
        [p for m, p in loader.iterate_with_property("expt", return_list=True)]
    )
    print(len(meanps))
    from statistics import mean, stdev

    for i in meanps:
        if len(i) > 1:
            print(mean(i), stdev(i) if len(i) > 1 else 0)
