#  Copyright (c) Matteo Ferreri 2024.
from somniiaMonitor.business.model.mask_business import MaskBusiness
from somniiaMonitor.model.mask import Mask


def main():
    mask = Mask()
    mask.set_name("mario")
    mask.set_mac_addr("00:00:00:00:00:01")
    mask.set_status("ok")

    mask_business: MaskBusiness = MaskBusiness.get_instance()
    response = mask_business.save_mask(mask)
    print(f"After Save -> result = {response.get_row_count()} message: {response.get_message()}")
    if response.get_row_count() > 0:
        print(f"Saved: {response.get_object()}")
        mask = response.get_object()

    old_name = mask.get_name()
    new_name = "Pollo"

    mask.set_name(new_name)
    response = mask_business.update_mask(mask)
    print(f"After Update -> result = {response.get_row_count()} message: {response.get_message()}")
    if response.get_row_count() > 0:
        print(f"Saved: {response.get_object()}")

    mask = mask_business.get_mask(mask.get_mac_addr())
    if mask.get_name() != old_name:
        print(f"New Name : {mask.get_name()}")

    response = mask_business.delete_mask(mask)
    print(f"After Remove -> result = {response.get_row_count()} message: {response.get_message()}")
    if response.get_row_count() > 0:
        print(f"User Saved: {response.get_object()}")

    mask = mask_business.get_mask(mask.get_mac_addr())
    if mask is None:
        print("User does not exist")
    else:
        print(f"user: {mask}")


if __name__ == "__main__":
    main()

