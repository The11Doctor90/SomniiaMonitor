#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.business.model.mask_business import MaskBusiness


class MaskIntegrityCheck:
    @classmethod
    def masks_are_present(cls) -> bool:
        """controlla se abbiamo delle mask inseriti nella db.
        Se sono presenti 1 o più mask ritorna True, altrimenti se non ci sono alcun mask ritorna False"""
        mask_business: MaskBusiness = MaskBusiness.get_instance()
        res: [] = mask_business.get_all_mask()
        return len(res) > 0
