#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2026 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/samsung/sm7125-common',
    'hardware/qcom-caf/sm8150',
    'hardware/qcom-caf/wlan',
    'hardware/samsung',
    'vendor/qcom/opensource/dataservices',
    'vendor/qcom/opensource/display',
]

def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'vendor.qti.hardware.fm@1.0_vendor',
        'libsecril-client',
    ): lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
    ('vendor/lib/hw/audio.primary.atoll.so'): blob_fixup()
        .add_needed('libshim_samsungaudioparams.so')
        .binary_regex_replace(b'str_parms_get_int', b'str_parms_get_mod'),
    ('vendor/lib/libwvhidl.so', 'vendor/lib/mediadrm/libwvdrmengine.so'): blob_fixup()
        .add_needed('libcrypto_shim.so'),
    ('vendor/lib/unihal_main@2.15.so', 'vendor/lib64/unihal_main@2.15.so'): blob_fixup()
        .add_needed('libui_shim.so'),
    ('vendor/lib64/hw/gatekeeper.mdfpp.so', 'vendor/lib64/libskeymaster4device.so', 'vendor/lib64/libkeymaster_helper.so'): blob_fixup()
        .replace_needed('libcrypto.so', 'libcrypto-v33.so'),
    ('vendor/lib64/libsec-ril.so', 'vendor/lib64/libsec-ril-dsds.so'): blob_fixup()
        .sig_replace(
            '60 0E 40 F9 82 0C 80 52 24 00 80 52 E1 03 15 AA 08 00 40 F9 E3 03 14 AA',
            '60 0E 40 F9 82 0C 80 52 24 00 80 52 E1 03 15 AA 08 00 40 F9 03 00 80 D2')
        # Always emit uiccApplicationsEnablementChanged
        .sig_replace(
            '88 58 9D 52 1F 00 08 6B AB 01 00 54', '88 58 9D 52 1F 00 08 6B 1F 20 03 D5')
        .sig_replace(
            '88 58 9D 52 FF 02 08 6B AB 01 00 54', '88 58 9D 52 FF 02 08 6B 1F 20 03 D5'),
} # fmt: skip

module = ExtractUtilsModule(
    'sm7125-common',
    'samsung',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
